import sys
from antlr4 import *
from covid19Lexer import covid19Lexer
from covid19Parser import covid19Parser
from covid19Listener import covid19Listener
from antlr4.tree.Trees import Trees
import logging

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = covid19Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = covid19Parser(stream)
    printer = covid19Listener()
    walker = ParseTreeWalker()
    tree = parser.programa()
    walker.walk(printer, tree)

    
    
    # print(Trees.toStringTree(tree, None, parser))

    if parser.getNumberOfSyntaxErrors() == 0:
        print("PROGRAMA CORRECTO")
    else:
        print("error!")
        exit(1)

if __name__ == '__main__':
    main(sys.argv)