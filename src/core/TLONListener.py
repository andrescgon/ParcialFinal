# Generated from TLON.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TLONParser import TLONParser
else:
    from TLONParser import TLONParser

# This class defines a complete listener for a parse tree produced by TLONParser.
class TLONListener(ParseTreeListener):

    # Enter a parse tree produced by TLONParser#parse.
    def enterParse(self, ctx:TLONParser.ParseContext):
        pass

    # Exit a parse tree produced by TLONParser#parse.
    def exitParse(self, ctx:TLONParser.ParseContext):
        pass


    # Enter a parse tree produced by TLONParser#from_input.
    def enterFrom_input(self, ctx:TLONParser.From_inputContext):
        pass

    # Exit a parse tree produced by TLONParser#from_input.
    def exitFrom_input(self, ctx:TLONParser.From_inputContext):
        pass


    # Enter a parse tree produced by TLONParser#from_file.
    def enterFrom_file(self, ctx:TLONParser.From_fileContext):
        pass

    # Exit a parse tree produced by TLONParser#from_file.
    def exitFrom_file(self, ctx:TLONParser.From_fileContext):
        pass


    # Enter a parse tree produced by TLONParser#stat.
    def enterStat(self, ctx:TLONParser.StatContext):
        pass

    # Exit a parse tree produced by TLONParser#stat.
    def exitStat(self, ctx:TLONParser.StatContext):
        pass


    # Enter a parse tree produced by TLONParser#compound_stat.
    def enterCompound_stat(self, ctx:TLONParser.Compound_statContext):
        pass

    # Exit a parse tree produced by TLONParser#compound_stat.
    def exitCompound_stat(self, ctx:TLONParser.Compound_statContext):
        pass


    # Enter a parse tree produced by TLONParser#simple_stat.
    def enterSimple_stat(self, ctx:TLONParser.Simple_statContext):
        pass

    # Exit a parse tree produced by TLONParser#simple_stat.
    def exitSimple_stat(self, ctx:TLONParser.Simple_statContext):
        pass


    # Enter a parse tree produced by TLONParser#linear_regression.
    def enterLinear_regression(self, ctx:TLONParser.Linear_regressionContext):
        pass

    # Exit a parse tree produced by TLONParser#linear_regression.
    def exitLinear_regression(self, ctx:TLONParser.Linear_regressionContext):
        pass


    # Enter a parse tree produced by TLONParser#mlp_expr.
    def enterMlp_expr(self, ctx:TLONParser.Mlp_exprContext):
        pass

    # Exit a parse tree produced by TLONParser#mlp_expr.
    def exitMlp_expr(self, ctx:TLONParser.Mlp_exprContext):
        pass


    # Enter a parse tree produced by TLONParser#mlp_train.
    def enterMlp_train(self, ctx:TLONParser.Mlp_trainContext):
        pass

    # Exit a parse tree produced by TLONParser#mlp_train.
    def exitMlp_train(self, ctx:TLONParser.Mlp_trainContext):
        pass


    # Enter a parse tree produced by TLONParser#mlp_predict.
    def enterMlp_predict(self, ctx:TLONParser.Mlp_predictContext):
        pass

    # Exit a parse tree produced by TLONParser#mlp_predict.
    def exitMlp_predict(self, ctx:TLONParser.Mlp_predictContext):
        pass


    # Enter a parse tree produced by TLONParser#clustering.
    def enterClustering(self, ctx:TLONParser.ClusteringContext):
        pass

    # Exit a parse tree produced by TLONParser#clustering.
    def exitClustering(self, ctx:TLONParser.ClusteringContext):
        pass


    # Enter a parse tree produced by TLONParser#clusteringPredict.
    def enterClusteringPredict(self, ctx:TLONParser.ClusteringPredictContext):
        pass

    # Exit a parse tree produced by TLONParser#clusteringPredict.
    def exitClusteringPredict(self, ctx:TLONParser.ClusteringPredictContext):
        pass


    # Enter a parse tree produced by TLONParser#plot.
    def enterPlot(self, ctx:TLONParser.PlotContext):
        pass

    # Exit a parse tree produced by TLONParser#plot.
    def exitPlot(self, ctx:TLONParser.PlotContext):
        pass


    # Enter a parse tree produced by TLONParser#mft_special.
    def enterMft_special(self, ctx:TLONParser.Mft_specialContext):
        pass

    # Exit a parse tree produced by TLONParser#mft_special.
    def exitMft_special(self, ctx:TLONParser.Mft_specialContext):
        pass


    # Enter a parse tree produced by TLONParser#assignment.
    def enterAssignment(self, ctx:TLONParser.AssignmentContext):
        pass

    # Exit a parse tree produced by TLONParser#assignment.
    def exitAssignment(self, ctx:TLONParser.AssignmentContext):
        pass


    # Enter a parse tree produced by TLONParser#if_stat.
    def enterIf_stat(self, ctx:TLONParser.If_statContext):
        pass

    # Exit a parse tree produced by TLONParser#if_stat.
    def exitIf_stat(self, ctx:TLONParser.If_statContext):
        pass


    # Enter a parse tree produced by TLONParser#while_stat.
    def enterWhile_stat(self, ctx:TLONParser.While_statContext):
        pass

    # Exit a parse tree produced by TLONParser#while_stat.
    def exitWhile_stat(self, ctx:TLONParser.While_statContext):
        pass


    # Enter a parse tree produced by TLONParser#for_stat.
    def enterFor_stat(self, ctx:TLONParser.For_statContext):
        pass

    # Exit a parse tree produced by TLONParser#for_stat.
    def exitFor_stat(self, ctx:TLONParser.For_statContext):
        pass


    # Enter a parse tree produced by TLONParser#log.
    def enterLog(self, ctx:TLONParser.LogContext):
        pass

    # Exit a parse tree produced by TLONParser#log.
    def exitLog(self, ctx:TLONParser.LogContext):
        pass


    # Enter a parse tree produced by TLONParser#funcion.
    def enterFuncion(self, ctx:TLONParser.FuncionContext):
        pass

    # Exit a parse tree produced by TLONParser#funcion.
    def exitFuncion(self, ctx:TLONParser.FuncionContext):
        pass


    # Enter a parse tree produced by TLONParser#importar.
    def enterImportar(self, ctx:TLONParser.ImportarContext):
        pass

    # Exit a parse tree produced by TLONParser#importar.
    def exitImportar(self, ctx:TLONParser.ImportarContext):
        pass


    # Enter a parse tree produced by TLONParser#retornar.
    def enterRetornar(self, ctx:TLONParser.RetornarContext):
        pass

    # Exit a parse tree produced by TLONParser#retornar.
    def exitRetornar(self, ctx:TLONParser.RetornarContext):
        pass


    # Enter a parse tree produced by TLONParser#condition_block.
    def enterCondition_block(self, ctx:TLONParser.Condition_blockContext):
        pass

    # Exit a parse tree produced by TLONParser#condition_block.
    def exitCondition_block(self, ctx:TLONParser.Condition_blockContext):
        pass


    # Enter a parse tree produced by TLONParser#stat_block.
    def enterStat_block(self, ctx:TLONParser.Stat_blockContext):
        pass

    # Exit a parse tree produced by TLONParser#stat_block.
    def exitStat_block(self, ctx:TLONParser.Stat_blockContext):
        pass


    # Enter a parse tree produced by TLONParser#array.
    def enterArray(self, ctx:TLONParser.ArrayContext):
        pass

    # Exit a parse tree produced by TLONParser#array.
    def exitArray(self, ctx:TLONParser.ArrayContext):
        pass


    # Enter a parse tree produced by TLONParser#accessarray.
    def enterAccessarray(self, ctx:TLONParser.AccessarrayContext):
        pass

    # Exit a parse tree produced by TLONParser#accessarray.
    def exitAccessarray(self, ctx:TLONParser.AccessarrayContext):
        pass


    # Enter a parse tree produced by TLONParser#variable.
    def enterVariable(self, ctx:TLONParser.VariableContext):
        pass

    # Exit a parse tree produced by TLONParser#variable.
    def exitVariable(self, ctx:TLONParser.VariableContext):
        pass


    # Enter a parse tree produced by TLONParser#parametro.
    def enterParametro(self, ctx:TLONParser.ParametroContext):
        pass

    # Exit a parse tree produced by TLONParser#parametro.
    def exitParametro(self, ctx:TLONParser.ParametroContext):
        pass


    # Enter a parse tree produced by TLONParser#atomExpr.
    def enterAtomExpr(self, ctx:TLONParser.AtomExprContext):
        pass

    # Exit a parse tree produced by TLONParser#atomExpr.
    def exitAtomExpr(self, ctx:TLONParser.AtomExprContext):
        pass


    # Enter a parse tree produced by TLONParser#orExpr.
    def enterOrExpr(self, ctx:TLONParser.OrExprContext):
        pass

    # Exit a parse tree produced by TLONParser#orExpr.
    def exitOrExpr(self, ctx:TLONParser.OrExprContext):
        pass


    # Enter a parse tree produced by TLONParser#accessArrayExpr.
    def enterAccessArrayExpr(self, ctx:TLONParser.AccessArrayExprContext):
        pass

    # Exit a parse tree produced by TLONParser#accessArrayExpr.
    def exitAccessArrayExpr(self, ctx:TLONParser.AccessArrayExprContext):
        pass


    # Enter a parse tree produced by TLONParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:TLONParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by TLONParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:TLONParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by TLONParser#relationalExpr.
    def enterRelationalExpr(self, ctx:TLONParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by TLONParser#relationalExpr.
    def exitRelationalExpr(self, ctx:TLONParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by TLONParser#comunidadExpr.
    def enterComunidadExpr(self, ctx:TLONParser.ComunidadExprContext):
        pass

    # Exit a parse tree produced by TLONParser#comunidadExpr.
    def exitComunidadExpr(self, ctx:TLONParser.ComunidadExprContext):
        pass


    # Enter a parse tree produced by TLONParser#parExpr.
    def enterParExpr(self, ctx:TLONParser.ParExprContext):
        pass

    # Exit a parse tree produced by TLONParser#parExpr.
    def exitParExpr(self, ctx:TLONParser.ParExprContext):
        pass


    # Enter a parse tree produced by TLONParser#notExpr.
    def enterNotExpr(self, ctx:TLONParser.NotExprContext):
        pass

    # Exit a parse tree produced by TLONParser#notExpr.
    def exitNotExpr(self, ctx:TLONParser.NotExprContext):
        pass


    # Enter a parse tree produced by TLONParser#unaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:TLONParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by TLONParser#unaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:TLONParser.UnaryMinusExprContext):
        pass


    # Enter a parse tree produced by TLONParser#agenteExpr.
    def enterAgenteExpr(self, ctx:TLONParser.AgenteExprContext):
        pass

    # Exit a parse tree produced by TLONParser#agenteExpr.
    def exitAgenteExpr(self, ctx:TLONParser.AgenteExprContext):
        pass


    # Enter a parse tree produced by TLONParser#mlpExpr.
    def enterMlpExpr(self, ctx:TLONParser.MlpExprContext):
        pass

    # Exit a parse tree produced by TLONParser#mlpExpr.
    def exitMlpExpr(self, ctx:TLONParser.MlpExprContext):
        pass


    # Enter a parse tree produced by TLONParser#multiplicationExpr.
    def enterMultiplicationExpr(self, ctx:TLONParser.MultiplicationExprContext):
        pass

    # Exit a parse tree produced by TLONParser#multiplicationExpr.
    def exitMultiplicationExpr(self, ctx:TLONParser.MultiplicationExprContext):
        pass


    # Enter a parse tree produced by TLONParser#powExpr.
    def enterPowExpr(self, ctx:TLONParser.PowExprContext):
        pass

    # Exit a parse tree produced by TLONParser#powExpr.
    def exitPowExpr(self, ctx:TLONParser.PowExprContext):
        pass


    # Enter a parse tree produced by TLONParser#equalityExpr.
    def enterEqualityExpr(self, ctx:TLONParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by TLONParser#equalityExpr.
    def exitEqualityExpr(self, ctx:TLONParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by TLONParser#andExpr.
    def enterAndExpr(self, ctx:TLONParser.AndExprContext):
        pass

    # Exit a parse tree produced by TLONParser#andExpr.
    def exitAndExpr(self, ctx:TLONParser.AndExprContext):
        pass


    # Enter a parse tree produced by TLONParser#numberAtom.
    def enterNumberAtom(self, ctx:TLONParser.NumberAtomContext):
        pass

    # Exit a parse tree produced by TLONParser#numberAtom.
    def exitNumberAtom(self, ctx:TLONParser.NumberAtomContext):
        pass


    # Enter a parse tree produced by TLONParser#booleanAtom.
    def enterBooleanAtom(self, ctx:TLONParser.BooleanAtomContext):
        pass

    # Exit a parse tree produced by TLONParser#booleanAtom.
    def exitBooleanAtom(self, ctx:TLONParser.BooleanAtomContext):
        pass


    # Enter a parse tree produced by TLONParser#stringAtom.
    def enterStringAtom(self, ctx:TLONParser.StringAtomContext):
        pass

    # Exit a parse tree produced by TLONParser#stringAtom.
    def exitStringAtom(self, ctx:TLONParser.StringAtomContext):
        pass


    # Enter a parse tree produced by TLONParser#arrayAtom.
    def enterArrayAtom(self, ctx:TLONParser.ArrayAtomContext):
        pass

    # Exit a parse tree produced by TLONParser#arrayAtom.
    def exitArrayAtom(self, ctx:TLONParser.ArrayAtomContext):
        pass


    # Enter a parse tree produced by TLONParser#objetoAtom.
    def enterObjetoAtom(self, ctx:TLONParser.ObjetoAtomContext):
        pass

    # Exit a parse tree produced by TLONParser#objetoAtom.
    def exitObjetoAtom(self, ctx:TLONParser.ObjetoAtomContext):
        pass


    # Enter a parse tree produced by TLONParser#accessToarray.
    def enterAccessToarray(self, ctx:TLONParser.AccessToarrayContext):
        pass

    # Exit a parse tree produced by TLONParser#accessToarray.
    def exitAccessToarray(self, ctx:TLONParser.AccessToarrayContext):
        pass


    # Enter a parse tree produced by TLONParser#accessVariable.
    def enterAccessVariable(self, ctx:TLONParser.AccessVariableContext):
        pass

    # Exit a parse tree produced by TLONParser#accessVariable.
    def exitAccessVariable(self, ctx:TLONParser.AccessVariableContext):
        pass


    # Enter a parse tree produced by TLONParser#nilAtom.
    def enterNilAtom(self, ctx:TLONParser.NilAtomContext):
        pass

    # Exit a parse tree produced by TLONParser#nilAtom.
    def exitNilAtom(self, ctx:TLONParser.NilAtomContext):
        pass


    # Enter a parse tree produced by TLONParser#agente.
    def enterAgente(self, ctx:TLONParser.AgenteContext):
        pass

    # Exit a parse tree produced by TLONParser#agente.
    def exitAgente(self, ctx:TLONParser.AgenteContext):
        pass


    # Enter a parse tree produced by TLONParser#comunidad.
    def enterComunidad(self, ctx:TLONParser.ComunidadContext):
        pass

    # Exit a parse tree produced by TLONParser#comunidad.
    def exitComunidad(self, ctx:TLONParser.ComunidadContext):
        pass


    # Enter a parse tree produced by TLONParser#objeto.
    def enterObjeto(self, ctx:TLONParser.ObjetoContext):
        pass

    # Exit a parse tree produced by TLONParser#objeto.
    def exitObjeto(self, ctx:TLONParser.ObjetoContext):
        pass


    # Enter a parse tree produced by TLONParser#keyvalue.
    def enterKeyvalue(self, ctx:TLONParser.KeyvalueContext):
        pass

    # Exit a parse tree produced by TLONParser#keyvalue.
    def exitKeyvalue(self, ctx:TLONParser.KeyvalueContext):
        pass


