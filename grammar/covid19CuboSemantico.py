class cuboSemantico():
    def __init__(self):
        self.cube = {

            #########################  INT  #############################

            "int": {
                "*" : {
                    "int": "int",
                    "float": "float",
                    "char": "Error: No se puede multiplicar un Int con un Char.",
                    "string": "Error: No se puede multiplicar un Int con un String.",
                    "Dataframe": "No se puede multiplicar un Int con un Dataframe."
                },
                "/" : {
                    "int": "float",
                    "float": "float",
                    "char": "Error: No se puede dividir un Int entre un Char.",
                    "string": "Error: No se puede dividir un Int entre un String.",
                    "Dataframe": "No se puede dividir un Int con un Dataframe."
                },
                "+" : {
                    "int": "int",
                    "float": "float",
                    "char": "Error: No se puede hacer una suma de un Int con un Char.",
                    "string": "Error: No se puede hacer una suma de un Int con un String.",
                    "Dataframe": "No se puede hacer una suma de un Int con un Dataframe."
                },
                "-" : {
                    "int": "int",
                    "float": "float",
                    "char": "Error: No se puede hacer una resta de un Int con un Char.",
                    "string": "Error: No se puede hacer una resta de un Int con un String.",
                    "Dataframe": "No se puede hacer una resta de un Int con un Dataframe."
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
                    "Dataframe": "No se puede comparar un Float con un Dataframe."
                },
                ">=" : {
                    "int": "int",
                    "float": "int",
                    "char": "Error: No se puede comparar un Float con un Char.",
                    "string": "Error: No se puede comparar un Float con un String.",
                    "Dataframe": "No se puede comparar un Float con un Dataframe."
                },
                "<=" : {
                    "int": "int",
                    "float": "int",
                    "char": "Error: No se puede comparar un Float con un Char.",
                    "string": "Error: No se puede comparar un Float con un String.",
                    "Dataframe": "No se puede comparar un Float con un Dataframe."
                },
                "==" : {
                    "int": "int",
                    "float": "int",
                    "char": "Error: No se puede comparar un Float con un Char.",
                    "string": "Error: No se puede comparar un Float con un String.",
                    "Dataframe": "No se puede comparar un Float con un Dataframe."
                },
                "!=" : {
                    "int": "int",
                    "float": "int",
                    "char": "Error: No se puede comparar un Float con un Char.",
                    "string": "Error: No se puede comparar un Float con un String.",
                    "Dataframe": "No se puede comparar un Float con un Dataframe."
                }
            },

              ######################### STRING #############################
        
            "string": {
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
                    "string": "No se puede sumar con un Dataframe.",
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

        self.idOfOper = {
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
            'Goto' : 13,
            'GotoV' : 14,
            'GotoF' : 15
        }