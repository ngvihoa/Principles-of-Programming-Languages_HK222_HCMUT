# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u01bd\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33")
        buf.write("\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3")
        buf.write("$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3,\3")
        buf.write("-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3\60\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\7\63\u0146")
        buf.write("\n\63\f\63\16\63\u0149\13\63\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\5\65\u0154\n\65\3\65\3\65\3\65\5")
        buf.write("\65\u0159\n\65\3\66\3\66\3\67\3\67\38\38\38\58\u0162\n")
        buf.write("8\38\78\u0165\n8\f8\168\u0168\138\58\u016a\n8\39\39\6")
        buf.write("9\u016e\n9\r9\169\u016f\3:\3:\5:\u0174\n:\3:\6:\u0177")
        buf.write("\n:\r:\16:\u0178\3;\3;\5;\u017d\n;\3;\3;\3;\3<\3<\6<\u0184")
        buf.write("\n<\r<\16<\u0185\3=\3=\3=\3>\3>\3>\3?\3?\3?\3?\7?\u0192")
        buf.write("\n?\f?\16?\u0195\13?\3?\3?\3?\3?\3?\3@\3@\3@\3@\7@\u01a0")
        buf.write("\n@\f@\16@\u01a3\13@\3@\3@\3A\6A\u01a8\nA\rA\16A\u01a9")
        buf.write("\3A\3A\3B\3B\3B\3C\3C\5C\u01b3\nC\3C\3C\3D\3D\5D\u01b9")
        buf.write("\nD\3D\3D\3D\3\u0193\2E\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\2m\2o\2q\2s\2u\67w\2y\2{\2}8\1779\u0081")
        buf.write(":\u0083;\u0085<\u0087=\3\2\f\5\2C\\aac|\6\2\62;C\\aac")
        buf.write("|\3\2\62;\3\2\63;\4\2GGgg\4\2--//\6\2\f\f\17\17$$^^\n")
        buf.write("\2$$))^^ddhhppttvv\4\2\f\f\17\17\5\2\13\f\17\17\"\"\2")
        buf.write("\u01c5\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2u\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2")
        buf.write("\u0087\3\2\2\2\3\u0089\3\2\2\2\5\u008b\3\2\2\2\7\u008d")
        buf.write("\3\2\2\2\t\u008f\3\2\2\2\13\u0091\3\2\2\2\r\u0093\3\2")
        buf.write("\2\2\17\u0095\3\2\2\2\21\u0098\3\2\2\2\23\u009b\3\2\2")
        buf.write("\2\25\u009e\3\2\2\2\27\u00a1\3\2\2\2\31\u00a3\3\2\2\2")
        buf.write("\33\u00a6\3\2\2\2\35\u00a8\3\2\2\2\37\u00ab\3\2\2\2!\u00ae")
        buf.write("\3\2\2\2#\u00b0\3\2\2\2%\u00b2\3\2\2\2\'\u00b4\3\2\2\2")
        buf.write(")\u00b6\3\2\2\2+\u00b8\3\2\2\2-\u00ba\3\2\2\2/\u00bc\3")
        buf.write("\2\2\2\61\u00be\3\2\2\2\63\u00c0\3\2\2\2\65\u00c2\3\2")
        buf.write("\2\2\67\u00c4\3\2\2\29\u00c6\3\2\2\2;\u00c8\3\2\2\2=\u00ce")
        buf.write("\3\2\2\2?\u00d3\3\2\2\2A\u00d9\3\2\2\2C\u00e1\3\2\2\2")
        buf.write("E\u00e4\3\2\2\2G\u00e9\3\2\2\2I\u00ef\3\2\2\2K\u00f5\3")
        buf.write("\2\2\2M\u00f9\3\2\2\2O\u0102\3\2\2\2Q\u0105\3\2\2\2S\u010d")
        buf.write("\3\2\2\2U\u0114\3\2\2\2W\u011b\3\2\2\2Y\u0120\3\2\2\2")
        buf.write("[\u0125\3\2\2\2]\u012b\3\2\2\2_\u012f\3\2\2\2a\u0138\3")
        buf.write("\2\2\2c\u013b\3\2\2\2e\u0143\3\2\2\2g\u014a\3\2\2\2i\u0158")
        buf.write("\3\2\2\2k\u015a\3\2\2\2m\u015c\3\2\2\2o\u0169\3\2\2\2")
        buf.write("q\u016b\3\2\2\2s\u0171\3\2\2\2u\u017a\3\2\2\2w\u0183\3")
        buf.write("\2\2\2y\u0187\3\2\2\2{\u018a\3\2\2\2}\u018d\3\2\2\2\177")
        buf.write("\u019b\3\2\2\2\u0081\u01a7\3\2\2\2\u0083\u01ad\3\2\2\2")
        buf.write("\u0085\u01b0\3\2\2\2\u0087\u01b6\3\2\2\2\u0089\u008a\7")
        buf.write("-\2\2\u008a\4\3\2\2\2\u008b\u008c\7/\2\2\u008c\6\3\2\2")
        buf.write("\2\u008d\u008e\7,\2\2\u008e\b\3\2\2\2\u008f\u0090\7\61")
        buf.write("\2\2\u0090\n\3\2\2\2\u0091\u0092\7\'\2\2\u0092\f\3\2\2")
        buf.write("\2\u0093\u0094\7#\2\2\u0094\16\3\2\2\2\u0095\u0096\7(")
        buf.write("\2\2\u0096\u0097\7(\2\2\u0097\20\3\2\2\2\u0098\u0099\7")
        buf.write("~\2\2\u0099\u009a\7~\2\2\u009a\22\3\2\2\2\u009b\u009c")
        buf.write("\7?\2\2\u009c\u009d\7?\2\2\u009d\24\3\2\2\2\u009e\u009f")
        buf.write("\7#\2\2\u009f\u00a0\7?\2\2\u00a0\26\3\2\2\2\u00a1\u00a2")
        buf.write("\7>\2\2\u00a2\30\3\2\2\2\u00a3\u00a4\7>\2\2\u00a4\u00a5")
        buf.write("\7?\2\2\u00a5\32\3\2\2\2\u00a6\u00a7\7@\2\2\u00a7\34\3")
        buf.write("\2\2\2\u00a8\u00a9\7@\2\2\u00a9\u00aa\7?\2\2\u00aa\36")
        buf.write("\3\2\2\2\u00ab\u00ac\7<\2\2\u00ac\u00ad\7<\2\2\u00ad ")
        buf.write("\3\2\2\2\u00ae\u00af\7a\2\2\u00af\"\3\2\2\2\u00b0\u00b1")
        buf.write("\7*\2\2\u00b1$\3\2\2\2\u00b2\u00b3\7+\2\2\u00b3&\3\2\2")
        buf.write("\2\u00b4\u00b5\7]\2\2\u00b5(\3\2\2\2\u00b6\u00b7\7_\2")
        buf.write("\2\u00b7*\3\2\2\2\u00b8\u00b9\7}\2\2\u00b9,\3\2\2\2\u00ba")
        buf.write("\u00bb\7\177\2\2\u00bb.\3\2\2\2\u00bc\u00bd\7\60\2\2\u00bd")
        buf.write("\60\3\2\2\2\u00be\u00bf\7.\2\2\u00bf\62\3\2\2\2\u00c0")
        buf.write("\u00c1\7<\2\2\u00c1\64\3\2\2\2\u00c2\u00c3\7=\2\2\u00c3")
        buf.write("\66\3\2\2\2\u00c4\u00c5\7?\2\2\u00c58\3\2\2\2\u00c6\u00c7")
        buf.write("\7$\2\2\u00c7:\3\2\2\2\u00c8\u00c9\7c\2\2\u00c9\u00ca")
        buf.write("\7t\2\2\u00ca\u00cb\7t\2\2\u00cb\u00cc\7c\2\2\u00cc\u00cd")
        buf.write("\7{\2\2\u00cd<\3\2\2\2\u00ce\u00cf\7c\2\2\u00cf\u00d0")
        buf.write("\7w\2\2\u00d0\u00d1\7v\2\2\u00d1\u00d2\7q\2\2\u00d2>\3")
        buf.write("\2\2\2\u00d3\u00d4\7d\2\2\u00d4\u00d5\7t\2\2\u00d5\u00d6")
        buf.write("\7g\2\2\u00d6\u00d7\7c\2\2\u00d7\u00d8\7m\2\2\u00d8@\3")
        buf.write("\2\2\2\u00d9\u00da\7d\2\2\u00da\u00db\7q\2\2\u00db\u00dc")
        buf.write("\7q\2\2\u00dc\u00dd\7n\2\2\u00dd\u00de\7g\2\2\u00de\u00df")
        buf.write("\7c\2\2\u00df\u00e0\7p\2\2\u00e0B\3\2\2\2\u00e1\u00e2")
        buf.write("\7f\2\2\u00e2\u00e3\7q\2\2\u00e3D\3\2\2\2\u00e4\u00e5")
        buf.write("\7g\2\2\u00e5\u00e6\7n\2\2\u00e6\u00e7\7u\2\2\u00e7\u00e8")
        buf.write("\7g\2\2\u00e8F\3\2\2\2\u00e9\u00ea\7h\2\2\u00ea\u00eb")
        buf.write("\7c\2\2\u00eb\u00ec\7n\2\2\u00ec\u00ed\7u\2\2\u00ed\u00ee")
        buf.write("\7g\2\2\u00eeH\3\2\2\2\u00ef\u00f0\7h\2\2\u00f0\u00f1")
        buf.write("\7n\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3\7c\2\2\u00f3\u00f4")
        buf.write("\7v\2\2\u00f4J\3\2\2\2\u00f5\u00f6\7h\2\2\u00f6\u00f7")
        buf.write("\7q\2\2\u00f7\u00f8\7t\2\2\u00f8L\3\2\2\2\u00f9\u00fa")
        buf.write("\7h\2\2\u00fa\u00fb\7w\2\2\u00fb\u00fc\7p\2\2\u00fc\u00fd")
        buf.write("\7e\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7k\2\2\u00ff\u0100")
        buf.write("\7q\2\2\u0100\u0101\7p\2\2\u0101N\3\2\2\2\u0102\u0103")
        buf.write("\7k\2\2\u0103\u0104\7h\2\2\u0104P\3\2\2\2\u0105\u0106")
        buf.write("\7k\2\2\u0106\u0107\7p\2\2\u0107\u0108\7v\2\2\u0108\u0109")
        buf.write("\7g\2\2\u0109\u010a\7i\2\2\u010a\u010b\7g\2\2\u010b\u010c")
        buf.write("\7t\2\2\u010cR\3\2\2\2\u010d\u010e\7t\2\2\u010e\u010f")
        buf.write("\7g\2\2\u010f\u0110\7v\2\2\u0110\u0111\7w\2\2\u0111\u0112")
        buf.write("\7t\2\2\u0112\u0113\7p\2\2\u0113T\3\2\2\2\u0114\u0115")
        buf.write("\7u\2\2\u0115\u0116\7v\2\2\u0116\u0117\7t\2\2\u0117\u0118")
        buf.write("\7k\2\2\u0118\u0119\7p\2\2\u0119\u011a\7i\2\2\u011aV\3")
        buf.write("\2\2\2\u011b\u011c\7v\2\2\u011c\u011d\7t\2\2\u011d\u011e")
        buf.write("\7w\2\2\u011e\u011f\7g\2\2\u011fX\3\2\2\2\u0120\u0121")
        buf.write("\7x\2\2\u0121\u0122\7q\2\2\u0122\u0123\7k\2\2\u0123\u0124")
        buf.write("\7f\2\2\u0124Z\3\2\2\2\u0125\u0126\7y\2\2\u0126\u0127")
        buf.write("\7j\2\2\u0127\u0128\7k\2\2\u0128\u0129\7n\2\2\u0129\u012a")
        buf.write("\7g\2\2\u012a\\\3\2\2\2\u012b\u012c\7q\2\2\u012c\u012d")
        buf.write("\7w\2\2\u012d\u012e\7v\2\2\u012e^\3\2\2\2\u012f\u0130")
        buf.write("\7e\2\2\u0130\u0131\7q\2\2\u0131\u0132\7p\2\2\u0132\u0133")
        buf.write("\7v\2\2\u0133\u0134\7k\2\2\u0134\u0135\7p\2\2\u0135\u0136")
        buf.write("\7w\2\2\u0136\u0137\7g\2\2\u0137`\3\2\2\2\u0138\u0139")
        buf.write("\7q\2\2\u0139\u013a\7h\2\2\u013ab\3\2\2\2\u013b\u013c")
        buf.write("\7k\2\2\u013c\u013d\7p\2\2\u013d\u013e\7j\2\2\u013e\u013f")
        buf.write("\7g\2\2\u013f\u0140\7t\2\2\u0140\u0141\7k\2\2\u0141\u0142")
        buf.write("\7v\2\2\u0142d\3\2\2\2\u0143\u0147\t\2\2\2\u0144\u0146")
        buf.write("\t\3\2\2\u0145\u0144\3\2\2\2\u0146\u0149\3\2\2\2\u0147")
        buf.write("\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148f\3\2\2\2\u0149")
        buf.write("\u0147\3\2\2\2\u014a\u014b\5o8\2\u014b\u014c\b\64\2\2")
        buf.write("\u014ch\3\2\2\2\u014d\u014e\5o8\2\u014e\u014f\5q9\2\u014f")
        buf.write("\u0150\b\65\3\2\u0150\u0159\3\2\2\2\u0151\u0153\5o8\2")
        buf.write("\u0152\u0154\5q9\2\u0153\u0152\3\2\2\2\u0153\u0154\3\2")
        buf.write("\2\2\u0154\u0155\3\2\2\2\u0155\u0156\5s:\2\u0156\u0157")
        buf.write("\b\65\4\2\u0157\u0159\3\2\2\2\u0158\u014d\3\2\2\2\u0158")
        buf.write("\u0151\3\2\2\2\u0159j\3\2\2\2\u015a\u015b\t\4\2\2\u015b")
        buf.write("l\3\2\2\2\u015c\u015d\t\5\2\2\u015dn\3\2\2\2\u015e\u016a")
        buf.write("\7\62\2\2\u015f\u0166\5m\67\2\u0160\u0162\5!\21\2\u0161")
        buf.write("\u0160\3\2\2\2\u0161\u0162\3\2\2\2\u0162\u0163\3\2\2\2")
        buf.write("\u0163\u0165\5k\66\2\u0164\u0161\3\2\2\2\u0165\u0168\3")
        buf.write("\2\2\2\u0166\u0164\3\2\2\2\u0166\u0167\3\2\2\2\u0167\u016a")
        buf.write("\3\2\2\2\u0168\u0166\3\2\2\2\u0169\u015e\3\2\2\2\u0169")
        buf.write("\u015f\3\2\2\2\u016ap\3\2\2\2\u016b\u016d\5/\30\2\u016c")
        buf.write("\u016e\5k\66\2\u016d\u016c\3\2\2\2\u016e\u016f\3\2\2\2")
        buf.write("\u016f\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170r\3\2\2")
        buf.write("\2\u0171\u0173\t\6\2\2\u0172\u0174\t\7\2\2\u0173\u0172")
        buf.write("\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0176\3\2\2\2\u0175")
        buf.write("\u0177\5k\66\2\u0176\u0175\3\2\2\2\u0177\u0178\3\2\2\2")
        buf.write("\u0178\u0176\3\2\2\2\u0178\u0179\3\2\2\2\u0179t\3\2\2")
        buf.write("\2\u017a\u017c\59\35\2\u017b\u017d\5w<\2\u017c\u017b\3")
        buf.write("\2\2\2\u017c\u017d\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u017f")
        buf.write("\59\35\2\u017f\u0180\b;\5\2\u0180v\3\2\2\2\u0181\u0184")
        buf.write("\n\b\2\2\u0182\u0184\5y=\2\u0183\u0181\3\2\2\2\u0183\u0182")
        buf.write("\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0183\3\2\2\2\u0185")
        buf.write("\u0186\3\2\2\2\u0186x\3\2\2\2\u0187\u0188\7^\2\2\u0188")
        buf.write("\u0189\t\t\2\2\u0189z\3\2\2\2\u018a\u018b\7^\2\2\u018b")
        buf.write("\u018c\n\t\2\2\u018c|\3\2\2\2\u018d\u018e\7\61\2\2\u018e")
        buf.write("\u018f\7,\2\2\u018f\u0193\3\2\2\2\u0190\u0192\13\2\2\2")
        buf.write("\u0191\u0190\3\2\2\2\u0192\u0195\3\2\2\2\u0193\u0194\3")
        buf.write("\2\2\2\u0193\u0191\3\2\2\2\u0194\u0196\3\2\2\2\u0195\u0193")
        buf.write("\3\2\2\2\u0196\u0197\7,\2\2\u0197\u0198\7\61\2\2\u0198")
        buf.write("\u0199\3\2\2\2\u0199\u019a\b?\6\2\u019a~\3\2\2\2\u019b")
        buf.write("\u019c\7\61\2\2\u019c\u019d\7\61\2\2\u019d\u01a1\3\2\2")
        buf.write("\2\u019e\u01a0\n\n\2\2\u019f\u019e\3\2\2\2\u01a0\u01a3")
        buf.write("\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2")
        buf.write("\u01a4\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a5\b@\6\2")
        buf.write("\u01a5\u0080\3\2\2\2\u01a6\u01a8\t\13\2\2\u01a7\u01a6")
        buf.write("\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9")
        buf.write("\u01aa\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ac\bA\6\2")
        buf.write("\u01ac\u0082\3\2\2\2\u01ad\u01ae\13\2\2\2\u01ae\u01af")
        buf.write("\bB\7\2\u01af\u0084\3\2\2\2\u01b0\u01b2\59\35\2\u01b1")
        buf.write("\u01b3\5w<\2\u01b2\u01b1\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3")
        buf.write("\u01b4\3\2\2\2\u01b4\u01b5\bC\b\2\u01b5\u0086\3\2\2\2")
        buf.write("\u01b6\u01b8\59\35\2\u01b7\u01b9\5w<\2\u01b8\u01b7\3\2")
        buf.write("\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bb")
        buf.write("\5{>\2\u01bb\u01bc\bD\t\2\u01bc\u0088\3\2\2\2\24\2\u0147")
        buf.write("\u0153\u0158\u0161\u0166\u0169\u016f\u0173\u0178\u017c")
        buf.write("\u0183\u0185\u0193\u01a1\u01a9\u01b2\u01b8\n\3\64\2\3")
        buf.write("\65\3\3\65\4\3;\5\b\2\2\3B\6\3C\7\3D\b")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4
    MOD = 5
    NOT = 6
    AND = 7
    OR = 8
    EQUAL = 9
    UNEQUAL = 10
    LT = 11
    LTE = 12
    GT = 13
    GTE = 14
    DCOLON = 15
    UNDERSCORE = 16
    LB = 17
    RB = 18
    LSB = 19
    RSB = 20
    LCB = 21
    RCB = 22
    DOT = 23
    COMMA = 24
    COLON = 25
    SMCOLON = 26
    ASSIGN = 27
    DQUOTE = 28
    ARRAY = 29
    AUTO = 30
    BREAK = 31
    BOOLEAN = 32
    DO = 33
    ELSE = 34
    FALSE = 35
    FLOAT = 36
    FOR = 37
    FUNCTION = 38
    IF = 39
    INTEGER = 40
    RETURN = 41
    STRING = 42
    TRUE = 43
    VOID = 44
    WHILE = 45
    OUT = 46
    CONTINUE = 47
    OF = 48
    INHERIT = 49
    ID = 50
    INT_LIT = 51
    FLOAT_LIT = 52
    STRING_LIT = 53
    BLOCK_COMMENT = 54
    INLINE_COMMENT = 55
    WS = 56
    ERROR_CHAR = 57
    UNCLOSE_STRING = 58
    ILLEGAL_ESCAPE = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", "'_'", "'('", 
            "')'", "'['", "']'", "'{'", "'}'", "'.'", "','", "':'", "';'", 
            "'='", "'\"'", "'array'", "'auto'", "'break'", "'boolean'", 
            "'do'", "'else'", "'false'", "'float'", "'for'", "'function'", 
            "'if'", "'integer'", "'return'", "'string'", "'true'", "'void'", 
            "'while'", "'out'", "'continue'", "'of'", "'inherit'" ]

    symbolicNames = [ "<INVALID>",
            "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", "EQUAL", 
            "UNEQUAL", "LT", "LTE", "GT", "GTE", "DCOLON", "UNDERSCORE", 
            "LB", "RB", "LSB", "RSB", "LCB", "RCB", "DOT", "COMMA", "COLON", 
            "SMCOLON", "ASSIGN", "DQUOTE", "ARRAY", "AUTO", "BREAK", "BOOLEAN", 
            "DO", "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
            "RETURN", "STRING", "TRUE", "VOID", "WHILE", "OUT", "CONTINUE", 
            "OF", "INHERIT", "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
            "BLOCK_COMMENT", "INLINE_COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                  "EQUAL", "UNEQUAL", "LT", "LTE", "GT", "GTE", "DCOLON", 
                  "UNDERSCORE", "LB", "RB", "LSB", "RSB", "LCB", "RCB", 
                  "DOT", "COMMA", "COLON", "SMCOLON", "ASSIGN", "DQUOTE", 
                  "ARRAY", "AUTO", "BREAK", "BOOLEAN", "DO", "ELSE", "FALSE", 
                  "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", 
                  "STRING", "TRUE", "VOID", "WHILE", "OUT", "CONTINUE", 
                  "OF", "INHERIT", "ID", "INT_LIT", "FLOAT_LIT", "DIGIT_Z", 
                  "DIGIT_N", "INT_PART", "DECPART", "EXP", "STRING_LIT", 
                  "STRING_SEQUENCE", "ESCAPE_C", "ILLEGAL_C", "BLOCK_COMMENT", 
                  "INLINE_COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[50] = self.INT_LIT_action 
            actions[51] = self.FLOAT_LIT_action 
            actions[57] = self.STRING_LIT_action 
            actions[64] = self.ERROR_CHAR_action 
            actions[65] = self.UNCLOSE_STRING_action 
            actions[66] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		self.text = self.text.replace('_','')
            	
     

    def FLOAT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		self.text = self.text.replace('_','')
            	
     

        if actionIndex == 2:

            		self.text = self.text.replace('_','')
            	
     

    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		self.text = self.text[1:-1]
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            		self.text = self.text[1:]
            		raise UncloseString(self.text)
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

            		self.text = self.text[1:]
            		raise IllegalEscape(self.text)
            	
     


