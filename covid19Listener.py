# Generated from covid19.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .covid19Parser import covid19Parser
else:
    from covid19Parser import covid19Parser

# This class defines a complete listener for a parse tree produced by covid19Parser.
class covid19Listener(ParseTreeListener):

    # Enter a parse tree produced by covid19Parser#program.
    def enterProgram(self, ctx:covid19Parser.ProgramContext):
        pass

    # Exit a parse tree produced by covid19Parser#program.
    def exitProgram(self, ctx:covid19Parser.ProgramContext):
        pass



del covid19Parser