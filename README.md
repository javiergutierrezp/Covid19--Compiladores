CVYR
# Lenguaje Covid19--


## Desarrolladores
* Emilio González Guerra          A00817507

* Javier Marcelo Gutiérrez Pérez  A01193217

## Requerimientos
* Python 3.7.2
* Antlr4

## Desarrollo


Para compilar la gramática, correr el siguiente comando:

	$Antlr4 -Dlanguage=Python3 grammar/covid19.g4

Después de haber compilado la gramática, para ejecutar en programa que usa el lenguaje de Covid19--, se corre el siguiente comando:

	$python3 compiler.py <nombre de archivo>

### **Estructura general de un programa:**

	Programa nombrePrograma1;

    	Declaración de variables

    	Declaración de funciones

	 principal() {
    	instrucciones
	 }


#### **Declaración de variables:**

	var
	int : a, b[1], c[1][2];
	float: d, e[], f[][];
	char: g, h[], i[][];
	string: j,kh[], l[][];

#### **Declaración de funciones:**

	funcion int funcion1(tipoParam1: Param1)
		Declaración de variables locales
	{
		estatutos
	}

### **Expresiones:**

Covid19-- implementa los siguientes operadores

	* '+'
	* '-'
	* '*'
	* '/'
	* '='
	* '<'
	* '<='
	* '>'
	* '>='
	* '=='
	* '!='

Para ello necesita *operador izquierdo* y *operador derecho* en todas las expresiones.

### Estatutos:

#### **Asignación:**

	variable1 = cualquierExpresion;
	variable2[variable1] = cualquierExpresion2;
	variable3[0][variable2[variable1]] = cualquierExpresion3;

#### **Llamada a una función:**

##### Si la función no regresa nada:

	nombreDeLaFuncion(paramNecesario1);

##### Si la función si regresa algo, dentro de la declaración, debe de tener una operación:

	regresa(expresionCualquiera);

#### **Lectura:**

##### Recibe valor de teclado y lo guarda en las variables establecidas entre parentesis, deben de ir separadas por una coma.

	lee(var1, var2, var3);

#### **Escritura:**

##### Escribe en consola los valores que recibe, deben de ir separados por comas.

	escribe(“Estoy desplegado en consola.”);

#### **Estatuto de decisión:** 

	si (condición) entonces {
		lo que se debe ejecutar si la condición es cierta
	}
	sino {
		lo que se debe de ejecutar si la condición es falsa
	}

#### **Ciclo condicional:**

	mientras (condición) haz {
		lo que se debe de ejecutar mientras la condición se cumpla
	}

#### **Ciclo no condicional:**

	desde var = x hasta valorFinal hacer {
		lo que se deba de ejecutar mientas var esté dentro del rango
	}
