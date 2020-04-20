# Generated from covid19.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\3")
        buf.write("\13\b\1\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\2\2\3\3\3\3\2")
        buf.write("\2\2\n\2\3\3\2\2\2\3\5\3\2\2\2\5\6\7j\2\2\6\7\7g\2\2\7")
        buf.write("\b\7n\2\2\b\t\7n\2\2\t\n\7q\2\2\n\4\3\2\2\2\3\2\2")
        return buf.getvalue()


class covid19Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    HOLA = 1

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'hello'" ]

    symbolicNames = [ "<INVALID>",
            "HOLA" ]

    ruleNames = [ "HOLA" ]

    grammarFileName = "covid19.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


