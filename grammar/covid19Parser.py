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
        buf.write("\u018e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\6\4I\n\4\r\4")
        buf.write("\16\4J\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\5\5Y\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\5\6c\n\6\3\6")
        buf.write("\3\6\3\6\5\6h\n\6\3\6\3\6\3\6\5\6m\n\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\5\7y\n\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\7\b\u0084\n\b\f\b\16\b\u0087\13\b\3\b")
        buf.write("\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u0096")
        buf.write("\n\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00a2")
        buf.write("\n\t\7\t\u00a4\n\t\f\t\16\t\u00a7\13\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\5\n\u00b1\n\n\3\n\3\n\3\n\7\n\u00b6\n")
        buf.write("\n\f\n\16\n\u00b9\13\n\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00c9\n\13")
        buf.write("\3\13\3\13\3\13\5\13\u00ce\n\13\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\5\f\u00d6\n\f\3\f\3\f\3\f\7\f\u00db\n\f\f\f\16\f\u00de")
        buf.write("\13\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00e6\n\r\3\r\3\r\3")
        buf.write("\r\7\r\u00eb\n\r\f\r\16\r\u00ee\13\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16")
        buf.write("\u00fd\n\16\3\17\3\17\5\17\u0101\n\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\5\17\u0114\n\17\3\20\3\20\3\20\3\20\3")
        buf.write("\20\7\20\u011b\n\20\f\20\16\20\u011e\13\20\3\20\3\20\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\5\23\u0132\n\23\3\23\3\23\3")
        buf.write("\23\3\23\5\23\u0138\n\23\3\23\3\23\5\23\u013c\n\23\5\23")
        buf.write("\u013e\n\23\3\24\3\24\3\24\3\24\5\24\u0144\n\24\3\24\3")
        buf.write("\24\3\24\7\24\u0149\n\24\f\24\16\24\u014c\13\24\3\24\3")
        buf.write("\24\3\25\3\25\3\25\3\25\7\25\u0154\n\25\f\25\16\25\u0157")
        buf.write("\13\25\3\25\3\25\6\25\u015b\n\25\r\25\16\25\u015c\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\5\31\u016e\n\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\7\31\u0177\n\31\f\31\16\31\u017a\13\31\5")
        buf.write("\31\u017c\n\31\3\31\3\31\3\31\3\31\3\31\3\31\7\31\u0184")
        buf.write("\n\31\f\31\16\31\u0187\13\31\3\31\5\31\u018a\n\31\3\31")
        buf.write("\3\31\3\31\2\2\32\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write("\36 \"$&(*,.\60\2\3\3\2\3\7\2\u01aa\2\62\3\2\2\2\4;\3")
        buf.write("\2\2\2\6F\3\2\2\2\bN\3\2\2\2\n\\\3\2\2\2\fx\3\2\2\2\16")
        buf.write("z\3\2\2\2\20\u008a\3\2\2\2\22\u00aa\3\2\2\2\24\u00ba\3")
        buf.write("\2\2\2\26\u00cf\3\2\2\2\30\u00df\3\2\2\2\32\u00fc\3\2")
        buf.write("\2\2\34\u0113\3\2\2\2\36\u0115\3\2\2\2 \u0121\3\2\2\2")
        buf.write("\"\u0126\3\2\2\2$\u012d\3\2\2\2&\u013f\3\2\2\2(\u014f")
        buf.write("\3\2\2\2*\u015e\3\2\2\2,\u0163\3\2\2\2.\u0169\3\2\2\2")
        buf.write("\60\u016b\3\2\2\2\62\63\7\23\2\2\63\64\5$\23\2\64\65\7")
        buf.write("\35\2\2\65\66\5\26\f\2\66\67\7\24\2\2\678\5\26\f\289\7")
        buf.write("\25\2\29:\5\6\4\2:\3\3\2\2\2;<\7\26\2\2<=\b\3\1\2=>\7")
        buf.write("\36\2\2>?\5\22\n\2?@\b\3\1\2@A\7\37\2\2AB\7\27\2\2BC\5")
        buf.write("\6\4\2CD\b\3\1\2DE\b\3\1\2E\5\3\2\2\2FH\7\33\2\2GI\5\34")
        buf.write("\17\2HG\3\2\2\2IJ\3\2\2\2JH\3\2\2\2JK\3\2\2\2KL\3\2\2")
        buf.write("\2LM\7\34\2\2M\7\3\2\2\2NO\7\13\2\2OP\7\36\2\2PQ\5\22")
        buf.write("\n\2QR\b\5\1\2RS\7\37\2\2ST\7\f\2\2TU\5\6\4\2UX\b\5\1")
        buf.write("\2VW\7\r\2\2WY\5\6\4\2XV\3\2\2\2XY\3\2\2\2YZ\3\2\2\2Z")
        buf.write("[\b\5\1\2[\t\3\2\2\2\\]\7\n\2\2]^\7\36\2\2^_\7\63\2\2")
        buf.write("_b\7\31\2\2`c\5$\23\2ac\5\f\7\2b`\3\2\2\2ba\3\2\2\2cd")
        buf.write("\3\2\2\2dg\7\31\2\2eh\5$\23\2fh\5\f\7\2ge\3\2\2\2gf\3")
        buf.write("\2\2\2hi\3\2\2\2il\7\31\2\2jm\5$\23\2km\5\f\7\2lj\3\2")
        buf.write("\2\2lk\3\2\2\2mn\3\2\2\2no\7\37\2\2o\13\3\2\2\2pq\7\61")
        buf.write("\2\2qy\b\7\1\2rs\7/\2\2sy\b\7\1\2tu\7\60\2\2uy\b\7\1\2")
        buf.write("vw\7\62\2\2wy\b\7\1\2xp\3\2\2\2xr\3\2\2\2xt\3\2\2\2xv")
        buf.write("\3\2\2\2y\r\3\2\2\2z{\7\17\2\2{|\7\36\2\2|}\5$\23\2}~")
        buf.write("\b\b\1\2~\u0085\3\2\2\2\177\u0080\7\31\2\2\u0080\u0081")
        buf.write("\5$\23\2\u0081\u0082\b\b\1\2\u0082\u0084\3\2\2\2\u0083")
        buf.write("\177\3\2\2\2\u0084\u0087\3\2\2\2\u0085\u0083\3\2\2\2\u0085")
        buf.write("\u0086\3\2\2\2\u0086\u0088\3\2\2\2\u0087\u0085\3\2\2\2")
        buf.write("\u0088\u0089\7\37\2\2\u0089\17\3\2\2\2\u008a\u008b\7\16")
        buf.write("\2\2\u008b\u0095\7\36\2\2\u008c\u008d\5$\23\2\u008d\u008e")
        buf.write("\b\t\1\2\u008e\u0096\3\2\2\2\u008f\u0090\5\f\7\2\u0090")
        buf.write("\u0091\b\t\1\2\u0091\u0096\3\2\2\2\u0092\u0093\5\26\f")
        buf.write("\2\u0093\u0094\b\t\1\2\u0094\u0096\3\2\2\2\u0095\u008c")
        buf.write("\3\2\2\2\u0095\u008f\3\2\2\2\u0095\u0092\3\2\2\2\u0096")
        buf.write("\u00a5\3\2\2\2\u0097\u00a1\7\31\2\2\u0098\u0099\5$\23")
        buf.write("\2\u0099\u009a\b\t\1\2\u009a\u00a2\3\2\2\2\u009b\u009c")
        buf.write("\5\f\7\2\u009c\u009d\b\t\1\2\u009d\u00a2\3\2\2\2\u009e")
        buf.write("\u009f\5\26\f\2\u009f\u00a0\b\t\1\2\u00a0\u00a2\3\2\2")
        buf.write("\2\u00a1\u0098\3\2\2\2\u00a1\u009b\3\2\2\2\u00a1\u009e")
        buf.write("\3\2\2\2\u00a2\u00a4\3\2\2\2\u00a3\u0097\3\2\2\2\u00a4")
        buf.write("\u00a7\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2")
        buf.write("\u00a6\u00a8\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a8\u00a9\7")
        buf.write("\37\2\2\u00a9\21\3\2\2\2\u00aa\u00ab\5\24\13\2\u00ab\u00b7")
        buf.write("\b\n\1\2\u00ac\u00ad\7-\2\2\u00ad\u00b1\b\n\1\2\u00ae")
        buf.write("\u00af\7.\2\2\u00af\u00b1\b\n\1\2\u00b0\u00ac\3\2\2\2")
        buf.write("\u00b0\u00ae\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\5")
        buf.write("\24\13\2\u00b3\u00b4\b\n\1\2\u00b4\u00b6\3\2\2\2\u00b5")
        buf.write("\u00b0\3\2\2\2\u00b6\u00b9\3\2\2\2\u00b7\u00b5\3\2\2\2")
        buf.write("\u00b7\u00b8\3\2\2\2\u00b8\23\3\2\2\2\u00b9\u00b7\3\2")
        buf.write("\2\2\u00ba\u00bb\5\26\f\2\u00bb\u00cd\b\13\1\2\u00bc\u00bd")
        buf.write("\7\"\2\2\u00bd\u00c9\b\13\1\2\u00be\u00bf\7#\2\2\u00bf")
        buf.write("\u00c9\b\13\1\2\u00c0\u00c1\7$\2\2\u00c1\u00c9\b\13\1")
        buf.write("\2\u00c2\u00c3\7%\2\2\u00c3\u00c9\b\13\1\2\u00c4\u00c5")
        buf.write("\7&\2\2\u00c5\u00c9\b\13\1\2\u00c6\u00c7\7\'\2\2\u00c7")
        buf.write("\u00c9\b\13\1\2\u00c8\u00bc\3\2\2\2\u00c8\u00be\3\2\2")
        buf.write("\2\u00c8\u00c0\3\2\2\2\u00c8\u00c2\3\2\2\2\u00c8\u00c4")
        buf.write("\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca")
        buf.write("\u00cb\5\26\f\2\u00cb\u00cc\b\13\1\2\u00cc\u00ce\3\2\2")
        buf.write("\2\u00cd\u00c8\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\25\3")
        buf.write("\2\2\2\u00cf\u00d0\5\30\r\2\u00d0\u00dc\b\f\1\2\u00d1")
        buf.write("\u00d2\7)\2\2\u00d2\u00d6\b\f\1\2\u00d3\u00d4\7*\2\2\u00d4")
        buf.write("\u00d6\b\f\1\2\u00d5\u00d1\3\2\2\2\u00d5\u00d3\3\2\2\2")
        buf.write("\u00d6\u00d7\3\2\2\2\u00d7\u00d8\5\30\r\2\u00d8\u00d9")
        buf.write("\b\f\1\2\u00d9\u00db\3\2\2\2\u00da\u00d5\3\2\2\2\u00db")
        buf.write("\u00de\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2")
        buf.write("\u00dd\27\3\2\2\2\u00de\u00dc\3\2\2\2\u00df\u00e0\5\32")
        buf.write("\16\2\u00e0\u00ec\b\r\1\2\u00e1\u00e2\7+\2\2\u00e2\u00e6")
        buf.write("\b\r\1\2\u00e3\u00e4\7,\2\2\u00e4\u00e6\b\r\1\2\u00e5")
        buf.write("\u00e1\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e6\u00e7\3\2\2\2")
        buf.write("\u00e7\u00e8\5\32\16\2\u00e8\u00e9\b\r\1\2\u00e9\u00eb")
        buf.write("\3\2\2\2\u00ea\u00e5\3\2\2\2\u00eb\u00ee\3\2\2\2\u00ec")
        buf.write("\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\31\3\2\2\2\u00ee")
        buf.write("\u00ec\3\2\2\2\u00ef\u00f0\5$\23\2\u00f0\u00f1\b\16\1")
        buf.write("\2\u00f1\u00fd\3\2\2\2\u00f2\u00f3\5\f\7\2\u00f3\u00f4")
        buf.write("\b\16\1\2\u00f4\u00fd\3\2\2\2\u00f5\u00fd\5\36\20\2\u00f6")
        buf.write("\u00f7\7\36\2\2\u00f7\u00f8\b\16\1\2\u00f8\u00f9\5\22")
        buf.write("\n\2\u00f9\u00fa\7\37\2\2\u00fa\u00fb\b\16\1\2\u00fb\u00fd")
        buf.write("\3\2\2\2\u00fc\u00ef\3\2\2\2\u00fc\u00f2\3\2\2\2\u00fc")
        buf.write("\u00f5\3\2\2\2\u00fc\u00f6\3\2\2\2\u00fd\33\3\2\2\2\u00fe")
        buf.write("\u0100\5\36\20\2\u00ff\u0101\7\30\2\2\u0100\u00ff\3\2")
        buf.write("\2\2\u0100\u0101\3\2\2\2\u0101\u0114\3\2\2\2\u0102\u0103")
        buf.write("\5\"\22\2\u0103\u0104\7\30\2\2\u0104\u0114\3\2\2\2\u0105")
        buf.write("\u0106\5\16\b\2\u0106\u0107\7\30\2\2\u0107\u0114\3\2\2")
        buf.write("\2\u0108\u0109\5\20\t\2\u0109\u010a\7\30\2\2\u010a\u0114")
        buf.write("\3\2\2\2\u010b\u010c\5\n\6\2\u010c\u010d\7\30\2\2\u010d")
        buf.write("\u0114\3\2\2\2\u010e\u0114\5\b\5\2\u010f\u0114\5\4\3\2")
        buf.write("\u0110\u0114\5\2\2\2\u0111\u0114\5\60\31\2\u0112\u0114")
        buf.write("\5 \21\2\u0113\u00fe\3\2\2\2\u0113\u0102\3\2\2\2\u0113")
        buf.write("\u0105\3\2\2\2\u0113\u0108\3\2\2\2\u0113\u010b\3\2\2\2")
        buf.write("\u0113\u010e\3\2\2\2\u0113\u010f\3\2\2\2\u0113\u0110\3")
        buf.write("\2\2\2\u0113\u0111\3\2\2\2\u0113\u0112\3\2\2\2\u0114\35")
        buf.write("\3\2\2\2\u0115\u0116\7\63\2\2\u0116\u0117\7\36\2\2\u0117")
        buf.write("\u011c\5\22\n\2\u0118\u0119\7\31\2\2\u0119\u011b\5\22")
        buf.write("\n\2\u011a\u0118\3\2\2\2\u011b\u011e\3\2\2\2\u011c\u011a")
        buf.write("\3\2\2\2\u011c\u011d\3\2\2\2\u011d\u011f\3\2\2\2\u011e")
        buf.write("\u011c\3\2\2\2\u011f\u0120\7\37\2\2\u0120\37\3\2\2\2\u0121")
        buf.write("\u0122\7\20\2\2\u0122\u0123\7\36\2\2\u0123\u0124\5\22")
        buf.write("\n\2\u0124\u0125\7\37\2\2\u0125!\3\2\2\2\u0126\u0127\5")
        buf.write("$\23\2\u0127\u0128\b\22\1\2\u0128\u0129\7\35\2\2\u0129")
        buf.write("\u012a\b\22\1\2\u012a\u012b\5\22\n\2\u012b\u012c\b\22")
        buf.write("\1\2\u012c#\3\2\2\2\u012d\u013d\7\63\2\2\u012e\u0131\7")
        buf.write(" \2\2\u012f\u0132\5$\23\2\u0130\u0132\5\f\7\2\u0131\u012f")
        buf.write("\3\2\2\2\u0131\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133")
        buf.write("\u013b\7!\2\2\u0134\u0137\7 \2\2\u0135\u0138\5$\23\2\u0136")
        buf.write("\u0138\5\f\7\2\u0137\u0135\3\2\2\2\u0137\u0136\3\2\2\2")
        buf.write("\u0138\u0139\3\2\2\2\u0139\u013a\7!\2\2\u013a\u013c\3")
        buf.write("\2\2\2\u013b\u0134\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u013e")
        buf.write("\3\2\2\2\u013d\u012e\3\2\2\2\u013d\u013e\3\2\2\2\u013e")
        buf.write("%\3\2\2\2\u013f\u0140\7\21\2\2\u0140\u0141\5$\23\2\u0141")
        buf.write("\u0143\7\30\2\2\u0142\u0144\5(\25\2\u0143\u0142\3\2\2")
        buf.write("\2\u0143\u0144\3\2\2\2\u0144\u0145\3\2\2\2\u0145\u0146")
        buf.write("\b\24\1\2\u0146\u014a\b\24\1\2\u0147\u0149\5\60\31\2\u0148")
        buf.write("\u0147\3\2\2\2\u0149\u014c\3\2\2\2\u014a\u0148\3\2\2\2")
        buf.write("\u014a\u014b\3\2\2\2\u014b\u014d\3\2\2\2\u014c\u014a\3")
        buf.write("\2\2\2\u014d\u014e\5,\27\2\u014e\'\3\2\2\2\u014f\u015a")
        buf.write("\7\b\2\2\u0150\u0155\5*\26\2\u0151\u0152\7\31\2\2\u0152")
        buf.write("\u0154\5$\23\2\u0153\u0151\3\2\2\2\u0154\u0157\3\2\2\2")
        buf.write("\u0155\u0153\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0158\3")
        buf.write("\2\2\2\u0157\u0155\3\2\2\2\u0158\u0159\7\30\2\2\u0159")
        buf.write("\u015b\3\2\2\2\u015a\u0150\3\2\2\2\u015b\u015c\3\2\2\2")
        buf.write("\u015c\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d)\3\2\2")
        buf.write("\2\u015e\u015f\5.\30\2\u015f\u0160\7\32\2\2\u0160\u0161")
        buf.write("\5$\23\2\u0161\u0162\b\26\1\2\u0162+\3\2\2\2\u0163\u0164")
        buf.write("\7\22\2\2\u0164\u0165\b\27\1\2\u0165\u0166\7\36\2\2\u0166")
        buf.write("\u0167\7\37\2\2\u0167\u0168\5\6\4\2\u0168-\3\2\2\2\u0169")
        buf.write("\u016a\t\2\2\2\u016a/\3\2\2\2\u016b\u016d\7\t\2\2\u016c")
        buf.write("\u016e\5.\30\2\u016d\u016c\3\2\2\2\u016d\u016e\3\2\2\2")
        buf.write("\u016e\u016f\3\2\2\2\u016f\u0170\7\63\2\2\u0170\u0171")
        buf.write("\b\31\1\2\u0171\u0172\b\31\1\2\u0172\u017b\7\36\2\2\u0173")
        buf.write("\u0178\5*\26\2\u0174\u0175\7\31\2\2\u0175\u0177\5*\26")
        buf.write("\2\u0176\u0174\3\2\2\2\u0177\u017a\3\2\2\2\u0178\u0176")
        buf.write("\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017c\3\2\2\2\u017a")
        buf.write("\u0178\3\2\2\2\u017b\u0173\3\2\2\2\u017b\u017c\3\2\2\2")
        buf.write("\u017c\u017d\3\2\2\2\u017d\u017e\7\37\2\2\u017e\u017f")
        buf.write("\7\30\2\2\u017f\u0180\5(\25\2\u0180\u0181\b\31\1\2\u0181")
        buf.write("\u0185\7\33\2\2\u0182\u0184\5\34\17\2\u0183\u0182\3\2")
        buf.write("\2\2\u0184\u0187\3\2\2\2\u0185\u0183\3\2\2\2\u0185\u0186")
        buf.write("\3\2\2\2\u0186\u0189\3\2\2\2\u0187\u0185\3\2\2\2\u0188")
        buf.write("\u018a\5 \21\2\u0189\u0188\3\2\2\2\u0189\u018a\3\2\2\2")
        buf.write("\u018a\u018b\3\2\2\2\u018b\u018c\7\34\2\2\u018c\61\3\2")
        buf.write("\2\2%JXbglx\u0085\u0095\u00a1\u00a5\u00b0\u00b7\u00c8")
        buf.write("\u00cd\u00d5\u00dc\u00e5\u00ec\u00fc\u0100\u0113\u011c")
        buf.write("\u0131\u0137\u013b\u013d\u0143\u014a\u0155\u015c\u016d")
        buf.write("\u0178\u017b\u0185\u0189")
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
    RULE_identificador = 17
    RULE_programa = 18
    RULE_varx = 19
    RULE_var = 20
    RULE_funcp = 21
    RULE_tipo = 22
    RULE_metodo = 23

    ruleNames =  [ "nocondicional", "condicional", "bloque", "decision", 
                   "cargadatos", "cte", "lectura", "escritura", "megaexpresion", 
                   "superexpresion", "expresion", "termino", "factor", "estatuto", 
                   "llamadametodo", "regresa", "asignacion", "identificador", 
                   "programa", "varx", "var", "funcp", "tipo", "metodo" ]

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

        def DESDE(self):
            return self.getToken(covid19Parser.DESDE, 0)

        def identificador(self):
            return self.getTypedRuleContext(covid19Parser.IdentificadorContext,0)


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
            self.state = 48
            self.match(covid19Parser.DESDE)
            self.state = 49
            self.identificador()
            self.state = 50
            self.match(covid19Parser.IGUAL)
            self.state = 51
            self.expresion()
            self.state = 52
            self.match(covid19Parser.HASTA)
            self.state = 53
            self.expresion()
            self.state = 54
            self.match(covid19Parser.HACER)
            self.state = 55
            self.bloque()
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
            self.state = 57
            self.match(covid19Parser.MIENTRAS)
            addMigajitaDePan()
            self.state = 59
            self.match(covid19Parser.PARENTESISI)
            self.state = 60
            self.megaexpresion()
            addGotoF()
            self.state = 62
            self.match(covid19Parser.PARENTESISD)
            self.state = 63
            self.match(covid19Parser.HAZ)
            self.state = 64
            self.bloque()
            addGotoA()
            addGotoEnd('mientras')
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
            self.state = 68
            self.match(covid19Parser.CORCHETEI)
            self.state = 70 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 69
                self.estatuto()
                self.state = 72 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << covid19Parser.FUNCION) | (1 << covid19Parser.CARGAARCHIVO) | (1 << covid19Parser.SI) | (1 << covid19Parser.ESCRIBE) | (1 << covid19Parser.LEE) | (1 << covid19Parser.REGRESA) | (1 << covid19Parser.DESDE) | (1 << covid19Parser.MIENTRAS) | (1 << covid19Parser.ID))) != 0)):
                    break

            self.state = 74
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
            self.state = 76
            self.match(covid19Parser.SI)
            self.state = 77
            self.match(covid19Parser.PARENTESISI)
            self.state = 78
            self.megaexpresion()
            addGotoF()
            self.state = 80
            self.match(covid19Parser.PARENTESISD)
            self.state = 81
            self.match(covid19Parser.ENTONCES)
            self.state = 82
            self.bloque()
            addGotoA()
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==covid19Parser.SINO:
                self.state = 84
                self.match(covid19Parser.SINO)
                self.state = 85
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

        def identificador(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.IdentificadorContext)
            else:
                return self.getTypedRuleContext(covid19Parser.IdentificadorContext,i)


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
            self.state = 90
            self.match(covid19Parser.CARGAARCHIVO)
            self.state = 91
            self.match(covid19Parser.PARENTESISI)
            self.state = 92
            self.match(covid19Parser.ID)
            self.state = 93
            self.match(covid19Parser.COMA)
            self.state = 96
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [covid19Parser.ID]:
                self.state = 94
                self.identificador()
                pass
            elif token in [covid19Parser.CTEINT, covid19Parser.CTEFLOAT, covid19Parser.CTESTRING, covid19Parser.CTECHAR]:
                self.state = 95
                self.cte()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 98
            self.match(covid19Parser.COMA)
            self.state = 101
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [covid19Parser.ID]:
                self.state = 99
                self.identificador()
                pass
            elif token in [covid19Parser.CTEINT, covid19Parser.CTEFLOAT, covid19Parser.CTESTRING, covid19Parser.CTECHAR]:
                self.state = 100
                self.cte()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 103
            self.match(covid19Parser.COMA)
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [covid19Parser.ID]:
                self.state = 104
                self.identificador()
                pass
            elif token in [covid19Parser.CTEINT, covid19Parser.CTEFLOAT, covid19Parser.CTESTRING, covid19Parser.CTECHAR]:
                self.state = 105
                self.cte()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 108
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
            self.state = 118
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [covid19Parser.CTESTRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.match(covid19Parser.CTESTRING)
                insertTypeToStack('string')
                pass
            elif token in [covid19Parser.CTEINT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 112
                self.match(covid19Parser.CTEINT)
                insertTypeToStack('int')
                pass
            elif token in [covid19Parser.CTEFLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 114
                self.match(covid19Parser.CTEFLOAT)
                insertTypeToStack('float')
                pass
            elif token in [covid19Parser.CTECHAR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 116
                self.match(covid19Parser.CTECHAR)
                insertTypeToStack('char')
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
            self._identificador = None # IdentificadorContext

        def LEE(self):
            return self.getToken(covid19Parser.LEE, 0)

        def PARENTESISI(self):
            return self.getToken(covid19Parser.PARENTESISI, 0)

        def PARENTESISD(self):
            return self.getToken(covid19Parser.PARENTESISD, 0)

        def identificador(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.IdentificadorContext)
            else:
                return self.getTypedRuleContext(covid19Parser.IdentificadorContext,i)


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
            self.state = 120
            self.match(covid19Parser.LEE)
            self.state = 121
            self.match(covid19Parser.PARENTESISI)

            self.state = 122
            localctx._identificador = self.identificador()
            readId((None if localctx._identificador is None else self._input.getText(localctx._identificador.start,localctx._identificador.stop)))
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.COMA:
                self.state = 125
                self.match(covid19Parser.COMA)
                self.state = 126
                localctx._identificador = self.identificador()
                readId((None if localctx._identificador is None else self._input.getText(localctx._identificador.start,localctx._identificador.stop)))
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 134
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
            self._identificador = None # IdentificadorContext
            self._cte = None # CteContext

        def ESCRIBE(self):
            return self.getToken(covid19Parser.ESCRIBE, 0)

        def PARENTESISI(self):
            return self.getToken(covid19Parser.PARENTESISI, 0)

        def PARENTESISD(self):
            return self.getToken(covid19Parser.PARENTESISD, 0)

        def identificador(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.IdentificadorContext)
            else:
                return self.getTypedRuleContext(covid19Parser.IdentificadorContext,i)


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
            self.state = 136
            self.match(covid19Parser.ESCRIBE)
            self.state = 137
            self.match(covid19Parser.PARENTESISI)
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 138
                localctx._identificador = self.identificador()
                write((None if localctx._identificador is None else self._input.getText(localctx._identificador.start,localctx._identificador.stop)))
                pass

            elif la_ == 2:
                self.state = 141
                localctx._cte = self.cte()
                write((None if localctx._cte is None else self._input.getText(localctx._cte.start,localctx._cte.stop)))
                pass

            elif la_ == 3:
                self.state = 144
                self.expresion()
                writeExpression()
                pass


            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.COMA:
                self.state = 149
                self.match(covid19Parser.COMA)
                self.state = 159
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 150
                    localctx._identificador = self.identificador()
                    write((None if localctx._identificador is None else self._input.getText(localctx._identificador.start,localctx._identificador.stop)))
                    pass

                elif la_ == 2:
                    self.state = 153
                    localctx._cte = self.cte()
                    write((None if localctx._cte is None else self._input.getText(localctx._cte.start,localctx._cte.stop)))
                    pass

                elif la_ == 3:
                    self.state = 156
                    self.expresion()
                    writeExpression()
                    pass


                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 166
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
            self.state = 168
            self.superexpresion()
            leaving('union')
            self.state = 181
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.Y or _la==covid19Parser.O:
                self.state = 174
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [covid19Parser.Y]:
                    self.state = 170
                    localctx._Y = self.match(covid19Parser.Y)
                    insertOperator((None if localctx._Y is None else localctx._Y.text))
                    pass
                elif token in [covid19Parser.O]:
                    self.state = 172
                    localctx._O = self.match(covid19Parser.O)
                    insertOperator((None if localctx._O is None else localctx._O.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 176
                self.superexpresion()
                leaving('union')
                self.state = 183
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
            self.state = 184
            self.expresion()
            leaving('comparacion')
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << covid19Parser.MAYOR) | (1 << covid19Parser.MENOR) | (1 << covid19Parser.MAYORIGUAL) | (1 << covid19Parser.MENORIGUAL) | (1 << covid19Parser.IGUALCOMP) | (1 << covid19Parser.DIFERENTE))) != 0):
                self.state = 198
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [covid19Parser.MAYOR]:
                    self.state = 186
                    localctx._MAYOR = self.match(covid19Parser.MAYOR)
                    insertOperator((None if localctx._MAYOR is None else localctx._MAYOR.text))
                    pass
                elif token in [covid19Parser.MENOR]:
                    self.state = 188
                    localctx._MENOR = self.match(covid19Parser.MENOR)
                    insertOperator((None if localctx._MENOR is None else localctx._MENOR.text))
                    pass
                elif token in [covid19Parser.MAYORIGUAL]:
                    self.state = 190
                    localctx._MAYORIGUAL = self.match(covid19Parser.MAYORIGUAL)
                    insertOperator((None if localctx._MAYORIGUAL is None else localctx._MAYORIGUAL.text))
                    pass
                elif token in [covid19Parser.MENORIGUAL]:
                    self.state = 192
                    localctx._MENORIGUAL = self.match(covid19Parser.MENORIGUAL)
                    insertOperator((None if localctx._MENORIGUAL is None else localctx._MENORIGUAL.text))
                    pass
                elif token in [covid19Parser.IGUALCOMP]:
                    self.state = 194
                    localctx._IGUALCOMP = self.match(covid19Parser.IGUALCOMP)
                    insertOperator((None if localctx._IGUALCOMP is None else localctx._IGUALCOMP.text))
                    pass
                elif token in [covid19Parser.DIFERENTE]:
                    self.state = 196
                    localctx._DIFERENTE = self.match(covid19Parser.DIFERENTE)
                    insertOperator((None if localctx._DIFERENTE is None else localctx._DIFERENTE.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 200
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
            self.state = 205
            self.termino()
            leaving('termino')
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.SUMA or _la==covid19Parser.RESTA:
                self.state = 211
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [covid19Parser.SUMA]:
                    self.state = 207
                    localctx._SUMA = self.match(covid19Parser.SUMA)
                    insertOperator((None if localctx._SUMA is None else localctx._SUMA.text))
                    pass
                elif token in [covid19Parser.RESTA]:
                    self.state = 209
                    localctx._RESTA = self.match(covid19Parser.RESTA)
                    insertOperator((None if localctx._RESTA is None else localctx._RESTA.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 213
                self.termino()
                leaving('termino')
                self.state = 220
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
            self.state = 221
            self.factor()
            leaving('factor')
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.MULTIPLICACION or _la==covid19Parser.DIVISION:
                self.state = 227
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [covid19Parser.MULTIPLICACION]:
                    self.state = 223
                    localctx._MULTIPLICACION = self.match(covid19Parser.MULTIPLICACION)
                    insertOperator((None if localctx._MULTIPLICACION is None else localctx._MULTIPLICACION.text))
                    pass
                elif token in [covid19Parser.DIVISION]:
                    self.state = 225
                    localctx._DIVISION = self.match(covid19Parser.DIVISION)
                    insertOperator((None if localctx._DIVISION is None else localctx._DIVISION.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 229
                self.factor()
                leaving('factor')
                self.state = 236
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
            self._identificador = None # IdentificadorContext
            self._cte = None # CteContext

        def identificador(self):
            return self.getTypedRuleContext(covid19Parser.IdentificadorContext,0)


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
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                localctx._identificador = self.identificador()
                insertIdToStack((None if localctx._identificador is None else self._input.getText(localctx._identificador.start,localctx._identificador.stop)))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                localctx._cte = self.cte()
                insertCteToStack((None if localctx._cte is None else self._input.getText(localctx._cte.start,localctx._cte.stop)))
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 243
                self.llamadametodo()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 244
                self.match(covid19Parser.PARENTESISI)
                insertParenthesis()
                self.state = 246
                self.megaexpresion()
                self.state = 247
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


        def asignacion(self):
            return self.getTypedRuleContext(covid19Parser.AsignacionContext,0)


        def PUNTOYCOMA(self):
            return self.getToken(covid19Parser.PUNTOYCOMA, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 252
                self.llamadametodo()
                self.state = 254
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==covid19Parser.PUNTOYCOMA:
                    self.state = 253
                    self.match(covid19Parser.PUNTOYCOMA)


                pass

            elif la_ == 2:
                self.state = 256
                self.asignacion()
                self.state = 257
                self.match(covid19Parser.PUNTOYCOMA)
                pass

            elif la_ == 3:
                self.state = 259
                self.lectura()
                self.state = 260
                self.match(covid19Parser.PUNTOYCOMA)
                pass

            elif la_ == 4:
                self.state = 262
                self.escritura()
                self.state = 263
                self.match(covid19Parser.PUNTOYCOMA)
                pass

            elif la_ == 5:
                self.state = 265
                self.cargadatos()
                self.state = 266
                self.match(covid19Parser.PUNTOYCOMA)
                pass

            elif la_ == 6:
                self.state = 268
                self.decision()
                pass

            elif la_ == 7:
                self.state = 269
                self.condicional()
                pass

            elif la_ == 8:
                self.state = 270
                self.nocondicional()
                pass

            elif la_ == 9:
                self.state = 271
                self.metodo()
                pass

            elif la_ == 10:
                self.state = 272
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

        def ID(self):
            return self.getToken(covid19Parser.ID, 0)

        def PARENTESISI(self):
            return self.getToken(covid19Parser.PARENTESISI, 0)

        def megaexpresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.MegaexpresionContext)
            else:
                return self.getTypedRuleContext(covid19Parser.MegaexpresionContext,i)


        def PARENTESISD(self):
            return self.getToken(covid19Parser.PARENTESISD, 0)

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
            self.state = 275
            self.match(covid19Parser.ID)
            self.state = 276
            self.match(covid19Parser.PARENTESISI)
            self.state = 277
            self.megaexpresion()
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.COMA:
                self.state = 278
                self.match(covid19Parser.COMA)
                self.state = 279
                self.megaexpresion()
                self.state = 284
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 285
            self.match(covid19Parser.PARENTESISD)
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

        def REGRESA(self):
            return self.getToken(covid19Parser.REGRESA, 0)

        def PARENTESISI(self):
            return self.getToken(covid19Parser.PARENTESISI, 0)

        def megaexpresion(self):
            return self.getTypedRuleContext(covid19Parser.MegaexpresionContext,0)


        def PARENTESISD(self):
            return self.getToken(covid19Parser.PARENTESISD, 0)

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
            self.state = 287
            self.match(covid19Parser.REGRESA)
            self.state = 288
            self.match(covid19Parser.PARENTESISI)
            self.state = 289
            self.megaexpresion()
            self.state = 290
            self.match(covid19Parser.PARENTESISD)
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
            self._identificador = None # IdentificadorContext
            self._IGUAL = None # Token

        def identificador(self):
            return self.getTypedRuleContext(covid19Parser.IdentificadorContext,0)


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
            self.state = 292
            localctx._identificador = self.identificador()
            insertIdToStack((None if localctx._identificador is None else self._input.getText(localctx._identificador.start,localctx._identificador.stop)))
            self.state = 294
            localctx._IGUAL = self.match(covid19Parser.IGUAL)
            insertOperator((None if localctx._IGUAL is None else localctx._IGUAL.text))
            self.state = 296
            self.megaexpresion()
            leaving('asignacion')
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentificadorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(covid19Parser.ID, 0)

        def CORCHETECUADRADOI(self, i:int=None):
            if i is None:
                return self.getTokens(covid19Parser.CORCHETECUADRADOI)
            else:
                return self.getToken(covid19Parser.CORCHETECUADRADOI, i)

        def CORCHETECUADRADOD(self, i:int=None):
            if i is None:
                return self.getTokens(covid19Parser.CORCHETECUADRADOD)
            else:
                return self.getToken(covid19Parser.CORCHETECUADRADOD, i)

        def identificador(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.IdentificadorContext)
            else:
                return self.getTypedRuleContext(covid19Parser.IdentificadorContext,i)


        def cte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.CteContext)
            else:
                return self.getTypedRuleContext(covid19Parser.CteContext,i)


        def getRuleIndex(self):
            return covid19Parser.RULE_identificador

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentificador" ):
                listener.enterIdentificador(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentificador" ):
                listener.exitIdentificador(self)




    def identificador(self):

        localctx = covid19Parser.IdentificadorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_identificador)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(covid19Parser.ID)
            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==covid19Parser.CORCHETECUADRADOI:
                self.state = 300
                self.match(covid19Parser.CORCHETECUADRADOI)
                self.state = 303
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [covid19Parser.ID]:
                    self.state = 301
                    self.identificador()
                    pass
                elif token in [covid19Parser.CTEINT, covid19Parser.CTEFLOAT, covid19Parser.CTESTRING, covid19Parser.CTECHAR]:
                    self.state = 302
                    self.cte()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 305
                self.match(covid19Parser.CORCHETECUADRADOD)
                self.state = 313
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==covid19Parser.CORCHETECUADRADOI:
                    self.state = 306
                    self.match(covid19Parser.CORCHETECUADRADOI)
                    self.state = 309
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [covid19Parser.ID]:
                        self.state = 307
                        self.identificador()
                        pass
                    elif token in [covid19Parser.CTEINT, covid19Parser.CTEFLOAT, covid19Parser.CTESTRING, covid19Parser.CTECHAR]:
                        self.state = 308
                        self.cte()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 311
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

        def identificador(self):
            return self.getTypedRuleContext(covid19Parser.IdentificadorContext,0)


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
        self.enterRule(localctx, 36, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(covid19Parser.PROGRAMA)
            self.state = 318
            self.identificador()
            self.state = 319
            self.match(covid19Parser.PUNTOYCOMA)
            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==covid19Parser.VAR:
                self.state = 320
                self.varx()


            addFunctionToDirectory('principal', '')
            includeVarsTableInFunction('principal')
            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.FUNCION:
                self.state = 325
                self.metodo()
                self.state = 330
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 331
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

        def identificador(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.IdentificadorContext)
            else:
                return self.getTypedRuleContext(covid19Parser.IdentificadorContext,i)


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
        self.enterRule(localctx, 38, self.RULE_varx)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(covid19Parser.VAR)
            self.state = 344 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 334
                self.var()
                self.state = 339
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==covid19Parser.COMA:
                    self.state = 335
                    self.match(covid19Parser.COMA)
                    self.state = 336
                    self.identificador()
                    self.state = 341
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 342
                self.match(covid19Parser.PUNTOYCOMA)
                self.state = 346 
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
            self._identificador = None # IdentificadorContext

        def tipo(self):
            return self.getTypedRuleContext(covid19Parser.TipoContext,0)


        def DOSPUNTOS(self):
            return self.getToken(covid19Parser.DOSPUNTOS, 0)

        def identificador(self):
            return self.getTypedRuleContext(covid19Parser.IdentificadorContext,0)


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
        self.enterRule(localctx, 40, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            localctx._tipo = self.tipo()
            self.state = 349
            self.match(covid19Parser.DOSPUNTOS)
            self.state = 350
            localctx._identificador = self.identificador()
            addVarToVarsTable((None if localctx._tipo is None else self._input.getText(localctx._tipo.start,localctx._tipo.stop)), (None if localctx._identificador is None else self._input.getText(localctx._identificador.start,localctx._identificador.stop)))
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
        self.enterRule(localctx, 42, self.RULE_funcp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            localctx._PRINCIPAL = self.match(covid19Parser.PRINCIPAL)
            setScope((None if localctx._PRINCIPAL is None else localctx._PRINCIPAL.text))
            self.state = 355
            self.match(covid19Parser.PARENTESISI)
            self.state = 356
            self.match(covid19Parser.PARENTESISD)
            self.state = 357
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
        self.enterRule(localctx, 44, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
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

        def varx(self):
            return self.getTypedRuleContext(covid19Parser.VarxContext,0)


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
        self.enterRule(localctx, 46, self.RULE_metodo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(covid19Parser.FUNCION)
            self.state = 363
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << covid19Parser.INT) | (1 << covid19Parser.FLOAT) | (1 << covid19Parser.STRING) | (1 << covid19Parser.CHAR) | (1 << covid19Parser.DATAFRAME))) != 0):
                self.state = 362
                localctx._tipo = self.tipo()


            self.state = 365
            localctx._ID = self.match(covid19Parser.ID)
            addFunctionToDirectory((None if localctx._ID is None else localctx._ID.text), (None if localctx._tipo is None else self._input.getText(localctx._tipo.start,localctx._tipo.stop)))
            setScope((None if localctx._ID is None else localctx._ID.text))
            self.state = 368
            self.match(covid19Parser.PARENTESISI)
            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << covid19Parser.INT) | (1 << covid19Parser.FLOAT) | (1 << covid19Parser.STRING) | (1 << covid19Parser.CHAR) | (1 << covid19Parser.DATAFRAME))) != 0):
                self.state = 369
                self.var()
                self.state = 374
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==covid19Parser.COMA:
                    self.state = 370
                    self.match(covid19Parser.COMA)
                    self.state = 371
                    self.var()
                    self.state = 376
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 379
            self.match(covid19Parser.PARENTESISD)
            self.state = 380
            self.match(covid19Parser.PUNTOYCOMA)
            self.state = 381
            self.varx()
            includeVarsTableInFunction((None if localctx._ID is None else localctx._ID.text))
            self.state = 383
            self.match(covid19Parser.CORCHETEI)
            self.state = 387
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 384
                    self.estatuto() 
                self.state = 389
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

            self.state = 391
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==covid19Parser.REGRESA:
                self.state = 390
                self.regresa()


            self.state = 393
            self.match(covid19Parser.CORCHETED)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





