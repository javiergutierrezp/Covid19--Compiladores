INT_SIZE = 2
FLOAT_SIZE = 3
CHAR_SIZE = 1
STRING_SIZE = 2
DATAFRAME_SIZE = 4

function_directory = {}
params_directory = {}
current_scope = ['principal']
var_directory = [{}]
cte_directory = [{}]
quads = []
operators_stack = []
jump_stack = []
ids_stack = []
type_stack = []
jumps_stack = []
operators = ['+','-','*','/', ';'] #TODO: Implementar
temp_number = [0]
temp_size = [0]
received_param_counter = [0]
scope = [None]
from grammar.covid19SemanticCube import semanticCube

semantic_cube = semanticCube()

class Quad:
  def __init__(self, operator, operand_left, operand_right, result_id):
    self.operator = operator
    self.operand_left = operand_left
    self.operand_right = operand_right
    self.result_id = result_id

  def __repr__(self):
    return "\nQuad({}, {}, {}, {})".format(
      self.operator,
      self.operand_left,
      self.operand_right,
      self.result_id,
    )

class Variable:
  def __init__(self, name, type, dimensions):
    self.name = name
    self.type = type
    self.dimensions = dimensions

  def __repr__(self):
    return "Variable({}, {}, {})".format(self.name, self.type, self.dimensions)

class Constant:
  def __init__(self, value, type):
    self.value = value
    self.type = type
  def __repr__(self):
    return "CTE({} : {})".format(self.type, self.value)

class Function:
  def __init__(self, name, var_type, params, first_quad, size, vars_table):
    self.name = name
    self.type = var_type
    self.params = params
    self.first_quad = first_quad
    self.size = size
    self.vars_table = vars_table

  def __repr__(self):
    return "Function({}, {}, {}, {}, {}, {})".format(self.name, self.type, str(self.params), self.first_quad, self.size, str(self.vars_table))

########## Utils ##########

def test():
  print("***************")
  print(ids_stack)
  print(type_stack)
  print("***************")

def addMigajitaDePan():
  jump_stack.append(len(quads))

########## Cuadruplos funciones ##########

def rememberBeginingOfFunction(function_name):
  temp_size[0] = 0
  function_directory[function_name].first_quad = len(quads);

def validateFunctionExistance(function_name):
  if function_name not in function_directory:
    raise EnvironmentError("""
          The function '{}' has not been declared.
        """.format(
          function_name,
        ))

def addVarToFunctionParams(var, function_name):
  # print(function_directory)
  var_id = var[var.find(':')+1:]
  var_type = var[:var.find(':')]
  dimensions, var_id = getDimensions(var_id)
  function_directory[function_name].params.append(Variable(var_id, var_type, dimensions))

def incrementReceivedParamCounter():
  received_param_counter[0] += 1

def receivedFunctionParameters(function_name):
  # print("receivedFunctionParameters")
  # print(function_directory[function_name])
  # print(type_stack)
  temp_vars_table = {}
  type_stack_len = len(type_stack)
  ids_stack_len = len(ids_stack)
  if len(function_directory[function_name].params) != received_param_counter[0]:
    raise EnvironmentError("""
      The amount of params received when trying to call
      function '{}' is incorrect. Was expecting {} and received 
      {}.
    """.format(
      function_name,
      len(function_directory[function_name].params),
      received_param_counter[0]
    ))
  for i in range(0, len(function_directory[function_name].params)):
      definition_param = function_directory[function_name].params[
        len(function_directory[function_name].params) - 1 - i
      ]
      given_param_type = type_stack[type_stack_len - 1 - i]

      
      if definition_param.dimensions != {}:
        given_param_dimensions = function_directory['principal'].vars_table[ids_stack[ids_stack_len - 1 - i]].dimensions
        print("{} vs {}".format(definition_param.dimensions, given_param_dimensions))

        if definition_param.dimensions != given_param_dimensions:
          raise EnvironmentError("""
            Given argument does not match the 
            parameter dimension of function '{}' - the argument #{} 
            does not have the same dimensions as the parameter declared
            in the function definition
          """.format(
            function_name,
            i + 1,
          ))

      if definition_param.type != given_param_type:
        raise EnvironmentError("""
          Given argument does not match the 
          parameter types of function '{}' - the argument #{} 
          was expecting type '{}' but received type '{}'
        """.format(
          function_name,
          i + 1,
          definition_param.type,
          given_param_type
        ))
      
      # temp_vars_table[]
  received_param_counter[0] = 0
  # initializeVarsTable();

def insertERASize(function_name):
  generateAndAppendQuad("ERA", function_name, None, None, False, None)

def initializeVarsTable():
  print("test")

def insertGOSUB(function_name):
  generateAndAppendQuad("GOSUB", function_name, None, None, False, None)
  generateAndAppendQuad("=", function_name, None, temp_number[0], True, function_directory['principal'].vars_table[function_name].type)



########## Cuadruplos estatutos no lineales ##########

