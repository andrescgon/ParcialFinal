from antlr4 import *
from core import *

from antlr4.error.ErrorListener import ErrorListener


class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Error de sintaxis en línea {line}, columna {column}:")
        print(f"Símbolo problemático: {offendingSymbol}")
        print(f"Mensaje: {msg}")
        
        # Imprimir los tokens actuales para diagnóstico
        print("Tokens actuales:")
        tokens = recognizer.getInputStream()
        for i in range(max(0, tokens.index - 5), min(tokens.size, tokens.index + 5)):
            token = tokens.get(i)
            print(f"Token {i}: {token.text} (Tipo: {token.type})")

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        print(f"ADVERTENCIA: Ambigüedad detectada")
        print(f"Índices: {startIndex}-{stopIndex}")
        print(f"Alternativas ambiguas: {ambigAlts}")
        # Opcional: continuar con el parsing
        return

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        print(f"ADVERTENCIA: Intentando contexto completo")
        print(f"Índices: {startIndex}-{stopIndex}")
        print(f"Alternativas en conflicto: {conflictingAlts}")
        # Opcional: permitir continuar
        return

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        print(f"ADVERTENCIA: Sensibilidad contextual")
        print(f"Índices: {startIndex}-{stopIndex}")
        return
     
def print_parse_tree(tree, parser, indent=''):
    if isinstance(tree, TerminalNode):
        print(f"{indent}Terminal: {tree.getText()}")
        return
    
    rule_name = parser.ruleNames[tree.getRuleIndex()]
    print(f"{indent}Rule: {rule_name}")
    
    for i in range(tree.getChildCount()):
        child = tree.getChild(i)
        print_parse_tree(child, parser, indent + '  ')

def main():

  print("""
  ███████████████████████████████████████████████████████████████████████████████████
  ██                                                                               ██
  ██                                                                               ██
  ██              ██████████   ██        ██████     █████     ██                   ██
  ██                  ██       ██      ██      ██   ██  ██    ██                   ██
  ██                  ██       ██      ██      ██   ██   ██   ██                   ██
  ██                  ██       ██      ██      ██   ██    ██  ██                   ██
  ██                  ██       ██████    ██████     ██      ████                   ██
  ██                                                                               ██
  ██                                 Non Plus Ultra                                ██
  ██                                                                               ██
  ██                   The Programming Language for Machine Learning               ██
  ██                                                                               ██
  ███████████████████████████████████████████████████████████████████████████████████
 """)



  visitor = Visitor()

  if len(sys.argv) > 1:
    try:
      input_stream = FileStream(sys.argv[1])
    except Exception as e:
      raise Exception('File not Found.')

    lexer = TLONLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = TLONParser(token_stream)
    tree = parser.from_file()

    visitor.visit(tree)
    #print_parse_tree(tree, parser)
  else:
    while True:
      print('>>> ', end='', flush=True)
      input_data = sys.stdin.readline().strip()
      tabs = input_data.count('{') + input_data.count('funcion') - \
             input_data.count('}') - input_data.count('end')

      if 'machetear' in input_data:
        print ('Ahhhh me machetearon...Muere')
        break

      while tabs > 0:
        print ('... ', end='', flush=True)
        input_data = input_data + sys.stdin.readline()
        tabs = input_data.count('{') + input_data.count('funcion') - input_data.count('}') - input_data.count('end')
      
      input_stream = InputStream(input_data)

      lexer = TLONLexer(input_stream)
      token_stream = CommonTokenStream(lexer)
      parser = TLONParser(token_stream)
      parser._listeners = [ MyErrorListener() ]
      tree = parser.parse()
      #imprime el arbol de parseo
      print_parse_tree(tree, parser)
      result=None
      try:
        result = visitor.visit(tree)
      except Exception as e:
        if type(e)!= AttributeError:
          print(e)
        

      if result is not None:
        print (result)


if __name__ == '__main__':
  main()
