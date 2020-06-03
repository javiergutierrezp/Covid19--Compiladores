grammar covid19;

@header {
from semantics import *
}

// Keywords
INT: 'int';
FLOAT: 'float';
STRING: 'string';
CHAR: 'char';
DATAFRAME: 'Dataframe';
VAR: 'var';
FUNCION: 'funcion';
CARGAARCHIVO: 'CargaArchivo';
SI: 'si';
ENTONCES: 'entonces';
SINO: 'sino';
ESCRIBE: 'escribe';
LEE: 'lee';
REGRESA: 'regresa';
PROGRAMA: 'Programa';
PRINCIPAL: 'principal';
DESDE: 'desde';
HASTA: 'hasta';
HACER: 'hacer';
MIENTRAS: 'mientras';
HAZ: 'haz';

//Tokens
PUNTOYCOMA: ';';
COMA: ',';
DOSPUNTOS: ':';
CORCHETEI: '{';
CORCHETED: '}';
IGUAL: '=';
PARENTESISI: '(';
PARENTESISD: ')';
CORCHETECUADRADOI: '[';
CORCHETECUADRADOD: ']';
MAYOR: '>';
MENOR: '<';
MAYORIGUAL: '>=';
MENORIGUAL: '<=';
IGUALCOMP: '==';
DIFERENTE: '!=';
NEGACION: '!';
SUMA: '+';
RESTA: '-';
MULTIPLICACION: '*';
DIVISION: '/';
Y: '&&';
O: '||';

CTEINT: [0-9]+;
CTEFLOAT: [0-9]+ '.' [0-9]+;
CTESTRING: '"' .*? '"';
CTECHAR: '"."';

ID: [_A-Za-z]([_A-Za-z0-9])*;

// Espacio en blanco y comentarios
COMENTARIO: '/' .? '*/' -> skip;
LINEACOMENTADA: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n\u000C]+ -> skip;

nocondicional : DESDE identificador_accesa {insertIdToStack($identificador_accesa.text)} IGUAL {insertOperator($IGUAL.text)} expresion {leaving('asignacion')} HASTA expresion {forEvaluation()} HACER bloque {addGotoEnd('for')}
              ;

condicional : MIENTRAS {addMigajitaDePan()} PARENTESISI megaexpresion {addGotoF()} PARENTESISD HAZ bloque {addGotoA()} {addGotoEnd('while')}
            ;  

bloque : CORCHETEI (estatuto)+ CORCHETED
       ;      

decision : SI PARENTESISI megaexpresion {addGotoF()} PARENTESISD ENTONCES bloque {addGotoA()} (SINO  bloque)? {addGotoEnd('si')}
         ;     

cargadatos : CARGAARCHIVO PARENTESISI ID COMA (identificador_accesa | cte) COMA (identificador_accesa | cte) COMA (identificador_accesa | cte) PARENTESISD
           ;   

cte : CTESTRING {insertCteToStructs($CTESTRING.text, 'string')} | CTEINT {insertCteToStructs($CTEINT.text, 'int')} | RESTA CTEINT {insertCteToStructs("-" + $CTEINT.text, 'int')} |CTEFLOAT {insertCteToStructs($CTEFLOAT.text, 'float')} | RESTA CTEFLOAT {insertCteToStructs("-" + $CTEFLOAT.text, 'float')} | CTECHAR {insertCteToStructs($CTECHAR.text, 'char')}
    ;

lectura : LEE PARENTESISI ((identificador_accesa {readId($identificador_accesa.text)}) (COMA identificador_accesa {readId($identificador_accesa.text)})*) PARENTESISD
        ;

escritura : ESCRIBE PARENTESISI (identificador_accesa {write($identificador_accesa.text)} | cte {write($cte.text)} | expresion {write(None)}) (COMA (identificador_accesa {write($identificador_accesa.text)} | cte {write($cte.text)} | expresion {write(None)}))* PARENTESISD
          ;

megaexpresion : superexpresion {leaving('union')} ((Y {insertOperator($Y.text)} | O {insertOperator($O.text)}) superexpresion {leaving('union')})*
              ;

