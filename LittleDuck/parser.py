import sys
import ply.yacc as yacc
from lexer import tokens


def p_program(p):
    '''program : PROGRAM ID PUNTOYCOMA variablesProg bloque'''
    p[0] = "PROGRAM COMPILED"

def p_variablesProg(p):
    '''variablesProg : variables
                   | vacio'''

def p_bloque(p):
    '''bloque : CORCHETEI estatutoBloque CORCHETED'''

def p_estatutoBloque(p):
    '''estatutoBloque : estatuto estatutoBloque
                      | vacio'''

def p_variables(p):
    '''variables : VAR varId DOSPUNTOS tipo PUNTOYCOMA a'''

def p_varId(p):
    '''varId : ID varsId'''

def p_varsId(p):
    '''varsId : COMA ID varsId
              | vacio'''

def p_a(p):
    '''a : varId DOSPUNTOS tipo PUNTOYCOMA a
         | vacio'''

def p_tipo(p):
    '''tipo : INT
            | FLOAT'''

def p_estatuto(p):
    '''estatuto : asignacion
                | condicion
                | escritura '''

def p_asignacion(p):
    '''asignacion : ID IGUAL expresion PUNTOYCOMA'''

def p_expresion(p):
    '''expresion : exp comparacion'''

def p_comparacion(p):
    '''comparacion : MAYOR comparacionExp
                  | MENOR comparacionExp
                  | DIFERENTE comparacionExp
                  | vacio'''

def p_comparisonExp(p):
    '''comparacionExp : exp'''

def p_escritura(p):
    '''escritura : PRINT PARENTESISI toprint PARENTESISD PUNTOYCOMA'''

def p_toprint(p):
    '''toprint : expresion toprintExp
               | CTESTRING toprintExp'''

def p_toprintExp(p):
    '''toprintExp : COMA  toprint
                  | vacio'''

def p_exp(p):
    '''exp : termino operador'''

def p_operator(p):
    '''operador : SUMA termino operador
            | RESTA termino operador
            | vacio'''

def p_termino(p):
    '''termino : factor operadorTerm'''

def p_termOperator(p):
    '''operadorTerm : MULTIPLICACION factor operadorTerm
                    | DIVISION factor operadorTerm
                    | vacio'''

def p_condicion(p):
    '''condicion : IF PARENTESISI expresion PARENTESISD bloque condicionElse PUNTOYCOMA'''

def p_elseCondition(p):
    '''condicionElse : ELSE bloque
                     | vacio'''

def p_varcte(p):
    '''varConst : ID
              | CTEINT
              | CTEFLOAT'''

def p_factor(p):
    '''factor : PARENTESISI expresion PARENTESISD
              | signo varConst'''

def p_signo(p):
    '''signo : SUMA
            | RESTA
            | vacio'''

def p_vacio(p):
    '''vacio :'''

def p_error(p):
    print("ERROR {}".format(p))

yacc.yacc()

if __name__ == '__main__':
	if (len(sys.argv) > 1):
		file = sys.argv[1]
		try:
			f = open(file,'r')
			data = f.read()
			f.close()
			if (yacc.parse(data, tracking=True) == 'PROGRAM COMPILED'):
				print ("Syntaxis correcto")

		except EOFError:
	   		print(EOFError)
	else:
		print('Archivo inexistente')