import sys
import ply.yacc as yacc
from lexer import tokens
from semantics import directory

def p_programa(p):
    '''
        program : PROGRAMA ID PUNTOYCOMA varsProg metodosLoop funcp 
    '''
    p[0] = "PROGRAM COMPILED"

def p_varsProg(p):
    '''
        varsProg : vars
                 | vacio
    '''

def p_vars(p):
    '''vars : VAR tipo DOSPUNTOS varId PUNTOYCOMA varsLoop'''

def p_varId(p):
    '''varId : IDs varsId'''

def p_varsId(p):
    '''varsId : COMA IDs varsId
              | vacio'''

def p_IDs(p):
    '''
    IDs : ID
        | idArreglo
        | idMatriz
    '''

def p_idArreglo(p):
    '''
        idArreglo : ID CORCHETECUADRADOI cte CORCHETECUADRADOD
    '''

def p_idMatriz(p):
    '''
        idMatriz : ID CORCHETECUADRADOI cte CORCHETECUADRADOD CORCHETECUADRADOI cte CORCHETECUADRADOD
    '''

def p_varsLoop(p):
    '''varsLoop : tipo DOSPUNTOS varId PUNTOYCOMA varsLoop
                | vacio'''


def p_funcp(p):
    '''
        funcp : PRINCIPAL PARENTESISI PARENTESISD bloque
    '''

def p_tipo(p):
    '''
        tipo : INT
             | FLOAT
             | STRING
             | CHAR
             | DATAFRAME
             | vacio
    '''

def p_parametros(p):
    '''
        parametros : parametro COMA parametros
                  | parametro
                  | vacio
    '''
    
def p_parametro(p):
    '''
        parametro : tipo DOSPUNTOS IDs
    '''

def p_metodosLoop(p):
    '''
        metodosLoop : metodo metodosLoop
                    | vacio
    '''

def p_metodo(p):
    '''
        metodo : FUNCION tipo ID PARENTESISI parametros PARENTESISD PUNTOYCOMA varsProg CORCHETEI estatutoBloque CORCHETED
    '''

def p_asignacionLoop(p):
    '''
        asignacionLoop : IGUAL megaExpresion asignacionLoop
                       | vacio
    '''

def p_asignacion(p):
    '''
        asignacion : IDs asignacionLoop
    '''

def p_megaExpresionLoop(p):
    '''
        megaExpresionLoop : COMA megaExpresion megaExpresionLoop
                          | vacio
    '''

def p_llamadaMetodo(p):
    '''
        llamadaMetodo : ID PARENTESISI megaExpresion megaExpresionLoop PARENTESISD
    '''

def p_factor(p):
    '''factor : cte
              | llamadaMetodo
              | PARENTESISI megaExpresion PARENTESISD'''

def p_termino(p):
    '''termino : factor mulDivLoop
               | vacio'''

def p_expresion(p):
    '''expresion : termino sumResLoop'''

def p_sumResLoopNoCondicional(p):
    '''
        sumResLoopNoCondicional : sumRes terminoNoCondicional
                   | vacio
    '''

def p_sumResLoop(p):
    '''
        sumResLoop : sumRes termino sumResLoop
                   | vacio
    '''

def p_comparacion(p):
    '''
        comparacion : MAYOR
                    | MAYORIGUAL
                    | MENORIGUAL
                    | MENOR
                    | IGUAL IGUAL
                    | DIFERENTE
                    | NEGACION
    '''

def p_superExpresion(p):
    '''
        superExpresion : expresion 
                       | expresion comparacion expresion
    '''

def p_megaExpresion(p):
    '''megaExpresion : superExpresion yOLoop'''

def p_yOLoop(p):
    '''
        yOLoop : yO superExpresion
               | vacio
    '''

def p_yO(p):
    '''
        yO : Y
           | O
    '''

def p_lectura(p):
    '''
        lectura : LEE PARENTESISI varId PARENTESISD
    '''

def p_escritura(p):
    '''
        escritura : ESCRIBE PARENTESISI megaExpresion megaExpresionLoop PARENTESISD
    '''

def p_cargaDatos(p):
    '''
        cargaDatos : CARGAARCHIVO PARENTESISI ID COMA cte COMA cte COMA cte PARENTESISD
    '''

def p_decision(p):
    '''
        decision : SI PARENTESISI megaExpresion PARENTESISD ENTONCES bloque
                 | SI PARENTESISI megaExpresion PARENTESISD ENTONCES bloque SINO bloque
    '''

def p_estatutoLoop(p):
    '''
        estatutoLoop : estatutoOpciones estatutoLoop
                     | vacio
    '''

def p_estatutoBloque(p):
    '''estatutoBloque : estatutoOpciones estatutoLoop'''

def p_bloque(p):
    '''
        bloque : CORCHETEI estatutoBloque CORCHETED
    '''

def p_condicional(p):
    '''
        condicional : MIENTRAS PARENTESISI megaExpresion PARENTESISD HAZ bloque
    '''

def p_noCondicional(p):
    '''
        noCondicional : DESDE ID IGUAL expresionNoCondicional HASTA expresionNoCondicional HACER bloque
    '''

def p_estatutoOpciones(p):
    '''
	    estatutoOpciones : estatuto
                         | vacio
    '''

def p_regresa(p):
    '''
        regresa : REGRESA PARENTESISI megaExpresion PARENTESISD
    '''

def p_estatuto(p):
    '''
        estatuto : asignacion PUNTOYCOMA
                 | lectura PUNTOYCOMA
                 | escritura PUNTOYCOMA
                 | decision
                 | condicional
                 | noCondicional
                 | llamadaMetodo PUNTOYCOMA
                 | cargaDatos PUNTOYCOMA
                 | metodo
                 | regresa
    '''

def p_factorNoCondicional(p):
    '''
        factorNoCondicional : cte
                            | llamadaMetodo
                            | PARENTESISI expresionNoCondicional PARENTESISD
    '''

def p_cte(p):
    '''
        cte : IDs
            | CTEINT
            | CTEFLOAT
            | CTESTRING
            | CTECHAR
    '''

def p_mulDivLoopNoCondicional(p):
    '''
        mulDivLoopNoCondicional : mulDiv factorNoCondicional
                                | vacio
    '''

def p_mulDivLoop(p):
    '''
        mulDivLoop : mulDiv factor
                   | vacio
    '''

def p_terminoNoCondicional(p):
    '''
        terminoNoCondicional : factorNoCondicional mulDivLoopNoCondicional
                             | vacio
    '''

def p_mulDiv(p):
    '''
        mulDiv : MULTIPLICACION
               | DIVISION
    '''

def p_expresionNoCondicional(p):
    '''expresionNoCondicional : terminoNoCondicional sumResLoopNoCondicional'''

def p_sumRes(p):
    '''
        sumRes : SUMA
               | RESTA
    '''

def p_vacio(p):
    '''vacio : '''

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

