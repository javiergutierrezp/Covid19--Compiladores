import sys
from antlr4 import *
from grammar.covid19Lexer import covid19Lexer
from grammar.covid19Parser import covid19Parser
from grammar.covid19Listener import covid19Listener
from antlr4.tree.Trees import Trees
from semantics import function_directory, quads

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = covid19Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = covid19Parser(stream)
    printer = covid19Listener()
    walker = ParseTreeWalker()
    tree = parser.programa()
    walker.walk(printer, tree)
    print(function_directory)

    if parser.getNumberOfSyntaxErrors() == 0:
        print("PROGRAMA CORRECTO")
    else:
        print("error!")
        exit(1)

if __name__ == '__main__':
    main(sys.argv)