superexpresion : expresion {leaving('comparacion')} ((MAYOR {insertOperator($MAYOR.text)} | MENOR {insertOperator($MENOR.text)} | MAYORIGUAL {insertOperator($MAYORIGUAL.text)} | MENORIGUAL {insertOperator($MENORIGUAL.text)} | IGUALCOMP {insertOperator($IGUALCOMP.text)} | DIFERENTE {insertOperator($DIFERENTE.text)}) expresion {leaving('comparacion')})?
               ;

expresion : termino {leaving('termino')} ((SUMA {insertOperator($SUMA.text)} | RESTA {insertOperator($RESTA.text)}) termino {leaving('termino')})* 
          ;

termino : factor {leaving('factor')} ((MULTIPLICACION {insertOperator($MULTIPLICACION.text)} | DIVISION {insertOperator($DIVISION.text)}) factor {leaving('factor')})*
        ;      

factor : identificador_accesa {insertIdToStack($identificador_accesa.text)} | cte | llamadametodo  | PARENTESISI {insertParenthesis()} megaexpresion PARENTESISD {deleteParenthesis()}
       ;       

estatuto : (llamadametodo PUNTOYCOMA | asignacion PUNTOYCOMA | lectura PUNTOYCOMA | escritura PUNTOYCOMA | cargadatos PUNTOYCOMA | decision | condicional | nocondicional | metodo | regresa)
         ;

llamadametodo : ID {validateFunctionExistance($ID.text)} {insertERASize($ID.text)} PARENTESISI {insertParenthesis()} (megaexpresion {incrementReceivedParamCounter()} (COMA megaexpresion {incrementReceivedParamCounter()})*)? {receivedFunctionParameters($ID.text)} PARENTESISD {deleteParenthesis()} {insertGOSUB($ID.text)} 
              ;

regresa : REGRESA PARENTESISI megaexpresion PARENTESISD {generateReturnQuad($megaexpresion.text)} PUNTOYCOMA
        ;

asignacion : identificador_accesa {insertIdToStack($identificador_accesa.text)} IGUAL {insertOperator($IGUAL.text)} megaexpresion {leaving('asignacion')} 
           ;

identificador_accesa : ID (CORCHETECUADRADOI expresion {verify('1', $ID.text)} CORCHETECUADRADOD (CORCHETECUADRADOI expresion {verify('2', $ID.text)} CORCHETECUADRADOD)?)?
                     ;           

identificador_definicion : ID (CORCHETECUADRADOI CTEINT {insertCteToDirectory($CTEINT.text, 'int')} CORCHETECUADRADOD (CORCHETECUADRADOI CTEINT {insertCteToDirectory($CTEINT.text, 'int')} CORCHETECUADRADOD)?)?
                         ;

programa : PROGRAMA identificador_accesa PUNTOYCOMA varx? {addFunctionToDirectory('principal', None)} {includeVarsTableInFunction('principal')} {addGotoPrincipal()} (metodo)* funcp
         ;     

varx : VAR (var (COMA identificador_definicion {addVarToVarsTable(None, $identificador_definicion.text, $var.text)})* PUNTOYCOMA)+
     ;

var : tipo DOSPUNTOS identificador_definicion {addVarToVarsTable($tipo.text, $identificador_definicion.text, None)}
    ;

funcp : PRINCIPAL {setScope($PRINCIPAL.text)} PARENTESISI PARENTESISD bloque
      ;        

tipo : (INT | FLOAT | STRING | CHAR | DATAFRAME)
     ;         

metodo : FUNCION tipo? ID {addFunctionToDirectory($ID.text, $tipo.text)} {setScope($ID.text)} PARENTESISI (var {addVarToFunctionParams($var.text, $ID.text)} (COMA var {addVarToFunctionParams($var.text, $ID.text)})*)?  PARENTESISD PUNTOYCOMA  (varx)? {includeVarsTableInFunction($ID.text)} {rememberBeginingOfFunction($ID.text)} CORCHETEI (estatuto)* regresa? CORCHETED {reachedFunctionDefinitionEnd($ID.text)}
       ;       