def addGotoF():
  # print(quads)
  exp_type = type_stack.pop()
  if exp_type != 'int':
    raise EnvironmentError("Type missmatch")
  operand = ids_stack.pop()
  generateAndAppendQuad('GOTOF', operand, -1, None, False, None)
  jump_stack.append(len(quads) - 1)

def addGotoA():
  last_goto_index = jump_stack.pop()
  generateAndAppendQuad('GOTO', -1, -1, None, False, None)
  jump_stack.append(len(quads) - 1)    
  quads[last_goto_index].result_id = len(quads)

def addGotoPrincipal():
  generateAndAppendQuad('GOTO', 'principal', None, None, False, None)

def addGotoEnd(origin):
  # print(jump_stack)
  last_goto_index = jump_stack.pop()
  if origin == 'while':
    quads[last_goto_index].result_id = jump_stack.pop()
  elif origin == 'si':
    quads[last_goto_index].result_id = len(quads)
  elif origin == 'for':
    # Decir que al finalizar el bloque for, re-evaluar la condición
    evaluation_index = jump_stack.pop()
    iterator_index = evaluation_index - 1
    generateAndAppendQuad('+', quads[iterator_index].result_id, 1, quads[iterator_index].result_id, False, "int")
    generateAndAppendQuad('GOTO', -1, -1, evaluation_index, False, None)
    # Decir que cuando N == M nos salimos del for
    quads[last_goto_index].result_id = len(quads)


def forEvaluation():
  last_quad = quads[len(quads) - 1]
  type_stack.append('int')
  operators_stack.append('==')
  ids_stack.append(last_quad.result_id)
  leaving('comparacion')
  jump_stack.append(len(quads) - 1)
  generateAndAppendQuad('GOTOV', ids_stack.pop(), -1, None, False, None)
  jump_stack.append(len(quads) - 1)

########## Cuadruplos estatutos lineales ##########

def insertCteToStructs(cte, cte_type):
  type_stack.append(cte_type)
  if (cte):
    cte_directory[0][str(cte)] = Constant(cte, cte_type)

def insertCteToStack(cte):
  ids_stack.append(cte)

def insertIdToStack(identificator):
  try:
    # print(function_directory)
    if identificator not in function_directory[current_scope[0]].vars_table:
      type_stack.append(function_directory['principal'].vars_table[identificator].type)
    else:
      type_stack.append(function_directory[current_scope[0]].vars_table[identificator].type)
    ids_stack.append(identificator)
  except:
    print("Hubo un error al intentar utilizar '{}' ¿Tal vez no fue declarado?".format(identificator))
    quit()

def insertOperator(operator):
  operators_stack.append(operator)

def deleteParenthesis():
  operators_stack.pop()

def insertParenthesis():
  operators_stack.append('(')

def leaving(origin):
  allowed_operators = None
  if origin == 'factor':
    allowed_operators = ['*', '/']
  elif origin == 'termino':
    allowed_operators = ['+', '-']
  elif origin == 'comparacion':
    allowed_operators = ['>', '<', '>=', '<=', '==', '!=']
  elif origin == 'union':
    allowed_operators = ['&', '|']
  elif origin == 'asignacion':
    allowed_operators = ['=']

  if len(operators_stack) >= 1 and len(ids_stack) >= 2 and operators_stack[len(operators_stack) - 1] in allowed_operators:
      operator = operators_stack.pop()
      right_operand = ids_stack.pop()
      right_operand_type = type_stack.pop()
      left_operand = ids_stack.pop()
      left_operand_type = type_stack.pop()
      print("{} ({}) {} {} ({})".format(
        left_operand,
        left_operand_type,
        operator,
        right_operand,
        right_operand_type,
      ))
      result_type = semantic_cube.cube[left_operand_type][operator][right_operand_type]
      if 'Error:' in result_type:
        raise EnvironmentError(result_type[7:])
      if (origin != 'asignacion'):
        generateAndAppendQuad(operator, left_operand, right_operand, temp_number[0], True, result_type)
        insertCteToStructs(None, result_type)
      else:
        generateAndAppendQuad(operator, right_operand, None, left_operand, False, result_type)

def readId(identificator):
  generateAndAppendQuad('lee', identificator, -1, temp_number[0], False, "string")
  type_stack.pop()

def writeExpression():
  write("t{}".format(temp_number[0] - 1))

def write(idOrCte):
  generateAndAppendQuad('escribe', idOrCte, -1, temp_number[0], False, "string")
  type_stack.pop()

def getSizeOfType(var_type):
  if(var_type == "string"):
    return STRING_SIZE
  elif(var_type == "int"):
    return INT_SIZE
  elif(var_type == "float"):
      return FLOAT_SIZE
  elif(var_type == "char"):
      return CHAR_SIZE
  elif(var_type == "Dataframe"):
      return DATAFRAME_SIZE

