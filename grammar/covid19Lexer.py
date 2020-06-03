# Generated from grammar/covid19.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from semantics import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\66")
        buf.write("\u016e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3")
        buf.write("\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3.\6.\u0131")
        buf.write("\n.\r.\16.\u0132\3/\6/\u0136\n/\r/\16/\u0137\3/\3/\6/")
        buf.write("\u013c\n/\r/\16/\u013d\3\60\3\60\7\60\u0142\n\60\f\60")
        buf.write("\16\60\u0145\13\60\3\60\3\60\3\61\3\61\3\61\3\61\3\62")
        buf.write("\3\62\7\62\u014f\n\62\f\62\16\62\u0152\13\62\3\63\3\63")
        buf.write("\5\63\u0156\n\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3")
        buf.write("\64\3\64\7\64\u0161\n\64\f\64\16\64\u0164\13\64\3\64\3")
        buf.write("\64\3\65\6\65\u0169\n\65\r\65\16\65\u016a\3\65\3\65\3")
        buf.write("\u0143\2\66\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66\3")
        buf.write("\2\7\3\2\62;\5\2C\\aac|\6\2\62;C\\aac|\4\2\f\f\17\17\5")
        buf.write("\2\13\f\16\17\"\"\2\u0175\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\3k\3\2\2\2")
        buf.write("\5o\3\2\2\2\7u\3\2\2\2\t|\3\2\2\2\13\u0081\3\2\2\2\r\u008b")
        buf.write("\3\2\2\2\17\u008f\3\2\2\2\21\u0097\3\2\2\2\23\u00a4\3")
        buf.write("\2\2\2\25\u00a7\3\2\2\2\27\u00b0\3\2\2\2\31\u00b5\3\2")
        buf.write("\2\2\33\u00bd\3\2\2\2\35\u00c1\3\2\2\2\37\u00c9\3\2\2")
        buf.write("\2!\u00d2\3\2\2\2#\u00dc\3\2\2\2%\u00e2\3\2\2\2\'\u00e8")
        buf.write("\3\2\2\2)\u00ee\3\2\2\2+\u00f7\3\2\2\2-\u00fb\3\2\2\2")
        buf.write("/\u00fd\3\2\2\2\61\u00ff\3\2\2\2\63\u0101\3\2\2\2\65\u0103")
        buf.write("\3\2\2\2\67\u0105\3\2\2\29\u0107\3\2\2\2;\u0109\3\2\2")
        buf.write("\2=\u010b\3\2\2\2?\u010d\3\2\2\2A\u010f\3\2\2\2C\u0111")
        buf.write("\3\2\2\2E\u0113\3\2\2\2G\u0116\3\2\2\2I\u0119\3\2\2\2")
        buf.write("K\u011c\3\2\2\2M\u011f\3\2\2\2O\u0121\3\2\2\2Q\u0123\3")
        buf.write("\2\2\2S\u0125\3\2\2\2U\u0127\3\2\2\2W\u0129\3\2\2\2Y\u012c")
        buf.write("\3\2\2\2[\u0130\3\2\2\2]\u0135\3\2\2\2_\u013f\3\2\2\2")
        buf.write("a\u0148\3\2\2\2c\u014c\3\2\2\2e\u0153\3\2\2\2g\u015c\3")
        buf.write("\2\2\2i\u0168\3\2\2\2kl\7k\2\2lm\7p\2\2mn\7v\2\2n\4\3")
        buf.write("\2\2\2op\7h\2\2pq\7n\2\2qr\7q\2\2rs\7c\2\2st\7v\2\2t\6")
        buf.write("\3\2\2\2uv\7u\2\2vw\7v\2\2wx\7t\2\2xy\7k\2\2yz\7p\2\2")
        buf.write("z{\7i\2\2{\b\3\2\2\2|}\7e\2\2}~\7j\2\2~\177\7c\2\2\177")
        buf.write("\u0080\7t\2\2\u0080\n\3\2\2\2\u0081\u0082\7F\2\2\u0082")
        buf.write("\u0083\7c\2\2\u0083\u0084\7v\2\2\u0084\u0085\7c\2\2\u0085")
        buf.write("\u0086\7h\2\2\u0086\u0087\7t\2\2\u0087\u0088\7c\2\2\u0088")
        buf.write("\u0089\7o\2\2\u0089\u008a\7g\2\2\u008a\f\3\2\2\2\u008b")
        buf.write("\u008c\7x\2\2\u008c\u008d\7c\2\2\u008d\u008e\7t\2\2\u008e")
        buf.write("\16\3\2\2\2\u008f\u0090\7h\2\2\u0090\u0091\7w\2\2\u0091")
        buf.write("\u0092\7p\2\2\u0092\u0093\7e\2\2\u0093\u0094\7k\2\2\u0094")
        buf.write("\u0095\7q\2\2\u0095\u0096\7p\2\2\u0096\20\3\2\2\2\u0097")
        buf.write("\u0098\7E\2\2\u0098\u0099\7c\2\2\u0099\u009a\7t\2\2\u009a")
        buf.write("\u009b\7i\2\2\u009b\u009c\7c\2\2\u009c\u009d\7C\2\2\u009d")
        buf.write("\u009e\7t\2\2\u009e\u009f\7e\2\2\u009f\u00a0\7j\2\2\u00a0")
        buf.write("\u00a1\7k\2\2\u00a1\u00a2\7x\2\2\u00a2\u00a3\7q\2\2\u00a3")
        buf.write("\22\3\2\2\2\u00a4\u00a5\7u\2\2\u00a5\u00a6\7k\2\2\u00a6")
        buf.write("\24\3\2\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9\7p\2\2\u00a9")
        buf.write("\u00aa\7v\2\2\u00aa\u00ab\7q\2\2\u00ab\u00ac\7p\2\2\u00ac")
        buf.write("\u00ad\7e\2\2\u00ad\u00ae\7g\2\2\u00ae\u00af\7u\2\2\u00af")
        buf.write("\26\3\2\2\2\u00b0\u00b1\7u\2\2\u00b1\u00b2\7k\2\2\u00b2")
        buf.write("\u00b3\7p\2\2\u00b3\u00b4\7q\2\2\u00b4\30\3\2\2\2\u00b5")
        buf.write("\u00b6\7g\2\2\u00b6\u00b7\7u\2\2\u00b7\u00b8\7e\2\2\u00b8")
        buf.write("\u00b9\7t\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb\7d\2\2\u00bb")
        buf.write("\u00bc\7g\2\2\u00bc\32\3\2\2\2\u00bd\u00be\7n\2\2\u00be")
        buf.write("\u00bf\7g\2\2\u00bf\u00c0\7g\2\2\u00c0\34\3\2\2\2\u00c1")
        buf.write("\u00c2\7t\2\2\u00c2\u00c3\7g\2\2\u00c3\u00c4\7i\2\2\u00c4")
        buf.write("\u00c5\7t\2\2\u00c5\u00c6\7g\2\2\u00c6\u00c7\7u\2\2\u00c7")
        buf.write("\u00c8\7c\2\2\u00c8\36\3\2\2\2\u00c9\u00ca\7R\2\2\u00ca")
        buf.write("\u00cb\7t\2\2\u00cb\u00cc\7q\2\2\u00cc\u00cd\7i\2\2\u00cd")
        buf.write("\u00ce\7t\2\2\u00ce\u00cf\7c\2\2\u00cf\u00d0\7o\2\2\u00d0")
        buf.write("\u00d1\7c\2\2\u00d1 \3\2\2\2\u00d2\u00d3\7r\2\2\u00d3")
        buf.write("\u00d4\7t\2\2\u00d4\u00d5\7k\2\2\u00d5\u00d6\7p\2\2\u00d6")
        buf.write("\u00d7\7e\2\2\u00d7\u00d8\7k\2\2\u00d8\u00d9\7r\2\2\u00d9")
        buf.write("\u00da\7c\2\2\u00da\u00db\7n\2\2\u00db\"\3\2\2\2\u00dc")
        buf.write("\u00dd\7f\2\2\u00dd\u00de\7g\2\2\u00de\u00df\7u\2\2\u00df")
        buf.write("\u00e0\7f\2\2\u00e0\u00e1\7g\2\2\u00e1$\3\2\2\2\u00e2")
        buf.write("\u00e3\7j\2\2\u00e3\u00e4\7c\2\2\u00e4\u00e5\7u\2\2\u00e5")
        buf.write("\u00e6\7v\2\2\u00e6\u00e7\7c\2\2\u00e7&\3\2\2\2\u00e8")
        buf.write("\u00e9\7j\2\2\u00e9\u00ea\7c\2\2\u00ea\u00eb\7e\2\2\u00eb")
        buf.write("\u00ec\7g\2\2\u00ec\u00ed\7t\2\2\u00ed(\3\2\2\2\u00ee")
        buf.write("\u00ef\7o\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1\7g\2\2\u00f1")
        buf.write("\u00f2\7p\2\2\u00f2\u00f3\7v\2\2\u00f3\u00f4\7t\2\2\u00f4")
        buf.write("\u00f5\7c\2\2\u00f5\u00f6\7u\2\2\u00f6*\3\2\2\2\u00f7")
        buf.write("\u00f8\7j\2\2\u00f8\u00f9\7c\2\2\u00f9\u00fa\7|\2\2\u00fa")
        buf.write(",\3\2\2\2\u00fb\u00fc\7=\2\2\u00fc.\3\2\2\2\u00fd\u00fe")
        buf.write("\7.\2\2\u00fe\60\3\2\2\2\u00ff\u0100\7<\2\2\u0100\62\3")
        buf.write("\2\2\2\u0101\u0102\7}\2\2\u0102\64\3\2\2\2\u0103\u0104")
        buf.write("\7\177\2\2\u0104\66\3\2\2\2\u0105\u0106\7?\2\2\u01068")
        buf.write("\3\2\2\2\u0107\u0108\7*\2\2\u0108:\3\2\2\2\u0109\u010a")
        buf.write("\7+\2\2\u010a<\3\2\2\2\u010b\u010c\7]\2\2\u010c>\3\2\2")
        buf.write("\2\u010d\u010e\7_\2\2\u010e@\3\2\2\2\u010f\u0110\7@\2")
        buf.write("\2\u0110B\3\2\2\2\u0111\u0112\7>\2\2\u0112D\3\2\2\2\u0113")
        buf.write("\u0114\7@\2\2\u0114\u0115\7?\2\2\u0115F\3\2\2\2\u0116")
        buf.write("\u0117\7>\2\2\u0117\u0118\7?\2\2\u0118H\3\2\2\2\u0119")
        buf.write("\u011a\7?\2\2\u011a\u011b\7?\2\2\u011bJ\3\2\2\2\u011c")
        buf.write("\u011d\7#\2\2\u011d\u011e\7?\2\2\u011eL\3\2\2\2\u011f")
        buf.write("\u0120\7#\2\2\u0120N\3\2\2\2\u0121\u0122\7-\2\2\u0122")
        buf.write("P\3\2\2\2\u0123\u0124\7/\2\2\u0124R\3\2\2\2\u0125\u0126")
        buf.write("\7,\2\2\u0126T\3\2\2\2\u0127\u0128\7\61\2\2\u0128V\3\2")
        buf.write("\2\2\u0129\u012a\7(\2\2\u012a\u012b\7(\2\2\u012bX\3\2")
        buf.write("\2\2\u012c\u012d\7~\2\2\u012d\u012e\7~\2\2\u012eZ\3\2")
        buf.write("\2\2\u012f\u0131\t\2\2\2\u0130\u012f\3\2\2\2\u0131\u0132")
        buf.write("\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133")
        buf.write("\\\3\2\2\2\u0134\u0136\t\2\2\2\u0135\u0134\3\2\2\2\u0136")
        buf.write("\u0137\3\2\2\2\u0137\u0135\3\2\2\2\u0137\u0138\3\2\2\2")
        buf.write("\u0138\u0139\3\2\2\2\u0139\u013b\7\60\2\2\u013a\u013c")
        buf.write("\t\2\2\2\u013b\u013a\3\2\2\2\u013c\u013d\3\2\2\2\u013d")
        buf.write("\u013b\3\2\2\2\u013d\u013e\3\2\2\2\u013e^\3\2\2\2\u013f")
        buf.write("\u0143\7$\2\2\u0140\u0142\13\2\2\2\u0141\u0140\3\2\2\2")
        buf.write("\u0142\u0145\3\2\2\2\u0143\u0144\3\2\2\2\u0143\u0141\3")
        buf.write("\2\2\2\u0144\u0146\3\2\2\2\u0145\u0143\3\2\2\2\u0146\u0147")
        buf.write("\7$\2\2\u0147`\3\2\2\2\u0148\u0149\7)\2\2\u0149\u014a")
        buf.write("\13\2\2\2\u014a\u014b\7)\2\2\u014bb\3\2\2\2\u014c\u0150")
        buf.write("\t\3\2\2\u014d\u014f\t\4\2\2\u014e\u014d\3\2\2\2\u014f")
        buf.write("\u0152\3\2\2\2\u0150\u014e\3\2\2\2\u0150\u0151\3\2\2\2")
        buf.write("\u0151d\3\2\2\2\u0152\u0150\3\2\2\2\u0153\u0155\7\61\2")
        buf.write("\2\u0154\u0156\13\2\2\2\u0155\u0154\3\2\2\2\u0155\u0156")
        buf.write("\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0158\7,\2\2\u0158")
        buf.write("\u0159\7\61\2\2\u0159\u015a\3\2\2\2\u015a\u015b\b\63\2")
        buf.write("\2\u015bf\3\2\2\2\u015c\u015d\7\61\2\2\u015d\u015e\7\61")
        buf.write("\2\2\u015e\u0162\3\2\2\2\u015f\u0161\n\5\2\2\u0160\u015f")
        buf.write("\3\2\2\2\u0161\u0164\3\2\2\2\u0162\u0160\3\2\2\2\u0162")
        buf.write("\u0163\3\2\2\2\u0163\u0165\3\2\2\2\u0164\u0162\3\2\2\2")
        buf.write("\u0165\u0166\b\64\2\2\u0166h\3\2\2\2\u0167\u0169\t\6\2")
        buf.write("\2\u0168\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u0168")
        buf.write("\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016c\3\2\2\2\u016c")
        buf.write("\u016d\b\65\2\2\u016dj\3\2\2\2\13\2\u0132\u0137\u013d")
        buf.write("\u0143\u0150\u0155\u0162\u016a\3\b\2\2")
        return buf.getvalue()


