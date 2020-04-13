import ply.lex as lex

claves = {
    'int':'INT',
    'float':'FLOAT',
    'var':'VAR',
    'if':'IF',
    'else':'ELSE',
    'print':'PRINT',
    'program':'PROGRAM'
}

tokens = [
    'PUNTOYCOMA', 'COMA', 'DOSPUNTOS', 
    'CORCHETEI', 'CORCHETED', 'IGUAL', 'CTESTRING',
    'PARENTESISI', 'PARENTESISD', 
    'MAYOR', 'MENOR', 'DIFERENTE',
    'SUMA', 'RESTA', 'MULTIPLICACION', 'DIVISION', 
    'ID', 'CTEINT', 'CTEFLOAT'
] + list(claves.values())

# Tokens
t_PUNTOYCOMA    = r';'
t_COMA        = r','
t_DOSPUNTOS        = r':'
t_CORCHETEI = r'{'
t_CORCHETED = r'}'
t_IGUAL    = r'='
t_CTESTRING = r'\".*\"'
t_PARENTESISI    = r'\('
t_PARENTESISD   = r'\)'
t_MAYOR   = r'>'
t_MENOR      = r'<'
t_DIFERENTE  = r'<>'
t_SUMA    = r'\+'
t_RESTA   = r'-'
t_MULTIPLICACION   = r'\*'
t_DIVISION  = r'/'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = claves.get(t.value,'ID')
    return t

def t_CTEINT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_CTEFLOAT(t):
    r'([0-9]+[.])[0-9]+'
    t.value = float(t.value)
    return t


t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Char ilegal '{}' en: {}".format(t.value[0], t.lexer.lineno))
    t.lexer.skip(1)


lex.lex()