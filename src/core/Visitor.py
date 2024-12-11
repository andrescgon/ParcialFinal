import sys
import math
import numpy as np

from numpy import arange
from inspect import signature, _empty, isbuiltin
from importlib import import_module

from .TLONParser import TLONParser
from .TLONVisitor import TLONVisitor


from .structures import *
from .mlp_model import *
from .clustering import ClusteringModel
from .plotter import AdvancedPlotter


sys.setrecursionlimit(100000)
sys.path.append('/src/lib')
from mas.__init__ import *

class Visitor(TLONVisitor):
  memory_manager = None
  memory_stack = None  # Add this line to define memory_stack
  value_returned = False
  line_error = -1

  def __init__(self):
        self.memory_manager = TLONGlobalMemory__()
        self.memory_stack = self.memory_manager.memory_stack  # Assign memory_stack here
        TLONVariable__._visitor = self
        TLONVariable__._memory_manager = self.memory_manager
        # Visit a parse tree produced by TLONParser#parse.

  def visitParse(self, ctx: TLONParser.ParseContext):
        if ctx.from_file is not None:
            return self.visit(ctx.from_file())
        else:
            return self.visit(ctx.from_input())

  # Visit a parse tree produced by TLONParser#from_input.
  def visitFrom_input(self, ctx: TLONParser.From_inputContext):
    return self.visit(ctx.stat())

  # Visit a parse tree produced by TLONParser#from_file.
  def visitFrom_file(self, ctx: TLONParser.From_fileContext):
    return self.visitChildren(ctx)

  # Visit a parse tree produced by TLONParser#stat.
  def visitStat(self, ctx: TLONParser.StatContext):
    if ctx.compound_stat() is not None:
      return self.visit(ctx.compound_stat())
    elif ctx.plot() is not None:
      return self.visit(ctx.plot())

    return self.visit(ctx.simple_stat())

  # Visit a parse tree produced by TLONParser#compound_stat.
  def visitCompound_stat(self, ctx: TLONParser.Compound_statContext):
    if ctx.if_stat() is not None:
      return self.visit(ctx.if_stat())
    elif ctx.while_stat() is not None:
      return self.visit(ctx.while_stat())
    elif ctx.for_stat() is not None:
      return self.visit(ctx.for_stat())

    return self.visit(ctx.funcion())

  # Visit a parse tree produced by TLONParser#simple_stat.
  def visitSimple_stat(self, ctx: TLONParser.Simple_statContext):
    if ctx.assignment() is not None:
      return self.visit(ctx.assignment())
    elif ctx.log() is not None:
      return self.visit(ctx.log())
    elif ctx.importar() is not None:
      return self.visit(ctx.importar())
    elif ctx.retornar() is not None:
      return self.visit(ctx.retornar())
    elif ctx.mft_special() is not None:
      return self.visit(ctx.mft_special())
    elif ctx.atom() is not None:
      return self.visit(ctx.atom())

    raise Exception('Semantic Error: Found ' + str(self.OTHER()))

  # Visit a parse tree produced by TLONParser#assignment.
  def visitAssignment(self, ctx: TLONParser.AssignmentContext):
    name = str(ctx.variable().getText())
    value = None
    
    if ctx.linear_regression():
        value = self.visit(ctx.linear_regression())
    elif ctx.mlp_expr():
        value = self.visit(ctx.mlp_expr())
    elif ctx.clustering():
        value = self.visit(ctx.clustering())
    elif ctx.clusteringPredict():
        value = self.visit(ctx.clusteringPredict())
    elif ctx.expr() is not None:
        value = self.visit(ctx.expr())
    elif ctx.assignment() is not None:
        value = self.visit(ctx.assignment())
        
    self.memory_manager.assign(name, value)
    return value

    
    
  # Visit a parse tree produced by TLONParser#if_stat.
  def visitIf_stat(self, ctx: TLONParser.If_statContext):
    conditions = ctx.condition_block()

    for condition in conditions:
      result = self.visit(condition)

      if result['accepted'] is True:
        return result['value_returned']

    if ctx.stat_block() is not None:
      self.memory_manager.add_memory('ELSE_STMT')
      value_returned = self.visit(ctx.stat_block())
      self.memory_manager.pop_memory()
      return value_returned

    return None

  # Visit a parse tree produced by TLONParser#while_stat.
  def visitWhile_stat(self, ctx: TLONParser.While_statContext):
    condition = self.visit(ctx.expr())
    returned_value = None

    while condition:
      self.memory_manager.add_memory('WHILE_STMT')
      returned_value = self.visit(ctx.stat_block())
      self.memory_manager.pop_memory()

      if type(returned_value) is tuple and returned_value[1] == 1:
        return returned_value[0]

      condition = self.visit(ctx.expr())

    return None

  # Visit a parse tree produced by TLONParser#for_stat.
  def visitFor_stat(self, ctx: TLONParser.For_statContext):
    items = self.visit(ctx.expr())
    var = str(ctx.ID())

    if self.memory_manager.find(var) is not None:
      raise Exception("Error: Cannot use variable " + var + ". Already assigned.")

    try:
      #validate if object is iterable
      items_iterator = iter(items)
      for item in items:
        self.memory_manager.add_memory('FOR_STMT')
        self.memory_manager.assign(var, item)
        returned_value = self.visit(ctx.stat_block())
        self.memory_manager.pop_memory()

        if type(returned_value) is tuple and returned_value[1] == 1:
          return returned_value[0]
    except:
      raise Exception("Error: Variable is not iterable.")

    return None

  # Visit a parse tree produced by TLONParser#log.
  def visitLog(self, ctx: TLONParser.LogContext):
    variable = self.visit(ctx.expr())

    if isinstance(variable, TLONVariable__):
      print(variable.value)
    else:
      print(variable)

    return None

  # Visit a parse tree produced by TLONParser#agente.
  def visitAgente(self, ctx:TLONParser.AgenteContext):
    array = []
    for param in ctx.atom():
      value = self.visit(param)
      array.append(value)
    agent = eval(array[0])(*array[1:])
    return agent

  # Visit a parse tree produced by TLONParser#comunidad.
  def visitComunidad(self, ctx:TLONParser.ComunidadContext):
      import json
      params = []
      for param in ctx.atom():
          value = self.visit(param)
          params.append(value)
      dict_agents = params[0].replace("'",'"')
      dict_agents = json.loads(dict_agents)
      comm = Community(dict_agents,params[1])
      return comm

  # Visit a parse tree produced by TLONParser#funcion.
  def visitFuncion(self, ctx: TLONParser.FuncionContext):
    opcionales = False

    name = str(ctx.ID())
    kind = 'user'
    value = ctx.stat()

    parameters = {}
    for param in ctx.parametro():
      param_name = str(param.ID())

      if self.memory_manager.find(param_name) is not None:
        raise Exception('Cannot assign variable as parameter of function. Already assigned.')

      if (opcionales and param.ASSIGN() is None):
        raise Exception('Cannot set mandatory parameter after optional parameter')

      parameter = TLONParameter__(param_name)

      if (param.ASSIGN() is not None):
        parameter.kind = 'optional'
        parameter.default = self.visit(param.expr())
        opcionales = True
      else:
        parameter.kind = 'mandatory'

      parameters[param_name] = parameter

    local_memory = self.memory_manager.peek_memory()

    funcion = TLONVariable__(name, value, kind, parameters)
    local_memory.assign(name, funcion,None)

    return funcion

  # Visit a parse tree produced by TLONParser#importar.
  def visitImportar(self, ctx: TLONParser.ImportarContext):
    try:
        mod=None
        package_name = '.'.join([str(x.getText()) for x in ctx.ID()])
        try:
          mod = import_module(package_name)
          global_mem = self.memory_manager.get_memory(0)
          for name, attribute in mod.__dict__.items():
              if not name.startswith('__'):
                  var = TLONVariable__(name, attribute, 'default')
                  global_mem.assign(name, var,None)
        except:
          if len((ctx.ID()))==2:
              package_name = import_module(str(ctx.ID()[0]))
              if str(ctx.ID()[1]) in package_name.__dict__:
                  mod = getattr(package_name,str(ctx.ID()[1]))
                  global_mem = self.memory_manager.get_memory(0)
                  var = TLONVariable__(str(ctx.ID()[1]), mod, 'default')
                  global_mem.assign(str(ctx.ID()[1]), var,None)
              else:
                  error = "No module named '" + str(ctx.ID()[1]) +"'; '"+ str(ctx.ID()[0]) + "' is not a package"
                  raise Exception(error)

        return mod
    except Exception as e:
      print (e)

  # Visit a parse tree produced by TLONParser#retornar.
  def visitRetornar(self, ctx: TLONParser.RetornarContext):
    return (self.visit(ctx.expr()), 1)

  # Visit a parse tree produced by TLONParser#condition_block.
  def visitCondition_block(self, ctx: TLONParser.Condition_blockContext):

    result = { 'accepted': self.visit(ctx.expr()) }

    if result['accepted'] is True:
      self.memory_manager.add_memory('IF_STMT')
      result['value_returned'] = self.visit(ctx.stat_block())
      self.memory_manager.pop_memory()

    return result

  # Visit a parse tree produced by TLONParser#stat_block.
  def visitStat_block(self, ctx: TLONParser.Stat_blockContext):
    value_returned = None

    for stat in ctx.stat():
      value_returned = self.visit(stat)

    return value_returned

  # Visit a parse tree produced by TLONParser#array.
  def visitArray(self, ctx: TLONParser.ArrayContext):
    array = []

    if (len(ctx.POINTS()) > 0):
      try:
        init = self.visit(ctx.expr(0))
        end = self.visit(ctx.expr(1)) + 1
        step = 1

        if ctx.step is not None:
          step = self.visit(ctx.expr(1))
          end = self.visit(ctx.expr(2)) + 1

        if type(init) is float or type(end) is float or type(step) is float:
          init = float(init)
          step = float(step)
          end = float(end)
        else:
          init = int(init)
          step = int(step)
          end = int(end)

        array = list(arange(init, end, step))
      except Exception as e:
        print (e)
        raise Exception('Error: Variable types are not numeric.')

    else:
      items = ctx.expr()

      for item in items:
        value = self.visit(item)
        array.append(value)

    return array

  # Visit a parse tree produced by TLONParser#accessarray.
  def visitAccessarray(self, ctx):
    try:
        variable_name = ctx.variable().getText()
        index = self.visit(ctx.expr())
        
        # Obtener el valor de la variable
        variable_wrapper = self.memory_manager.get(variable_name)
        
        # Si es un TLONVariable__, obtén su valor
        if isinstance(variable_wrapper, TLONVariable__):
            variable = variable_wrapper.get_value()
        else:
            variable = variable_wrapper
        
        # Verificaciones de tipo y rango
        if not isinstance(variable, (list, tuple)):
            raise TypeError(f"'{variable_name}' no es un array")
        
        if not isinstance(index, int):
            raise TypeError("El índice debe ser un número entero")
        
        if index < 0 or index >= len(variable):
            raise IndexError(f"Índice {index} fuera de rango para array de longitud {len(variable)}")
        
        return variable[index]
    
    except Exception as e:
        print(f"Error al acceder al array: {e}")
        raise


  # Visit a parse tree produced by TLONParser#variable.
  def visitVariable(self, ctx: TLONParser.VariableContext):
    name = ctx.ID()

    name = '.'.join(list(map(lambda x: x.getText(), name)))

    item = self.memory_manager.find(name)

    if item==None:
      raise Exception('Error: Variable not found.')

    if item.kind == 'default' or (item.kind == 'any' and not (type(item.value) is int or type(item.value) is float or
                                                                  type(item.value) is str or type(item.value) is list or
                                                                  type(item.value) is dict)):
      if ctx.OPAR() is not None:
        params = list(map(lambda x: self.visit(x), ctx.expr()))
        if not isbuiltin(item.value):
          def_func_params = signature(item.value).parameters

          count_mandatory = sum(type(v.default) is type(_empty) for k, v in def_func_params.items())
          count = len(def_func_params)

          if len(params) > count:
            raise Exception('FunctionError: Too many parameter to call function.')
          if len(params) < count_mandatory:
            raise Exception('FunctionError: Too few parameter to call function.')

        func = item.value

        #try:
        return func(*params)
        #except Exception as e:
        #  raise Exception('FunctionError: Builtin function throws error:', e)
      else:
        item = item.value
    elif item.kind == 'user':
      if ctx.OPAR() is not None:
        params = list(map(lambda x: self.visit(x), ctx.expr()))
        count_mandatory = sum(param.kind == 'mandatory' for name, param in item.params.items())

        count = len(item.params)

        if len(params) > count:
          raise Exception('FunctionError: Too many parameter to call function.')
        if len(params) < count_mandatory:
          raise Exception('FunctionError: Too few parameter to call function.')

        index = 0
        func_params = {}
        ########################################################
        # ERROR
        # Resolver problema con programacion funcional
        # A veces se cambia el orden de los items en 'iem.params.items()' en python 3.4.2
        ########################################################
        for name, param in item.params.items():
          if len(params) <= index:
            break

          func_params[name] = params[index]
          index += 1

        local_memory = self.memory_manager.add_memory('FUNCTION', func_params)
        func = item.value

        returned = None
        for stat in func:
          value = self.visit(stat)

          if type(value) is tuple and value[1] == 1:
            self.memory_manager.pop_memory()
            return value[0]

        item = returned
      else:
        return item
    elif item.kind == 'any':
      if (type(item.value) is int or type(item.value) is float or type(item.value) is str or
              type(item.value) is list or type(item.value) is dict):
        item = item.value
        
    return item
        
  def visitLinear_regression(self, ctx: TLONParser.Linear_regressionContext):
    try:
        x = self.visit(ctx.expr(0))
        y = self.visit(ctx.expr(1))

        if x is None or y is None:
            print("Error: x o y es None")
            return None
            
        if not isinstance(x, list):
            print(f"Error: x debe ser una lista, no {type(x)}")
            return None
            
        if not isinstance(y, list):
            print(f"Error: y debe ser una lista, no {type(y)}")
            return None
            
        # Convertir a numpy arrays para los cálculos
        x_arr = np.array(x, dtype=float)
        y_arr = np.array(y, dtype=float)
        
        # Calcular la regresión lineal
        n = len(x)
        mean_x = np.mean(x_arr)
        mean_y = np.mean(y_arr)
        
        numerador = np.sum((x_arr - mean_x) * (y_arr - mean_y))
        denominador = np.sum((x_arr - mean_x) ** 2)
        
        if denominador == 0:
            print("Error: División por cero en el cálculo")
            return None
        
        # Calcular pendiente (m) y intersección (b)
        m = numerador / denominador
        b = mean_y - m * mean_x
        
        # Crear el objeto TLON para el retorno
        result = TLONVariable__("linear_regression_result", {
            "pendiente": round(float(m), 4),
            "interseccion": round(float(b), 4),
            "ecuacion": f'y = {m:.4f}x + {b:.4f}'
        }, kind="default")

        return result
            
    except Exception as e:
        print(f"Error en linear_regression: {str(e)}")
        import traceback
        traceback.print_exc()
        return None

                     
  def visitMlp_expr(self, ctx: TLONParser.Mlp_exprContext):
    if ctx.mlp_train():
        # Procesar entrenamiento
        X_obj = self.visit(ctx.mlp_train().expr(0))
        y = self.visit(ctx.mlp_train().expr(1))
        
        # Convertir layers a lista de enteros
        layers_expr = self.visit(ctx.mlp_train().expr(2))
        layers = layers_expr if isinstance(layers_expr, list) else [int(layers_expr)]
        
        # Obtener epochs y learning_rate
        epochs = int(self.visit(ctx.mlp_train().expr(3)))
        learning_rate = float(self.visit(ctx.mlp_train().expr(4)))
        
        # Crear y entrenar modelo
        model = MLPModel(layers, epochs, learning_rate)
        return model.train(X_obj, y)
    
    elif ctx.mlp_predict():
        # Procesar predicción
        model = self.visit(ctx.mlp_predict().expr(0))
        X_obj = self.visit(ctx.mlp_predict().expr(1))
        predictions = model.predict(X_obj)
        return predictions.tolist()
        
  def visitClustering(self, ctx):
        method = str(ctx.method.text).lower()
        params = self._parse_clustering_params(ctx.params)
        X_obj = self.visit(ctx.expr())
        
        model = ClusteringModel(method, params)
        model.fit(X_obj)
        return model
    
  def visitClusteringPredict(self, ctx):
        model = self.visit(ctx.expr(0))
        X_obj = self.visit(ctx.expr(1))
        predictions = model.predict(X_obj)
        return predictions
    
  def _parse_clustering_params(self, params_ctx):
        params = {}
        for param in params_ctx.keyvalue():
            key = str(param.ID())
            value = self.visit(param.expr())
            params[key] = value
        return params
        

  def visitPlot(self, ctx: TLONParser.PlotContext):
    try:
        x_data = self.visit(ctx.expr(0))  # Obtener datos X o rango
        y_expr = ctx.expr(1)  # Obtener expresión Y
        
        # Create a function that safely evaluates the y expression
        def eval_y_expr(x):
            try:
                # Use the top-most local memory
                local_mem = self.memory_stack[-1]
                
                # Temporarily assign x to the local memory
                local_mem.assign('x', TLONVariable__('x', x, kind='default'), self.memory_stack)
                
                # Custom visitor method to handle function compositions
                def evaluate_expression(expr):
                    # If it's a binary expression (like sin + 1)
                    if hasattr(expr, 'left') and hasattr(expr, 'right') and hasattr(expr, 'op'):
                        left_val = evaluate_expression(expr.left)
                        right_val = evaluate_expression(expr.right)
                        op = expr.op.text if hasattr(expr.op, 'text') else expr.op
                        
                        # Handle different arithmetic operations
                        if op in ['+', '-', '*', '/', '^']:
                            if callable(left_val) and isinstance(right_val, (int, float)):
                                return lambda x: left_val(x) + right_val if op == '+' else \
                                       left_val(x) - right_val if op == '-' else \
                                       left_val(x) * right_val if op == '*' else \
                                       left_val(x) / right_val if op == '/' else \
                                       left_val(x) ** right_val
                            elif isinstance(left_val, (int, float)) and callable(right_val):
                                return lambda x: left_val + right_val(x) if op == '+' else \
                                       left_val - right_val(x) if op == '-' else \
                                       left_val * right_val(x) if op == '*' else \
                                       left_val / right_val(x) if op == '/' else \
                                       left_val ** right_val(x)
                            elif callable(left_val) and callable(right_val):
                                return lambda x: left_val(x) + right_val(x) if op == '+' else \
                                       left_val(x) - right_val(x) if op == '-' else \
                                       left_val(x) * right_val(x) if op == '*' else \
                                       left_val(x) / right_val(x) if op == '/' else \
                                       left_val(x) ** right_val(x)
                    
                    # If it's a simple visit
                    value = self.visit(expr)
                    return value
                
                # Evaluate the full expression
                y_value = evaluate_expression(y_expr)
                
                # If it's a function, apply it to x
                if callable(y_value):
                    return y_value(x)
                
                # If it's a direct value
                return y_value
            
            except Exception as e:
                return 0

        # Determine X range
        if isinstance(x_data, list):
            x_min, x_max = min(x_data), max(x_data)
        elif isinstance(x_data, (int, float)):
            x_min, x_max = -x_data, x_data
        else:
            raise Exception("Error: X debe ser un rango o un número")
        
        plotter = AdvancedPlotter(width=80, height=30)
        
        if isinstance(x_data, list) and isinstance(eval_y_expr(x_data), list) :
            data = list(zip(x_data, eval_y_expr(x_data)))
            plotter.plot_scatter(data)
        else:
            plotter.plot_function(eval_y_expr, x_min, x_max)
            
        plotter.display()
    
    except Exception as e:
        print(f"Plot error: {e}")


  # Visit a parse tree produced by TLONParser#parametro.
  def visitParametro(self, ctx: TLONParser.ParametroContext):
    return self.visitChildren(ctx)


  # Visit a parse tree produced by TLONParser#parExpr.
  def visitParExpr(self, ctx: TLONParser.ParExprContext):
    return self.visit(ctx.expr())

  # Visit a parse tree produced by TLONParser#notExpr.
  def visitNotExpr(self, ctx: TLONParser.NotExprContext):
    value = self.visit(ctx.expr())

    if isinstance(value, TLONVariable__):
      value = value.value

    return not value

  # Visit a parse tree produced by TLONParser#unaryMinusExpr.
  def visitUnaryMinusExpr(self, ctx: TLONParser.UnaryMinusExprContext):
    data = self.visit(ctx.expr())
    if isinstance(data, TLONVariable__):
      data = data.value
    return -data

  # Visit a parse tree produced by TLONParser#multiplicationExpr.
  def visitMultiplicationExpr(self, ctx: TLONParser.MultiplicationExprContext):
    left = self.visit(ctx.expr(0))
    right = self.visit(ctx.expr(1))

    if isinstance(left, TLONVariable__):
      left = left.value
    if isinstance(right, TLONVariable__):
      right = right.value

    if ctx.op.type == TLONParser.MULT:
      return left * right
    if ctx.op.type == TLONParser.DIV:
      value = 0

      if right == 0:
        raise Exception("Error: Can\'t divide by zero.")
      else:
        value = left / right

      return value
    if ctx.op.type == TLONParser.MOD:
      return left % right

  # Visit a parse tree produced by TLONParser#atomExpr.
  def visitAtomExpr(self, ctx: TLONParser.AtomExprContext):
    return self.visitChildren(ctx)

  # Visit a parse tree produced by TLONParser#orExpr.
  def visitOrExpr(self, ctx: TLONParser.OrExprContext):
    left = self.visit(ctx.expr(0))
    right = self.visit(ctx.expr(1))

    if isinstance(left, TLONVariable__):
      left = left.value
    if isinstance(right, TLONVariable__):
      right = right.value

    return left or right

  # Visit a parse tree produced by TLONParser#additiveExpr.
  def visitAdditiveExpr(self, ctx: TLONParser.AdditiveExprContext):
    left = self.visit(ctx.expr(0))
    right = self.visit(ctx.expr(1))

    if isinstance(left, TLONVariable__):
      left = left.value
    if isinstance(right, TLONVariable__):
      right = right.value

    if ctx.op.type == TLONParser.PLUS:
      if isinstance(left, str) or isinstance(right, str):
        return str(left) + str(right)
      return left + right
    if ctx.op.type == TLONParser.MINUS:
      return left - right

  # Visit a parse tree produced by TLONParser#powExpr.
  def visitPowExpr(self, ctx: TLONParser.PowExprContext):
    left = self.visit(ctx.expr(0))
    right = self.visit(ctx.expr(1))

    if isinstance(left, TLONVariable__):
      left = left.value
    if isinstance(right, TLONVariable__):
      right = right.value

    return math.pow(left, right)

  # Visit a parse tree produced by TLONParser#relationalExpr.
  def visitRelationalExpr(self, ctx: TLONParser.RelationalExprContext):
    left = self.visit(ctx.expr(0))
    right = self.visit(ctx.expr(1))

    if isinstance(left, TLONVariable__):
      left = left.value
    if isinstance(right, TLONVariable__):
      right = right.value

    if ctx.op.type == TLONParser.LT:
      return left < right
    if ctx.op.type == TLONParser.LTEQ:
      return left <= right
    if ctx.op.type == TLONParser.GT:
      return left > right
    if ctx.op.type == TLONParser.GTEQ:
      return left >= right

  # Visit a parse tree produced by TLONParser#equalityExpr.
  def visitEqualityExpr(self, ctx: TLONParser.EqualityExprContext):
    left = self.visit(ctx.expr(0))
    right = self.visit(ctx.expr(1))

    if isinstance(left, TLONVariable__):
      left = left.value
    if isinstance(right, TLONVariable__):
      right = right.value

    if ctx.op.type == TLONParser.EQ:
      return left == right
    elif ctx.op.type == TLONParser.NEQ:
      return left != right

    
  def visitMft_special(self, ctx: TLONParser.Mft_specialContext):
    messages = [
        "Modo Muerte instantanea : ACTIVADO",
        "Te estamos vigilando... 👀",
        "A MFT no hay que tenerle miedo, hay que tenerle respeto",
        "MFT Literalmente",
        "Profe MFT Esta...Esta creando un trastorno mental derivado del consumo excesivo de material p*rnografico"
    ]
    import random
    print(random.choice(messages))
    return None

  # Visit a parse tree produced by TLONParser#andExpr.
  def visitAndExpr(self, ctx: TLONParser.AndExprContext):
    left = self.visit(ctx.expr(0))
    right = self.visit(ctx.expr(1))

    if isinstance(left, TLONVariable__):
      left = left.value
    if isinstance(right, TLONVariable__):
      right = right.value

    return left and right

  # Visit a parse tree produced by TLONParser#numberAtom.
  def visitNumberAtom(self, ctx: TLONParser.NumberAtomContext):
    if ctx.INT() is not None:
      return int(ctx.INT().getText())

    return float(ctx.FLOAT().getText())

  # Visit a parse tree produced by TLONParser#booleanAtom.
  def visitBooleanAtom(self, ctx: TLONParser.BooleanAtomContext):
    if ctx.TRUE() is not None:
      return True

    return False

  # Visit a parse tree produced by TLONParser#stringAtom.
  def visitStringAtom(self, ctx: TLONParser.StringAtomContext):
    string = str(ctx.STRING().getText())
    string = string[1:len(string) - 1]

    return string

  # Visit a parse tree produced by TLONParser#arrayAtom.
  def visitArrayAtom(self, ctx: TLONParser.ArrayAtomContext):
    return self.visit(ctx.array());

  # Visit a parse tree produced by TLONParser#objetoAtom.
  def visitObjetoAtom(self, ctx: TLONParser.ObjetoAtomContext):
    return self.visitChildren(ctx)

  def visitAccessToarray(self, ctx: TLONParser.AccessToarrayContext):
    return self.visitChildren(ctx)
    
  # Visit a parse tree produced by TLONParser#accessVariable.
  def visitAccessVariable(self, ctx: TLONParser.AccessVariableContext):
    return self.visitChildren(ctx)

  # Visit a parse tree produced by TLONParser#nilAtom.
  def visitNilAtom(self, ctx: TLONParser.NilAtomContext):
    return None

  # Visit a parse tree produced by TLONParser#objeto.
  def visitObjeto(self, ctx: TLONParser.ObjetoContext):
    items = {}

    for it in ctx.keyvalue():
      item = self.visit(it)
      items[item.name] = item

    return items

  # Visit a parse tree produced by TLONParser#keyvalue.
  def visitKeyvalue(self, ctx: TLONParser.KeyvalueContext):
    name = str(ctx.ID())
    value = self.visit(ctx.expr())

    obj = TLONVariable__(name, value, 'any')

    return obj
