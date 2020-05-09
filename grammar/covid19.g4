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
Y: '&';
O: '|';

CTEINT: [0-9]+;
CTEFLOAT: [0-9]+ '.' [0-9]+;
CTESTRING: '"' .*? '"';
CTECHAR: '"."';

ID: [_A-Za-z]([_A-Za-z0-9])*;

// Espacio en blanco y comentarios
COMENTARIO: '/' .? '*/' -> skip;
LINEACOMENTADA: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n\u000C]+ -> skip;

nocondicional : DESDE identificador {insertIdToStack($identificador.text)} IGUAL {insertOperator($IGUAL.text)} expresion {leaving('asignacion')} HASTA expresion {forEvaluation()} HACER bloque {addGotoEnd('for')}
              ;

condicional : MIENTRAS {addMigajitaDePan()} PARENTESISI megaexpresion {addGotoF()} PARENTESISD HAZ bloque {addGotoA()} {addGotoEnd('while')}
            ;  

bloque : CORCHETEI (estatuto)+ CORCHETED
       ;      

decision : SI PARENTESISI megaexpresion {addGotoF()} PARENTESISD ENTONCES bloque {addGotoA()} (SINO  bloque)? {addGotoEnd('si')}
         ;     

cargadatos : CARGAARCHIVO PARENTESISI ID COMA (identificador | cte) COMA (identificador | cte) COMA (identificador | cte) PARENTESISD
           ;   

cte : CTESTRING {insertTypeToStack('string')} | CTEINT {insertTypeToStack('int')} | CTEFLOAT {insertTypeToStack('float')} | CTECHAR {insertTypeToStack('char')}
    ;

lectura : LEE PARENTESISI ((identificador {readId($identificador.text)}) (COMA identificador {readId($identificador.text)})*) PARENTESISD
        ;

escritura : ESCRIBE PARENTESISI (identificador {write($identificador.text)} | cte {write($cte.text)} | expresion {writeExpression()}) (COMA (identificador {write($identificador.text)} | cte {write($cte.text)} | expresion {writeExpression()}))* PARENTESISD
          ;

// En escritura estamos aceptando cualquier cte como letrero, atacar con semantica?

megaexpresion : superexpresion {leaving('union')} ((Y {insertOperator($Y.text)} | O {insertOperator($O.text)}) superexpresion {leaving('union')})*
              ;

superexpresion : expresion {leaving('comparacion')} ((MAYOR {insertOperator($MAYOR.text)} | MENOR {insertOperator($MENOR.text)} | MAYORIGUAL {insertOperator($MAYORIGUAL.text)} | MENORIGUAL {insertOperator($MENORIGUAL.text)} | IGUALCOMP {insertOperator($IGUALCOMP.text)} | DIFERENTE {insertOperator($DIFERENTE.text)}) expresion {leaving('comparacion')})?
               ;

expresion : termino {leaving('termino')} ((SUMA {insertOperator($SUMA.text)} | RESTA {insertOperator($RESTA.text)}) termino {leaving('termino')})* 
          ;

termino : factor {leaving('factor')} ((MULTIPLICACION {insertOperator($MULTIPLICACION.text)} | DIVISION {insertOperator($DIVISION.text)}) factor {leaving('factor')})*
        ;      

factor : identificador {insertIdToStack($identificador.text)} | cte {insertCteToStack($cte.text)} | llamadametodo  | PARENTESISI {insertParenthesis()} megaexpresion PARENTESISD {deleteParenthesis()}
       ;       

estatuto : (llamadametodo PUNTOYCOMA? | asignacion PUNTOYCOMA | lectura PUNTOYCOMA | escritura PUNTOYCOMA | cargadatos PUNTOYCOMA | decision | condicional | nocondicional | metodo | regresa)
         ;

llamadametodo : ID {validateFunctionExistance($ID.text)} PARENTESISI (megaexpresion (COMA megaexpresion)*)? {receivedFunctionParameters($ID.text)} PARENTESISD
              ;

regresa : REGRESA PARENTESISI megaexpresion PARENTESISD
        ;

asignacion : identificador {insertIdToStack($identificador.text)} IGUAL {insertOperator($IGUAL.text)} megaexpresion {leaving('asignacion')} 
           ;

identificador : ID (CORCHETECUADRADOI (identificador | cte) CORCHETECUADRADOD (CORCHETECUADRADOI (identificador | cte) CORCHETECUADRADOD)?)?
              ;           

programa : PROGRAMA identificador PUNTOYCOMA varx? {addFunctionToDirectory('principal', None)} {includeVarsTableInFunction('principal')} (metodo)* funcp
         ;     

varx : VAR (var (COMA identificador)* PUNTOYCOMA)+
     ;

var : tipo DOSPUNTOS identificador {addVarToVarsTable($tipo.text, $identificador.text)}
    ;

funcp : PRINCIPAL {setScope($PRINCIPAL.text)} PARENTESISI PARENTESISD bloque
      ;        

tipo : (INT | FLOAT | STRING | CHAR | DATAFRAME)
     ;         

metodo : FUNCION tipo? ID {addFunctionToDirectory($ID.text, $tipo.text)} {setScope($ID.text)} PARENTESISI (var {addVarToFunctionParams($var.text, $ID.text)} (COMA var {addVarToFunctionParams($var.text, $ID.text)})*)? PARENTESISD PUNTOYCOMA  (varx)? {includeVarsTableInFunction($ID.text)} CORCHETEI (estatuto)* regresa? CORCHETED {removeVarsTableInFunction($ID.text)}
       ;       