def generateReturnQuad(megaexpresion):
  # print(megaexpresion)
  megaexpresion_return_type = None
  return_value = None
  if (any(operator in megaexpresion for operator in operators)): # Operation
    # print("operation found")
    # print(quads)
    # print(ids_stack)
    # print(type_stack)
    return_value = ids_stack[len(ids_stack) - 1]
    megaexpresion_return_type = type_stack[len(type_stack) - 1]
  elif ('(' in megaexpresion): # Function
    called_function = megaexpresion[: megaexpresion.find('(')]
    megaexpresion_return_type = function_directory['principal'].vars_table[called_function].type
    return_value = called_function
  else: # CTE or ID
    # print("cte or id found")
    if (megaexpresion in cte_directory): #cte
      # print("it's a constantttt")
      megaexpresion_return_type = cte_directory[megaexpresion].type
    elif (megaexpresion in function_directory[current_scope[0]].vars_table):
      # print("it's a local id")
      megaexpresion_return_type = function_directory[current_scope[0]].vars_table[megaexpresion].type
    elif (megaexpresion in function_directory['principal'].vars_table):
      # print("it's a global id")
      megaexpresion_return_type = function_directory['principal'].vars_table[megaexpresion].type
    else:
      # print("something's wrong")
      quit()
    # print("assigning...")
    return_value = megaexpresion
  if (megaexpresion_return_type == function_directory['principal'].vars_table[current_scope[0]].type):
    generateAndAppendQuad('RETURN', None, None, return_value, False, megaexpresion_return_type)
  else:
    raise EnvironmentError("""
        The return type the function '{}' expected was '{}' but received '{}'.
      """.format(
        current_scope[0],
        function_directory['principal'].vars_table[current_scope[0]].type,
        megaexpresion_return_type
      ))

def generateAndAppendQuad(operator, left_operand, right_operand, temp_num, append_temp, result_type):
  if 'GOTO' in operator:
    new_quad = Quad(operator, left_operand, right_operand, temp_num)
    quads.append(new_quad)
  else:
    if type(temp_num) == int: # No asignacion
      new_quad = Quad(operator, left_operand, right_operand, "t{}".format(temp_num))
    else: # Asignacion
      new_quad = Quad(operator, left_operand, right_operand, temp_num)
    quads.append(new_quad)
    if append_temp:
      ids_stack.append("t{}".format(temp_num))
    if type(temp_num) == int:
      temp_number[0] = temp_num + 1
      temp_size[0] += getSizeOfType(result_type)


def getDimensions(var_id):
  id_string = str(var_id)
  dimensions = {}
  if id_string.count('[') == 1:
    dimensions['1'] = int(id_string[id_string.find('[') + 1:id_string.find(']')])
    id_string = id_string[:id_string.find('[')]
  elif id_string.count('[') == 2:
    dimensions['1'] = int(id_string[id_string.find('[') + 1:id_string.find(']')])
    dimensions['2'] = int(id_string[id_string.rfind('[') + 1:id_string.rfind(']')])
    id_string = id_string[:id_string.find('[')]
  return dimensions, id_string

def addVarToVarsTable(var_type, var_id, last_var):
  if not last_var:
    final_type = var_type
  else:
    final_type = last_var[:last_var.find(':')]
  dimensions, id_string = getDimensions(var_id)
  var_directory[0][id_string] = Variable(id_string, final_type, dimensions)


def setScope(id):
  current_scope[0] = id

def addFunctionToDirectory(id, type):
  function_directory[id] = Function(id, type, [], None, None, {})
  function_directory['principal'].vars_table[id] = Variable(id, type, {})

def includeVarsTableInFunction(id):
  function_directory[id].vars_table = var_directory[0]
  var_directory[0] = {}

def getCellCount(dimensions):
  cells = 1
  for dimension in dimensions:
    cells *= dimensions[dimension]
  return cells

def getVarCount(dimensions):
  if dimensions == {}:
    return 1
  else:
    return getCellCount(dimensions)

def getSizeFromVarsTable(vars_table):
  int_counter = 0
  float_counter = 0
  char_counter = 0
  string_counter = 0
  dataframe_counter = 0

  for key in vars_table:
    var_type = vars_table[key].type
    var_dimensions = vars_table[key].dimensions
    if var_type == 'int':
      int_counter += getVarCount(var_dimensions)
    elif var_type == 'float':
      float_counter += getVarCount(var_dimensions)
    elif var_type == 'char':
      char_counter += getVarCount(var_dimensions)
    elif var_type == 'string':
      string_counter += getVarCount(var_dimensions)
    elif var_type == 'Dataframe':
      dataframe_counter += 1
  
  return (
    int_counter * INT_SIZE + 
    float_counter * FLOAT_SIZE +
    char_counter * CHAR_SIZE +
    string_counter * STRING_SIZE +
    dataframe_counter * DATAFRAME_SIZE
  )

def reachedFunctionDefinitionEnd(id):
  # Save ERA Size on function_directory
  size = getSizeFromVarsTable(function_directory[id].vars_table)
  size += temp_size[0]
  function_directory[id].size = size
  # Release varstable
  function_directory[id].vars_table = {}
  # Generate ENDFUNC quad
  generateAndAppendQuad('ENDFUNC', None, None, None, False, None)