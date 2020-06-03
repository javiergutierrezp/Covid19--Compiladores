# Generated from grammar/covid19.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from semantics import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\66")
        buf.write("\u01b9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\6\4Q\n\4\r\4\16\4R\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5a\n\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\5\6k\n\6\3\6\3\6\3\6\5\6p\n\6\3")
        buf.write("\6\3\6\3\6\5\6u\n\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u0087\n\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\7\b\u0092\n\b\f\b\16\b\u0095")
        buf.write("\13\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\5\t\u00a4\n\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\5\t\u00b0\n\t\7\t\u00b2\n\t\f\t\16\t\u00b5\13\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00bf\n\n\3\n\3\n\3")
        buf.write("\n\7\n\u00c4\n\n\f\n\16\n\u00c7\13\n\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\5\13\u00d7\n\13\3\13\3\13\3\13\5\13\u00dc\n\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\5\f\u00e4\n\f\3\f\3\f\3\f\7\f\u00e9")
        buf.write("\n\f\f\f\16\f\u00ec\13\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00f4")
        buf.write("\n\r\3\r\3\r\3\r\7\r\u00f9\n\r\f\r\16\r\u00fc\13\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16")
        buf.write("\u0109\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\5\17\u011f\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\7\20\u012c\n\20\f\20\16\20\u012f")
        buf.write("\13\20\5\20\u0131\n\20\3\20\3\20\3\20\3\20\3\20\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\5\23\u0150\n\23\5\23\u0152\n\23\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\5\24\u015d\n\24\5\24\u015f")
        buf.write("\n\24\3\25\3\25\3\25\3\25\5\25\u0165\n\25\3\25\3\25\3")
        buf.write("\25\3\25\7\25\u016b\n\25\f\25\16\25\u016e\13\25\3\25\3")
        buf.write("\25\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u0178\n\26\f\26")
        buf.write("\16\26\u017b\13\26\3\26\3\26\6\26\u017f\n\26\r\26\16\26")
        buf.write("\u0180\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\31\3\31\3\32\3\32\5\32\u0192\n\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\7\32\u019e\n")
        buf.write("\32\f\32\16\32\u01a1\13\32\5\32\u01a3\n\32\3\32\3\32\3")
        buf.write("\32\5\32\u01a8\n\32\3\32\3\32\3\32\3\32\7\32\u01ae\n\32")
        buf.write("\f\32\16\32\u01b1\13\32\3\32\5\32\u01b4\n\32\3\32\3\32")
        buf.write("\3\32\3\32\2\2\33\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\62\2\3\3\2\3\7\2\u01d7\2\64\3\2\2\2\4")
        buf.write("C\3\2\2\2\6N\3\2\2\2\bV\3\2\2\2\nd\3\2\2\2\f\u0086\3\2")
        buf.write("\2\2\16\u0088\3\2\2\2\20\u0098\3\2\2\2\22\u00b8\3\2\2")
        buf.write("\2\24\u00c8\3\2\2\2\26\u00dd\3\2\2\2\30\u00ed\3\2\2\2")
        buf.write("\32\u0108\3\2\2\2\34\u011e\3\2\2\2\36\u0120\3\2\2\2 \u0137")
        buf.write("\3\2\2\2\"\u013e\3\2\2\2$\u0145\3\2\2\2&\u0153\3\2\2\2")
        buf.write("(\u0160\3\2\2\2*\u0171\3\2\2\2,\u0182\3\2\2\2.\u0187\3")
        buf.write("\2\2\2\60\u018d\3\2\2\2\62\u018f\3\2\2\2\64\65\7\23\2")
        buf.write("\2\65\66\5$\23\2\66\67\b\2\1\2\678\7\35\2\289\b\2\1\2")
        buf.write("9:\5\26\f\2:;\b\2\1\2;<\b\2\1\2<=\7\24\2\2=>\5\26\f\2")
        buf.write(">?\b\2\1\2?@\7\25\2\2@A\5\6\4\2AB\b\2\1\2B\3\3\2\2\2C")
        buf.write("D\7\26\2\2DE\b\3\1\2EF\7\36\2\2FG\5\22\n\2GH\b\3\1\2H")
        buf.write("I\7\37\2\2IJ\7\27\2\2JK\5\6\4\2KL\b\3\1\2LM\b\3\1\2M\5")
        buf.write("\3\2\2\2NP\7\33\2\2OQ\5\34\17\2PO\3\2\2\2QR\3\2\2\2RP")
        buf.write("\3\2\2\2RS\3\2\2\2ST\3\2\2\2TU\7\34\2\2U\7\3\2\2\2VW\7")
        buf.write("\13\2\2WX\7\36\2\2XY\5\22\n\2YZ\b\5\1\2Z[\7\37\2\2[\\")
        buf.write("\7\f\2\2\\]\5\6\4\2]`\b\5\1\2^_\7\r\2\2_a\5\6\4\2`^\3")
        buf.write("\2\2\2`a\3\2\2\2ab\3\2\2\2bc\b\5\1\2c\t\3\2\2\2de\7\n")
        buf.write("\2\2ef\7\36\2\2fg\7\63\2\2gj\7\31\2\2hk\5$\23\2ik\5\f")
        buf.write("\7\2jh\3\2\2\2ji\3\2\2\2kl\3\2\2\2lo\7\31\2\2mp\5$\23")
        buf.write("\2np\5\f\7\2om\3\2\2\2on\3\2\2\2pq\3\2\2\2qt\7\31\2\2")
        buf.write("ru\5$\23\2su\5\f\7\2tr\3\2\2\2ts\3\2\2\2uv\3\2\2\2vw\7")
        buf.write("\37\2\2w\13\3\2\2\2xy\7\61\2\2y\u0087\b\7\1\2z{\7/\2\2")
        buf.write("{\u0087\b\7\1\2|}\7*\2\2}~\7/\2\2~\u0087\b\7\1\2\177\u0080")
        buf.write("\7\60\2\2\u0080\u0087\b\7\1\2\u0081\u0082\7*\2\2\u0082")
        buf.write("\u0083\7\60\2\2\u0083\u0087\b\7\1\2\u0084\u0085\7\62\2")
        buf.write("\2\u0085\u0087\b\7\1\2\u0086x\3\2\2\2\u0086z\3\2\2\2\u0086")
        buf.write("|\3\2\2\2\u0086\177\3\2\2\2\u0086\u0081\3\2\2\2\u0086")
        buf.write("\u0084\3\2\2\2\u0087\r\3\2\2\2\u0088\u0089\7\17\2\2\u0089")
        buf.write("\u008a\7\36\2\2\u008a\u008b\5$\23\2\u008b\u008c\b\b\1")
        buf.write("\2\u008c\u0093\3\2\2\2\u008d\u008e\7\31\2\2\u008e\u008f")
        buf.write("\5$\23\2\u008f\u0090\b\b\1\2\u0090\u0092\3\2\2\2\u0091")
        buf.write("\u008d\3\2\2\2\u0092\u0095\3\2\2\2\u0093\u0091\3\2\2\2")
        buf.write("\u0093\u0094\3\2\2\2\u0094\u0096\3\2\2\2\u0095\u0093\3")
        buf.write("\2\2\2\u0096\u0097\7\37\2\2\u0097\17\3\2\2\2\u0098\u0099")
        buf.write("\7\16\2\2\u0099\u00a3\7\36\2\2\u009a\u009b\5$\23\2\u009b")
        buf.write("\u009c\b\t\1\2\u009c\u00a4\3\2\2\2\u009d\u009e\5\f\7\2")
        buf.write("\u009e\u009f\b\t\1\2\u009f\u00a4\3\2\2\2\u00a0\u00a1\5")
        buf.write("\26\f\2\u00a1\u00a2\b\t\1\2\u00a2\u00a4\3\2\2\2\u00a3")
        buf.write("\u009a\3\2\2\2\u00a3\u009d\3\2\2\2\u00a3\u00a0\3\2\2\2")
        buf.write("\u00a4\u00b3\3\2\2\2\u00a5\u00af\7\31\2\2\u00a6\u00a7")
        buf.write("\5$\23\2\u00a7\u00a8\b\t\1\2\u00a8\u00b0\3\2\2\2\u00a9")
        buf.write("\u00aa\5\f\7\2\u00aa\u00ab\b\t\1\2\u00ab\u00b0\3\2\2\2")
        buf.write("\u00ac\u00ad\5\26\f\2\u00ad\u00ae\b\t\1\2\u00ae\u00b0")
        buf.write("\3\2\2\2\u00af\u00a6\3\2\2\2\u00af\u00a9\3\2\2\2\u00af")
        buf.write("\u00ac\3\2\2\2\u00b0\u00b2\3\2\2\2\u00b1\u00a5\3\2\2\2")
        buf.write("\u00b2\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3")
        buf.write("\2\2\2\u00b4\u00b6\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00b7")
        buf.write("\7\37\2\2\u00b7\21\3\2\2\2\u00b8\u00b9\5\24\13\2\u00b9")
        buf.write("\u00c5\b\n\1\2\u00ba\u00bb\7-\2\2\u00bb\u00bf\b\n\1\2")
        buf.write("\u00bc\u00bd\7.\2\2\u00bd\u00bf\b\n\1\2\u00be\u00ba\3")
        buf.write("\2\2\2\u00be\u00bc\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c1")
        buf.write("\5\24\13\2\u00c1\u00c2\b\n\1\2\u00c2\u00c4\3\2\2\2\u00c3")
        buf.write("\u00be\3\2\2\2\u00c4\u00c7\3\2\2\2\u00c5\u00c3\3\2\2\2")
        buf.write("\u00c5\u00c6\3\2\2\2\u00c6\23\3\2\2\2\u00c7\u00c5\3\2")
        buf.write("\2\2\u00c8\u00c9\5\26\f\2\u00c9\u00db\b\13\1\2\u00ca\u00cb")
        buf.write("\7\"\2\2\u00cb\u00d7\b\13\1\2\u00cc\u00cd\7#\2\2\u00cd")
        buf.write("\u00d7\b\13\1\2\u00ce\u00cf\7$\2\2\u00cf\u00d7\b\13\1")
        buf.write("\2\u00d0\u00d1\7%\2\2\u00d1\u00d7\b\13\1\2\u00d2\u00d3")
        buf.write("\7&\2\2\u00d3\u00d7\b\13\1\2\u00d4\u00d5\7\'\2\2\u00d5")
        buf.write("\u00d7\b\13\1\2\u00d6\u00ca\3\2\2\2\u00d6\u00cc\3\2\2")
        buf.write("\2\u00d6\u00ce\3\2\2\2\u00d6\u00d0\3\2\2\2\u00d6\u00d2")
        buf.write("\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8")
        buf.write("\u00d9\5\26\f\2\u00d9\u00da\b\13\1\2\u00da\u00dc\3\2\2")
        buf.write("\2\u00db\u00d6\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\25\3")
        buf.write("\2\2\2\u00dd\u00de\5\30\r\2\u00de\u00ea\b\f\1\2\u00df")
        buf.write("\u00e0\7)\2\2\u00e0\u00e4\b\f\1\2\u00e1\u00e2\7*\2\2\u00e2")
        buf.write("\u00e4\b\f\1\2\u00e3\u00df\3\2\2\2\u00e3\u00e1\3\2\2\2")
        buf.write("\u00e4\u00e5\3\2\2\2\u00e5\u00e6\5\30\r\2\u00e6\u00e7")
        buf.write("\b\f\1\2\u00e7\u00e9\3\2\2\2\u00e8\u00e3\3\2\2\2\u00e9")
        buf.write("\u00ec\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2")
        buf.write("\u00eb\27\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ed\u00ee\5\32")
        buf.write("\16\2\u00ee\u00fa\b\r\1\2\u00ef\u00f0\7+\2\2\u00f0\u00f4")
        buf.write("\b\r\1\2\u00f1\u00f2\7,\2\2\u00f2\u00f4\b\r\1\2\u00f3")
        buf.write("\u00ef\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f4\u00f5\3\2\2\2")
        buf.write("\u00f5\u00f6\5\32\16\2\u00f6\u00f7\b\r\1\2\u00f7\u00f9")
        buf.write("\3\2\2\2\u00f8\u00f3\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa")
        buf.write("\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\31\3\2\2\2\u00fc")
        buf.write("\u00fa\3\2\2\2\u00fd\u00fe\5$\23\2\u00fe\u00ff\b\16\1")
        buf.write("\2\u00ff\u0109\3\2\2\2\u0100\u0109\5\f\7\2\u0101\u0109")
        buf.write("\5\36\20\2\u0102\u0103\7\36\2\2\u0103\u0104\b\16\1\2\u0104")
        buf.write("\u0105\5\22\n\2\u0105\u0106\7\37\2\2\u0106\u0107\b\16")
        buf.write("\1\2\u0107\u0109\3\2\2\2\u0108\u00fd\3\2\2\2\u0108\u0100")
        buf.write("\3\2\2\2\u0108\u0101\3\2\2\2\u0108\u0102\3\2\2\2\u0109")
        buf.write("\33\3\2\2\2\u010a\u010b\5\36\20\2\u010b\u010c\7\30\2\2")
        buf.write("\u010c\u011f\3\2\2\2\u010d\u010e\5\"\22\2\u010e\u010f")
        buf.write("\7\30\2\2\u010f\u011f\3\2\2\2\u0110\u0111\5\16\b\2\u0111")
        buf.write("\u0112\7\30\2\2\u0112\u011f\3\2\2\2\u0113\u0114\5\20\t")
        buf.write("\2\u0114\u0115\7\30\2\2\u0115\u011f\3\2\2\2\u0116\u0117")
        buf.write("\5\n\6\2\u0117\u0118\7\30\2\2\u0118\u011f\3\2\2\2\u0119")
        buf.write("\u011f\5\b\5\2\u011a\u011f\5\4\3\2\u011b\u011f\5\2\2\2")
        buf.write("\u011c\u011f\5\62\32\2\u011d\u011f\5 \21\2\u011e\u010a")
        buf.write("\3\2\2\2\u011e\u010d\3\2\2\2\u011e\u0110\3\2\2\2\u011e")
        buf.write("\u0113\3\2\2\2\u011e\u0116\3\2\2\2\u011e\u0119\3\2\2\2")
        buf.write("\u011e\u011a\3\2\2\2\u011e\u011b\3\2\2\2\u011e\u011c\3")
        buf.write("\2\2\2\u011e\u011d\3\2\2\2\u011f\35\3\2\2\2\u0120\u0121")
        buf.write("\7\63\2\2\u0121\u0122\b\20\1\2\u0122\u0123\b\20\1\2\u0123")
        buf.write("\u0124\7\36\2\2\u0124\u0130\b\20\1\2\u0125\u0126\5\22")
        buf.write("\n\2\u0126\u012d\b\20\1\2\u0127\u0128\7\31\2\2\u0128\u0129")
        buf.write("\5\22\n\2\u0129\u012a\b\20\1\2\u012a\u012c\3\2\2\2\u012b")
        buf.write("\u0127\3\2\2\2\u012c\u012f\3\2\2\2\u012d\u012b\3\2\2\2")
        buf.write("\u012d\u012e\3\2\2\2\u012e\u0131\3\2\2\2\u012f\u012d\3")
        buf.write("\2\2\2\u0130\u0125\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0132")
        buf.write("\3\2\2\2\u0132\u0133\b\20\1\2\u0133\u0134\7\37\2\2\u0134")
        buf.write("\u0135\b\20\1\2\u0135\u0136\b\20\1\2\u0136\37\3\2\2\2")
        buf.write("\u0137\u0138\7\20\2\2\u0138\u0139\7\36\2\2\u0139\u013a")
        buf.write("\5\22\n\2\u013a\u013b\7\37\2\2\u013b\u013c\b\21\1\2\u013c")
        buf.write("\u013d\7\30\2\2\u013d!\3\2\2\2\u013e\u013f\5$\23\2\u013f")
        buf.write("\u0140\b\22\1\2\u0140\u0141\7\35\2\2\u0141\u0142\b\22")
        buf.write("\1\2\u0142\u0143\5\22\n\2\u0143\u0144\b\22\1\2\u0144#")
        buf.write("\3\2\2\2\u0145\u0151\7\63\2\2\u0146\u0147\7 \2\2\u0147")
        buf.write("\u0148\5\26\f\2\u0148\u0149\b\23\1\2\u0149\u014f\7!\2")
        buf.write("\2\u014a\u014b\7 \2\2\u014b\u014c\5\26\f\2\u014c\u014d")
        buf.write("\b\23\1\2\u014d\u014e\7!\2\2\u014e\u0150\3\2\2\2\u014f")
        buf.write("\u014a\3\2\2\2\u014f\u0150\3\2\2\2\u0150\u0152\3\2\2\2")
        buf.write("\u0151\u0146\3\2\2\2\u0151\u0152\3\2\2\2\u0152%\3\2\2")
        buf.write("\2\u0153\u015e\7\63\2\2\u0154\u0155\7 \2\2\u0155\u0156")
        buf.write("\7/\2\2\u0156\u0157\b\24\1\2\u0157\u015c\7!\2\2\u0158")
        buf.write("\u0159\7 \2\2\u0159\u015a\7/\2\2\u015a\u015b\b\24\1\2")
        buf.write("\u015b\u015d\7!\2\2\u015c\u0158\3\2\2\2\u015c\u015d\3")
        buf.write("\2\2\2\u015d\u015f\3\2\2\2\u015e\u0154\3\2\2\2\u015e\u015f")
        buf.write("\3\2\2\2\u015f\'\3\2\2\2\u0160\u0161\7\21\2\2\u0161\u0162")
        buf.write("\5$\23\2\u0162\u0164\7\30\2\2\u0163\u0165\5*\26\2\u0164")
        buf.write("\u0163\3\2\2\2\u0164\u0165\3\2\2\2\u0165\u0166\3\2\2\2")
        buf.write("\u0166\u0167\b\25\1\2\u0167\u0168\b\25\1\2\u0168\u016c")
        buf.write("\b\25\1\2\u0169\u016b\5\62\32\2\u016a\u0169\3\2\2\2\u016b")
        buf.write("\u016e\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d\3\2\2\2")
        buf.write("\u016d\u016f\3\2\2\2\u016e\u016c\3\2\2\2\u016f\u0170\5")
        buf.write(".\30\2\u0170)\3\2\2\2\u0171\u017e\7\b\2\2\u0172\u0179")
        buf.write("\5,\27\2\u0173\u0174\7\31\2\2\u0174\u0175\5&\24\2\u0175")
        buf.write("\u0176\b\26\1\2\u0176\u0178\3\2\2\2\u0177\u0173\3\2\2")
        buf.write("\2\u0178\u017b\3\2\2\2\u0179\u0177\3\2\2\2\u0179\u017a")
        buf.write("\3\2\2\2\u017a\u017c\3\2\2\2\u017b\u0179\3\2\2\2\u017c")
        buf.write("\u017d\7\30\2\2\u017d\u017f\3\2\2\2\u017e\u0172\3\2\2")
        buf.write("\2\u017f\u0180\3\2\2\2\u0180\u017e\3\2\2\2\u0180\u0181")
        buf.write("\3\2\2\2\u0181+\3\2\2\2\u0182\u0183\5\60\31\2\u0183\u0184")
        buf.write("\7\32\2\2\u0184\u0185\5&\24\2\u0185\u0186\b\27\1\2\u0186")
        buf.write("-\3\2\2\2\u0187\u0188\7\22\2\2\u0188\u0189\b\30\1\2\u0189")
        buf.write("\u018a\7\36\2\2\u018a\u018b\7\37\2\2\u018b\u018c\5\6\4")
        buf.write("\2\u018c/\3\2\2\2\u018d\u018e\t\2\2\2\u018e\61\3\2\2\2")
        buf.write("\u018f\u0191\7\t\2\2\u0190\u0192\5\60\31\2\u0191\u0190")
        buf.write("\3\2\2\2\u0191\u0192\3\2\2\2\u0192\u0193\3\2\2\2\u0193")
        buf.write("\u0194\7\63\2\2\u0194\u0195\b\32\1\2\u0195\u0196\b\32")
        buf.write("\1\2\u0196\u01a2\7\36\2\2\u0197\u0198\5,\27\2\u0198\u019f")
        buf.write("\b\32\1\2\u0199\u019a\7\31\2\2\u019a\u019b\5,\27\2\u019b")
        buf.write("\u019c\b\32\1\2\u019c\u019e\3\2\2\2\u019d\u0199\3\2\2")
        buf.write("\2\u019e\u01a1\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0")
        buf.write("\3\2\2\2\u01a0\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2")
        buf.write("\u0197\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a4\3\2\2\2")
        buf.write("\u01a4\u01a5\7\37\2\2\u01a5\u01a7\7\30\2\2\u01a6\u01a8")
        buf.write("\5*\26\2\u01a7\u01a6\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8")
        buf.write("\u01a9\3\2\2\2\u01a9\u01aa\b\32\1\2\u01aa\u01ab\b\32\1")
        buf.write("\2\u01ab\u01af\7\33\2\2\u01ac\u01ae\5\34\17\2\u01ad\u01ac")
        buf.write("\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af\u01ad\3\2\2\2\u01af")
        buf.write("\u01b0\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2")
        buf.write("\u01b2\u01b4\5 \21\2\u01b3\u01b2\3\2\2\2\u01b3\u01b4\3")
        buf.write("\2\2\2\u01b4\u01b5\3\2\2\2\u01b5\u01b6\7\34\2\2\u01b6")
        buf.write("\u01b7\b\32\1\2\u01b7\63\3\2\2\2&R`jot\u0086\u0093\u00a3")
        buf.write("\u00af\u00b3\u00be\u00c5\u00d6\u00db\u00e3\u00ea\u00f3")
        buf.write("\u00fa\u0108\u011e\u012d\u0130\u014f\u0151\u015c\u015e")
        buf.write("\u0164\u016c\u0179\u0180\u0191\u019f\u01a2\u01a7\u01af")
        buf.write("\u01b3")
        return buf.getvalue()


