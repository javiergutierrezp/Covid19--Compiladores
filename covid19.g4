grammar covid19;

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

cargadatos : CARGAARCHIVO PARENTESISI ID COMA cte COMA cte COMA cte PARENTESISD
           ;   

cte : CTESTRING | CTEINT | identificador | CTEFLOAT | CTECHAR
    ;

lectura : LEE PARENTESISI ((identificador) (COMA identificador)*) PARENTESISD
        ;

escritura : ESCRIBE PARENTESISI (cte | megaexpresion) (COMA (cte | megaexpresion))* PARENTESISD
          ;

// En escritura estamos aceptando cualquier cte como letrero, atacar con semantica?

megaexpresion : (superexpresion | Y | O)
              ;

superexpresion : expresion ((MAYOR | MENOR | MAYORIGUAL | MENORIGUAL | IGUALCOMP | DIFERENTE) expresion)?
              ;

expresion : termino ((SUMA | RESTA) termino)*
          ;

termino : factor ((MULTIPLICACION | DIVISION) factor)*
        ;      

factor : cte | llamadametodo  | PARENTESISI megaexpresion PARENTESISD 
       ;       

estatuto : (llamadametodo PUNTOYCOMA? | asignacion PUNTOYCOMA | lectura PUNTOYCOMA | escritura PUNTOYCOMA | cargadatos PUNTOYCOMA | decision | condicional | nocondicional | metodo | regresa)
         ;

llamadametodo : ID PARENTESISI megaexpresion (COMA megaexpresion)* PARENTESISD
              ;

regresa : REGRESA PARENTESISI megaexpresion PARENTESISD
        ;

asignacion : identificador IGUAL megaexpresion // (identificador IGUAL)*
           ;

identificador : ID (CORCHETECUADRADOI cte CORCHETECUADRADOD (CORCHETECUADRADOI cte CORCHETECUADRADOD)?)?
              ;           

programa : PROGRAMA identificador PUNTOYCOMA varx (metodo)* funcp
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
