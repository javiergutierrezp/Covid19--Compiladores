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
        buf.write("\u015f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\6\4E\n\4\r\4\16\4F\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5S\n\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\5\6[\n\6\3\6\3\6\3\6\5\6`\n\6\3\6\3\6\3\6\5")
        buf.write("\6e\n\6\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\7\bt\n\b\f\b\16\bw\13\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u0086\n\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u0092\n\t\7\t\u0094\n")
        buf.write("\t\f\t\16\t\u0097\13\t\3\t\3\t\3\n\3\n\3\n\7\n\u009e\n")
        buf.write("\n\f\n\16\n\u00a1\13\n\3\13\3\13\3\13\5\13\u00a6\n\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00ae\n\f\3\f\3\f\3\f\7\f")
        buf.write("\u00b3\n\f\f\f\16\f\u00b6\13\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\5\r\u00be\n\r\3\r\3\r\3\r\7\r\u00c3\n\r\f\r\16\r\u00c6")
        buf.write("\13\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\5\16\u00d5\n\16\3\17\3\17\5\17\u00d9\n")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00ec\n\17\3")
        buf.write("\20\3\20\3\20\3\20\3\20\7\20\u00f3\n\20\f\20\16\20\u00f6")
        buf.write("\13\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u010a")
        buf.write("\n\23\3\23\3\23\3\23\3\23\5\23\u0110\n\23\3\23\3\23\5")
        buf.write("\23\u0114\n\23\5\23\u0116\n\23\3\24\3\24\3\24\3\24\5\24")
        buf.write("\u011c\n\24\3\24\7\24\u011f\n\24\f\24\16\24\u0122\13\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\7\25\u012a\n\25\f\25\16")
        buf.write("\25\u012d\13\25\3\25\3\25\6\25\u0131\n\25\r\25\16\25\u0132")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\5\31\u0142\n\31\3\31\3\31\3\31\3\31\3\31\7")
        buf.write("\31\u0149\n\31\f\31\16\31\u014c\13\31\5\31\u014e\n\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\7\31\u0155\n\31\f\31\16\31\u0158")
        buf.write("\13\31\3\31\5\31\u015b\n\31\3\31\3\31\3\31\2\2\32\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\2\6\3")
        buf.write("\2/\62\3\2-.\3\2\"\'\3\2\3\7\2\u0172\2\62\3\2\2\2\4;\3")
        buf.write("\2\2\2\6B\3\2\2\2\bJ\3\2\2\2\nT\3\2\2\2\fh\3\2\2\2\16")
        buf.write("j\3\2\2\2\20z\3\2\2\2\22\u009a\3\2\2\2\24\u00a2\3\2\2")
        buf.write("\2\26\u00a7\3\2\2\2\30\u00b7\3\2\2\2\32\u00d4\3\2\2\2")
        buf.write("\34\u00eb\3\2\2\2\36\u00ed\3\2\2\2 \u00f9\3\2\2\2\"\u00fe")
        buf.write("\3\2\2\2$\u0105\3\2\2\2&\u0117\3\2\2\2(\u0125\3\2\2\2")
        buf.write("*\u0134\3\2\2\2,\u0138\3\2\2\2.\u013d\3\2\2\2\60\u013f")
        buf.write("\3\2\2\2\62\63\7\23\2\2\63\64\5$\23\2\64\65\7\35\2\2\65")
        buf.write("\66\5\26\f\2\66\67\7\24\2\2\678\5\26\f\289\7\25\2\29:")
        buf.write("\5\6\4\2:\3\3\2\2\2;<\7\26\2\2<=\7\36\2\2=>\5\22\n\2>")
        buf.write("?\7\37\2\2?@\7\27\2\2@A\5\6\4\2A\5\3\2\2\2BD\7\33\2\2")
        buf.write("CE\5\34\17\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2\2\2G")
        buf.write("H\3\2\2\2HI\7\34\2\2I\7\3\2\2\2JK\7\13\2\2KL\7\36\2\2")
        buf.write("LM\5\22\n\2MN\7\37\2\2NO\7\f\2\2OR\5\6\4\2PQ\7\r\2\2Q")
        buf.write("S\5\6\4\2RP\3\2\2\2RS\3\2\2\2S\t\3\2\2\2TU\7\n\2\2UV\7")
        buf.write("\36\2\2VW\7\63\2\2WZ\7\31\2\2X[\5$\23\2Y[\5\f\7\2ZX\3")
        buf.write("\2\2\2ZY\3\2\2\2[\\\3\2\2\2\\_\7\31\2\2]`\5$\23\2^`\5")
        buf.write("\f\7\2_]\3\2\2\2_^\3\2\2\2`a\3\2\2\2ad\7\31\2\2be\5$\23")
        buf.write("\2ce\5\f\7\2db\3\2\2\2dc\3\2\2\2ef\3\2\2\2fg\7\37\2\2")
        buf.write("g\13\3\2\2\2hi\t\2\2\2i\r\3\2\2\2jk\7\17\2\2kl\7\36\2")
        buf.write("\2lm\5$\23\2mn\b\b\1\2nu\3\2\2\2op\7\31\2\2pq\5$\23\2")
        buf.write("qr\b\b\1\2rt\3\2\2\2so\3\2\2\2tw\3\2\2\2us\3\2\2\2uv\3")
        buf.write("\2\2\2vx\3\2\2\2wu\3\2\2\2xy\7\37\2\2y\17\3\2\2\2z{\7")
        buf.write("\16\2\2{\u0085\7\36\2\2|}\5$\23\2}~\b\t\1\2~\u0086\3\2")
        buf.write("\2\2\177\u0080\5\f\7\2\u0080\u0081\b\t\1\2\u0081\u0086")
        buf.write("\3\2\2\2\u0082\u0083\5\26\f\2\u0083\u0084\b\t\1\2\u0084")
        buf.write("\u0086\3\2\2\2\u0085|\3\2\2\2\u0085\177\3\2\2\2\u0085")
        buf.write("\u0082\3\2\2\2\u0086\u0095\3\2\2\2\u0087\u0091\7\31\2")
        buf.write("\2\u0088\u0089\5$\23\2\u0089\u008a\b\t\1\2\u008a\u0092")
        buf.write("\3\2\2\2\u008b\u008c\5\f\7\2\u008c\u008d\b\t\1\2\u008d")
        buf.write("\u0092\3\2\2\2\u008e\u008f\5\26\f\2\u008f\u0090\b\t\1")
        buf.write("\2\u0090\u0092\3\2\2\2\u0091\u0088\3\2\2\2\u0091\u008b")
        buf.write("\3\2\2\2\u0091\u008e\3\2\2\2\u0092\u0094\3\2\2\2\u0093")
        buf.write("\u0087\3\2\2\2\u0094\u0097\3\2\2\2\u0095\u0093\3\2\2\2")
        buf.write("\u0095\u0096\3\2\2\2\u0096\u0098\3\2\2\2\u0097\u0095\3")
        buf.write("\2\2\2\u0098\u0099\7\37\2\2\u0099\21\3\2\2\2\u009a\u009f")
        buf.write("\5\24\13\2\u009b\u009c\t\3\2\2\u009c\u009e\5\24\13\2\u009d")
        buf.write("\u009b\3\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d\3\2\2\2")
        buf.write("\u009f\u00a0\3\2\2\2\u00a0\23\3\2\2\2\u00a1\u009f\3\2")
        buf.write("\2\2\u00a2\u00a5\5\26\f\2\u00a3\u00a4\t\4\2\2\u00a4\u00a6")
        buf.write("\5\26\f\2\u00a5\u00a3\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6")
        buf.write("\25\3\2\2\2\u00a7\u00a8\5\30\r\2\u00a8\u00b4\b\f\1\2\u00a9")
        buf.write("\u00aa\7)\2\2\u00aa\u00ae\b\f\1\2\u00ab\u00ac\7*\2\2\u00ac")
        buf.write("\u00ae\b\f\1\2\u00ad\u00a9\3\2\2\2\u00ad\u00ab\3\2\2\2")
        buf.write("\u00ae\u00af\3\2\2\2\u00af\u00b0\5\30\r\2\u00b0\u00b1")
        buf.write("\b\f\1\2\u00b1\u00b3\3\2\2\2\u00b2\u00ad\3\2\2\2\u00b3")
        buf.write("\u00b6\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2")
        buf.write("\u00b5\27\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b7\u00b8\5\32")
        buf.write("\16\2\u00b8\u00c4\b\r\1\2\u00b9\u00ba\7+\2\2\u00ba\u00be")
        buf.write("\b\r\1\2\u00bb\u00bc\7,\2\2\u00bc\u00be\b\r\1\2\u00bd")
        buf.write("\u00b9\3\2\2\2\u00bd\u00bb\3\2\2\2\u00be\u00bf\3\2\2\2")
        buf.write("\u00bf\u00c0\5\32\16\2\u00c0\u00c1\b\r\1\2\u00c1\u00c3")
        buf.write("\3\2\2\2\u00c2\u00bd\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4")
        buf.write("\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\31\3\2\2\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c7\u00c8\5$\23\2\u00c8\u00c9\b\16\1")
        buf.write("\2\u00c9\u00d5\3\2\2\2\u00ca\u00cb\5\f\7\2\u00cb\u00cc")
        buf.write("\b\16\1\2\u00cc\u00d5\3\2\2\2\u00cd\u00d5\5\36\20\2\u00ce")
        buf.write("\u00cf\7\36\2\2\u00cf\u00d0\b\16\1\2\u00d0\u00d1\5\22")
        buf.write("\n\2\u00d1\u00d2\7\37\2\2\u00d2\u00d3\b\16\1\2\u00d3\u00d5")
        buf.write("\3\2\2\2\u00d4\u00c7\3\2\2\2\u00d4\u00ca\3\2\2\2\u00d4")
        buf.write("\u00cd\3\2\2\2\u00d4\u00ce\3\2\2\2\u00d5\33\3\2\2\2\u00d6")
        buf.write("\u00d8\5\36\20\2\u00d7\u00d9\7\30\2\2\u00d8\u00d7\3\2")
        buf.write("\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00ec\3\2\2\2\u00da\u00db")
        buf.write("\5\"\22\2\u00db\u00dc\7\30\2\2\u00dc\u00ec\3\2\2\2\u00dd")
        buf.write("\u00de\5\16\b\2\u00de\u00df\7\30\2\2\u00df\u00ec\3\2\2")
        buf.write("\2\u00e0\u00e1\5\20\t\2\u00e1\u00e2\7\30\2\2\u00e2\u00ec")
        buf.write("\3\2\2\2\u00e3\u00e4\5\n\6\2\u00e4\u00e5\7\30\2\2\u00e5")
        buf.write("\u00ec\3\2\2\2\u00e6\u00ec\5\b\5\2\u00e7\u00ec\5\4\3\2")
        buf.write("\u00e8\u00ec\5\2\2\2\u00e9\u00ec\5\60\31\2\u00ea\u00ec")
        buf.write("\5 \21\2\u00eb\u00d6\3\2\2\2\u00eb\u00da\3\2\2\2\u00eb")
        buf.write("\u00dd\3\2\2\2\u00eb\u00e0\3\2\2\2\u00eb\u00e3\3\2\2\2")
        buf.write("\u00eb\u00e6\3\2\2\2\u00eb\u00e7\3\2\2\2\u00eb\u00e8\3")
        buf.write("\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ea\3\2\2\2\u00ec\35")
        buf.write("\3\2\2\2\u00ed\u00ee\7\63\2\2\u00ee\u00ef\7\36\2\2\u00ef")
        buf.write("\u00f4\5\22\n\2\u00f0\u00f1\7\31\2\2\u00f1\u00f3\5\22")
        buf.write("\n\2\u00f2\u00f0\3\2\2\2\u00f3\u00f6\3\2\2\2\u00f4\u00f2")
        buf.write("\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f7\3\2\2\2\u00f6")
        buf.write("\u00f4\3\2\2\2\u00f7\u00f8\7\37\2\2\u00f8\37\3\2\2\2\u00f9")
        buf.write("\u00fa\7\20\2\2\u00fa\u00fb\7\36\2\2\u00fb\u00fc\5\22")
        buf.write("\n\2\u00fc\u00fd\7\37\2\2\u00fd!\3\2\2\2\u00fe\u00ff\5")
        buf.write("$\23\2\u00ff\u0100\b\22\1\2\u0100\u0101\7\35\2\2\u0101")
        buf.write("\u0102\b\22\1\2\u0102\u0103\5\22\n\2\u0103\u0104\b\22")
        buf.write("\1\2\u0104#\3\2\2\2\u0105\u0115\7\63\2\2\u0106\u0109\7")
        buf.write(" \2\2\u0107\u010a\5$\23\2\u0108\u010a\5\f\7\2\u0109\u0107")
        buf.write("\3\2\2\2\u0109\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b")
        buf.write("\u0113\7!\2\2\u010c\u010f\7 \2\2\u010d\u0110\5$\23\2\u010e")
        buf.write("\u0110\5\f\7\2\u010f\u010d\3\2\2\2\u010f\u010e\3\2\2\2")
        buf.write("\u0110\u0111\3\2\2\2\u0111\u0112\7!\2\2\u0112\u0114\3")
        buf.write("\2\2\2\u0113\u010c\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0116")
        buf.write("\3\2\2\2\u0115\u0106\3\2\2\2\u0115\u0116\3\2\2\2\u0116")
        buf.write("%\3\2\2\2\u0117\u0118\7\21\2\2\u0118\u0119\5$\23\2\u0119")
        buf.write("\u011b\7\30\2\2\u011a\u011c\5(\25\2\u011b\u011a\3\2\2")
        buf.write("\2\u011b\u011c\3\2\2\2\u011c\u0120\3\2\2\2\u011d\u011f")
        buf.write("\5\60\31\2\u011e\u011d\3\2\2\2\u011f\u0122\3\2\2\2\u0120")
        buf.write("\u011e\3\2\2\2\u0120\u0121\3\2\2\2\u0121\u0123\3\2\2\2")
        buf.write("\u0122\u0120\3\2\2\2\u0123\u0124\5,\27\2\u0124\'\3\2\2")
        buf.write("\2\u0125\u0130\7\b\2\2\u0126\u012b\5*\26\2\u0127\u0128")
        buf.write("\7\31\2\2\u0128\u012a\5$\23\2\u0129\u0127\3\2\2\2\u012a")
        buf.write("\u012d\3\2\2\2\u012b\u0129\3\2\2\2\u012b\u012c\3\2\2\2")
        buf.write("\u012c\u012e\3\2\2\2\u012d\u012b\3\2\2\2\u012e\u012f\7")
        buf.write("\30\2\2\u012f\u0131\3\2\2\2\u0130\u0126\3\2\2\2\u0131")
        buf.write("\u0132\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2")
        buf.write("\u0133)\3\2\2\2\u0134\u0135\5.\30\2\u0135\u0136\7\32\2")
        buf.write("\2\u0136\u0137\5$\23\2\u0137+\3\2\2\2\u0138\u0139\7\22")
        buf.write("\2\2\u0139\u013a\7\36\2\2\u013a\u013b\7\37\2\2\u013b\u013c")
        buf.write("\5\6\4\2\u013c-\3\2\2\2\u013d\u013e\t\5\2\2\u013e/\3\2")
        buf.write("\2\2\u013f\u0141\7\t\2\2\u0140\u0142\5.\30\2\u0141\u0140")
        buf.write("\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0143\3\2\2\2\u0143")
        buf.write("\u0144\7\63\2\2\u0144\u014d\7\36\2\2\u0145\u014a\5*\26")
        buf.write("\2\u0146\u0147\7\31\2\2\u0147\u0149\5*\26\2\u0148\u0146")
        buf.write("\3\2\2\2\u0149\u014c\3\2\2\2\u014a\u0148\3\2\2\2\u014a")
        buf.write("\u014b\3\2\2\2\u014b\u014e\3\2\2\2\u014c\u014a\3\2\2\2")
        buf.write("\u014d\u0145\3\2\2\2\u014d\u014e\3\2\2\2\u014e\u014f\3")
        buf.write("\2\2\2\u014f\u0150\7\37\2\2\u0150\u0151\7\30\2\2\u0151")
        buf.write("\u0152\5(\25\2\u0152\u0156\7\33\2\2\u0153\u0155\5\34\17")
        buf.write("\2\u0154\u0153\3\2\2\2\u0155\u0158\3\2\2\2\u0156\u0154")
        buf.write("\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u015a\3\2\2\2\u0158")
        buf.write("\u0156\3\2\2\2\u0159\u015b\5 \21\2\u015a\u0159\3\2\2\2")
        buf.write("\u015a\u015b\3\2\2\2\u015b\u015c\3\2\2\2\u015c\u015d\7")
        buf.write("\34\2\2\u015d\61\3\2\2\2\"FRZ_du\u0085\u0091\u0095\u009f")
        buf.write("\u00a5\u00ad\u00b4\u00bd\u00c4\u00d4\u00d8\u00eb\u00f4")
        buf.write("\u0109\u010f\u0113\u0115\u011b\u0120\u012b\u0132\u0141")
        buf.write("\u014a\u014d\u0156\u015a")
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << covid19Parser.CTEINT) | (1 << covid19Parser.CTEFLOAT) | (1 << covid19Parser.CTESTRING) | (1 << covid19Parser.CTECHAR))) != 0)):
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
            self.state = 104
            self.match(covid19Parser.LEE)
            self.state = 105
            self.match(covid19Parser.PARENTESISI)

            self.state = 106
            localctx._identificador = self.identificador()
            readId((None if localctx._identificador is None else self._input.getText(localctx._identificador.start,localctx._identificador.stop)))
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.COMA:
                self.state = 109
                self.match(covid19Parser.COMA)
                self.state = 110
                localctx._identificador = self.identificador()
                readId((None if localctx._identificador is None else self._input.getText(localctx._identificador.start,localctx._identificador.stop)))
                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118
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
            self.state = 120
            self.match(covid19Parser.ESCRIBE)
            self.state = 121
            self.match(covid19Parser.PARENTESISI)
            self.state = 131
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 122
                localctx._identificador = self.identificador()
                write((None if localctx._identificador is None else self._input.getText(localctx._identificador.start,localctx._identificador.stop)))
                pass

            elif la_ == 2:
                self.state = 125
                localctx._cte = self.cte()
                write((None if localctx._cte is None else self._input.getText(localctx._cte.start,localctx._cte.stop)))
                pass

            elif la_ == 3:
                self.state = 128
                self.expresion()
                writeExpression()
                pass


            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.COMA:
                self.state = 133
                self.match(covid19Parser.COMA)
                self.state = 143
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 134
                    localctx._identificador = self.identificador()
                    write((None if localctx._identificador is None else self._input.getText(localctx._identificador.start,localctx._identificador.stop)))
                    pass

                elif la_ == 2:
                    self.state = 137
                    localctx._cte = self.cte()
                    write((None if localctx._cte is None else self._input.getText(localctx._cte.start,localctx._cte.stop)))
                    pass

                elif la_ == 3:
                    self.state = 140
                    self.expresion()
                    writeExpression()
                    pass


                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 150
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
            self.state = 152
            self.superexpresion()
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.Y or _la==covid19Parser.O:
                self.state = 153
                _la = self._input.LA(1)
                if not(_la==covid19Parser.Y or _la==covid19Parser.O):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 154
                self.superexpresion()
                self.state = 159
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
            self.state = 160
            self.expresion()
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << covid19Parser.MAYOR) | (1 << covid19Parser.MENOR) | (1 << covid19Parser.MAYORIGUAL) | (1 << covid19Parser.MENORIGUAL) | (1 << covid19Parser.IGUALCOMP) | (1 << covid19Parser.DIFERENTE))) != 0):
                self.state = 161
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << covid19Parser.MAYOR) | (1 << covid19Parser.MENOR) | (1 << covid19Parser.MAYORIGUAL) | (1 << covid19Parser.MENORIGUAL) | (1 << covid19Parser.IGUALCOMP) | (1 << covid19Parser.DIFERENTE))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 162
                self.expresion()


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
            self.state = 165
            self.termino()
            leaving('termino')
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.SUMA or _la==covid19Parser.RESTA:
                self.state = 171
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [covid19Parser.SUMA]:
                    self.state = 167
                    localctx._SUMA = self.match(covid19Parser.SUMA)
                    insertOperator((None if localctx._SUMA is None else localctx._SUMA.text))
                    pass
                elif token in [covid19Parser.RESTA]:
                    self.state = 169
                    localctx._RESTA = self.match(covid19Parser.RESTA)
                    insertOperator((None if localctx._RESTA is None else localctx._RESTA.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 173
                self.termino()
                leaving('termino')
                self.state = 180
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
            self.state = 181
            self.factor()
            leaving('factor')
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.MULTIPLICACION or _la==covid19Parser.DIVISION:
                self.state = 187
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [covid19Parser.MULTIPLICACION]:
                    self.state = 183
                    localctx._MULTIPLICACION = self.match(covid19Parser.MULTIPLICACION)
                    insertOperator((None if localctx._MULTIPLICACION is None else localctx._MULTIPLICACION.text))
                    pass
                elif token in [covid19Parser.DIVISION]:
                    self.state = 185
                    localctx._DIVISION = self.match(covid19Parser.DIVISION)
                    insertOperator((None if localctx._DIVISION is None else localctx._DIVISION.text))
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 189
                self.factor()
                leaving('factor')
                self.state = 196
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
            self.state = 210
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                localctx._identificador = self.identificador()
                insertIdToQueue((None if localctx._identificador is None else self._input.getText(localctx._identificador.start,localctx._identificador.stop)))
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                localctx._cte = self.cte()
                insertIdToQueue((None if localctx._cte is None else self._input.getText(localctx._cte.start,localctx._cte.stop)))
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 203
                self.llamadametodo()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 204
                self.match(covid19Parser.PARENTESISI)
                insertParenthesis()
                self.state = 206
                self.megaexpresion()
                self.state = 207
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
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 212
                self.llamadametodo()
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==covid19Parser.PUNTOYCOMA:
                    self.state = 213
                    self.match(covid19Parser.PUNTOYCOMA)


                pass

            elif la_ == 2:
                self.state = 216
                self.asignacion()
                self.state = 217
                self.match(covid19Parser.PUNTOYCOMA)
                pass

            elif la_ == 3:
                self.state = 219
                self.lectura()
                self.state = 220
                self.match(covid19Parser.PUNTOYCOMA)
                pass

            elif la_ == 4:
                self.state = 222
                self.escritura()
                self.state = 223
                self.match(covid19Parser.PUNTOYCOMA)
                pass

            elif la_ == 5:
                self.state = 225
                self.cargadatos()
                self.state = 226
                self.match(covid19Parser.PUNTOYCOMA)
                pass

            elif la_ == 6:
                self.state = 228
                self.decision()
                pass

            elif la_ == 7:
                self.state = 229
                self.condicional()
                pass

            elif la_ == 8:
                self.state = 230
                self.nocondicional()
                pass

            elif la_ == 9:
                self.state = 231
                self.metodo()
                pass

            elif la_ == 10:
                self.state = 232
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
            self.state = 235
            self.match(covid19Parser.ID)
            self.state = 236
            self.match(covid19Parser.PARENTESISI)
            self.state = 237
            self.megaexpresion()
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.COMA:
                self.state = 238
                self.match(covid19Parser.COMA)
                self.state = 239
                self.megaexpresion()
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 245
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
            self.state = 247
            self.match(covid19Parser.REGRESA)
            self.state = 248
            self.match(covid19Parser.PARENTESISI)
            self.state = 249
            self.megaexpresion()
            self.state = 250
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
            self.state = 252
            localctx._identificador = self.identificador()
            insertIdToQueue((None if localctx._identificador is None else self._input.getText(localctx._identificador.start,localctx._identificador.stop)))
            self.state = 254
            localctx._IGUAL = self.match(covid19Parser.IGUAL)
            insertOperator((None if localctx._IGUAL is None else localctx._IGUAL.text))
            self.state = 256
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
            self.state = 259
            self.match(covid19Parser.ID)
            self.state = 275
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==covid19Parser.CORCHETECUADRADOI:
                self.state = 260
                self.match(covid19Parser.CORCHETECUADRADOI)
                self.state = 263
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [covid19Parser.ID]:
                    self.state = 261
                    self.identificador()
                    pass
                elif token in [covid19Parser.CTEINT, covid19Parser.CTEFLOAT, covid19Parser.CTESTRING, covid19Parser.CTECHAR]:
                    self.state = 262
                    self.cte()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 265
                self.match(covid19Parser.CORCHETECUADRADOD)
                self.state = 273
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==covid19Parser.CORCHETECUADRADOI:
                    self.state = 266
                    self.match(covid19Parser.CORCHETECUADRADOI)
                    self.state = 269
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [covid19Parser.ID]:
                        self.state = 267
                        self.identificador()
                        pass
                    elif token in [covid19Parser.CTEINT, covid19Parser.CTEFLOAT, covid19Parser.CTESTRING, covid19Parser.CTECHAR]:
                        self.state = 268
                        self.cte()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 271
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
            self.state = 277
            self.match(covid19Parser.PROGRAMA)
            self.state = 278
            self.identificador()
            self.state = 279
            self.match(covid19Parser.PUNTOYCOMA)
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==covid19Parser.VAR:
                self.state = 280
                self.varx()


            self.state = 286
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==covid19Parser.FUNCION:
                self.state = 283
                self.metodo()
                self.state = 288
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 289
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
            self.state = 291
            self.match(covid19Parser.VAR)
            self.state = 302 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 292
                self.var()
                self.state = 297
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==covid19Parser.COMA:
                    self.state = 293
                    self.match(covid19Parser.COMA)
                    self.state = 294
                    self.identificador()
                    self.state = 299
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 300
                self.match(covid19Parser.PUNTOYCOMA)
                self.state = 304 
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
            self.state = 306
            self.tipo()
            self.state = 307
            self.match(covid19Parser.DOSPUNTOS)
            self.state = 308
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
            self.state = 310
            self.match(covid19Parser.PRINCIPAL)
            self.state = 311
            self.match(covid19Parser.PARENTESISI)
            self.state = 312
            self.match(covid19Parser.PARENTESISD)
            self.state = 313
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
            self.state = 315
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
            self.state = 317
            self.match(covid19Parser.FUNCION)
            self.state = 319
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << covid19Parser.INT) | (1 << covid19Parser.FLOAT) | (1 << covid19Parser.STRING) | (1 << covid19Parser.CHAR) | (1 << covid19Parser.DATAFRAME))) != 0):
                self.state = 318
                self.tipo()


            self.state = 321
            self.match(covid19Parser.ID)
            self.state = 322
            self.match(covid19Parser.PARENTESISI)
            self.state = 331
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << covid19Parser.INT) | (1 << covid19Parser.FLOAT) | (1 << covid19Parser.STRING) | (1 << covid19Parser.CHAR) | (1 << covid19Parser.DATAFRAME))) != 0):
                self.state = 323
                self.var()
                self.state = 328
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==covid19Parser.COMA:
                    self.state = 324
                    self.match(covid19Parser.COMA)
                    self.state = 325
                    self.var()
                    self.state = 330
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 333
            self.match(covid19Parser.PARENTESISD)
            self.state = 334
            self.match(covid19Parser.PUNTOYCOMA)
            self.state = 335
            self.varx()
            self.state = 336
            self.match(covid19Parser.CORCHETEI)
            self.state = 340
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 337
                    self.estatuto() 
                self.state = 342
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

            self.state = 344
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==covid19Parser.REGRESA:
                self.state = 343
                self.regresa()


            self.state = 346
            self.match(covid19Parser.CORCHETED)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





