import sys
from antlr4 import *
from grammar.covid19Lexer import covid19Lexer
from grammar.covid19Parser import covid19Parser
from grammar.covid19Listener import covid19Listener
from antlr4.tree.Trees import Trees
from semantics import *

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = covid19Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = covid19Parser(stream)
    printer = covid19Listener()
    walker = ParseTreeWalker()
    tree = parser.programa()
    walker.walk(printer, tree)

    # Print them quadsssss
    for (i, item) in enumerate(quads, start=1):
        print("{} - {}".format(i - 1, item))

    # print(virtual_cte_directory)
    # print(function_directory)

    # if SHOW_VIRTUAL:
    #     # Crear MV etc etc
    #     print("manda llamar mv")
    

    if parser.getNumberOfSyntaxErrors() == 0:
        print("PROGRAMA CORRECTO")
    else:
        print("error!")
        exit(1)

if __name__ == '__main__':
    main(sys.argv)