class covid19Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    FLOAT = 2
    STRING = 3
    CHAR = 4
    DATAFRAME = 5
    VAR = 6
    FUNCION = 7
    CARGAARCHIVO = 8
    SI = 9
    ENTONCES = 10
    SINO = 11
    ESCRIBE = 12
    LEE = 13
    REGRESA = 14
    PROGRAMA = 15
    PRINCIPAL = 16
    DESDE = 17
    HASTA = 18
    HACER = 19
    MIENTRAS = 20
    HAZ = 21
    PUNTOYCOMA = 22
    COMA = 23
    DOSPUNTOS = 24
    CORCHETEI = 25
    CORCHETED = 26
    IGUAL = 27
    PARENTESISI = 28
    PARENTESISD = 29
    CORCHETECUADRADOI = 30
    CORCHETECUADRADOD = 31
    MAYOR = 32
    MENOR = 33
    MAYORIGUAL = 34
    MENORIGUAL = 35
    IGUALCOMP = 36
    DIFERENTE = 37
    NEGACION = 38
    SUMA = 39
    RESTA = 40
    MULTIPLICACION = 41
    DIVISION = 42
    Y = 43
    O = 44
    CTEINT = 45
    CTEFLOAT = 46
    CTESTRING = 47
    CTECHAR = 48
    ID = 49
    COMENTARIO = 50
    LINEACOMENTADA = 51
    WS = 52

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'string'", "'char'", "'Dataframe'", "'var'", 
            "'funcion'", "'CargaArchivo'", "'si'", "'entonces'", "'sino'", 
            "'escribe'", "'lee'", "'regresa'", "'Programa'", "'principal'", 
            "'desde'", "'hasta'", "'hacer'", "'mientras'", "'haz'", "';'", 
            "','", "':'", "'{'", "'}'", "'='", "'('", "')'", "'['", "']'", 
            "'>'", "'<'", "'>='", "'<='", "'=='", "'!='", "'!'", "'+'", 
            "'-'", "'*'", "'/'", "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "STRING", "CHAR", "DATAFRAME", "VAR", "FUNCION", 
            "CARGAARCHIVO", "SI", "ENTONCES", "SINO", "ESCRIBE", "LEE", 
            "REGRESA", "PROGRAMA", "PRINCIPAL", "DESDE", "HASTA", "HACER", 
            "MIENTRAS", "HAZ", "PUNTOYCOMA", "COMA", "DOSPUNTOS", "CORCHETEI", 
            "CORCHETED", "IGUAL", "PARENTESISI", "PARENTESISD", "CORCHETECUADRADOI", 
            "CORCHETECUADRADOD", "MAYOR", "MENOR", "MAYORIGUAL", "MENORIGUAL", 
            "IGUALCOMP", "DIFERENTE", "NEGACION", "SUMA", "RESTA", "MULTIPLICACION", 
            "DIVISION", "Y", "O", "CTEINT", "CTEFLOAT", "CTESTRING", "CTECHAR", 
            "ID", "COMENTARIO", "LINEACOMENTADA", "WS" ]

    ruleNames = [ "INT", "FLOAT", "STRING", "CHAR", "DATAFRAME", "VAR", 
                  "FUNCION", "CARGAARCHIVO", "SI", "ENTONCES", "SINO", "ESCRIBE", 
                  "LEE", "REGRESA", "PROGRAMA", "PRINCIPAL", "DESDE", "HASTA", 
                  "HACER", "MIENTRAS", "HAZ", "PUNTOYCOMA", "COMA", "DOSPUNTOS", 
                  "CORCHETEI", "CORCHETED", "IGUAL", "PARENTESISI", "PARENTESISD", 
                  "CORCHETECUADRADOI", "CORCHETECUADRADOD", "MAYOR", "MENOR", 
                  "MAYORIGUAL", "MENORIGUAL", "IGUALCOMP", "DIFERENTE", 
                  "NEGACION", "SUMA", "RESTA", "MULTIPLICACION", "DIVISION", 
                  "Y", "O", "CTEINT", "CTEFLOAT", "CTESTRING", "CTECHAR", 
                  "ID", "COMENTARIO", "LINEACOMENTADA", "WS" ]

    grammarFileName = "covid19.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


