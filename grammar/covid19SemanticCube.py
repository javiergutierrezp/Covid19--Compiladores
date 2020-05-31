class semanticCube():
    def __init__(self):
        self.cube = {

            #########################  INT  #############################

            "int": {
                "=" : {
                    "int": "int",
                    "float": "Error: No se puede asignar un Float a un Int.",
                    "char": "Error: No se puede asignar un Char a un Int.",
                    "string": "Error: No se puede asignar un String a un Int.",
                    "Dataframe": "Error: No se puede asignar un Dataframe a un Int."
                },
                "*" : {
                    "int": "int",
                    "float": "float",
                    "char": "Error: No se puede multiplicar un Int con un Char.",
                    "string": "Error: No se puede multiplicar un Int con un String.",
                    "Dataframe": "Error: No se puede multiplicar un Int con un Dataframe."
                },
                "/" : {
                    "int": "float",
                    "float": "float",
                    "char": "Error: No se puede dividir un Int entre un Char.",
                    "string": "Error: No se puede dividir un Int entre un String.",
                    "Dataframe": "Error: No se puede dividir un Int con un Dataframe."
                },
                "+" : {
                    "int": "int",
                    "float": "float",
                    "char": "Error: No se puede hacer una suma de un Int con un Char.",
                    "string": "Error: No se puede hacer una suma de un Int con un String.",
                    "Dataframe": "Error: No se puede hacer una suma de un Int con un Dataframe."
                },
                "-" : {
                    "int": "int",
                    "float": "float",
                    "char": "Error: No se puede hacer una resta de un Int con un Char.",
                    "string": "Error: No se puede hacer una resta de un Int con un String.",
                    "Dataframe": "Error: No se puede hacer una resta de un Int con un Dataframe."
                },
                "<" : {
                    "int": "int",
                    "float": "int",
                    "char": "Error: No se puede comparar un Int con un Char.",
                    "string": "Error: No se puede comparar un Int con un String.",
                    "Dataframe": "Error: No se puede comparar un Int con un Dataframe."
                },
                ">" : {
                    "int": "int",
                    "float": "int",
                    "char": "Error: No se puede comparar un Int con un Char.",
                    "string": "Error: No se puede comparar un Int con un String.",
                    "Dataframe": "Error: No se puede comparar un Int con un Dataframe."
                },
                ">=" : {
                    "int": "int",
                    "float": "int",
                    "char": "Error: No se puede comparar un Int con un Char.",
                    "string": "Error: No se puede comparar un Int con un String.",
                    "Dataframe": "Error: No se puede comparar un Int con un Dataframe."
                },
                "<=" : {
                    "int": "int",
                    "float": "int",
                    "char": "Error: No se puede comparar un Int con un Char.",
                    "string": "Error: No se puede comparar un Int con un String.",
                    "Dataframe": "Error: No se puede comparar un Int con un Dataframe."
                },
                "==" : {
                    "int": "int",
                    "float": "int",
                    "char": "Error: No se puede comparar un Int con un Char.",
                    "string": "Error: No se puede comparar un Int con un String.",
                    "Dataframe": "Error: No se puede comparar un Int con un Dataframe."
                },
                "!=" : {
                    "int": "int",
                    "float": "int",
                    "char": "Error: No se puede comparar un Int con un Char.",
                    "string": "Error: No se puede comparar un Int con un String.",
                    "Dataframe": "Error: No se puede comparar un Int con un Dataframe."
                }
            },
            ######################### FLOAT #############################
            "float" : {
                "=" : {
                    "int": "Error: No se puede asignar un Int a un Float.",
                    "float": "float",
                    "char": "Error: No se puede asignar un Char a un Float.",
                    "string": "Error: No se puede asignar un String a un Float.",
                    "Dataframe": "Error: No se puede asignar un Dataframe a un Float."
                },
                "*" : {
                    "int": "float",
                    "float": "float",
                    "char": "Error: No se puede multiplicar un Float con un Char.",
                    "string": "Error: No se puede multiplicar un Float con un String.",
                    "Dataframe": "Error: No se puede multiplicar un Float con un Dataframe."
                },
                "/" : {
                    "int": "float",
                    "float": "float",
                    "char": "Error: No se puede dividir un Float entre un Char.",
                    "string": "Error: No se puede dividir un Float entre un String.",
                    "Dataframe": "Error: No se puede dividir un Float con un Dataframe."
                },
                "+" : {
                    "int": "float",
                    "float": "float",
                    "char": "Error: No se puede sumar un Float con un Char.",
                    "string": "Error: No se puede sumar un Float con un String.",
                    "Dataframe": "Error: No se puede sumar un Float con un Dataframe."
                },
                "-" : {
                    "int": "float",
                    "float": "float",
                    "char": "Error: No se puede restar un Float con un Char.",
                    "string": "Error: No se puede restar un Float con un String.",
                    "Dataframe": "Error: No se puede restar un Float con un Dataframe."
                },
                "<" : {
                    "int": "int",
                    "float": "int",
                    "char": "Error: No se puede comparar un Float con un Char.",
                    "string": "Error: No se puede comparar un Float con un String.",
                    "Dataframe": "Error: No se puede comparar un Float con un Dataframe."
                },
                ">" : {
                    "int": "int",
                    "float": "int",
                    "char": "Error: No se puede comparar un Float con un Char.",
                    "string": "Error: No se puede comparar un Float con un String.",
                    "Dataframe": "Error: No se puede comparar un Float con un Dataframe."
                },
                ">=" : {
                    "int": "int",
                    "float": "int",
                    "char": "Error: No se puede comparar un Float con un Char.",
                    "string": "Error: No se puede comparar un Float con un String.",
                    "Dataframe": "Error: No se puede comparar un Float con un Dataframe."
                },
                "<=" : {
                    "int": "int",
                    "float": "int",
                    "char": "Error: No se puede comparar un Float con un Char.",
                    "string": "Error: No se puede comparar un Float con un String.",
                    "Dataframe": "Error: No se puede comparar un Float con un Dataframe."
                },
                "==" : {
                    "int": "int",
                    "float": "int",
                    "char": "Error: No se puede comparar un Float con un Char.",
                    "string": "Error: No se puede comparar un Float con un String.",
                    "Dataframe": "Error: No se puede comparar un Float con un Dataframe."
                },
                "!=" : {
                    "int": "int",
                    "float": "int",
                    "char": "Error: No se puede comparar un Float con un Char.",
                    "string": "Error: No se puede comparar un Float con un String.",
                    "Dataframe": "Error: No se puede comparar un Float con un Dataframe."
                }
            },

              ######################### STRING #############################
        
            "string": {
                "=" : {
                    "int": "Error: No se puede asignar un Int a un String.",
                    "float": "Error: No se puede asignar un Float a un String.",
                    "char": "Error: No se puede asignar un Char a un String.",
                    "string": "string",
                    "Dataframe": "Error: No se puede asignar un Dataframe a un String."
                },
                "*" : {
                    "int": "Error: No se puede multiplicar con un String.",
                    "float": "Error: No se puede multiplicar con un String.",
                    "char": "Error: No se puede multiplicar con un String.",
                    "string": "Error: No se puede multiplicar con un String.",
                    "Dataframe": "Error: No se puede multiplicar con un String."
                },
                "/" : {
                    "int": "Error: No se puede dividir con un String.",
                    "float": "Error: No se puede dividir con un String.",
                    "char": "Error: No se puede dividir con un String.",
                    "string": "Error: No se puede dividir con un String.",
                    "Dataframe": "Error: No se puede dividir con un String."
                },
                "+" : {
                    "int": "Error: No se puede sumar con un String.",
                    "float": "Error: No se puede sumar con un String.",
                    "char": "Error: No se puede sumar con un String.",
                    "string": "string",
                    "Dataframe": "Error: No se puede sumar con un String."
                },
                "-" : {
                    "int": "Error: No se puede restar con un String.",
                    "float": "Error: No se puede restar con un String.",
                    "char": "Error: No se puede restar con un String.",
                    "string": "Error: No se puede restar con un String.",
                    "Dataframe": "Error: No se puede restar con un String."
                },
                "<" : {
                    "int": "Error: No se puede comparar un String con un <.",
                    "float": "Error: No se puede comparar un String con un <.",
                    "char": "Error: No se puede comparar un String con un <.",
                    "string": "Error: No se puede comparar un String con un <.",
                    "Dataframe": "Error: No se puede comparar un String con un <."
                },
                ">" : {
                    "int": "Error: No se puede comparar un String con un >.",
                    "float": "Error: No se puede comparar un String con un >.",
                    "char": "Error: No se puede comparar un String con un >.",
                    "string": "Error: No se puede comparar un String con un >.",
                    "Dataframe": "Error: No se puede comparar un String con un >."
                },
                ">=" : {
                    "int": "Error: No se puede comparar un String con un >=.",
                    "float": "Error: No se puede comparar un String con un >=.",
                    "char": "Error: No se puede comparar un String con un >=.",
                    "string": "Error: No se puede comparar un String con un >=.",
                    "Dataframe": "Error: No se puede comparar un String con un >=."
                },
                "<=" : {
                    "int": "Error: No se puede comparar un String con un <=.",
                    "float": "Error: No se puede comparar un String con un <=.",
                    "char": "Error: No se puede comparar un String con un <=.",
                    "string": "Error: No se puede comparar un String con un <=.",
                    "Dataframe": "Error: No se puede comparar un String con un <=."
                },
                "==" : {
                    "int": "Error: No se puede comparar en String con un Int.",
                    "float": "Error: No se puede comparar en String con un Float.",
                    "char": "Error: No se puede comparar en String con un Char.",
                    "string": "int",
                    "Dataframe": "Error: No se puede comparar un String con un Dataframe."
                },
                "!=" : {
                    "int": "Error: No se puede comparar en String con un Int.",
                    "float": "Error: No se puede comparar en String con un Float.",
                    "char": "Error: No se puede comparar en String con un Char.",
                    "string": "int",
                    "Dataframe": "Error: No se puede comparar un String con un Dataframe."
                }
            },

                ######################### CHAR #############################
            "char": {
                "=" : {
                    "int": "Error: No se puede asignar un Int a un Char.",
                    "float": "Error: No se puede asignar un Float a un Char.",
                    "char": "char",
                    "string": "Error: No se puede asignar un String a un Char.",
                    "Dataframe": "Error: No se puede asignar un Dataframe a un Char."
                },
                "*" : {
                    "int": "Error: No se puede multiplicar con un Char.",
                    "float": "Error: No se puede multiplicar con un Char.",
                    "char": "Error: No se puede multiplicar con un Char.",
                    "string": "Error: No se puede multiplicar con un Char.",
                    "Dataframe": "Error: No se puede multiplicar con un Char."
                },
                "/" : {
                    "int": "Error: No se puede dividir con un Char.",
                    "float": "Error: No se puede dividir con un Char.",
                    "char": "Error: No se puede dividir con un Char.",
                    "string": "Error: No se puede dividir con un Char.",
                    "Dataframe": "Error: No se puede dividir con un Char."
                },
                "+" : {
                    "int": "Error: No se puede sumar con un Char.",
                    "float": "Error: No se puede sumar con un Char.",
                    "char": "string",
                    "string": "string",
                    "Dataframe": "Error: No se puede sumar con un Char."
                },
                "-" : {
                    "int": "Error: No se puede restar con un Char.",
                    "float": "Error: No se puede restar con un Char.",
                    "char": "Error: No se puede restar con un Char.",
                    "string": "Error: No se puede restar con un Char.",
                    "Dataframe": "Error: No se puede restar con un Char."
                },
                "<" : {
                    "int": "Error: No se puede comparar un Char con un <.",
                    "float": "Error: No se puede comparar un Char con un <.",
                    "char": "Error: No se puede comparar un Char con un <.",
                    "string": "Error: No se puede comparar un Char con un <.",
                    "Dataframe": "Error: No se puede comparar un Char con un <."
                },
                ">" : {
                    "int": "Error: No se puede comparar un Char con un >.",
                    "float": "Error: No se puede comparar un Char con un >.",
                    "char": "Error: No se puede comparar un Char con un >.",
                    "string": "Error: No se puede comparar un Char con un >.",
                    "Dataframe": "Error: No se puede comparar un Char con un >."
                },
                ">=" : {
                    "int": "Error: No se puede comparar un Char con un >=.",
                    "float": "Error: No se puede comparar un Char con un >=.",
                    "char": "Error: No se puede comparar un Char con un >=.",
                    "string": "Error: No se puede comparar un Char con un >=.",
                    "Dataframe": "Error: No se puede comparar un Char con un >=."
                },
                "<=" : {
                    "int": "Error: No se puede comparar un Char con un <=.",
                    "float": "Error: No se puede comparar un Char con un <=.",
                    "char": "Error: No se puede comparar un Char con un <=.",
                    "string": "Error: No se puede comparar un Char con un <=.",
                    "Dataframe": "Error: No se puede comparar un Char con un <=."
                },
                "==" : {
                    "int": "Error: No se puede comparar en Char con un Int.",
                    "float": "Error: No se puede comparar en Char con un Float.",
                    "char": "int",
                    "string": "Error: No se puede comparar en Char con un String.",
                    "Dataframe": "Error: No se puede comparar en Char con un Dataframe."
                },
                "!=" : {
                    "int": "Error: No se puede comparar en Char con un Int.",
                    "float": "Error: No se puede comparar en Char con un Float.",
                    "char": "int",
                    "string": "Error: No se puede comparar en Char con un String.",
                    "Dataframe": "Error: No se puede comparar en Char con un Dataframe."
                }
            },

                ######################### DATAFRAME #############################

            "Dataframe": {
                "=" : {
                    "int": "Error: No se puede asignar un Int a un Dataframe.",
                    "float": "Error: No se puede asignar un Float a un Dataframe.",
                    "char": "Error: No se puede asignar un Char a un Dataframe.",
                    "string": "Error: No se puede asignar un String a un Dataframe.",
                    "Dataframe": "Dataframe"
                },
                "*" : {     
                    "int": "Error: No se puede multiplicar con un Dataframe.",
                    "float": "Error: No se puede multiplicar con un Dataframe.",
                    "char": "Error: No se puede multiplicar con un Dataframe.",
                    "string": "Error: No se puede multiplicar con un Dataframe.",
                    "Dataframe": "Error: No se puede multiplicar con un Dataframe."
                },
                "/" : {
                    "int": "Error: No se puede dividir con un Dataframe.",
                    "float": "Error: No se puede dividir con un Dataframe.",
                    "char": "Error: No se puede dividir con un Dataframe.",
                    "string": "Error: No se puede dividir con un Dataframe.",
                    "Dataframe": "Error: No se puede dividir con un Dataframe."
                },
                "+" : {
                    "int": "Error: No se puede sumar con un Dataframe.",
                    "float": "Error: No se puede sumar con un Dataframe.",
                    "char": "Error: No se puede sumar con un Dataframe.",
                    "string": "Error: No se puede sumar con un Dataframe.",
                    "Dataframe": "Error: No se puede sumar con un Dataframe."
                },
                "-" : {
                    "int": "Error: No se puede restar con un Dataframe.",
                    "float": "Error: No se puede restar con un Dataframe.",
                    "char": "Error: No se puede restar con un Dataframe.",
                    "string": "Error: No se puede restar con un Dataframe.",
                    "Dataframe": "Error: No se puede restar con un Dataframe."
                },
                "<" : {
                    "int": "Error: No se puede comparar un Dataframe con un <.",
                    "float": "Error: No se puede comparar un Dataframe con un <.",
                    "char": "Error: No se puede comparar un Dataframe con un <.",
                    "string": "Error: No se puede comparar un Dataframe con un <.",
                    "Dataframe": "Error: No se puede comparar un Dataframe con un <."
                },
                ">" : {
                    "int": "Error: No se puede comparar un Dataframe con un >.",
                    "float": "Error: No se puede comparar un Dataframe con un >.",
                    "char": "Error: No se puede comparar un Dataframe con un >.",
                    "string": "Error: No se puede comparar un Dataframe con un >.",
                    "Dataframe": "Error: No se puede comparar un Dataframe con un >."
                },
                ">=" : {
                    "int": "Error: No se puede comparar un Dataframe con un >=.",
                    "float": "Error: No se puede comparar un Dataframe con un >=.",
                    "char": "Error: No se puede comparar un Dataframe con un >=.",
                    "string": "Error: No se puede comparar un Dataframe con un >=.",
                    "Dataframe": "Error: No se puede comparar un Dataframe con un >=."
                },
                "<=" : {
                    "int": "Error: No se puede comparar un Dataframe con un <=.",
                    "float": "Error: No se puede comparar un Dataframe con un <=.",
                    "char": "Error: No se puede comparar un Dataframe con un <=.",
                    "string": "Error: No se puede comparar un Dataframe con un <=.",
                    "Dataframe": "Error: No se puede comparar un Dataframe con un <=."
                },
                "==" : {
                    "int": "Error: No se puede comparar en Dataframe con un Int.",
                    "float": "Error: No se puede comparar en Dataframe con un Float.",
                    "char": "Error: No se puede comparar en Dataframe con un Char.",
                    "string": "Error: No se puede comparar en Dataframe con un String.",
                    "Dataframe": "Error: No se puede comparar en Dataframe con un Dataframe."
                },
                "!=" : {
                    "int": "Error: No se puede comparar en Dataframe con un Int.",
                    "float": "Error: No se puede comparar en Dataframe con un Float.",
                    "char": "Error: No se puede comparar en Dataframe con un Char.",
                    "string": "Error: No se puede comparar en Dataframe con un String.",
                    "Dataframe": "Error: No se puede comparar en Dataframe con un Dataframe."
                }
            }
        }

        self.id_to_oper = {
            0 : '*',
            1 : '/',
            2 : '+',
            3 : '-',
            4 : '=',
            5 : '<',
            6 : '>',
            7 : '!=',
            8 : '==',
            9 : '>=',
            10 : '<=',
            11 : 'AND',
            12 : 'OR',
            13 : 'Goto',
            14 : 'GotoV',
            15 : 'GotoF',
            16 : 'GOSUB',
            17 : 'ERA',
            18 : 'ENDFUNC',
            19 : 'LEE',
            20 : 'ESCRIBE',
            21 : 'REGRESA',
            22 : 'PARAM'
        }

        self.id_of_oper = {
            '*' : 0,
            '/' : 1,
            '+' : 2,
            '-' : 3,
            '=' : 4,
            '<' : 5,
            '>' : 6,
            '!=' : 7,
            '==' : 8,
            '>=' : 9,
            '<=' : 10,
            'AND' : 11,
            'OR' : 12,
            'GOTO' : 13,
            'GOTOV' : 14,
            'GOTOF' : 15,
            'GOSUB' : 16,
            'ERA' : 17,
            'ENDFUNC' : 18,
            'LEE' : 19,
            'ESCRIBE' : 20,
            'REGRESA' : 21,
            'PARAM' : 22
        }