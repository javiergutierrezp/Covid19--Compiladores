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

nocondicional : DESDE identificador_acceso {insertIdToStack($identificador_acceso.text)} IGUAL {insertOperator($IGUAL.text)} expresion {leaving('asignacion')} HASTA expresion {forEvaluation()} HACER bloque {addGotoEnd('for')}
              ;

condicional : MIENTRAS {addMigajitaDePan()} PARENTESISI megaexpresion {addGotoF()} PARENTESISD HAZ bloque {addGotoA()} {addGotoEnd('while')}
            ;  

bloque : CORCHETEI (estatuto)+ CORCHETED
       ;      

decision : SI PARENTESISI megaexpresion {addGotoF()} PARENTESISD ENTONCES bloque {addGotoA()} (SINO  bloque)? {addGotoEnd('si')}
         ;     

cargadatos : CARGAARCHIVO PARENTESISI ID COMA (identificador_acceso | cte) COMA (identificador_acceso | cte) COMA (identificador_acceso | cte) PARENTESISD
           ;   

cte : CTESTRING {insertCteToStructs($CTESTRING.text, 'string')} | CTEINT {insertCteToStructs($CTEINT.text, 'int')} | CTEFLOAT {insertCteToStructs($CTEFLOAT.text, 'float')} | CTECHAR {insertCteToStructs($CTECHAR.text, 'char')}
    ;

lectura : LEE PARENTESISI ((identificador_acceso {readId($identificador_acceso.text)}) (COMA identificador_acceso {readId($identificador_acceso.text)})*) PARENTESISD
        ;

escritura : ESCRIBE PARENTESISI (identificador_acceso {write($identificador_acceso.text)} | cte {write($cte.text)} | expresion {write(None)}) (COMA (identificador_acceso {write($identificador_acceso.text)} | cte {write($cte.text)} | expresion {write(None)}))* PARENTESISD
          ;

megaexpresion : superexpresion {leaving('union')} ((Y {insertOperator($Y.text)} | O {insertOperator($O.text)}) superexpresion {leaving('union')})*
              ;

superexpresion : expresion {leaving('comparacion')} ((MAYOR {insertOperator($MAYOR.text)} | MENOR {insertOperator($MENOR.text)} | MAYORIGUAL {insertOperator($MAYORIGUAL.text)} | MENORIGUAL {insertOperator($MENORIGUAL.text)} | IGUALCOMP {insertOperator($IGUALCOMP.text)} | DIFERENTE {insertOperator($DIFERENTE.text)}) expresion {leaving('comparacion')})?
               ;

expresion : termino {leaving('termino')} ((SUMA {insertOperator($SUMA.text)} | RESTA {insertOperator($RESTA.text)}) termino {leaving('termino')})* 
          ;

termino : factor {leaving('factor')} ((MULTIPLICACION {insertOperator($MULTIPLICACION.text)} | DIVISION {insertOperator($DIVISION.text)}) factor {leaving('factor')})*
        ;      

factor : identificador_acceso {insertIdToStack($identificador_acceso.text)} | cte | llamadametodo  | PARENTESISI {insertParenthesis()} megaexpresion PARENTESISD {deleteParenthesis()}
       ;       

estatuto : (llamadametodo PUNTOYCOMA | asignacion PUNTOYCOMA | lectura PUNTOYCOMA | escritura PUNTOYCOMA | cargadatos PUNTOYCOMA | decision | condicional | nocondicional | metodo | regresa)
         ;

llamadametodo : ID {validateFunctionExistance($ID.text)} {insertERASize($ID.text)} PARENTESISI {insertParenthesis()} (megaexpresion {incrementReceivedParamCounter()} (COMA megaexpresion {incrementReceivedParamCounter()})*)? {receivedFunctionParameters($ID.text)} PARENTESISD {deleteParenthesis()} {insertGOSUB($ID.text)} 
              ;

regresa : REGRESA PARENTESISI megaexpresion PARENTESISD {generateReturnQuad($megaexpresion.text)} PUNTOYCOMA
        ;

asignacion : identificador_acceso {insertIdToStack($identificador_acceso.text)} IGUAL {insertOperator($IGUAL.text)} megaexpresion {leaving('asignacion')} 
           ;

identificador_acceso : ID (CORCHETECUADRADOI expresion {verify(1)} CORCHETECUADRADOD (CORCHETECUADRADOI expresion {verify(2)} CORCHETECUADRADOD)?)?
              ;

identificador_declaracion : ID (CORCHETECUADRADOI CTEINT {insertCteToCteVirtualMemory($CTEINT.text, 'int')} CORCHETECUADRADOD (CORCHETECUADRADOI CTEINT {insertCteToCteVirtualMemory($CTEINT.text, 'int')} CORCHETECUADRADOD)?)?
              ;

programa : PROGRAMA identificador_acceso PUNTOYCOMA varx? {addFunctionToDirectory('principal', None)} {includeVarsTableInFunction('principal')} {addGotoPrincipal()} (metodo)* funcp
         ;     

varx : VAR (var (COMA identificador_declaracion {addVarToVarsTable(None, $identificador_declaracion.text, $var.text)})* PUNTOYCOMA)+
     ;

var : tipo DOSPUNTOS identificador_declaracion {addVarToVarsTable($tipo.text, $identificador_declaracion.text, None)}
    ;

funcp : PRINCIPAL {setScope($PRINCIPAL.text)} PARENTESISI PARENTESISD bloque
      ;        

tipo : (INT | FLOAT | STRING | CHAR | DATAFRAME)
     ;         

metodo : FUNCION tipo? ID {addFunctionToDirectory($ID.text, $tipo.text)} {setScope($ID.text)} PARENTESISI (var {addVarToFunctionParams($var.text, $ID.text)} (COMA var {addVarToFunctionParams($var.text, $ID.text)})*)?  PARENTESISD PUNTOYCOMA  (varx)? {includeVarsTableInFunction($ID.text)} {rememberBeginingOfFunction($ID.text)} CORCHETEI (estatuto)* regresa? CORCHETED {reachedFunctionDefinitionEnd($ID.text)}
       ;       
