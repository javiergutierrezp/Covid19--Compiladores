import sys
from antlr4 import *
from grammar.covid19Lexer import covid19Lexer
from grammar.covid19Parser import covid19Parser
from grammar.covid19Listener import covid19Listener
from antlr4.tree.Trees import Trees
from semantics import *
from virtualmemory import *
from utils import pq

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
    print(compilation_memory)

    if parser.getNumberOfSyntaxErrors() == 0:
        # Print them quadsssss
        pq(quads)

        # print(virtual_cte_directory)
        print(function_directory)

        if SHOW_VIRTUAL:
            # Crear MV etc etc
            virtual_machine = VirtualMachine(quads, virtual_cte_directory[0], function_directory)
            virtual_machine.execute()    
    else:
        print("error!")
        exit(1)

if __name__ == '__main__':
    main(sys.argv)