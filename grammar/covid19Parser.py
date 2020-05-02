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
        buf.write("\u0180\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\6\4E\n\4\r\4\16\4F\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5S\n\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\5\6[\n\6\3\6\3\6\3\6\5\6`\n\6\3\6\3\6\3\6\5")
        buf.write("\6e\n\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7q\n")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\b|\n\b\f\b\16")
        buf.write("\b\177\13\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\5\t\u008e\n\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\5\t\u009a\n\t\7\t\u009c\n\t\f\t\16\t\u009f")
        buf.write("\13\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00a9\n\n\3")
        buf.write("\n\3\n\3\n\7\n\u00ae\n\n\f\n\16\n\u00b1\13\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\5\13\u00c1\n\13\3\13\3\13\3\13\5\13\u00c6\n\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\5\f\u00ce\n\f\3\f\3\f\3\f\7\f\u00d3")
        buf.write("\n\f\f\f\16\f\u00d6\13\f\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00de")
        buf.write("\n\r\3\r\3\r\3\r\7\r\u00e3\n\r\f\r\16\r\u00e6\13\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\5\16\u00f5\n\16\3\17\3\17\5\17\u00f9\n\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\5\17\u010c\n\17\3\20\3\20\3")
        buf.write("\20\3\20\3\20\7\20\u0113\n\20\f\20\16\20\u0116\13\20\3")
        buf.write("\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u012a\n\23\3")
        buf.write("\23\3\23\3\23\3\23\5\23\u0130\n\23\3\23\3\23\5\23\u0134")
        buf.write("\n\23\5\23\u0136\n\23\3\24\3\24\3\24\3\24\5\24\u013c\n")
        buf.write("\24\3\24\7\24\u013f\n\24\f\24\16\24\u0142\13\24\3\24\3")
        buf.write("\24\3\25\3\25\3\25\3\25\7\25\u014a\n\25\f\25\16\25\u014d")
        buf.write("\13\25\3\25\3\25\6\25\u0151\n\25\r\25\16\25\u0152\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\5\31\u0162\n\31\3\31\3\31\3\31\3\31\3\31\3\31\7")
        buf.write("\31\u016a\n\31\f\31\16\31\u016d\13\31\5\31\u016f\n\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\7\31\u0176\n\31\f\31\16\31\u0179")
        buf.write("\13\31\3\31\5\31\u017c\n\31\3\31\3\31\3\31\2\2\32\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\2\3\3")
        buf.write("\2\3\7\2\u019c\2\62\3\2\2\2\4;\3\2\2\2\6B\3\2\2\2\bJ\3")
        buf.write("\2\2\2\nT\3\2\2\2\fp\3\2\2\2\16r\3\2\2\2\20\u0082\3\2")
        buf.write("\2\2\22\u00a2\3\2\2\2\24\u00b2\3\2\2\2\26\u00c7\3\2\2")
        buf.write("\2\30\u00d7\3\2\2\2\32\u00f4\3\2\2\2\34\u010b\3\2\2\2")
        buf.write("\36\u010d\3\2\2\2 \u0119\3\2\2\2\"\u011e\3\2\2\2$\u0125")
        buf.write("\3\2\2\2&\u0137\3\2\2\2(\u0145\3\2\2\2*\u0154\3\2\2\2")
        buf.write(",\u0158\3\2\2\2.\u015d\3\2\2\2\60\u015f\3\2\2\2\62\63")
        buf.write("\7\23\2\2\63\64\5$\23\2\64\65\7\35\2\2\65\66\5\26\f\2")
        buf.write("\66\67\7\24\2\2\678\5\26\f\289\7\25\2\29:\5\6\4\2:\3\3")
        buf.write("\2\2\2;<\7\26\2\2<=\7\36\2\2=>\5\22\n\2>?\7\37\2\2?@\7")
        buf.write("\27\2\2@A\5\6\4\2A\5\3\2\2\2BD\7\33\2\2CE\5\34\17\2DC")
        buf.write("\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2\2\2GH\3\2\2\2HI\7\34")
        buf.write("\2\2I\7\3\2\2\2JK\7\13\2\2KL\7\36\2\2LM\5\22\n\2MN\7\37")
        buf.write("\2\2NO\7\f\2\2OR\5\6\4\2PQ\7\r\2\2QS\5\6\4\2RP\3\2\2\2")
        buf.write("RS\3\2\2\2S\t\3\2\2\2TU\7\n\2\2UV\7\36\2\2VW\7\63\2\2")
        buf.write("WZ\7\31\2\2X[\5$\23\2Y[\5\f\7\2ZX\3\2\2\2ZY\3\2\2\2[\\")
        buf.write("\3\2\2\2\\_\7\31\2\2]`\5$\23\2^`\5\f\7\2_]\3\2\2\2_^\3")
        buf.write("\2\2\2`a\3\2\2\2ad\7\31\2\2be\5$\23\2ce\5\f\7\2db\3\2")
        buf.write("\2\2dc\3\2\2\2ef\3\2\2\2fg\7\37\2\2g\13\3\2\2\2hi\7\61")
        buf.write("\2\2iq\b\7\1\2jk\7/\2\2kq\b\7\1\2lm\7\60\2\2mq\b\7\1\2")
        buf.write("no\7\62\2\2oq\b\7\1\2ph\3\2\2\2pj\3\2\2\2pl\3\2\2\2pn")
        buf.write("\3\2\2\2q\r\3\2\2\2rs\7\17\2\2st\7\36\2\2tu\5$\23\2uv")
        buf.write("\b\b\1\2v}\3\2\2\2wx\7\31\2\2xy\5$\23\2yz\b\b\1\2z|\3")
        buf.write("\2\2\2{w\3\2\2\2|\177\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\u0080")
        buf.write("\3\2\2\2\177}\3\2\2\2\u0080\u0081\7\37\2\2\u0081\17\3")
        buf.write("\2\2\2\u0082\u0083\7\16\2\2\u0083\u008d\7\36\2\2\u0084")
        buf.write("\u0085\5$\23\2\u0085\u0086\b\t\1\2\u0086\u008e\3\2\2\2")
        buf.write("\u0087\u0088\5\f\7\2\u0088\u0089\b\t\1\2\u0089\u008e\3")
        buf.write("\2\2\2\u008a\u008b\5\26\f\2\u008b\u008c\b\t\1\2\u008c")
        buf.write("\u008e\3\2\2\2\u008d\u0084\3\2\2\2\u008d\u0087\3\2\2\2")
        buf.write("\u008d\u008a\3\2\2\2\u008e\u009d\3\2\2\2\u008f\u0099\7")
        buf.write("\31\2\2\u0090\u0091\5$\23\2\u0091\u0092\b\t\1\2\u0092")
        buf.write("\u009a\3\2\2\2\u0093\u0094\5\f\7\2\u0094\u0095\b\t\1\2")
        buf.write("\u0095\u009a\3\2\2\2\u0096\u0097\5\26\f\2\u0097\u0098")
        buf.write("\b\t\1\2\u0098\u009a\3\2\2\2\u0099\u0090\3\2\2\2\u0099")
        buf.write("\u0093\3\2\2\2\u0099\u0096\3\2\2\2\u009a\u009c\3\2\2\2")
        buf.write("\u009b\u008f\3\2\2\2\u009c\u009f\3\2\2\2\u009d\u009b\3")
        buf.write("\2\2\2\u009d\u009e\3\2\2\2\u009e\u00a0\3\2\2\2\u009f\u009d")
        buf.write("\3\2\2\2\u00a0\u00a1\7\37\2\2\u00a1\21\3\2\2\2\u00a2\u00a3")
        buf.write("\5\24\13\2\u00a3\u00af\b\n\1\2\u00a4\u00a5\7-\2\2\u00a5")
        buf.write("\u00a9\b\n\1\2\u00a6\u00a7\7.\2\2\u00a7\u00a9\b\n\1\2")
        buf.write("\u00a8\u00a4\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a9\u00aa\3")
        buf.write("\2\2\2\u00aa\u00ab\5\24\13\2\u00ab\u00ac\b\n\1\2\u00ac")
        buf.write("\u00ae\3\2\2\2\u00ad\u00a8\3\2\2\2\u00ae\u00b1\3\2\2\2")
        buf.write("\u00af\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\23\3\2")
        buf.write("\2\2\u00b1\u00af\3\2\2\2\u00b2\u00b3\5\26\f\2\u00b3\u00c5")
        buf.write("\b\13\1\2\u00b4\u00b5\7\"\2\2\u00b5\u00c1\b\13\1\2\u00b6")
        buf.write("\u00b7\7#\2\2\u00b7\u00c1\b\13\1\2\u00b8\u00b9\7$\2\2")
        buf.write("\u00b9\u00c1\b\13\1\2\u00ba\u00bb\7%\2\2\u00bb\u00c1\b")
        buf.write("\13\1\2\u00bc\u00bd\7&\2\2\u00bd\u00c1\b\13\1\2\u00be")
        buf.write("\u00bf\7\'\2\2\u00bf\u00c1\b\13\1\2\u00c0\u00b4\3\2\2")
        buf.write("\2\u00c0\u00b6\3\2\2\2\u00c0\u00b8\3\2\2\2\u00c0\u00ba")
        buf.write("\3\2\2\2\u00c0\u00bc\3\2\2\2\u00c0\u00be\3\2\2\2\u00c1")
        buf.write("\u00c2\3\2\2\2\u00c2\u00c3\5\26\f\2\u00c3\u00c4\b\13\1")
        buf.write("\2\u00c4\u00c6\3\2\2\2\u00c5\u00c0\3\2\2\2\u00c5\u00c6")
        buf.write("\3\2\2\2\u00c6\25\3\2\2\2\u00c7\u00c8\5\30\r\2\u00c8\u00d4")
        buf.write("\b\f\1\2\u00c9\u00ca\7)\2\2\u00ca\u00ce\b\f\1\2\u00cb")
        buf.write("\u00cc\7*\2\2\u00cc\u00ce\b\f\1\2\u00cd\u00c9\3\2\2\2")
        buf.write("\u00cd\u00cb\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0\5")
        buf.write("\30\r\2\u00d0\u00d1\b\f\1\2\u00d1\u00d3\3\2\2\2\u00d2")
        buf.write("\u00cd\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2")
        buf.write("\u00d4\u00d5\3\2\2\2\u00d5\27\3\2\2\2\u00d6\u00d4\3\2")
        buf.write("\2\2\u00d7\u00d8\5\32\16\2\u00d8\u00e4\b\r\1\2\u00d9\u00da")
        buf.write("\7+\2\2\u00da\u00de\b\r\1\2\u00db\u00dc\7,\2\2\u00dc\u00de")
        buf.write("\b\r\1\2\u00dd\u00d9\3\2\2\2\u00dd\u00db\3\2\2\2\u00de")
        buf.write("\u00df\3\2\2\2\u00df\u00e0\5\32\16\2\u00e0\u00e1\b\r\1")
        buf.write("\2\u00e1\u00e3\3\2\2\2\u00e2\u00dd\3\2\2\2\u00e3\u00e6")
        buf.write("\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5")
        buf.write("\31\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e7\u00e8\5$\23\2\u00e8")
        buf.write("\u00e9\b\16\1\2\u00e9\u00f5\3\2\2\2\u00ea\u00eb\5\f\7")
        buf.write("\2\u00eb\u00ec\b\16\1\2\u00ec\u00f5\3\2\2\2\u00ed\u00f5")
        buf.write("\5\36\20\2\u00ee\u00ef\7\36\2\2\u00ef\u00f0\b\16\1\2\u00f0")
        buf.write("\u00f1\5\22\n\2\u00f1\u00f2\7\37\2\2\u00f2\u00f3\b\16")
        buf.write("\1\2\u00f3\u00f5\3\2\2\2\u00f4\u00e7\3\2\2\2\u00f4\u00ea")
        buf.write("\3\2\2\2\u00f4\u00ed\3\2\2\2\u00f4\u00ee\3\2\2\2\u00f5")
        buf.write("\33\3\2\2\2\u00f6\u00f8\5\36\20\2\u00f7\u00f9\7\30\2\2")
        buf.write("\u00f8\u00f7\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u010c\3")
        buf.write("\2\2\2\u00fa\u00fb\5\"\22\2\u00fb\u00fc\7\30\2\2\u00fc")
        buf.write("\u010c\3\2\2\2\u00fd\u00fe\5\16\b\2\u00fe\u00ff\7\30\2")
        buf.write("\2\u00ff\u010c\3\2\2\2\u0100\u0101\5\20\t\2\u0101\u0102")
        buf.write("\7\30\2\2\u0102\u010c\3\2\2\2\u0103\u0104\5\n\6\2\u0104")
        buf.write("\u0105\7\30\2\2\u0105\u010c\3\2\2\2\u0106\u010c\5\b\5")
        buf.write("\2\u0107\u010c\5\4\3\2\u0108\u010c\5\2\2\2\u0109\u010c")
        buf.write("\5\60\31\2\u010a\u010c\5 \21\2\u010b\u00f6\3\2\2\2\u010b")
        buf.write("\u00fa\3\2\2\2\u010b\u00fd\3\2\2\2\u010b\u0100\3\2\2\2")
        buf.write("\u010b\u0103\3\2\2\2\u010b\u0106\3\2\2\2\u010b\u0107\3")
        buf.write("\2\2\2\u010b\u0108\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010a")
        buf.write("\3\2\2\2\u010c\35\3\2\2\2\u010d\u010e\7\63\2\2\u010e\u010f")
        buf.write("\7\36\2\2\u010f\u0114\5\22\n\2\u0110\u0111\7\31\2\2\u0111")
        buf.write("\u0113\5\22\n\2\u0112\u0110\3\2\2\2\u0113\u0116\3\2\2")
        buf.write("\2\u0114\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0117")
        buf.write("\3\2\2\2\u0116\u0114\3\2\2\2\u0117\u0118\7\37\2\2\u0118")
        buf.write("\37\3\2\2\2\u0119\u011a\7\20\2\2\u011a\u011b\7\36\2\2")
        buf.write("\u011b\u011c\5\22\n\2\u011c\u011d\7\37\2\2\u011d!\3\2")
        buf.write("\2\2\u011e\u011f\5$\23\2\u011f\u0120\b\22\1\2\u0120\u0121")
        buf.write("\7\35\2\2\u0121\u0122\b\22\1\2\u0122\u0123\5\22\n\2\u0123")
        buf.write("\u0124\b\22\1\2\u0124#\3\2\2\2\u0125\u0135\7\63\2\2\u0126")
        buf.write("\u0129\7 \2\2\u0127\u012a\5$\23\2\u0128\u012a\5\f\7\2")
        buf.write("\u0129\u0127\3\2\2\2\u0129\u0128\3\2\2\2\u012a\u012b\3")
        buf.write("\2\2\2\u012b\u0133\7!\2\2\u012c\u012f\7 \2\2\u012d\u0130")
        buf.write("\5$\23\2\u012e\u0130\5\f\7\2\u012f\u012d\3\2\2\2\u012f")
        buf.write("\u012e\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0132\7!\2\2")
        buf.write("\u0132\u0134\3\2\2\2\u0133\u012c\3\2\2\2\u0133\u0134\3")
        buf.write("\2\2\2\u0134\u0136\3\2\2\2\u0135\u0126\3\2\2\2\u0135\u0136")
        buf.write("\3\2\2\2\u0136%\3\2\2\2\u0137\u0138\7\21\2\2\u0138\u0139")
        buf.write("\5$\23\2\u0139\u013b\7\30\2\2\u013a\u013c\5(\25\2\u013b")
        buf.write("\u013a\3\2\2\2\u013b\u013c\3\2\2\2\u013c\u0140\3\2\2\2")
        buf.write("\u013d\u013f\5\60\31\2\u013e\u013d\3\2\2\2\u013f\u0142")
        buf.write("\3\2\2\2\u0140\u013e\3\2\2\2\u0140\u0141\3\2\2\2\u0141")
        buf.write("\u0143\3\2\2\2\u0142\u0140\3\2\2\2\u0143\u0144\5,\27\2")
        buf.write("\u0144\'\3\2\2\2\u0145\u0150\7\b\2\2\u0146\u014b\5*\26")
        buf.write("\2\u0147\u0148\7\31\2\2\u0148\u014a\5$\23\2\u0149\u0147")
        buf.write("\3\2\2\2\u014a\u014d\3\2\2\2\u014b\u0149\3\2\2\2\u014b")
        buf.write("\u014c\3\2\2\2\u014c\u014e\3\2\2\2\u014d\u014b\3\2\2\2")
        buf.write("\u014e\u014f\7\30\2\2\u014f\u0151\3\2\2\2\u0150\u0146")
        buf.write("\3\2\2\2\u0151\u0152\3\2\2\2\u0152\u0150\3\2\2\2\u0152")
        buf.write("\u0153\3\2\2\2\u0153)\3\2\2\2\u0154\u0155\5.\30\2\u0155")
        buf.write("\u0156\7\32\2\2\u0156\u0157\5$\23\2\u0157+\3\2\2\2\u0158")
        buf.write("\u0159\7\22\2\2\u0159\u015a\7\36\2\2\u015a\u015b\7\37")
        buf.write("\2\2\u015b\u015c\5\6\4\2\u015c-\3\2\2\2\u015d\u015e\t")
        buf.write("\2\2\2\u015e/\3\2\2\2\u015f\u0161\7\t\2\2\u0160\u0162")
        buf.write("\5.\30\2\u0161\u0160\3\2\2\2\u0161\u0162\3\2\2\2\u0162")
        buf.write("\u0163\3\2\2\2\u0163\u0164\7\63\2\2\u0164\u016e\7\36\2")
        buf.write("\2\u0165\u0166\5*\26\2\u0166\u016b\b\31\1\2\u0167\u0168")
        buf.write("\7\31\2\2\u0168\u016a\5*\26\2\u0169\u0167\3\2\2\2\u016a")
        buf.write("\u016d\3\2\2\2\u016b\u0169\3\2\2\2\u016b\u016c\3\2\2\2")
        buf.write("\u016c\u016f\3\2\2\2\u016d\u016b\3\2\2\2\u016e\u0165\3")
        buf.write("\2\2\2\u016e\u016f\3\2\2\2\u016f\u0170\3\2\2\2\u0170\u0171")
        buf.write("\7\37\2\2\u0171\u0172\7\30\2\2\u0172\u0173\5(\25\2\u0173")
        buf.write("\u0177\7\33\2\2\u0174\u0176\5\34\17\2\u0175\u0174\3\2")
        buf.write("\2\2\u0176\u0179\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0178")
        buf.write("\3\2\2\2\u0178\u017b\3\2\2\2\u0179\u0177\3\2\2\2\u017a")
        buf.write("\u017c\5 \21\2\u017b\u017a\3\2\2\2\u017b\u017c\3\2\2\2")
        buf.write("\u017c\u017d\3\2\2\2\u017d\u017e\7\34\2\2\u017e\61\3\2")
        buf.write("\2\2%FRZ_dp}\u008d\u0099\u009d\u00a8\u00af\u00c0\u00c5")
        buf.write("\u00cd\u00d4\u00dd\u00e4\u00f4\u00f8\u010b\u0114\u0129")
        buf.write("\u012f\u0133\u0135\u013b\u0140\u014b\u0152\u0161\u016b")
        buf.write("\u016e\u0177\u017b")
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
            self.state = 58
            self.match(covid19Parser.PARENTESISI)
            self.state = 59
            self.megaexpresion()
            self.state = 60
            self.match(covid19Parser.PARENTESISD)
            self.state = 61
            self.match(covid19Parser.HAZ)
            self.state = 62
            self.bloque()
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
            self.state = 64
            self.match(covid19Parser.CORCHETEI)
            self.state = 66 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 65
                self.estatuto()
                self.state = 68 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << covid19Parser.FUNCION) | (1 << covid19Parser.CARGAARCHIVO) | (1 << covid19Parser.SI) | (1 << covid19Parser.ESCRIBE) | (1 << covid19Parser.LEE) | (1 << covid19Parser.REGRESA) | (1 << covid19Parser.DESDE) | (1 << covid19Parser.MIENTRAS) | (1 << covid19Parser.ID))) != 0)):
                    break

            self.state = 70
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
            self.state = 72
            self.match(covid19Parser.SI)
            self.state = 73
            self.match(covid19Parser.PARENTESISI)
            self.state = 74
            self.megaexpresion()
            self.state = 75
            self.match(covid19Parser.PARENTESISD)
            self.state = 76
            self.match(covid19Parser.ENTONCES)
            self.state = 77
            self.bloque()
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==covid19Parser.SINO:
                self.state = 78
                self.match(covid19Parser.SINO)
                self.state = 79
                self.bloque()


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
            self.state = 82
            self.match(covid19Parser.CARGAARCHIVO)
            self.state = 83
            self.match(covid19Parser.PARENTESISI)
            self.state = 84
            self.match(covid19Parser.ID)
            self.state = 85
            self.match(covid19Parser.COMA)
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [covid19Parser.ID]:
                self.state = 86
                self.identificador()
                pass
            elif token in [covid19Parser.CTEINT, covid19Parser.CTEFLOAT, covid19Parser.CTESTRING, covid19Parser.CTECHAR]:
                self.state = 87
                self.cte()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 90
            self.match(covid19Parser.COMA)
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [covid19Parser.ID]:
                self.state = 91
                self.identificador()
                pass
            elif token in [covid19Parser.CTEINT, covid19Parser.CTEFLOAT, covid19Parser.CTESTRING, covid19Parser.CTECHAR]:
                self.state = 92
                self.cte()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 95
            self.match(covid19Parser.COMA)
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [covid19Parser.ID]:
                self.state = 96
                self.identificador()
                pass
            elif token in [covid19Parser.CTEINT, covid19Parser.CTEFLOAT, covid19Parser.CTESTRING, covid19Parser.CTECHAR]:
                self.state = 97
                self.cte()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 100
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
            self.state = 110
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [covid19Parser.CTESTRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.match(covid19Parser.CTESTRING)
                insertTypeToStack('string')
                pass
            elif token in [covid19Parser.CTEINT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.match(covid19Parser.CTEINT)
                insertTypeToStack('int')
                pass
            elif token in [covid19Parser.CTEFLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 106
                self.match(covid19Parser.CTEFLOAT)
                insertTypeToStack('float')
                pass
            elif token in [covid19Parser.CTECHAR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 108
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
            self.state = 112
            self.match(covid19Parser.LEE)
            self.state = 113
            self.match(covid19Parser.PARENTESISI)

            self.state = 114
            localctx._identificador = self.identificador()
            readId((None if localctx._identificador is None else self._input.getText(localctx._identificador.start,localctx._identificador.stop)))
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.COMA:
                self.state = 117
                self.match(covid19Parser.COMA)
                self.state = 118
                localctx._identificador = self.identificador()
                readId((None if localctx._identificador is None else self._input.getText(localctx._identificador.start,localctx._identificador.stop)))
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 126
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
            self.state = 128
            self.match(covid19Parser.ESCRIBE)
            self.state = 129
            self.match(covid19Parser.PARENTESISI)
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 130
                localctx._identificador = self.identificador()
                write((None if localctx._identificador is None else self._input.getText(localctx._identificador.start,localctx._identificador.stop)))
                pass

            elif la_ == 2:
                self.state = 133
                localctx._cte = self.cte()
                write((None if localctx._cte is None else self._input.getText(localctx._cte.start,localctx._cte.stop)))
                pass

            elif la_ == 3:
                self.state = 136
                self.expresion()
                writeExpression()
                pass


            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.COMA:
                self.state = 141
                self.match(covid19Parser.COMA)
                self.state = 151
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 142
                    localctx._identificador = self.identificador()
                    write((None if localctx._identificador is None else self._input.getText(localctx._identificador.start,localctx._identificador.stop)))
                    pass

                elif la_ == 2:
                    self.state = 145
                    localctx._cte = self.cte()
                    write((None if localctx._cte is None else self._input.getText(localctx._cte.start,localctx._cte.stop)))
                    pass

                elif la_ == 3:
                    self.state = 148
                    self.expresion()
                    writeExpression()
                    pass


                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 158
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
            self.state = 160
            self.superexpresion()
            leaving('union')
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.Y or _la==covid19Parser.O:
                self.state = 166
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [covid19Parser.Y]:
                    self.state = 162
                    localctx._Y = self.match(covid19Parser.Y)
                    insertOperator((None if localctx._Y is None else localctx._Y.text))
                    pass
                elif token in [covid19Parser.O]:
                    self.state = 164
                    localctx._O = self.match(covid19Parser.O)
                    insertOperator((None if localctx._O is None else localctx._O.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 168
                self.superexpresion()
                leaving('union')
                self.state = 175
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
            self.state = 176
            self.expresion()
            leaving('comparacion')
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << covid19Parser.MAYOR) | (1 << covid19Parser.MENOR) | (1 << covid19Parser.MAYORIGUAL) | (1 << covid19Parser.MENORIGUAL) | (1 << covid19Parser.IGUALCOMP) | (1 << covid19Parser.DIFERENTE))) != 0):
                self.state = 190
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [covid19Parser.MAYOR]:
                    self.state = 178
                    localctx._MAYOR = self.match(covid19Parser.MAYOR)
                    insertOperator((None if localctx._MAYOR is None else localctx._MAYOR.text))
                    pass
                elif token in [covid19Parser.MENOR]:
                    self.state = 180
                    localctx._MENOR = self.match(covid19Parser.MENOR)
                    insertOperator((None if localctx._MENOR is None else localctx._MENOR.text))
                    pass
                elif token in [covid19Parser.MAYORIGUAL]:
                    self.state = 182
                    localctx._MAYORIGUAL = self.match(covid19Parser.MAYORIGUAL)
                    insertOperator((None if localctx._MAYORIGUAL is None else localctx._MAYORIGUAL.text))
                    pass
                elif token in [covid19Parser.MENORIGUAL]:
                    self.state = 184
                    localctx._MENORIGUAL = self.match(covid19Parser.MENORIGUAL)
                    insertOperator((None if localctx._MENORIGUAL is None else localctx._MENORIGUAL.text))
                    pass
                elif token in [covid19Parser.IGUALCOMP]:
                    self.state = 186
                    localctx._IGUALCOMP = self.match(covid19Parser.IGUALCOMP)
                    insertOperator((None if localctx._IGUALCOMP is None else localctx._IGUALCOMP.text))
                    pass
                elif token in [covid19Parser.DIFERENTE]:
                    self.state = 188
                    localctx._DIFERENTE = self.match(covid19Parser.DIFERENTE)
                    insertOperator((None if localctx._DIFERENTE is None else localctx._DIFERENTE.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 192
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
            self.state = 197
            self.termino()
            leaving('termino')
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.SUMA or _la==covid19Parser.RESTA:
                self.state = 203
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [covid19Parser.SUMA]:
                    self.state = 199
                    localctx._SUMA = self.match(covid19Parser.SUMA)
                    insertOperator((None if localctx._SUMA is None else localctx._SUMA.text))
                    pass
                elif token in [covid19Parser.RESTA]:
                    self.state = 201
                    localctx._RESTA = self.match(covid19Parser.RESTA)
                    insertOperator((None if localctx._RESTA is None else localctx._RESTA.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 205
                self.termino()
                leaving('termino')
                self.state = 212
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
            self.state = 213
            self.factor()
            leaving('factor')
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.MULTIPLICACION or _la==covid19Parser.DIVISION:
                self.state = 219
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [covid19Parser.MULTIPLICACION]:
                    self.state = 215
                    localctx._MULTIPLICACION = self.match(covid19Parser.MULTIPLICACION)
                    insertOperator((None if localctx._MULTIPLICACION is None else localctx._MULTIPLICACION.text))
                    pass
                elif token in [covid19Parser.DIVISION]:
                    self.state = 217
                    localctx._DIVISION = self.match(covid19Parser.DIVISION)
                    insertOperator((None if localctx._DIVISION is None else localctx._DIVISION.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 221
                self.factor()
                leaving('factor')
                self.state = 228
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
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                localctx._identificador = self.identificador()
                insertIdToStack((None if localctx._identificador is None else self._input.getText(localctx._identificador.start,localctx._identificador.stop)))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                localctx._cte = self.cte()
                insertCteToStack((None if localctx._cte is None else self._input.getText(localctx._cte.start,localctx._cte.stop)))
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 235
                self.llamadametodo()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 236
                self.match(covid19Parser.PARENTESISI)
                insertParenthesis()
                self.state = 238
                self.megaexpresion()
                self.state = 239
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
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 244
                self.llamadametodo()
                self.state = 246
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==covid19Parser.PUNTOYCOMA:
                    self.state = 245
                    self.match(covid19Parser.PUNTOYCOMA)


                pass

            elif la_ == 2:
                self.state = 248
                self.asignacion()
                self.state = 249
                self.match(covid19Parser.PUNTOYCOMA)
                pass

            elif la_ == 3:
                self.state = 251
                self.lectura()
                self.state = 252
                self.match(covid19Parser.PUNTOYCOMA)
                pass

            elif la_ == 4:
                self.state = 254
                self.escritura()
                self.state = 255
                self.match(covid19Parser.PUNTOYCOMA)
                pass

            elif la_ == 5:
                self.state = 257
                self.cargadatos()
                self.state = 258
                self.match(covid19Parser.PUNTOYCOMA)
                pass

            elif la_ == 6:
                self.state = 260
                self.decision()
                pass

            elif la_ == 7:
                self.state = 261
                self.condicional()
                pass

            elif la_ == 8:
                self.state = 262
                self.nocondicional()
                pass

            elif la_ == 9:
                self.state = 263
                self.metodo()
                pass

            elif la_ == 10:
                self.state = 264
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
            self.state = 267
            self.match(covid19Parser.ID)
            self.state = 268
            self.match(covid19Parser.PARENTESISI)
            self.state = 269
            self.megaexpresion()
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.COMA:
                self.state = 270
                self.match(covid19Parser.COMA)
                self.state = 271
                self.megaexpresion()
                self.state = 276
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 277
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
            self.state = 279
            self.match(covid19Parser.REGRESA)
            self.state = 280
            self.match(covid19Parser.PARENTESISI)
            self.state = 281
            self.megaexpresion()
            self.state = 282
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
            self.state = 284
            localctx._identificador = self.identificador()
            insertIdToStack((None if localctx._identificador is None else self._input.getText(localctx._identificador.start,localctx._identificador.stop)))
            self.state = 286
            localctx._IGUAL = self.match(covid19Parser.IGUAL)
            insertOperator((None if localctx._IGUAL is None else localctx._IGUAL.text))
            self.state = 288
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
            self.state = 291
            self.match(covid19Parser.ID)
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==covid19Parser.CORCHETECUADRADOI:
                self.state = 292
                self.match(covid19Parser.CORCHETECUADRADOI)
                self.state = 295
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [covid19Parser.ID]:
                    self.state = 293
                    self.identificador()
                    pass
                elif token in [covid19Parser.CTEINT, covid19Parser.CTEFLOAT, covid19Parser.CTESTRING, covid19Parser.CTECHAR]:
                    self.state = 294
                    self.cte()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 297
                self.match(covid19Parser.CORCHETECUADRADOD)
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==covid19Parser.CORCHETECUADRADOI:
                    self.state = 298
                    self.match(covid19Parser.CORCHETECUADRADOI)
                    self.state = 301
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [covid19Parser.ID]:
                        self.state = 299
                        self.identificador()
                        pass
                    elif token in [covid19Parser.CTEINT, covid19Parser.CTEFLOAT, covid19Parser.CTESTRING, covid19Parser.CTECHAR]:
                        self.state = 300
                        self.cte()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 303
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
            self.state = 309
            self.match(covid19Parser.PROGRAMA)
            self.state = 310
            self.identificador()
            self.state = 311
            self.match(covid19Parser.PUNTOYCOMA)
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==covid19Parser.VAR:
                self.state = 312
                self.varx()


            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.FUNCION:
                self.state = 315
                self.metodo()
                self.state = 320
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 321
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
            self.state = 323
            self.match(covid19Parser.VAR)
            self.state = 334 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 324
                self.var()
                self.state = 329
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==covid19Parser.COMA:
                    self.state = 325
                    self.match(covid19Parser.COMA)
                    self.state = 326
                    self.identificador()
                    self.state = 331
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 332
                self.match(covid19Parser.PUNTOYCOMA)
                self.state = 336 
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
            self.state = 338
            self.tipo()
            self.state = 339
            self.match(covid19Parser.DOSPUNTOS)
            self.state = 340
            self.identificador()
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
            self.state = 342
            self.match(covid19Parser.PRINCIPAL)
            self.state = 343
            self.match(covid19Parser.PARENTESISI)
            self.state = 344
            self.match(covid19Parser.PARENTESISD)
            self.state = 345
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
            self.state = 347
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
            self.variable = None # VarContext

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


        def estatuto(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.EstatutoContext)
            else:
                return self.getTypedRuleContext(covid19Parser.EstatutoContext,i)


        def regresa(self):
            return self.getTypedRuleContext(covid19Parser.RegresaContext,0)


        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(covid19Parser.VarContext)
            else:
                return self.getTypedRuleContext(covid19Parser.VarContext,i)


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
            self.state = 349
            self.match(covid19Parser.FUNCION)
            self.state = 351
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << covid19Parser.INT) | (1 << covid19Parser.FLOAT) | (1 << covid19Parser.STRING) | (1 << covid19Parser.CHAR) | (1 << covid19Parser.DATAFRAME))) != 0):
                self.state = 350
                self.tipo()


            self.state = 353
            self.match(covid19Parser.ID)
            self.state = 354
            self.match(covid19Parser.PARENTESISI)
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << covid19Parser.INT) | (1 << covid19Parser.FLOAT) | (1 << covid19Parser.STRING) | (1 << covid19Parser.CHAR) | (1 << covid19Parser.DATAFRAME))) != 0):
                self.state = 355
                localctx.variable = self.var()
                receiveVar((None if localctx.variable is None else self._input.getText(localctx.variable.start,localctx.variable.stop)))
                self.state = 361
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==covid19Parser.COMA:
                    self.state = 357
                    self.match(covid19Parser.COMA)
                    self.state = 358
                    self.var()
                    self.state = 363
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 366
            self.match(covid19Parser.PARENTESISD)
            self.state = 367
            self.match(covid19Parser.PUNTOYCOMA)
            self.state = 368
            self.varx()
            self.state = 369
            self.match(covid19Parser.CORCHETEI)
            self.state = 373
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 370
                    self.estatuto() 
                self.state = 375
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==covid19Parser.REGRESA:
                self.state = 376
                self.regresa()


            self.state = 379
            self.match(covid19Parser.CORCHETED)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





