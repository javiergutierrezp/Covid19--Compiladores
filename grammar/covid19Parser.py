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
        buf.write("\u01b2\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\6\4P\n\4\r\4\16\4Q\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5`\n\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\5\6j\n\6\3\6\3\6\3\6\5\6o\n\6\3\6\3")
        buf.write("\6\3\6\5\6t\n\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\5\7\u0080\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7")
        buf.write("\b\u008b\n\b\f\b\16\b\u008e\13\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u009d\n\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00a9\n\t\7\t\u00ab")
        buf.write("\n\t\f\t\16\t\u00ae\13\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\5\n\u00b8\n\n\3\n\3\n\3\n\7\n\u00bd\n\n\f\n\16\n\u00c0")
        buf.write("\13\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\5\13\u00d0\n\13\3\13\3\13\3\13\5")
        buf.write("\13\u00d5\n\13\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00dd\n\f\3")
        buf.write("\f\3\f\3\f\7\f\u00e2\n\f\f\f\16\f\u00e5\13\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\5\r\u00ed\n\r\3\r\3\r\3\r\7\r\u00f2\n\r")
        buf.write("\f\r\16\r\u00f5\13\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\5\16\u0102\n\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u0118\n\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\7\20")
        buf.write("\u0125\n\20\f\20\16\20\u0128\13\20\5\20\u012a\n\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0149\n\23\5\23\u014b")
        buf.write("\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24")
        buf.write("\u0156\n\24\5\24\u0158\n\24\3\25\3\25\3\25\3\25\5\25\u015e")
        buf.write("\n\25\3\25\3\25\3\25\3\25\7\25\u0164\n\25\f\25\16\25\u0167")
        buf.write("\13\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u0171")
        buf.write("\n\26\f\26\16\26\u0174\13\26\3\26\3\26\6\26\u0178\n\26")
        buf.write("\r\26\16\26\u0179\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\31\3\31\3\32\3\32\5\32\u018b\n\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\7\32")
        buf.write("\u0197\n\32\f\32\16\32\u019a\13\32\5\32\u019c\n\32\3\32")
        buf.write("\3\32\3\32\5\32\u01a1\n\32\3\32\3\32\3\32\3\32\7\32\u01a7")
        buf.write("\n\32\f\32\16\32\u01aa\13\32\3\32\5\32\u01ad\n\32\3\32")
        buf.write("\3\32\3\32\3\32\2\2\33\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\2\3\3\2\3\7\2\u01ce\2\64\3\2\2\2")
        buf.write("\4B\3\2\2\2\6M\3\2\2\2\bU\3\2\2\2\nc\3\2\2\2\f\177\3\2")
        buf.write("\2\2\16\u0081\3\2\2\2\20\u0091\3\2\2\2\22\u00b1\3\2\2")
        buf.write("\2\24\u00c1\3\2\2\2\26\u00d6\3\2\2\2\30\u00e6\3\2\2\2")
        buf.write("\32\u0101\3\2\2\2\34\u0117\3\2\2\2\36\u0119\3\2\2\2 \u0130")
        buf.write("\3\2\2\2\"\u0137\3\2\2\2$\u013e\3\2\2\2&\u014c\3\2\2\2")
        buf.write("(\u0159\3\2\2\2*\u016a\3\2\2\2,\u017b\3\2\2\2.\u0180\3")
        buf.write("\2\2\2\60\u0186\3\2\2\2\62\u0188\3\2\2\2\64\65\7\23\2")
        buf.write("\2\65\66\5$\23\2\66\67\b\2\1\2\678\7\35\2\289\b\2\1\2")
        buf.write("9:\5\26\f\2:;\b\2\1\2;<\7\24\2\2<=\5\26\f\2=>\b\2\1\2")
        buf.write(">?\7\25\2\2?@\5\6\4\2@A\b\2\1\2A\3\3\2\2\2BC\7\26\2\2")
        buf.write("CD\b\3\1\2DE\7\36\2\2EF\5\22\n\2FG\b\3\1\2GH\7\37\2\2")
        buf.write("HI\7\27\2\2IJ\5\6\4\2JK\b\3\1\2KL\b\3\1\2L\5\3\2\2\2M")
        buf.write("O\7\33\2\2NP\5\34\17\2ON\3\2\2\2PQ\3\2\2\2QO\3\2\2\2Q")
        buf.write("R\3\2\2\2RS\3\2\2\2ST\7\34\2\2T\7\3\2\2\2UV\7\13\2\2V")
        buf.write("W\7\36\2\2WX\5\22\n\2XY\b\5\1\2YZ\7\37\2\2Z[\7\f\2\2[")
        buf.write("\\\5\6\4\2\\_\b\5\1\2]^\7\r\2\2^`\5\6\4\2_]\3\2\2\2_`")
        buf.write("\3\2\2\2`a\3\2\2\2ab\b\5\1\2b\t\3\2\2\2cd\7\n\2\2de\7")
        buf.write("\36\2\2ef\7\63\2\2fi\7\31\2\2gj\5$\23\2hj\5\f\7\2ig\3")
        buf.write("\2\2\2ih\3\2\2\2jk\3\2\2\2kn\7\31\2\2lo\5$\23\2mo\5\f")
        buf.write("\7\2nl\3\2\2\2nm\3\2\2\2op\3\2\2\2ps\7\31\2\2qt\5$\23")
        buf.write("\2rt\5\f\7\2sq\3\2\2\2sr\3\2\2\2tu\3\2\2\2uv\7\37\2\2")
        buf.write("v\13\3\2\2\2wx\7\61\2\2x\u0080\b\7\1\2yz\7/\2\2z\u0080")
        buf.write("\b\7\1\2{|\7\60\2\2|\u0080\b\7\1\2}~\7\62\2\2~\u0080\b")
        buf.write("\7\1\2\177w\3\2\2\2\177y\3\2\2\2\177{\3\2\2\2\177}\3\2")
        buf.write("\2\2\u0080\r\3\2\2\2\u0081\u0082\7\17\2\2\u0082\u0083")
        buf.write("\7\36\2\2\u0083\u0084\5$\23\2\u0084\u0085\b\b\1\2\u0085")
        buf.write("\u008c\3\2\2\2\u0086\u0087\7\31\2\2\u0087\u0088\5$\23")
        buf.write("\2\u0088\u0089\b\b\1\2\u0089\u008b\3\2\2\2\u008a\u0086")
        buf.write("\3\2\2\2\u008b\u008e\3\2\2\2\u008c\u008a\3\2\2\2\u008c")
        buf.write("\u008d\3\2\2\2\u008d\u008f\3\2\2\2\u008e\u008c\3\2\2\2")
        buf.write("\u008f\u0090\7\37\2\2\u0090\17\3\2\2\2\u0091\u0092\7\16")
        buf.write("\2\2\u0092\u009c\7\36\2\2\u0093\u0094\5$\23\2\u0094\u0095")
        buf.write("\b\t\1\2\u0095\u009d\3\2\2\2\u0096\u0097\5\f\7\2\u0097")
        buf.write("\u0098\b\t\1\2\u0098\u009d\3\2\2\2\u0099\u009a\5\26\f")
        buf.write("\2\u009a\u009b\b\t\1\2\u009b\u009d\3\2\2\2\u009c\u0093")
        buf.write("\3\2\2\2\u009c\u0096\3\2\2\2\u009c\u0099\3\2\2\2\u009d")
        buf.write("\u00ac\3\2\2\2\u009e\u00a8\7\31\2\2\u009f\u00a0\5$\23")
        buf.write("\2\u00a0\u00a1\b\t\1\2\u00a1\u00a9\3\2\2\2\u00a2\u00a3")
        buf.write("\5\f\7\2\u00a3\u00a4\b\t\1\2\u00a4\u00a9\3\2\2\2\u00a5")
        buf.write("\u00a6\5\26\f\2\u00a6\u00a7\b\t\1\2\u00a7\u00a9\3\2\2")
        buf.write("\2\u00a8\u009f\3\2\2\2\u00a8\u00a2\3\2\2\2\u00a8\u00a5")
        buf.write("\3\2\2\2\u00a9\u00ab\3\2\2\2\u00aa\u009e\3\2\2\2\u00ab")
        buf.write("\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2")
        buf.write("\u00ad\u00af\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b0\7")
        buf.write("\37\2\2\u00b0\21\3\2\2\2\u00b1\u00b2\5\24\13\2\u00b2\u00be")
        buf.write("\b\n\1\2\u00b3\u00b4\7-\2\2\u00b4\u00b8\b\n\1\2\u00b5")
        buf.write("\u00b6\7.\2\2\u00b6\u00b8\b\n\1\2\u00b7\u00b3\3\2\2\2")
        buf.write("\u00b7\u00b5\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00ba\5")
        buf.write("\24\13\2\u00ba\u00bb\b\n\1\2\u00bb\u00bd\3\2\2\2\u00bc")
        buf.write("\u00b7\3\2\2\2\u00bd\u00c0\3\2\2\2\u00be\u00bc\3\2\2\2")
        buf.write("\u00be\u00bf\3\2\2\2\u00bf\23\3\2\2\2\u00c0\u00be\3\2")
        buf.write("\2\2\u00c1\u00c2\5\26\f\2\u00c2\u00d4\b\13\1\2\u00c3\u00c4")
        buf.write("\7\"\2\2\u00c4\u00d0\b\13\1\2\u00c5\u00c6\7#\2\2\u00c6")
        buf.write("\u00d0\b\13\1\2\u00c7\u00c8\7$\2\2\u00c8\u00d0\b\13\1")
        buf.write("\2\u00c9\u00ca\7%\2\2\u00ca\u00d0\b\13\1\2\u00cb\u00cc")
        buf.write("\7&\2\2\u00cc\u00d0\b\13\1\2\u00cd\u00ce\7\'\2\2\u00ce")
        buf.write("\u00d0\b\13\1\2\u00cf\u00c3\3\2\2\2\u00cf\u00c5\3\2\2")
        buf.write("\2\u00cf\u00c7\3\2\2\2\u00cf\u00c9\3\2\2\2\u00cf\u00cb")
        buf.write("\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1")
        buf.write("\u00d2\5\26\f\2\u00d2\u00d3\b\13\1\2\u00d3\u00d5\3\2\2")
        buf.write("\2\u00d4\u00cf\3\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\25\3")
        buf.write("\2\2\2\u00d6\u00d7\5\30\r\2\u00d7\u00e3\b\f\1\2\u00d8")
        buf.write("\u00d9\7)\2\2\u00d9\u00dd\b\f\1\2\u00da\u00db\7*\2\2\u00db")
        buf.write("\u00dd\b\f\1\2\u00dc\u00d8\3\2\2\2\u00dc\u00da\3\2\2\2")
        buf.write("\u00dd\u00de\3\2\2\2\u00de\u00df\5\30\r\2\u00df\u00e0")
        buf.write("\b\f\1\2\u00e0\u00e2\3\2\2\2\u00e1\u00dc\3\2\2\2\u00e2")
        buf.write("\u00e5\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2")
        buf.write("\u00e4\27\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e6\u00e7\5\32")
        buf.write("\16\2\u00e7\u00f3\b\r\1\2\u00e8\u00e9\7+\2\2\u00e9\u00ed")
        buf.write("\b\r\1\2\u00ea\u00eb\7,\2\2\u00eb\u00ed\b\r\1\2\u00ec")
        buf.write("\u00e8\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ed\u00ee\3\2\2\2")
        buf.write("\u00ee\u00ef\5\32\16\2\u00ef\u00f0\b\r\1\2\u00f0\u00f2")
        buf.write("\3\2\2\2\u00f1\u00ec\3\2\2\2\u00f2\u00f5\3\2\2\2\u00f3")
        buf.write("\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\31\3\2\2\2\u00f5")
        buf.write("\u00f3\3\2\2\2\u00f6\u00f7\5$\23\2\u00f7\u00f8\b\16\1")
        buf.write("\2\u00f8\u0102\3\2\2\2\u00f9\u0102\5\f\7\2\u00fa\u0102")
        buf.write("\5\36\20\2\u00fb\u00fc\7\36\2\2\u00fc\u00fd\b\16\1\2\u00fd")
        buf.write("\u00fe\5\22\n\2\u00fe\u00ff\7\37\2\2\u00ff\u0100\b\16")
        buf.write("\1\2\u0100\u0102\3\2\2\2\u0101\u00f6\3\2\2\2\u0101\u00f9")
        buf.write("\3\2\2\2\u0101\u00fa\3\2\2\2\u0101\u00fb\3\2\2\2\u0102")
        buf.write("\33\3\2\2\2\u0103\u0104\5\36\20\2\u0104\u0105\7\30\2\2")
        buf.write("\u0105\u0118\3\2\2\2\u0106\u0107\5\"\22\2\u0107\u0108")
        buf.write("\7\30\2\2\u0108\u0118\3\2\2\2\u0109\u010a\5\16\b\2\u010a")
        buf.write("\u010b\7\30\2\2\u010b\u0118\3\2\2\2\u010c\u010d\5\20\t")
        buf.write("\2\u010d\u010e\7\30\2\2\u010e\u0118\3\2\2\2\u010f\u0110")
        buf.write("\5\n\6\2\u0110\u0111\7\30\2\2\u0111\u0118\3\2\2\2\u0112")
        buf.write("\u0118\5\b\5\2\u0113\u0118\5\4\3\2\u0114\u0118\5\2\2\2")
        buf.write("\u0115\u0118\5\62\32\2\u0116\u0118\5 \21\2\u0117\u0103")
        buf.write("\3\2\2\2\u0117\u0106\3\2\2\2\u0117\u0109\3\2\2\2\u0117")
        buf.write("\u010c\3\2\2\2\u0117\u010f\3\2\2\2\u0117\u0112\3\2\2\2")
        buf.write("\u0117\u0113\3\2\2\2\u0117\u0114\3\2\2\2\u0117\u0115\3")
        buf.write("\2\2\2\u0117\u0116\3\2\2\2\u0118\35\3\2\2\2\u0119\u011a")
        buf.write("\7\63\2\2\u011a\u011b\b\20\1\2\u011b\u011c\b\20\1\2\u011c")
        buf.write("\u011d\7\36\2\2\u011d\u0129\b\20\1\2\u011e\u011f\5\22")
        buf.write("\n\2\u011f\u0126\b\20\1\2\u0120\u0121\7\31\2\2\u0121\u0122")
        buf.write("\5\22\n\2\u0122\u0123\b\20\1\2\u0123\u0125\3\2\2\2\u0124")
        buf.write("\u0120\3\2\2\2\u0125\u0128\3\2\2\2\u0126\u0124\3\2\2\2")
        buf.write("\u0126\u0127\3\2\2\2\u0127\u012a\3\2\2\2\u0128\u0126\3")
        buf.write("\2\2\2\u0129\u011e\3\2\2\2\u0129\u012a\3\2\2\2\u012a\u012b")
        buf.write("\3\2\2\2\u012b\u012c\b\20\1\2\u012c\u012d\7\37\2\2\u012d")
        buf.write("\u012e\b\20\1\2\u012e\u012f\b\20\1\2\u012f\37\3\2\2\2")
        buf.write("\u0130\u0131\7\20\2\2\u0131\u0132\7\36\2\2\u0132\u0133")
        buf.write("\5\22\n\2\u0133\u0134\7\37\2\2\u0134\u0135\b\21\1\2\u0135")
        buf.write("\u0136\7\30\2\2\u0136!\3\2\2\2\u0137\u0138\5$\23\2\u0138")
        buf.write("\u0139\b\22\1\2\u0139\u013a\7\35\2\2\u013a\u013b\b\22")
        buf.write("\1\2\u013b\u013c\5\22\n\2\u013c\u013d\b\22\1\2\u013d#")
        buf.write("\3\2\2\2\u013e\u014a\7\63\2\2\u013f\u0140\7 \2\2\u0140")
        buf.write("\u0141\5\26\f\2\u0141\u0142\b\23\1\2\u0142\u0148\7!\2")
        buf.write("\2\u0143\u0144\7 \2\2\u0144\u0145\5\26\f\2\u0145\u0146")
        buf.write("\b\23\1\2\u0146\u0147\7!\2\2\u0147\u0149\3\2\2\2\u0148")
        buf.write("\u0143\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014b\3\2\2\2")
        buf.write("\u014a\u013f\3\2\2\2\u014a\u014b\3\2\2\2\u014b%\3\2\2")
        buf.write("\2\u014c\u0157\7\63\2\2\u014d\u014e\7 \2\2\u014e\u014f")
        buf.write("\7/\2\2\u014f\u0150\b\24\1\2\u0150\u0155\7!\2\2\u0151")
        buf.write("\u0152\7 \2\2\u0152\u0153\7/\2\2\u0153\u0154\b\24\1\2")
        buf.write("\u0154\u0156\7!\2\2\u0155\u0151\3\2\2\2\u0155\u0156\3")
        buf.write("\2\2\2\u0156\u0158\3\2\2\2\u0157\u014d\3\2\2\2\u0157\u0158")
        buf.write("\3\2\2\2\u0158\'\3\2\2\2\u0159\u015a\7\21\2\2\u015a\u015b")
        buf.write("\5$\23\2\u015b\u015d\7\30\2\2\u015c\u015e\5*\26\2\u015d")
        buf.write("\u015c\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u015f\3\2\2\2")
        buf.write("\u015f\u0160\b\25\1\2\u0160\u0161\b\25\1\2\u0161\u0165")
        buf.write("\b\25\1\2\u0162\u0164\5\62\32\2\u0163\u0162\3\2\2\2\u0164")
        buf.write("\u0167\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0166\3\2\2\2")
        buf.write("\u0166\u0168\3\2\2\2\u0167\u0165\3\2\2\2\u0168\u0169\5")
        buf.write(".\30\2\u0169)\3\2\2\2\u016a\u0177\7\b\2\2\u016b\u0172")
        buf.write("\5,\27\2\u016c\u016d\7\31\2\2\u016d\u016e\5&\24\2\u016e")
        buf.write("\u016f\b\26\1\2\u016f\u0171\3\2\2\2\u0170\u016c\3\2\2")
        buf.write("\2\u0171\u0174\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173")
        buf.write("\3\2\2\2\u0173\u0175\3\2\2\2\u0174\u0172\3\2\2\2\u0175")
        buf.write("\u0176\7\30\2\2\u0176\u0178\3\2\2\2\u0177\u016b\3\2\2")
        buf.write("\2\u0178\u0179\3\2\2\2\u0179\u0177\3\2\2\2\u0179\u017a")
        buf.write("\3\2\2\2\u017a+\3\2\2\2\u017b\u017c\5\60\31\2\u017c\u017d")
        buf.write("\7\32\2\2\u017d\u017e\5&\24\2\u017e\u017f\b\27\1\2\u017f")
        buf.write("-\3\2\2\2\u0180\u0181\7\22\2\2\u0181\u0182\b\30\1\2\u0182")
        buf.write("\u0183\7\36\2\2\u0183\u0184\7\37\2\2\u0184\u0185\5\6\4")
        buf.write("\2\u0185/\3\2\2\2\u0186\u0187\t\2\2\2\u0187\61\3\2\2\2")
        buf.write("\u0188\u018a\7\t\2\2\u0189\u018b\5\60\31\2\u018a\u0189")
        buf.write("\3\2\2\2\u018a\u018b\3\2\2\2\u018b\u018c\3\2\2\2\u018c")
        buf.write("\u018d\7\63\2\2\u018d\u018e\b\32\1\2\u018e\u018f\b\32")
        buf.write("\1\2\u018f\u019b\7\36\2\2\u0190\u0191\5,\27\2\u0191\u0198")
        buf.write("\b\32\1\2\u0192\u0193\7\31\2\2\u0193\u0194\5,\27\2\u0194")
        buf.write("\u0195\b\32\1\2\u0195\u0197\3\2\2\2\u0196\u0192\3\2\2")
        buf.write("\2\u0197\u019a\3\2\2\2\u0198\u0196\3\2\2\2\u0198\u0199")
        buf.write("\3\2\2\2\u0199\u019c\3\2\2\2\u019a\u0198\3\2\2\2\u019b")
        buf.write("\u0190\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u019d\3\2\2\2")
        buf.write("\u019d\u019e\7\37\2\2\u019e\u01a0\7\30\2\2\u019f\u01a1")
        buf.write("\5*\26\2\u01a0\u019f\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1")
        buf.write("\u01a2\3\2\2\2\u01a2\u01a3\b\32\1\2\u01a3\u01a4\b\32\1")
        buf.write("\2\u01a4\u01a8\7\33\2\2\u01a5\u01a7\5\34\17\2\u01a6\u01a5")
        buf.write("\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8")
        buf.write("\u01a9\3\2\2\2\u01a9\u01ac\3\2\2\2\u01aa\u01a8\3\2\2\2")
        buf.write("\u01ab\u01ad\5 \21\2\u01ac\u01ab\3\2\2\2\u01ac\u01ad\3")
        buf.write("\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01af\7\34\2\2\u01af")
        buf.write("\u01b0\b\32\1\2\u01b0\63\3\2\2\2&Q_ins\177\u008c\u009c")
        buf.write("\u00a8\u00ac\u00b7\u00be\u00cf\u00d4\u00dc\u00e3\u00ec")
        buf.write("\u00f3\u0101\u0117\u0126\u0129\u0148\u014a\u0155\u0157")
        buf.write("\u015d\u0165\u0172\u0179\u018a\u0198\u019b\u01a0\u01a8")
        buf.write("\u01ac")
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
                     "'!'", "'+'", "'-'", "'*'", "'/'", "'&'", "'|'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\".\"'" ]

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
            leaving('asignacion')
            self.state = 57
            self.match(covid19Parser.HASTA)
            self.state = 58
            self.expresion()
            forEvaluation()
            self.state = 60
            self.match(covid19Parser.HACER)
            self.state = 61
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
            self.state = 64
            self.match(covid19Parser.MIENTRAS)
            addMigajitaDePan()
            self.state = 66
            self.match(covid19Parser.PARENTESISI)
            self.state = 67
            self.megaexpresion()
            addGotoF()
            self.state = 69
            self.match(covid19Parser.PARENTESISD)
            self.state = 70
            self.match(covid19Parser.HAZ)
            self.state = 71
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
            self.state = 75
            self.match(covid19Parser.CORCHETEI)
            self.state = 77 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 76
                self.estatuto()
                self.state = 79 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << covid19Parser.FUNCION) | (1 << covid19Parser.CARGAARCHIVO) | (1 << covid19Parser.SI) | (1 << covid19Parser.ESCRIBE) | (1 << covid19Parser.LEE) | (1 << covid19Parser.REGRESA) | (1 << covid19Parser.DESDE) | (1 << covid19Parser.MIENTRAS) | (1 << covid19Parser.ID))) != 0)):
                    break

            self.state = 81
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
            self.state = 83
            self.match(covid19Parser.SI)
            self.state = 84
            self.match(covid19Parser.PARENTESISI)
            self.state = 85
            self.megaexpresion()
            addGotoF()
            self.state = 87
            self.match(covid19Parser.PARENTESISD)
            self.state = 88
            self.match(covid19Parser.ENTONCES)
            self.state = 89
            self.bloque()
            addGotoA()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==covid19Parser.SINO:
                self.state = 91
                self.match(covid19Parser.SINO)
                self.state = 92
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
            self.state = 97
            self.match(covid19Parser.CARGAARCHIVO)
            self.state = 98
            self.match(covid19Parser.PARENTESISI)
            self.state = 99
            self.match(covid19Parser.ID)
            self.state = 100
            self.match(covid19Parser.COMA)
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [covid19Parser.ID]:
                self.state = 101
                self.identificador_accesa()
                pass
            elif token in [covid19Parser.CTEINT, covid19Parser.CTEFLOAT, covid19Parser.CTESTRING, covid19Parser.CTECHAR]:
                self.state = 102
                self.cte()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 105
            self.match(covid19Parser.COMA)
            self.state = 108
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [covid19Parser.ID]:
                self.state = 106
                self.identificador_accesa()
                pass
            elif token in [covid19Parser.CTEINT, covid19Parser.CTEFLOAT, covid19Parser.CTESTRING, covid19Parser.CTECHAR]:
                self.state = 107
                self.cte()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 110
            self.match(covid19Parser.COMA)
            self.state = 113
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [covid19Parser.ID]:
                self.state = 111
                self.identificador_accesa()
                pass
            elif token in [covid19Parser.CTEINT, covid19Parser.CTEFLOAT, covid19Parser.CTESTRING, covid19Parser.CTECHAR]:
                self.state = 112
                self.cte()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 115
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
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [covid19Parser.CTESTRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                localctx._CTESTRING = self.match(covid19Parser.CTESTRING)
                insertCteToStructs((None if localctx._CTESTRING is None else localctx._CTESTRING.text), 'string')
                pass
            elif token in [covid19Parser.CTEINT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 119
                localctx._CTEINT = self.match(covid19Parser.CTEINT)
                insertCteToStructs((None if localctx._CTEINT is None else localctx._CTEINT.text), 'int')
                pass
            elif token in [covid19Parser.CTEFLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 121
                localctx._CTEFLOAT = self.match(covid19Parser.CTEFLOAT)
                insertCteToStructs((None if localctx._CTEFLOAT is None else localctx._CTEFLOAT.text), 'float')
                pass
            elif token in [covid19Parser.CTECHAR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 123
                localctx._CTECHAR = self.match(covid19Parser.CTECHAR)
                insertCteToStructs((None if localctx._CTECHAR is None else localctx._CTECHAR.text), 'char')
                pass
            else:
                raise NoViableAltException(self)

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
            self.state = 127
            self.match(covid19Parser.LEE)
            self.state = 128
            self.match(covid19Parser.PARENTESISI)

            self.state = 129
            localctx._identificador_accesa = self.identificador_accesa()
            readId((None if localctx._identificador_accesa is None else self._input.getText(localctx._identificador_accesa.start,localctx._identificador_accesa.stop)))
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.COMA:
                self.state = 132
                self.match(covid19Parser.COMA)
                self.state = 133
                localctx._identificador_accesa = self.identificador_accesa()
                readId((None if localctx._identificador_accesa is None else self._input.getText(localctx._identificador_accesa.start,localctx._identificador_accesa.stop)))
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 141
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
            self.state = 143
            self.match(covid19Parser.ESCRIBE)
            self.state = 144
            self.match(covid19Parser.PARENTESISI)
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 145
                localctx._identificador_accesa = self.identificador_accesa()
                write((None if localctx._identificador_accesa is None else self._input.getText(localctx._identificador_accesa.start,localctx._identificador_accesa.stop)))
                pass

            elif la_ == 2:
                self.state = 148
                localctx._cte = self.cte()
                write((None if localctx._cte is None else self._input.getText(localctx._cte.start,localctx._cte.stop)))
                pass

            elif la_ == 3:
                self.state = 151
                self.expresion()
                write(None)
                pass


            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.COMA:
                self.state = 156
                self.match(covid19Parser.COMA)
                self.state = 166
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 157
                    localctx._identificador_accesa = self.identificador_accesa()
                    write((None if localctx._identificador_accesa is None else self._input.getText(localctx._identificador_accesa.start,localctx._identificador_accesa.stop)))
                    pass

                elif la_ == 2:
                    self.state = 160
                    localctx._cte = self.cte()
                    write((None if localctx._cte is None else self._input.getText(localctx._cte.start,localctx._cte.stop)))
                    pass

                elif la_ == 3:
                    self.state = 163
                    self.expresion()
                    write(None)
                    pass


                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 173
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
            self.state = 175
            self.superexpresion()
            leaving('union')
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.Y or _la==covid19Parser.O:
                self.state = 181
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [covid19Parser.Y]:
                    self.state = 177
                    localctx._Y = self.match(covid19Parser.Y)
                    insertOperator((None if localctx._Y is None else localctx._Y.text))
                    pass
                elif token in [covid19Parser.O]:
                    self.state = 179
                    localctx._O = self.match(covid19Parser.O)
                    insertOperator((None if localctx._O is None else localctx._O.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 183
                self.superexpresion()
                leaving('union')
                self.state = 190
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
            self.state = 191
            self.expresion()
            leaving('comparacion')
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << covid19Parser.MAYOR) | (1 << covid19Parser.MENOR) | (1 << covid19Parser.MAYORIGUAL) | (1 << covid19Parser.MENORIGUAL) | (1 << covid19Parser.IGUALCOMP) | (1 << covid19Parser.DIFERENTE))) != 0):
                self.state = 205
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [covid19Parser.MAYOR]:
                    self.state = 193
                    localctx._MAYOR = self.match(covid19Parser.MAYOR)
                    insertOperator((None if localctx._MAYOR is None else localctx._MAYOR.text))
                    pass
                elif token in [covid19Parser.MENOR]:
                    self.state = 195
                    localctx._MENOR = self.match(covid19Parser.MENOR)
                    insertOperator((None if localctx._MENOR is None else localctx._MENOR.text))
                    pass
                elif token in [covid19Parser.MAYORIGUAL]:
                    self.state = 197
                    localctx._MAYORIGUAL = self.match(covid19Parser.MAYORIGUAL)
                    insertOperator((None if localctx._MAYORIGUAL is None else localctx._MAYORIGUAL.text))
                    pass
                elif token in [covid19Parser.MENORIGUAL]:
                    self.state = 199
                    localctx._MENORIGUAL = self.match(covid19Parser.MENORIGUAL)
                    insertOperator((None if localctx._MENORIGUAL is None else localctx._MENORIGUAL.text))
                    pass
                elif token in [covid19Parser.IGUALCOMP]:
                    self.state = 201
                    localctx._IGUALCOMP = self.match(covid19Parser.IGUALCOMP)
                    insertOperator((None if localctx._IGUALCOMP is None else localctx._IGUALCOMP.text))
                    pass
                elif token in [covid19Parser.DIFERENTE]:
                    self.state = 203
                    localctx._DIFERENTE = self.match(covid19Parser.DIFERENTE)
                    insertOperator((None if localctx._DIFERENTE is None else localctx._DIFERENTE.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 207
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
            self.state = 212
            self.termino()
            leaving('termino')
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.SUMA or _la==covid19Parser.RESTA:
                self.state = 218
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [covid19Parser.SUMA]:
                    self.state = 214
                    localctx._SUMA = self.match(covid19Parser.SUMA)
                    insertOperator((None if localctx._SUMA is None else localctx._SUMA.text))
                    pass
                elif token in [covid19Parser.RESTA]:
                    self.state = 216
                    localctx._RESTA = self.match(covid19Parser.RESTA)
                    insertOperator((None if localctx._RESTA is None else localctx._RESTA.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 220
                self.termino()
                leaving('termino')
                self.state = 227
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
            self.state = 228
            self.factor()
            leaving('factor')
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.MULTIPLICACION or _la==covid19Parser.DIVISION:
                self.state = 234
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [covid19Parser.MULTIPLICACION]:
                    self.state = 230
                    localctx._MULTIPLICACION = self.match(covid19Parser.MULTIPLICACION)
                    insertOperator((None if localctx._MULTIPLICACION is None else localctx._MULTIPLICACION.text))
                    pass
                elif token in [covid19Parser.DIVISION]:
                    self.state = 232
                    localctx._DIVISION = self.match(covid19Parser.DIVISION)
                    insertOperator((None if localctx._DIVISION is None else localctx._DIVISION.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 236
                self.factor()
                leaving('factor')
                self.state = 243
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
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                localctx._identificador_accesa = self.identificador_accesa()
                insertIdToStack((None if localctx._identificador_accesa is None else self._input.getText(localctx._identificador_accesa.start,localctx._identificador_accesa.stop)))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.cte()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 248
                self.llamadametodo()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 249
                self.match(covid19Parser.PARENTESISI)
                insertParenthesis()
                self.state = 251
                self.megaexpresion()
                self.state = 252
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
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 257
                self.llamadametodo()
                self.state = 258
                self.match(covid19Parser.PUNTOYCOMA)
                pass

            elif la_ == 2:
                self.state = 260
                self.asignacion()
                self.state = 261
                self.match(covid19Parser.PUNTOYCOMA)
                pass

            elif la_ == 3:
                self.state = 263
                self.lectura()
                self.state = 264
                self.match(covid19Parser.PUNTOYCOMA)
                pass

            elif la_ == 4:
                self.state = 266
                self.escritura()
                self.state = 267
                self.match(covid19Parser.PUNTOYCOMA)
                pass

            elif la_ == 5:
                self.state = 269
                self.cargadatos()
                self.state = 270
                self.match(covid19Parser.PUNTOYCOMA)
                pass

            elif la_ == 6:
                self.state = 272
                self.decision()
                pass

            elif la_ == 7:
                self.state = 273
                self.condicional()
                pass

            elif la_ == 8:
                self.state = 274
                self.nocondicional()
                pass

            elif la_ == 9:
                self.state = 275
                self.metodo()
                pass

            elif la_ == 10:
                self.state = 276
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
            self.state = 279
            localctx._ID = self.match(covid19Parser.ID)
            validateFunctionExistance((None if localctx._ID is None else localctx._ID.text))
            insertERASize((None if localctx._ID is None else localctx._ID.text))
            self.state = 282
            self.match(covid19Parser.PARENTESISI)
            insertParenthesis()
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << covid19Parser.PARENTESISI) | (1 << covid19Parser.CTEINT) | (1 << covid19Parser.CTEFLOAT) | (1 << covid19Parser.CTESTRING) | (1 << covid19Parser.CTECHAR) | (1 << covid19Parser.ID))) != 0):
                self.state = 284
                self.megaexpresion()
                incrementReceivedParamCounter()
                self.state = 292
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==covid19Parser.COMA:
                    self.state = 286
                    self.match(covid19Parser.COMA)
                    self.state = 287
                    self.megaexpresion()
                    incrementReceivedParamCounter()
                    self.state = 294
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            receivedFunctionParameters((None if localctx._ID is None else localctx._ID.text))
            self.state = 298
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
            self.state = 302
            self.match(covid19Parser.REGRESA)
            self.state = 303
            self.match(covid19Parser.PARENTESISI)
            self.state = 304
            localctx._megaexpresion = self.megaexpresion()
            self.state = 305
            self.match(covid19Parser.PARENTESISD)
            generateReturnQuad((None if localctx._megaexpresion is None else self._input.getText(localctx._megaexpresion.start,localctx._megaexpresion.stop)))
            self.state = 307
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
            self.state = 309
            localctx._identificador_accesa = self.identificador_accesa()
            insertIdToStack((None if localctx._identificador_accesa is None else self._input.getText(localctx._identificador_accesa.start,localctx._identificador_accesa.stop)), 'asignacion')
            self.state = 311
            localctx._IGUAL = self.match(covid19Parser.IGUAL)
            insertOperator((None if localctx._IGUAL is None else localctx._IGUAL.text))
            self.state = 313
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
            self.state = 316
            localctx._ID = self.match(covid19Parser.ID)
            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==covid19Parser.CORCHETECUADRADOI:
                self.state = 317
                self.match(covid19Parser.CORCHETECUADRADOI)
                self.state = 318
                self.expresion()
                verify('1', (None if localctx._ID is None else localctx._ID.text))
                self.state = 320
                self.match(covid19Parser.CORCHETECUADRADOD)
                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==covid19Parser.CORCHETECUADRADOI:
                    self.state = 321
                    self.match(covid19Parser.CORCHETECUADRADOI)
                    self.state = 322
                    self.expresion()
                    verify('2', (None if localctx._ID is None else localctx._ID.text))
                    self.state = 324
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
            self.state = 330
            self.match(covid19Parser.ID)
            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==covid19Parser.CORCHETECUADRADOI:
                self.state = 331
                self.match(covid19Parser.CORCHETECUADRADOI)
                self.state = 332
                localctx._CTEINT = self.match(covid19Parser.CTEINT)
                insertCteToDirectory((None if localctx._CTEINT is None else localctx._CTEINT.text), 'int')
                self.state = 334
                self.match(covid19Parser.CORCHETECUADRADOD)
                self.state = 339
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==covid19Parser.CORCHETECUADRADOI:
                    self.state = 335
                    self.match(covid19Parser.CORCHETECUADRADOI)
                    self.state = 336
                    localctx._CTEINT = self.match(covid19Parser.CTEINT)
                    insertCteToDirectory((None if localctx._CTEINT is None else localctx._CTEINT.text), 'int')
                    self.state = 338
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
            self.state = 343
            self.match(covid19Parser.PROGRAMA)
            self.state = 344
            self.identificador_accesa()
            self.state = 345
            self.match(covid19Parser.PUNTOYCOMA)
            self.state = 347
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==covid19Parser.VAR:
                self.state = 346
                self.varx()


            addFunctionToDirectory('principal', None)
            includeVarsTableInFunction('principal')
            addGotoPrincipal()
            self.state = 355
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.FUNCION:
                self.state = 352
                self.metodo()
                self.state = 357
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 358
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
            self.state = 360
            self.match(covid19Parser.VAR)
            self.state = 373 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 361
                localctx._var = self.var()
                self.state = 368
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==covid19Parser.COMA:
                    self.state = 362
                    self.match(covid19Parser.COMA)
                    self.state = 363
                    localctx._identificador_definicion = self.identificador_definicion()
                    addVarToVarsTable(None, (None if localctx._identificador_definicion is None else self._input.getText(localctx._identificador_definicion.start,localctx._identificador_definicion.stop)), (None if localctx._var is None else self._input.getText(localctx._var.start,localctx._var.stop)))
                    self.state = 370
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 371
                self.match(covid19Parser.PUNTOYCOMA)
                self.state = 375 
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
            self.state = 377
            localctx._tipo = self.tipo()
            self.state = 378
            self.match(covid19Parser.DOSPUNTOS)
            self.state = 379
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
            self.state = 382
            localctx._PRINCIPAL = self.match(covid19Parser.PRINCIPAL)
            setScope((None if localctx._PRINCIPAL is None else localctx._PRINCIPAL.text))
            self.state = 384
            self.match(covid19Parser.PARENTESISI)
            self.state = 385
            self.match(covid19Parser.PARENTESISD)
            self.state = 386
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
            self.state = 388
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
            self.state = 390
            self.match(covid19Parser.FUNCION)
            self.state = 392
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << covid19Parser.INT) | (1 << covid19Parser.FLOAT) | (1 << covid19Parser.STRING) | (1 << covid19Parser.CHAR) | (1 << covid19Parser.DATAFRAME))) != 0):
                self.state = 391
                localctx._tipo = self.tipo()


            self.state = 394
            localctx._ID = self.match(covid19Parser.ID)
            addFunctionToDirectory((None if localctx._ID is None else localctx._ID.text), (None if localctx._tipo is None else self._input.getText(localctx._tipo.start,localctx._tipo.stop)))
            setScope((None if localctx._ID is None else localctx._ID.text))
            self.state = 397
            self.match(covid19Parser.PARENTESISI)
            self.state = 409
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << covid19Parser.INT) | (1 << covid19Parser.FLOAT) | (1 << covid19Parser.STRING) | (1 << covid19Parser.CHAR) | (1 << covid19Parser.DATAFRAME))) != 0):
                self.state = 398
                localctx._var = self.var()
                addVarToFunctionParams((None if localctx._var is None else self._input.getText(localctx._var.start,localctx._var.stop)), (None if localctx._ID is None else localctx._ID.text))
                self.state = 406
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==covid19Parser.COMA:
                    self.state = 400
                    self.match(covid19Parser.COMA)
                    self.state = 401
                    localctx._var = self.var()
                    addVarToFunctionParams((None if localctx._var is None else self._input.getText(localctx._var.start,localctx._var.stop)), (None if localctx._ID is None else localctx._ID.text))
                    self.state = 408
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 411
            self.match(covid19Parser.PARENTESISD)
            self.state = 412
            self.match(covid19Parser.PUNTOYCOMA)
            self.state = 414
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==covid19Parser.VAR:
                self.state = 413
                self.varx()


            includeVarsTableInFunction((None if localctx._ID is None else localctx._ID.text))
            rememberBeginingOfFunction((None if localctx._ID is None else localctx._ID.text))
            self.state = 418
            self.match(covid19Parser.CORCHETEI)
            self.state = 422
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 419
                    self.estatuto() 
                self.state = 424
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

            self.state = 426
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==covid19Parser.REGRESA:
                self.state = 425
                self.regresa()


            self.state = 428
            self.match(covid19Parser.CORCHETED)
            reachedFunctionDefinitionEnd((None if localctx._ID is None else localctx._ID.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





