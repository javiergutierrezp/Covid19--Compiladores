import sys
import ply.yacc as yacc
from lexer import tokens

def p_programa(p):
    '''
        program : PROGRAM ID PUNTOYCOMA variablesProg funcp 
    '''
    p[0] = "PROGRAM COMPILED"

def p_variablesProg(p):
    '''variablesProg : variables
                   | vacio'''

def p_variables(p):
    '''variables : VAR tipo DOSPUNTOS varId PUNTOYCOMA a'''

def p_varId(p):
    '''varId : IDs varsId'''

def p_varsId(p):
    '''varsId : COMA IDs varsId
              | vacio'''

def p_IDs(p):
    '''IDs : ID | IDARREGLO | IDMATRIZ'''

def p_a(p):
    '''a : varId DOSPUNTOS tipo PUNTOYCOMA a
         | vacio'''


def p_funcp(p):
    '''
        funcp: PRINCIPAL PARENTESISI PARENTESISD bloque
    '''

def p_tipo(p):
    '''
        tipo: INT | FLOAT | STRING | CHAR
    '''

def p_tipoONo(p):
    '''
        tipoONo: tipo | vacio
    '''

def p_regresaONo(p):
    '''
        regresaONo: REGRESA PARENTESISI ID PARENTESISD | vacio
    '''


def p_metodo(p):
    '''
        metodo: FUNCION tipoONo ID PARENTESISI megaExpresionONo PARENTESISD PUNTOYCOMA vars CORCHETEI estatuto regresaONo CORCHETED
    '''

def p_asignacionLoop(p):
    '''
        asignacionLoop: IGUAL megaExpresion asignacionLoop
                    | vacio
    '''

def p_asignacion(p):
    '''
        asignacion: IDs asignacionLoop PUNTOYCOMA
    '''


def p_factor(p):
    '''factor : cte
                | ID PARENTESISI megaExpresion PARENTESISD
                | PARENTESISI megaExpresion PARENTESISD'''

def p_termino(p):
    '''termino : factor mulDivLoop
                 | vacio'''

def p_expresion(p):
    '''expresion : termino sumResLoop'''

def p_comparacion(p):
    '''
    MAYOR | MAYORIGUAL | MENORIGUAL | MENOR | MAYOR | IGUAL IGUAL | DIFERENTE | NEGACION
    '''

def p_superExpresion(p):
    '''
        superExpresion: expresion
                                 | comparacion expresion
    '''

def p_megaExpresion(p):
    '''
        megaExpresion: superExpresion | Y | O
    '''

def p_lectura(p):
    '''
        lectura: LEE PARENTESISI varID PARENTESISD PUNTOYCOMA
    '''

def p_escrituraOpciones(p):
	 '''
        escrituraOpciones: STRING | megaexpresion escrituraOpcionesCiclo
    '''

def p_escrituraOpcionesCiclo(p):
	 '''
        escrituraOpcionesCiclo: COMA escrituraOpciones | vacio 
    '''

def p_escritura(p):
    '''
        escritura: ESCRIBE PARENTESISI escrituraOpciones PARENTESISD PUNTOYCOMA
    '''

def p_cargaDatos(p):
    '''
        cargaDatos: CARGAARCHIVO PARENTESISI ID STRING INTEGER INTEGER PARENTESISD PUNTOYCOMA
    '''

def p_decision(p):
    '''
        decision: SI PARENTESISI megaExpresion PARENTESISD ENTONCES bloque
                     | SI PARENTESISI megaExpresion PARENTESISD ENTONCES bloque SINO bloque
    '''

def p_estatutoLoop(p):
    '''estatutoLoop : COMA estatutoLoop
                 | vacio'''

def p_estatuto(p):
    '''estatuto : estatuto estatutoLoop'''

def p_bloque(p):
    '''
        bloque: CORCHETEI estatuto CORCHETED
    '''

def p_condicional(p):
    '''
        condicional: MIENTRAS PARENTESISI megaexpresion PARENTESISD HAZ bloque
    '''

def p_noCondicional(p):
    '''
        noCondicional: DESDE ID IGUAL expr HASTA expr HACER bloque
    '''

def p_estatutoOpciones(p):
    '''
	estatutoOpciones: estatuto PUNTOYCOMA
    '''
def p_estatutoOpciones(p):
    '''
        estatuto: asignacion | lectura | escritura | cargaDatos | decision | condicional | noCondicional | expresion | metodo
    '''

def p_megaExpresionONo(p):
    '''megaExpresionONo : megaExpresiones | vacio'''

def p_megaExpresiones(p):
    '''megaExpresiones : megaExpresion megaExpresionLoop'''

def megaExpresionLoop(p):
    '''megaExpresionLoop : COMA megaExpresiones
              | vacio'''

def p_fact(p):
    '''fact : cte
                | ID PARENTESISI megaExpresion PARENTESISD
                | PARENTESISI expr PARENTESISD'''

def p_cte(p):
    '''cte : ID
              | CTEINT
              | CTEFLOAT'''

def p_mulDivLoop(p):
    '''mulDivLoop : mulDiv factor
                 | vacio'''

def p_term(p):
    '''term : fact mulDivLoop
                 | vacio'''

def p_mulDiv(p):
    '''mulDiv : SUMA
             | RESTA'''

def p_sumResLoop(p):
    '''sumResLoop : sumRes term
                 | vacio'''

def p_expr(p):
    '''expr : term sumResLoop'''

def p_sumRes(p):
    '''sumRes : SUMA
             | RESTA'''

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