class covid19Parser ( Parser ):

    grammarFileName = "covid19.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "'string'", "'char'", 
                     "'Dataframe'", "'var'", "'funcion'", "'CargaArchivo'", 
                     "'si'", "'entonces'", "'sino'", "'escribe'", "'lee'", 
                     "'regresa'", "'Programa'", "'principal'", "'desde'", 
                     "'hasta'", "'hacer'", "'mientras'", "'haz'", "';'", 
                     "','", "':'", "'{'", "'}'", "'='", "'('", "')'", "'['", 
                     "']'", "'>'", "'<'", "'>='", "'<='", "'=='", "'!='", 
                     "'!'", "'+'", "'-'", "'*'", "'/'", "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>", "INT", "FLOAT", "STRING", "CHAR", "DATAFRAME", 
                      "VAR", "FUNCION", "CARGAARCHIVO", "SI", "ENTONCES", 
                      "SINO", "ESCRIBE", "LEE", "REGRESA", "PROGRAMA", "PRINCIPAL", 
                      "DESDE", "HASTA", "HACER", "MIENTRAS", "HAZ", "PUNTOYCOMA", 
                      "COMA", "DOSPUNTOS", "CORCHETEI", "CORCHETED", "IGUAL", 
                      "PARENTESISI", "PARENTESISD", "CORCHETECUADRADOI", 
                      "CORCHETECUADRADOD", "MAYOR", "MENOR", "MAYORIGUAL", 
                      "MENORIGUAL", "IGUALCOMP", "DIFERENTE", "NEGACION", 
                      "SUMA", "RESTA", "MULTIPLICACION", "DIVISION", "Y", 
                      "O", "CTEINT", "CTEFLOAT", "CTESTRING", "CTECHAR", 
                      "ID", "COMENTARIO", "LINEACOMENTADA", "WS" ]

    RULE_nocondicional = 0
    RULE_condicional = 1
    RULE_bloque = 2
    RULE_decision = 3
    RULE_cargadatos = 4
    RULE_cte = 5
    RULE_lectura = 6
    RULE_escritura = 7
    RULE_megaexpresion = 8
    RULE_superexpresion = 9
    RULE_expresion = 10
    RULE_termino = 11
    RULE_factor = 12
    RULE_estatuto = 13
    RULE_llamadametodo = 14
    RULE_regresa = 15
    RULE_asignacion = 16
    RULE_identificador_accesa = 17
    RULE_identificador_definicion = 18
    RULE_programa = 19
    RULE_varx = 20
    RULE_var = 21
    RULE_funcp = 22
    RULE_tipo = 23
    RULE_metodo = 24

    ruleNames =  [ "nocondicional", "condicional", "bloque", "decision", 
                   "cargadatos", "cte", "lectura", "escritura", "megaexpresion", 
                   "superexpresion", "expresion", "termino", "factor", "estatuto", 
                   "llamadametodo", "regresa", "asignacion", "identificador_accesa", 
                   "identificador_definicion", "programa", "varx", "var", 
                   "funcp", "tipo", "metodo" ]

    EOF = Token.EOF
    INT=1
    FLOAT=2
    STRING=3
    CHAR=4
    DATAFRAME=5
    VAR=6
    FUNCION=7
    CARGAARCHIVO=8
    SI=9
    ENTONCES=10
    SINO=11
    ESCRIBE=12
    LEE=13
    REGRESA=14
    PROGRAMA=15
    PRINCIPAL=16
    DESDE=17
    HASTA=18
    HACER=19
    MIENTRAS=20
    HAZ=21
    PUNTOYCOMA=22
    COMA=23
    DOSPUNTOS=24
    CORCHETEI=25
    CORCHETED=26
    IGUAL=27
    PARENTESISI=28
    PARENTESISD=29
    CORCHETECUADRADOI=30
    CORCHETECUADRADOD=31
    MAYOR=32
    MENOR=33
    MAYORIGUAL=34
    MENORIGUAL=35
    IGUALCOMP=36
    DIFERENTE=37
    NEGACION=38
    SUMA=39
    RESTA=40
    MULTIPLICACION=41
    DIVISION=42
    Y=43
    O=44
    CTEINT=45
    CTEFLOAT=46
    CTESTRING=47
    CTECHAR=48
    ID=49
    COMENTARIO=50
    LINEACOMENTADA=51
    WS=52

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class NocondicionalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._identificador_accesa = None # Identificador_accesaContext
            self._IGUAL = None # Token

        def DESDE(self):
            return self.getToken(covid19Parser.DESDE, 0)

        def identificador_accesa(self):
            return self.getTypedRuleContext(covid19Parser.Identificador_accesaContext,0)


        def IGUAL(self):
            return self.getToken(covid19Parser.IGUAL, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(covid19Parser.ExpresionContext,i)


        def HASTA(self):
            return self.getToken(covid19Parser.HASTA, 0)

        def HACER(self):
            return self.getToken(covid19Parser.HACER, 0)

        def bloque(self):
            return self.getTypedRuleContext(covid19Parser.BloqueContext,0)


        def getRuleIndex(self):
            return covid19Parser.RULE_nocondicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNocondicional" ):
                listener.enterNocondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNocondicional" ):
                listener.exitNocondicional(self)




    def nocondicional(self):

        localctx = covid19Parser.NocondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_nocondicional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(covid19Parser.DESDE)
            self.state = 51
            localctx._identificador_accesa = self.identificador_accesa()
            insertIdToStack((None if localctx._identificador_accesa is None else self._input.getText(localctx._identificador_accesa.start,localctx._identificador_accesa.stop)))
            self.state = 53
            localctx._IGUAL = self.match(covid19Parser.IGUAL)
            insertOperator((None if localctx._IGUAL is None else localctx._IGUAL.text))
            self.state = 55
            self.expresion()
            leaving('asignacion', True)
            addMigajitaDePan()
            self.state = 58
            self.match(covid19Parser.HASTA)
            self.state = 59
            self.expresion()
            forEvaluation()
            self.state = 61
            self.match(covid19Parser.HACER)
            self.state = 62
            self.bloque()
            addGotoEnd('for')
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIENTRAS(self):
            return self.getToken(covid19Parser.MIENTRAS, 0)

        def PARENTESISI(self):
            return self.getToken(covid19Parser.PARENTESISI, 0)

        def megaexpresion(self):
            return self.getTypedRuleContext(covid19Parser.MegaexpresionContext,0)


        def PARENTESISD(self):
            return self.getToken(covid19Parser.PARENTESISD, 0)

        def HAZ(self):
            return self.getToken(covid19Parser.HAZ, 0)

        def bloque(self):
            return self.getTypedRuleContext(covid19Parser.BloqueContext,0)


        def getRuleIndex(self):
            return covid19Parser.RULE_condicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicional" ):
                listener.enterCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicional" ):
                listener.exitCondicional(self)




    def condicional(self):

        localctx = covid19Parser.CondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_condicional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(covid19Parser.MIENTRAS)
            addMigajitaDePan()
            self.state = 67
            self.match(covid19Parser.PARENTESISI)
            self.state = 68
            self.megaexpresion()
            addGotoF()
            self.state = 70
            self.match(covid19Parser.PARENTESISD)
            self.state = 71
            self.match(covid19Parser.HAZ)
            self.state = 72
            self.bloque()
            addGotoA()
            addGotoEnd('while')
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CORCHETEI(self):
            return self.getToken(covid19Parser.CORCHETEI, 0)

        def CORCHETED(self):
            return self.getToken(covid19Parser.CORCHETED, 0)

        def estatuto(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.EstatutoContext)
            else:
                return self.getTypedRuleContext(covid19Parser.EstatutoContext,i)


        def getRuleIndex(self):
            return covid19Parser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)




    def bloque(self):

        localctx = covid19Parser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(covid19Parser.CORCHETEI)
            self.state = 78 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 77
                self.estatuto()
                self.state = 80 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << covid19Parser.FUNCION) | (1 << covid19Parser.CARGAARCHIVO) | (1 << covid19Parser.SI) | (1 << covid19Parser.ESCRIBE) | (1 << covid19Parser.LEE) | (1 << covid19Parser.REGRESA) | (1 << covid19Parser.DESDE) | (1 << covid19Parser.MIENTRAS) | (1 << covid19Parser.ID))) != 0)):
                    break

            self.state = 82
            self.match(covid19Parser.CORCHETED)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecisionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(covid19Parser.SI, 0)

        def PARENTESISI(self):
            return self.getToken(covid19Parser.PARENTESISI, 0)

        def megaexpresion(self):
            return self.getTypedRuleContext(covid19Parser.MegaexpresionContext,0)


        def PARENTESISD(self):
            return self.getToken(covid19Parser.PARENTESISD, 0)

        def ENTONCES(self):
            return self.getToken(covid19Parser.ENTONCES, 0)

        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.BloqueContext)
            else:
                return self.getTypedRuleContext(covid19Parser.BloqueContext,i)


        def SINO(self):
            return self.getToken(covid19Parser.SINO, 0)

        def getRuleIndex(self):
            return covid19Parser.RULE_decision

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecision" ):
                listener.enterDecision(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecision" ):
                listener.exitDecision(self)




    def decision(self):

        localctx = covid19Parser.DecisionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_decision)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(covid19Parser.SI)
            self.state = 85
            self.match(covid19Parser.PARENTESISI)
            self.state = 86
            self.megaexpresion()
            addGotoF()
            self.state = 88
            self.match(covid19Parser.PARENTESISD)
            self.state = 89
            self.match(covid19Parser.ENTONCES)
            self.state = 90
            self.bloque()
            addGotoA()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==covid19Parser.SINO:
                self.state = 92
                self.match(covid19Parser.SINO)
                self.state = 93
                self.bloque()


            addGotoEnd('si')
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CargadatosContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CARGAARCHIVO(self):
            return self.getToken(covid19Parser.CARGAARCHIVO, 0)

        def PARENTESISI(self):
            return self.getToken(covid19Parser.PARENTESISI, 0)

        def ID(self):
            return self.getToken(covid19Parser.ID, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(covid19Parser.COMA)
            else:
                return self.getToken(covid19Parser.COMA, i)

        def PARENTESISD(self):
            return self.getToken(covid19Parser.PARENTESISD, 0)

        def identificador_accesa(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.Identificador_accesaContext)
            else:
                return self.getTypedRuleContext(covid19Parser.Identificador_accesaContext,i)


        def cte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.CteContext)
            else:
                return self.getTypedRuleContext(covid19Parser.CteContext,i)


        def getRuleIndex(self):
            return covid19Parser.RULE_cargadatos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCargadatos" ):
                listener.enterCargadatos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCargadatos" ):
                listener.exitCargadatos(self)




    def cargadatos(self):

        localctx = covid19Parser.CargadatosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_cargadatos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(covid19Parser.CARGAARCHIVO)
            self.state = 99
            self.match(covid19Parser.PARENTESISI)
            self.state = 100
            self.match(covid19Parser.ID)
            self.state = 101
            self.match(covid19Parser.COMA)
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [covid19Parser.ID]:
                self.state = 102
                self.identificador_accesa()
                pass
            elif token in [covid19Parser.RESTA, covid19Parser.CTEINT, covid19Parser.CTEFLOAT, covid19Parser.CTESTRING, covid19Parser.CTECHAR]:
                self.state = 103
                self.cte()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 106
            self.match(covid19Parser.COMA)
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [covid19Parser.ID]:
                self.state = 107
                self.identificador_accesa()
                pass
            elif token in [covid19Parser.RESTA, covid19Parser.CTEINT, covid19Parser.CTEFLOAT, covid19Parser.CTESTRING, covid19Parser.CTECHAR]:
                self.state = 108
                self.cte()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 111
            self.match(covid19Parser.COMA)
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [covid19Parser.ID]:
                self.state = 112
                self.identificador_accesa()
                pass
            elif token in [covid19Parser.RESTA, covid19Parser.CTEINT, covid19Parser.CTEFLOAT, covid19Parser.CTESTRING, covid19Parser.CTECHAR]:
                self.state = 113
                self.cte()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 116
            self.match(covid19Parser.PARENTESISD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._CTESTRING = None # Token
            self._CTEINT = None # Token
            self._CTEFLOAT = None # Token
            self._CTECHAR = None # Token

        def CTESTRING(self):
            return self.getToken(covid19Parser.CTESTRING, 0)

        def CTEINT(self):
            return self.getToken(covid19Parser.CTEINT, 0)

        def RESTA(self):
            return self.getToken(covid19Parser.RESTA, 0)

        def CTEFLOAT(self):
            return self.getToken(covid19Parser.CTEFLOAT, 0)

        def CTECHAR(self):
            return self.getToken(covid19Parser.CTECHAR, 0)

        def getRuleIndex(self):
            return covid19Parser.RULE_cte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCte" ):
                listener.enterCte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCte" ):
                listener.exitCte(self)




    def cte(self):

        localctx = covid19Parser.CteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_cte)
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                localctx._CTESTRING = self.match(covid19Parser.CTESTRING)
                insertCteToStructs((None if localctx._CTESTRING is None else localctx._CTESTRING.text), 'string')
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                localctx._CTEINT = self.match(covid19Parser.CTEINT)
                insertCteToStructs((None if localctx._CTEINT is None else localctx._CTEINT.text), 'int')
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 122
                self.match(covid19Parser.RESTA)
                self.state = 123
                localctx._CTEINT = self.match(covid19Parser.CTEINT)
                insertCteToStructs("-" + (None if localctx._CTEINT is None else localctx._CTEINT.text), 'int')
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 125
                localctx._CTEFLOAT = self.match(covid19Parser.CTEFLOAT)
                insertCteToStructs((None if localctx._CTEFLOAT is None else localctx._CTEFLOAT.text), 'float')
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 127
                self.match(covid19Parser.RESTA)
                self.state = 128
                localctx._CTEFLOAT = self.match(covid19Parser.CTEFLOAT)
                insertCteToStructs("-" + (None if localctx._CTEFLOAT is None else localctx._CTEFLOAT.text), 'float')
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 130
                localctx._CTECHAR = self.match(covid19Parser.CTECHAR)
                insertCteToStructs((None if localctx._CTECHAR is None else localctx._CTECHAR.text), 'char')
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LecturaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._identificador_accesa = None # Identificador_accesaContext

        def LEE(self):
            return self.getToken(covid19Parser.LEE, 0)

        def PARENTESISI(self):
            return self.getToken(covid19Parser.PARENTESISI, 0)

        def PARENTESISD(self):
            return self.getToken(covid19Parser.PARENTESISD, 0)

        def identificador_accesa(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.Identificador_accesaContext)
            else:
                return self.getTypedRuleContext(covid19Parser.Identificador_accesaContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(covid19Parser.COMA)
            else:
                return self.getToken(covid19Parser.COMA, i)

        def getRuleIndex(self):
            return covid19Parser.RULE_lectura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLectura" ):
                listener.enterLectura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLectura" ):
                listener.exitLectura(self)




    def lectura(self):

        localctx = covid19Parser.LecturaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_lectura)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(covid19Parser.LEE)
            self.state = 135
            self.match(covid19Parser.PARENTESISI)

            self.state = 136
            localctx._identificador_accesa = self.identificador_accesa()
            readId((None if localctx._identificador_accesa is None else self._input.getText(localctx._identificador_accesa.start,localctx._identificador_accesa.stop)))
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.COMA:
                self.state = 139
                self.match(covid19Parser.COMA)
                self.state = 140
                localctx._identificador_accesa = self.identificador_accesa()
                readId((None if localctx._identificador_accesa is None else self._input.getText(localctx._identificador_accesa.start,localctx._identificador_accesa.stop)))
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 148
            self.match(covid19Parser.PARENTESISD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EscrituraContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._identificador_accesa = None # Identificador_accesaContext
            self._cte = None # CteContext

        def ESCRIBE(self):
            return self.getToken(covid19Parser.ESCRIBE, 0)

        def PARENTESISI(self):
            return self.getToken(covid19Parser.PARENTESISI, 0)

        def PARENTESISD(self):
            return self.getToken(covid19Parser.PARENTESISD, 0)

        def identificador_accesa(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.Identificador_accesaContext)
            else:
                return self.getTypedRuleContext(covid19Parser.Identificador_accesaContext,i)


        def cte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.CteContext)
            else:
                return self.getTypedRuleContext(covid19Parser.CteContext,i)


        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(covid19Parser.ExpresionContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(covid19Parser.COMA)
            else:
                return self.getToken(covid19Parser.COMA, i)

        def getRuleIndex(self):
            return covid19Parser.RULE_escritura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscritura" ):
                listener.enterEscritura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscritura" ):
                listener.exitEscritura(self)




    def escritura(self):

        localctx = covid19Parser.EscrituraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_escritura)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(covid19Parser.ESCRIBE)
            self.state = 151
            self.match(covid19Parser.PARENTESISI)
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 152
                localctx._identificador_accesa = self.identificador_accesa()
                write((None if localctx._identificador_accesa is None else self._input.getText(localctx._identificador_accesa.start,localctx._identificador_accesa.stop)))
                pass

            elif la_ == 2:
                self.state = 155
                localctx._cte = self.cte()
                write((None if localctx._cte is None else self._input.getText(localctx._cte.start,localctx._cte.stop)))
                pass

            elif la_ == 3:
                self.state = 158
                self.expresion()
                write(None)
                pass


            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.COMA:
                self.state = 163
                self.match(covid19Parser.COMA)
                self.state = 173
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 164
                    localctx._identificador_accesa = self.identificador_accesa()
                    write((None if localctx._identificador_accesa is None else self._input.getText(localctx._identificador_accesa.start,localctx._identificador_accesa.stop)))
                    pass

                elif la_ == 2:
                    self.state = 167
                    localctx._cte = self.cte()
                    write((None if localctx._cte is None else self._input.getText(localctx._cte.start,localctx._cte.stop)))
                    pass

                elif la_ == 3:
                    self.state = 170
                    self.expresion()
                    write(None)
                    pass


                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 180
            self.match(covid19Parser.PARENTESISD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MegaexpresionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._Y = None # Token
            self._O = None # Token

        def superexpresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.SuperexpresionContext)
            else:
                return self.getTypedRuleContext(covid19Parser.SuperexpresionContext,i)


        def Y(self, i:int=None):
            if i is None:
                return self.getTokens(covid19Parser.Y)
            else:
                return self.getToken(covid19Parser.Y, i)

        def O(self, i:int=None):
            if i is None:
                return self.getTokens(covid19Parser.O)
            else:
                return self.getToken(covid19Parser.O, i)

        def getRuleIndex(self):
            return covid19Parser.RULE_megaexpresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMegaexpresion" ):
                listener.enterMegaexpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMegaexpresion" ):
                listener.exitMegaexpresion(self)




    def megaexpresion(self):

        localctx = covid19Parser.MegaexpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_megaexpresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.superexpresion()
            leaving('union')
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.Y or _la==covid19Parser.O:
                self.state = 188
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [covid19Parser.Y]:
                    self.state = 184
                    localctx._Y = self.match(covid19Parser.Y)
                    insertOperator((None if localctx._Y is None else localctx._Y.text))
                    pass
                elif token in [covid19Parser.O]:
                    self.state = 186
                    localctx._O = self.match(covid19Parser.O)
                    insertOperator((None if localctx._O is None else localctx._O.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 190
                self.superexpresion()
                leaving('union')
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SuperexpresionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._MAYOR = None # Token
            self._MENOR = None # Token
            self._MAYORIGUAL = None # Token
            self._MENORIGUAL = None # Token
            self._IGUALCOMP = None # Token
            self._DIFERENTE = None # Token

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(covid19Parser.ExpresionContext,i)


        def MAYOR(self):
            return self.getToken(covid19Parser.MAYOR, 0)

        def MENOR(self):
            return self.getToken(covid19Parser.MENOR, 0)

        def MAYORIGUAL(self):
            return self.getToken(covid19Parser.MAYORIGUAL, 0)

        def MENORIGUAL(self):
            return self.getToken(covid19Parser.MENORIGUAL, 0)

        def IGUALCOMP(self):
            return self.getToken(covid19Parser.IGUALCOMP, 0)

        def DIFERENTE(self):
            return self.getToken(covid19Parser.DIFERENTE, 0)

        def getRuleIndex(self):
            return covid19Parser.RULE_superexpresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSuperexpresion" ):
                listener.enterSuperexpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSuperexpresion" ):
                listener.exitSuperexpresion(self)




    def superexpresion(self):

        localctx = covid19Parser.SuperexpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_superexpresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.expresion()
            leaving('comparacion')
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << covid19Parser.MAYOR) | (1 << covid19Parser.MENOR) | (1 << covid19Parser.MAYORIGUAL) | (1 << covid19Parser.MENORIGUAL) | (1 << covid19Parser.IGUALCOMP) | (1 << covid19Parser.DIFERENTE))) != 0):
                self.state = 212
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [covid19Parser.MAYOR]:
                    self.state = 200
                    localctx._MAYOR = self.match(covid19Parser.MAYOR)
                    insertOperator((None if localctx._MAYOR is None else localctx._MAYOR.text))
                    pass
                elif token in [covid19Parser.MENOR]:
                    self.state = 202
                    localctx._MENOR = self.match(covid19Parser.MENOR)
                    insertOperator((None if localctx._MENOR is None else localctx._MENOR.text))
                    pass
                elif token in [covid19Parser.MAYORIGUAL]:
                    self.state = 204
                    localctx._MAYORIGUAL = self.match(covid19Parser.MAYORIGUAL)
                    insertOperator((None if localctx._MAYORIGUAL is None else localctx._MAYORIGUAL.text))
                    pass
                elif token in [covid19Parser.MENORIGUAL]:
                    self.state = 206
                    localctx._MENORIGUAL = self.match(covid19Parser.MENORIGUAL)
                    insertOperator((None if localctx._MENORIGUAL is None else localctx._MENORIGUAL.text))
                    pass
                elif token in [covid19Parser.IGUALCOMP]:
                    self.state = 208
                    localctx._IGUALCOMP = self.match(covid19Parser.IGUALCOMP)
                    insertOperator((None if localctx._IGUALCOMP is None else localctx._IGUALCOMP.text))
                    pass
                elif token in [covid19Parser.DIFERENTE]:
                    self.state = 210
                    localctx._DIFERENTE = self.match(covid19Parser.DIFERENTE)
                    insertOperator((None if localctx._DIFERENTE is None else localctx._DIFERENTE.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 214
                self.expresion()
                leaving('comparacion')


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._SUMA = None # Token
            self._RESTA = None # Token

        def termino(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.TerminoContext)
            else:
                return self.getTypedRuleContext(covid19Parser.TerminoContext,i)


        def SUMA(self, i:int=None):
            if i is None:
                return self.getTokens(covid19Parser.SUMA)
            else:
                return self.getToken(covid19Parser.SUMA, i)

        def RESTA(self, i:int=None):
            if i is None:
                return self.getTokens(covid19Parser.RESTA)
            else:
                return self.getToken(covid19Parser.RESTA, i)

        def getRuleIndex(self):
            return covid19Parser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)




    def expresion(self):

        localctx = covid19Parser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.termino()
            leaving('termino')
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.SUMA or _la==covid19Parser.RESTA:
                self.state = 225
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [covid19Parser.SUMA]:
                    self.state = 221
                    localctx._SUMA = self.match(covid19Parser.SUMA)
                    insertOperator((None if localctx._SUMA is None else localctx._SUMA.text))
                    pass
                elif token in [covid19Parser.RESTA]:
                    self.state = 223
                    localctx._RESTA = self.match(covid19Parser.RESTA)
                    insertOperator((None if localctx._RESTA is None else localctx._RESTA.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 227
                self.termino()
                leaving('termino')
                self.state = 234
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._MULTIPLICACION = None # Token
            self._DIVISION = None # Token

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.FactorContext)
            else:
                return self.getTypedRuleContext(covid19Parser.FactorContext,i)


        def MULTIPLICACION(self, i:int=None):
            if i is None:
                return self.getTokens(covid19Parser.MULTIPLICACION)
            else:
                return self.getToken(covid19Parser.MULTIPLICACION, i)

        def DIVISION(self, i:int=None):
            if i is None:
                return self.getTokens(covid19Parser.DIVISION)
            else:
                return self.getToken(covid19Parser.DIVISION, i)

        def getRuleIndex(self):
            return covid19Parser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)




    def termino(self):

        localctx = covid19Parser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.factor()
            leaving('factor')
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.MULTIPLICACION or _la==covid19Parser.DIVISION:
                self.state = 241
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [covid19Parser.MULTIPLICACION]:
                    self.state = 237
                    localctx._MULTIPLICACION = self.match(covid19Parser.MULTIPLICACION)
                    insertOperator((None if localctx._MULTIPLICACION is None else localctx._MULTIPLICACION.text))
                    pass
                elif token in [covid19Parser.DIVISION]:
                    self.state = 239
                    localctx._DIVISION = self.match(covid19Parser.DIVISION)
                    insertOperator((None if localctx._DIVISION is None else localctx._DIVISION.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 243
                self.factor()
                leaving('factor')
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._identificador_accesa = None # Identificador_accesaContext

        def identificador_accesa(self):
            return self.getTypedRuleContext(covid19Parser.Identificador_accesaContext,0)


        def cte(self):
            return self.getTypedRuleContext(covid19Parser.CteContext,0)


        def llamadametodo(self):
            return self.getTypedRuleContext(covid19Parser.LlamadametodoContext,0)


        def PARENTESISI(self):
            return self.getToken(covid19Parser.PARENTESISI, 0)

        def megaexpresion(self):
            return self.getTypedRuleContext(covid19Parser.MegaexpresionContext,0)


        def PARENTESISD(self):
            return self.getToken(covid19Parser.PARENTESISD, 0)

        def getRuleIndex(self):
            return covid19Parser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = covid19Parser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_factor)
        try:
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                localctx._identificador_accesa = self.identificador_accesa()
                insertIdToStack((None if localctx._identificador_accesa is None else self._input.getText(localctx._identificador_accesa.start,localctx._identificador_accesa.stop)))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.cte()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 255
                self.llamadametodo()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 256
                self.match(covid19Parser.PARENTESISI)
                insertParenthesis()
                self.state = 258
                self.megaexpresion()
                self.state = 259
                self.match(covid19Parser.PARENTESISD)
                deleteParenthesis()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EstatutoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def llamadametodo(self):
            return self.getTypedRuleContext(covid19Parser.LlamadametodoContext,0)


        def PUNTOYCOMA(self):
            return self.getToken(covid19Parser.PUNTOYCOMA, 0)

        def asignacion(self):
            return self.getTypedRuleContext(covid19Parser.AsignacionContext,0)


        def lectura(self):
            return self.getTypedRuleContext(covid19Parser.LecturaContext,0)


        def escritura(self):
            return self.getTypedRuleContext(covid19Parser.EscrituraContext,0)


        def cargadatos(self):
            return self.getTypedRuleContext(covid19Parser.CargadatosContext,0)


        def decision(self):
            return self.getTypedRuleContext(covid19Parser.DecisionContext,0)


        def condicional(self):
            return self.getTypedRuleContext(covid19Parser.CondicionalContext,0)


        def nocondicional(self):
            return self.getTypedRuleContext(covid19Parser.NocondicionalContext,0)


        def metodo(self):
            return self.getTypedRuleContext(covid19Parser.MetodoContext,0)


        def regresa(self):
            return self.getTypedRuleContext(covid19Parser.RegresaContext,0)


        def getRuleIndex(self):
            return covid19Parser.RULE_estatuto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEstatuto" ):
                listener.enterEstatuto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEstatuto" ):
                listener.exitEstatuto(self)




    def estatuto(self):

        localctx = covid19Parser.EstatutoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_estatuto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 264
                self.llamadametodo()
                self.state = 265
                self.match(covid19Parser.PUNTOYCOMA)
                pass

            elif la_ == 2:
                self.state = 267
                self.asignacion()
                self.state = 268
                self.match(covid19Parser.PUNTOYCOMA)
                pass

            elif la_ == 3:
                self.state = 270
                self.lectura()
                self.state = 271
                self.match(covid19Parser.PUNTOYCOMA)
                pass

            elif la_ == 4:
                self.state = 273
                self.escritura()
                self.state = 274
                self.match(covid19Parser.PUNTOYCOMA)
                pass

            elif la_ == 5:
                self.state = 276
                self.cargadatos()
                self.state = 277
                self.match(covid19Parser.PUNTOYCOMA)
                pass

            elif la_ == 6:
                self.state = 279
                self.decision()
                pass

            elif la_ == 7:
                self.state = 280
                self.condicional()
                pass

            elif la_ == 8:
                self.state = 281
                self.nocondicional()
                pass

            elif la_ == 9:
                self.state = 282
                self.metodo()
                pass

            elif la_ == 10:
                self.state = 283
                self.regresa()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamadametodoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(covid19Parser.ID, 0)

        def PARENTESISI(self):
            return self.getToken(covid19Parser.PARENTESISI, 0)

        def PARENTESISD(self):
            return self.getToken(covid19Parser.PARENTESISD, 0)

        def megaexpresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.MegaexpresionContext)
            else:
                return self.getTypedRuleContext(covid19Parser.MegaexpresionContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(covid19Parser.COMA)
            else:
                return self.getToken(covid19Parser.COMA, i)

        def getRuleIndex(self):
            return covid19Parser.RULE_llamadametodo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamadametodo" ):
                listener.enterLlamadametodo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamadametodo" ):
                listener.exitLlamadametodo(self)




    def llamadametodo(self):

        localctx = covid19Parser.LlamadametodoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_llamadametodo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            localctx._ID = self.match(covid19Parser.ID)
            validateFunctionExistance((None if localctx._ID is None else localctx._ID.text))
            insertERASize((None if localctx._ID is None else localctx._ID.text))
            self.state = 289
            self.match(covid19Parser.PARENTESISI)
            insertParenthesis()
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << covid19Parser.PARENTESISI) | (1 << covid19Parser.RESTA) | (1 << covid19Parser.CTEINT) | (1 << covid19Parser.CTEFLOAT) | (1 << covid19Parser.CTESTRING) | (1 << covid19Parser.CTECHAR) | (1 << covid19Parser.ID))) != 0):
                self.state = 291
                self.megaexpresion()
                incrementReceivedParamCounter()
                self.state = 299
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==covid19Parser.COMA:
                    self.state = 293
                    self.match(covid19Parser.COMA)
                    self.state = 294
                    self.megaexpresion()
                    incrementReceivedParamCounter()
                    self.state = 301
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            receivedFunctionParameters((None if localctx._ID is None else localctx._ID.text))
            self.state = 305
            self.match(covid19Parser.PARENTESISD)
            deleteParenthesis()
            insertGOSUB((None if localctx._ID is None else localctx._ID.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RegresaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._megaexpresion = None # MegaexpresionContext

        def REGRESA(self):
            return self.getToken(covid19Parser.REGRESA, 0)

        def PARENTESISI(self):
            return self.getToken(covid19Parser.PARENTESISI, 0)

        def megaexpresion(self):
            return self.getTypedRuleContext(covid19Parser.MegaexpresionContext,0)


        def PARENTESISD(self):
            return self.getToken(covid19Parser.PARENTESISD, 0)

        def PUNTOYCOMA(self):
            return self.getToken(covid19Parser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return covid19Parser.RULE_regresa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegresa" ):
                listener.enterRegresa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegresa" ):
                listener.exitRegresa(self)




    def regresa(self):

        localctx = covid19Parser.RegresaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_regresa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(covid19Parser.REGRESA)
            self.state = 310
            self.match(covid19Parser.PARENTESISI)
            self.state = 311
            localctx._megaexpresion = self.megaexpresion()
            self.state = 312
            self.match(covid19Parser.PARENTESISD)
            generateReturnQuad((None if localctx._megaexpresion is None else self._input.getText(localctx._megaexpresion.start,localctx._megaexpresion.stop)))
            self.state = 314
            self.match(covid19Parser.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._identificador_accesa = None # Identificador_accesaContext
            self._IGUAL = None # Token

        def identificador_accesa(self):
            return self.getTypedRuleContext(covid19Parser.Identificador_accesaContext,0)


        def IGUAL(self):
            return self.getToken(covid19Parser.IGUAL, 0)

        def megaexpresion(self):
            return self.getTypedRuleContext(covid19Parser.MegaexpresionContext,0)


        def getRuleIndex(self):
            return covid19Parser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)




    def asignacion(self):

        localctx = covid19Parser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            localctx._identificador_accesa = self.identificador_accesa()
            insertIdToStack((None if localctx._identificador_accesa is None else self._input.getText(localctx._identificador_accesa.start,localctx._identificador_accesa.stop)))
            self.state = 318
            localctx._IGUAL = self.match(covid19Parser.IGUAL)
            insertOperator((None if localctx._IGUAL is None else localctx._IGUAL.text))
            self.state = 320
            self.megaexpresion()
            leaving('asignacion')
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Identificador_accesaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._ID = None # Token

        def ID(self):
            return self.getToken(covid19Parser.ID, 0)

        def CORCHETECUADRADOI(self, i:int=None):
            if i is None:
                return self.getTokens(covid19Parser.CORCHETECUADRADOI)
            else:
                return self.getToken(covid19Parser.CORCHETECUADRADOI, i)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(covid19Parser.ExpresionContext,i)


        def CORCHETECUADRADOD(self, i:int=None):
            if i is None:
                return self.getTokens(covid19Parser.CORCHETECUADRADOD)
            else:
                return self.getToken(covid19Parser.CORCHETECUADRADOD, i)

        def getRuleIndex(self):
            return covid19Parser.RULE_identificador_accesa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentificador_accesa" ):
                listener.enterIdentificador_accesa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentificador_accesa" ):
                listener.exitIdentificador_accesa(self)




    def identificador_accesa(self):

        localctx = covid19Parser.Identificador_accesaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_identificador_accesa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            localctx._ID = self.match(covid19Parser.ID)
            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==covid19Parser.CORCHETECUADRADOI:
                self.state = 324
                self.match(covid19Parser.CORCHETECUADRADOI)
                self.state = 325
                self.expresion()
                verify('1', (None if localctx._ID is None else localctx._ID.text))
                self.state = 327
                self.match(covid19Parser.CORCHETECUADRADOD)
                self.state = 333
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==covid19Parser.CORCHETECUADRADOI:
                    self.state = 328
                    self.match(covid19Parser.CORCHETECUADRADOI)
                    self.state = 329
                    self.expresion()
                    verify('2', (None if localctx._ID is None else localctx._ID.text))
                    self.state = 331
                    self.match(covid19Parser.CORCHETECUADRADOD)




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Identificador_definicionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._CTEINT = None # Token

        def ID(self):
            return self.getToken(covid19Parser.ID, 0)

        def CORCHETECUADRADOI(self, i:int=None):
            if i is None:
                return self.getTokens(covid19Parser.CORCHETECUADRADOI)
            else:
                return self.getToken(covid19Parser.CORCHETECUADRADOI, i)

        def CTEINT(self, i:int=None):
            if i is None:
                return self.getTokens(covid19Parser.CTEINT)
            else:
                return self.getToken(covid19Parser.CTEINT, i)

        def CORCHETECUADRADOD(self, i:int=None):
            if i is None:
                return self.getTokens(covid19Parser.CORCHETECUADRADOD)
            else:
                return self.getToken(covid19Parser.CORCHETECUADRADOD, i)

        def getRuleIndex(self):
            return covid19Parser.RULE_identificador_definicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentificador_definicion" ):
                listener.enterIdentificador_definicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentificador_definicion" ):
                listener.exitIdentificador_definicion(self)




    def identificador_definicion(self):

        localctx = covid19Parser.Identificador_definicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_identificador_definicion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(covid19Parser.ID)
            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==covid19Parser.CORCHETECUADRADOI:
                self.state = 338
                self.match(covid19Parser.CORCHETECUADRADOI)
                self.state = 339
                localctx._CTEINT = self.match(covid19Parser.CTEINT)
                insertCteToDirectory((None if localctx._CTEINT is None else localctx._CTEINT.text), 'int')
                self.state = 341
                self.match(covid19Parser.CORCHETECUADRADOD)
                self.state = 346
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==covid19Parser.CORCHETECUADRADOI:
                    self.state = 342
                    self.match(covid19Parser.CORCHETECUADRADOI)
                    self.state = 343
                    localctx._CTEINT = self.match(covid19Parser.CTEINT)
                    insertCteToDirectory((None if localctx._CTEINT is None else localctx._CTEINT.text), 'int')
                    self.state = 345
                    self.match(covid19Parser.CORCHETECUADRADOD)




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAMA(self):
            return self.getToken(covid19Parser.PROGRAMA, 0)

        def identificador_accesa(self):
            return self.getTypedRuleContext(covid19Parser.Identificador_accesaContext,0)


        def PUNTOYCOMA(self):
            return self.getToken(covid19Parser.PUNTOYCOMA, 0)

        def funcp(self):
            return self.getTypedRuleContext(covid19Parser.FuncpContext,0)


        def varx(self):
            return self.getTypedRuleContext(covid19Parser.VarxContext,0)


        def metodo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.MetodoContext)
            else:
                return self.getTypedRuleContext(covid19Parser.MetodoContext,i)


        def getRuleIndex(self):
            return covid19Parser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = covid19Parser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(covid19Parser.PROGRAMA)
            self.state = 351
            self.identificador_accesa()
            self.state = 352
            self.match(covid19Parser.PUNTOYCOMA)
            self.state = 354
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==covid19Parser.VAR:
                self.state = 353
                self.varx()


            addFunctionToDirectory('principal', None)
            includeVarsTableInFunction('principal')
            addGotoPrincipal()
            self.state = 362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.FUNCION:
                self.state = 359
                self.metodo()
                self.state = 364
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 365
            self.funcp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._var = None # VarContext
            self._identificador_definicion = None # Identificador_definicionContext

        def VAR(self):
            return self.getToken(covid19Parser.VAR, 0)

        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.VarContext)
            else:
                return self.getTypedRuleContext(covid19Parser.VarContext,i)


        def PUNTOYCOMA(self, i:int=None):
            if i is None:
                return self.getTokens(covid19Parser.PUNTOYCOMA)
            else:
                return self.getToken(covid19Parser.PUNTOYCOMA, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(covid19Parser.COMA)
            else:
                return self.getToken(covid19Parser.COMA, i)

        def identificador_definicion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.Identificador_definicionContext)
            else:
                return self.getTypedRuleContext(covid19Parser.Identificador_definicionContext,i)


        def getRuleIndex(self):
            return covid19Parser.RULE_varx

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarx" ):
                listener.enterVarx(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarx" ):
                listener.exitVarx(self)




    def varx(self):

        localctx = covid19Parser.VarxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_varx)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(covid19Parser.VAR)
            self.state = 380 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 368
                localctx._var = self.var()
                self.state = 375
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==covid19Parser.COMA:
                    self.state = 369
                    self.match(covid19Parser.COMA)
                    self.state = 370
                    localctx._identificador_definicion = self.identificador_definicion()
                    addVarToVarsTable(None, (None if localctx._identificador_definicion is None else self._input.getText(localctx._identificador_definicion.start,localctx._identificador_definicion.stop)), (None if localctx._var is None else self._input.getText(localctx._var.start,localctx._var.stop)))
                    self.state = 377
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 378
                self.match(covid19Parser.PUNTOYCOMA)
                self.state = 382 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << covid19Parser.INT) | (1 << covid19Parser.FLOAT) | (1 << covid19Parser.STRING) | (1 << covid19Parser.CHAR) | (1 << covid19Parser.DATAFRAME))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._tipo = None # TipoContext
            self._identificador_definicion = None # Identificador_definicionContext

        def tipo(self):
            return self.getTypedRuleContext(covid19Parser.TipoContext,0)


        def DOSPUNTOS(self):
            return self.getToken(covid19Parser.DOSPUNTOS, 0)

        def identificador_definicion(self):
            return self.getTypedRuleContext(covid19Parser.Identificador_definicionContext,0)


        def getRuleIndex(self):
            return covid19Parser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)




    def var(self):

        localctx = covid19Parser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            localctx._tipo = self.tipo()
            self.state = 385
            self.match(covid19Parser.DOSPUNTOS)
            self.state = 386
            localctx._identificador_definicion = self.identificador_definicion()
            addVarToVarsTable((None if localctx._tipo is None else self._input.getText(localctx._tipo.start,localctx._tipo.stop)), (None if localctx._identificador_definicion is None else self._input.getText(localctx._identificador_definicion.start,localctx._identificador_definicion.stop)), None)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._PRINCIPAL = None # Token

        def PRINCIPAL(self):
            return self.getToken(covid19Parser.PRINCIPAL, 0)

        def PARENTESISI(self):
            return self.getToken(covid19Parser.PARENTESISI, 0)

        def PARENTESISD(self):
            return self.getToken(covid19Parser.PARENTESISD, 0)

        def bloque(self):
            return self.getTypedRuleContext(covid19Parser.BloqueContext,0)


        def getRuleIndex(self):
            return covid19Parser.RULE_funcp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncp" ):
                listener.enterFuncp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncp" ):
                listener.exitFuncp(self)




    def funcp(self):

        localctx = covid19Parser.FuncpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_funcp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            localctx._PRINCIPAL = self.match(covid19Parser.PRINCIPAL)
            setScope((None if localctx._PRINCIPAL is None else localctx._PRINCIPAL.text))
            self.state = 391
            self.match(covid19Parser.PARENTESISI)
            self.state = 392
            self.match(covid19Parser.PARENTESISD)
            self.state = 393
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(covid19Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(covid19Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(covid19Parser.STRING, 0)

        def CHAR(self):
            return self.getToken(covid19Parser.CHAR, 0)

        def DATAFRAME(self):
            return self.getToken(covid19Parser.DATAFRAME, 0)

        def getRuleIndex(self):
            return covid19Parser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = covid19Parser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << covid19Parser.INT) | (1 << covid19Parser.FLOAT) | (1 << covid19Parser.STRING) | (1 << covid19Parser.CHAR) | (1 << covid19Parser.DATAFRAME))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MetodoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._tipo = None # TipoContext
            self._ID = None # Token
            self._var = None # VarContext

        def FUNCION(self):
            return self.getToken(covid19Parser.FUNCION, 0)

        def ID(self):
            return self.getToken(covid19Parser.ID, 0)

        def PARENTESISI(self):
            return self.getToken(covid19Parser.PARENTESISI, 0)

        def PARENTESISD(self):
            return self.getToken(covid19Parser.PARENTESISD, 0)

        def PUNTOYCOMA(self):
            return self.getToken(covid19Parser.PUNTOYCOMA, 0)

        def CORCHETEI(self):
            return self.getToken(covid19Parser.CORCHETEI, 0)

        def CORCHETED(self):
            return self.getToken(covid19Parser.CORCHETED, 0)

        def tipo(self):
            return self.getTypedRuleContext(covid19Parser.TipoContext,0)


        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.VarContext)
            else:
                return self.getTypedRuleContext(covid19Parser.VarContext,i)


        def varx(self):
            return self.getTypedRuleContext(covid19Parser.VarxContext,0)


        def estatuto(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.EstatutoContext)
            else:
                return self.getTypedRuleContext(covid19Parser.EstatutoContext,i)


        def regresa(self):
            return self.getTypedRuleContext(covid19Parser.RegresaContext,0)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(covid19Parser.COMA)
            else:
                return self.getToken(covid19Parser.COMA, i)

        def getRuleIndex(self):
            return covid19Parser.RULE_metodo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMetodo" ):
                listener.enterMetodo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMetodo" ):
                listener.exitMetodo(self)




    def metodo(self):

        localctx = covid19Parser.MetodoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_metodo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.match(covid19Parser.FUNCION)
            self.state = 399
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << covid19Parser.INT) | (1 << covid19Parser.FLOAT) | (1 << covid19Parser.STRING) | (1 << covid19Parser.CHAR) | (1 << covid19Parser.DATAFRAME))) != 0):
                self.state = 398
                localctx._tipo = self.tipo()


            self.state = 401
            localctx._ID = self.match(covid19Parser.ID)
            addFunctionToDirectory((None if localctx._ID is None else localctx._ID.text), (None if localctx._tipo is None else self._input.getText(localctx._tipo.start,localctx._tipo.stop)))
            setScope((None if localctx._ID is None else localctx._ID.text))
            self.state = 404
            self.match(covid19Parser.PARENTESISI)
            self.state = 416
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << covid19Parser.INT) | (1 << covid19Parser.FLOAT) | (1 << covid19Parser.STRING) | (1 << covid19Parser.CHAR) | (1 << covid19Parser.DATAFRAME))) != 0):
                self.state = 405
                localctx._var = self.var()
                addVarToFunctionParams((None if localctx._var is None else self._input.getText(localctx._var.start,localctx._var.stop)), (None if localctx._ID is None else localctx._ID.text))
                self.state = 413
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==covid19Parser.COMA:
                    self.state = 407
                    self.match(covid19Parser.COMA)
                    self.state = 408
                    localctx._var = self.var()
                    addVarToFunctionParams((None if localctx._var is None else self._input.getText(localctx._var.start,localctx._var.stop)), (None if localctx._ID is None else localctx._ID.text))
                    self.state = 415
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 418
            self.match(covid19Parser.PARENTESISD)
            self.state = 419
            self.match(covid19Parser.PUNTOYCOMA)
            self.state = 421
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==covid19Parser.VAR:
                self.state = 420
                self.varx()


            includeVarsTableInFunction((None if localctx._ID is None else localctx._ID.text))
            rememberBeginingOfFunction((None if localctx._ID is None else localctx._ID.text))
            self.state = 425
            self.match(covid19Parser.CORCHETEI)
            self.state = 429
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 426
                    self.estatuto() 
                self.state = 431
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

            self.state = 433
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==covid19Parser.REGRESA:
                self.state = 432
                self.regresa()


            self.state = 435
            self.match(covid19Parser.CORCHETED)
            reachedFunctionDefinitionEnd((None if localctx._ID is None else localctx._ID.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





