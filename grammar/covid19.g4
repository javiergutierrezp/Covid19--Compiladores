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

nocondicional : DESDE identificador IGUAL expresion HASTA expresion HACER bloque
              ;

condicional : MIENTRAS PARENTESISI megaexpresion PARENTESISD HAZ bloque
            ;  

bloque : CORCHETEI (estatuto)+ CORCHETED
       ;      

decision : SI PARENTESISI megaexpresion PARENTESISD ENTONCES bloque (SINO bloque)?
         ;     

cargadatos : CARGAARCHIVO PARENTESISI ID COMA (identificador | cte) COMA (identificador | cte) COMA (identificador | cte) PARENTESISD
           ;   

cte : CTESTRING | CTEINT | CTEFLOAT | CTECHAR
    ;

lectura : LEE PARENTESISI ((identificador {readId($identificador.text)}) (COMA identificador {readId($identificador.text)})*) PARENTESISD
        ;

escritura : ESCRIBE PARENTESISI (identificador {write($identificador.text)} | cte {write($cte.text)} | expresion {writeExpression()}) (COMA (identificador {write($identificador.text)} | cte {write($cte.text)} | expresion {writeExpression()}))* PARENTESISD
          ;

// En escritura estamos aceptando cualquier cte como letrero, atacar con semantica?

megaexpresion : (superexpresion | Y | O)
              ;

superexpresion : expresion ((MAYOR | MENOR | MAYORIGUAL | MENORIGUAL | IGUALCOMP | DIFERENTE) expresion)?
              ;

expresion : termino {leaving('termino')} ((SUMA {insertOperator($SUMA.text)} | RESTA {insertOperator($RESTA.text)}) termino {leaving('termino')})* 
          ;

termino : factor {leaving('factor')} ((MULTIPLICACION {insertOperator($MULTIPLICACION.text)} | DIVISION {insertOperator($DIVISION.text)}) factor {leaving('factor')})*
        ;      

factor : identificador {insertIdToQueue($identificador.text)} | cte {insertIdToQueue($cte.text)} | llamadametodo  | PARENTESISI {insertParenthesis()} megaexpresion PARENTESISD {deleteParenthesis()}
       ;       

estatuto : (llamadametodo PUNTOYCOMA? | asignacion PUNTOYCOMA | lectura PUNTOYCOMA | escritura PUNTOYCOMA | cargadatos PUNTOYCOMA | decision | condicional | nocondicional | metodo | regresa)
         ;

llamadametodo : ID PARENTESISI megaexpresion (COMA megaexpresion)* PARENTESISD
              ;

regresa : REGRESA PARENTESISI megaexpresion PARENTESISD
        ;

asignacion : identificador IGUAL megaexpresion
           ;

identificador : ID (CORCHETECUADRADOI (identificador | cte) CORCHETECUADRADOD (CORCHETECUADRADOI (identificador | cte) CORCHETECUADRADOD)?)?
              ;           

programa : PROGRAMA identificador PUNTOYCOMA varx? (metodo)* funcp
         ;     

varx : VAR (var (COMA identificador)* PUNTOYCOMA)+
     ;

var : tipo DOSPUNTOS identificador
    ;

funcp : PRINCIPAL PARENTESISI PARENTESISD bloque
      ;        

tipo : (INT | FLOAT | STRING | CHAR | DATAFRAME)
     ;         

metodo : FUNCION tipo? ID PARENTESISI (var (COMA var)*)? PARENTESISD PUNTOYCOMA varx CORCHETEI (estatuto)* regresa? CORCHETED
       ;       
