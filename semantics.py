function_directory = {}
params_directory = {}
current_scope = ['principal']
var_directory = [{}]
quads = []
operators_stack = []
jump_stack = []
ids_stack = []
type_stack = []
jumps_stack = []
operators = ['+','-','*','/', ';'] #TODO: Implementar
temp_number = [0]
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

class Function:
  def __init__(self, name, var_type, params, vars_table):
    self.name = name
    self.type = var_type
    self.params = params
    self.vars_table = vars_table

  def __repr__(self):
    return "Function({}, {}, {}, {})".format(self.name, self.type, str(self.params), str(self.vars_table))

########## Cuadruplos funciones ##########

def validateFunctionExistance(function_name):
  if function_name not in function_directory:
    raise EnvironmentError("""
          The function '{}' has not been declared.
        """.format(
          function_name,
        ))

def addVarToFunctionParams(var, function_name):
  print(function_directory)
  var_id = var[var.find(':')+1:]
  var_type = var[:var.find(':')]
  dimensions, var_id = getDimensions(var_id)
  function_directory[function_name].params.append(Variable(var_id, var_type, dimensions))

def receivedFunctionParameters(function_name):
  print("receivedFunctionParameters")
  print(function_directory[function_name])
  print(type_stack)
  type_stack_len = len(type_stack)
  ids_stack_len = len(ids_stack)
  for i in range(0, len(function_directory[function_name].params)):
      definition_param = function_directory[function_name].params[
        len(function_directory[function_name].params) - 1 - i
      ]
      given_param_type = type_stack[type_stack_len - 1 - i]
      # print(function_directory['principal'])
      # print(function_directory['principal'].vars_table)
      # print(ids_stack)
      # print(ids_stack[type_stack_len - 1 - i])
      # print(function_directory['principal'].vars_table[ids_stack[ids_stack_len - 1 - i]])
      
      given_param_dimensions = function_directory['principal'].vars_table[ids_stack[ids_stack_len - 1 - i]].dimensions
      print("{} vs {}".format(definition_param.dimensions, given_param_dimensions))

      if definition_param.dimensions != given_param_dimensions:
        raise EnvironmentError("""
          Given argument does not match the 
          parameter dimension of function '{}' - the argument #{} 
          was expecting a variable with '{}' dimension but received one with '{}' dimesions.
        """.format(
          function_name,
          i + 1,
          definition_param.dimesions,
          given_param_dimensions
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

def initializeVarsTable():
  print("test")



########## Cuadruplos estatutos no lineales ##########

def addGotoF():
  # print(quads)
  exp_type = type_stack.pop()
  if exp_type != 'int':
    raise EnvironmentError("Type missmatch")
  operand = ids_stack.pop()
  generateQuad('GOTOF', operand, -1, None, False)
  jump_stack.append(len(quads) - 1)

def addGotoA():
  last_goto_index = jump_stack.pop()
  generateQuad('GOTO', -1, -1, None, False)
  jump_stack.append(len(quads) - 1)    
  quads[last_goto_index].result_id = len(quads)

def addMigajitaDePan():
  jump_stack.append(len(quads))

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
    generateQuad('+', quads[iterator_index].result_id, 1, quads[iterator_index].result_id, False)
    generateQuad('GOTO', -1, -1, evaluation_index, False)
    # Decir que cuando N == M nos salimos del for
    quads[last_goto_index].result_id = len(quads)


def forEvaluation():
  last_quad = quads[len(quads) - 1]
  type_stack.append('int')
  operators_stack.append('==')
  ids_stack.append(last_quad.result_id)
  leaving('comparacion')
  jump_stack.append(len(quads) - 1)
  generateQuad('GOTOV', ids_stack.pop(), -1, None, False)
  jump_stack.append(len(quads) - 1)

########## Cuadruplos estatutos lineales ##########

def insertTypeToStack(t):
  type_stack.append(t)

def insertCteToStack(cte):
  ids_stack.append(cte)

def insertIdToStack(identificator):
  try:
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
        generateQuad(operator, left_operand, right_operand, temp_number[0], True)
        insertTypeToStack(result_type)
      else:
        generateQuad(operator, right_operand, None, left_operand, False)

def readId(identificator):
  generateQuad('lee', identificator, -1, temp_number[0], False)
  type_stack.pop()

def writeExpression():
  write("t{}".format(temp_number[0] - 1))

def write(idOrCte):
  generateQuad('escribe', idOrCte, -1, temp_number[0], False)
  type_stack.pop()

def generateQuad(operator, left_operand, right_operand, temp_num, append_temp):
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

def addVarToVarsTable(type, var_id):
  dimensions, id_string = getDimensions(var_id)
  print("addVarToVarsTable")
  print(dimensions, id_string)
  var_directory[0][id_string] = Variable(id_string, type, dimensions)


def setScope(id):
  current_scope[0] = id

def addFunctionToDirectory(id, type):
  function_directory[id] = Function(id, type, [], {})

def includeVarsTableInFunction(id):
  function_directory[id].vars_table = var_directory[0]
  var_directory[0] = {}

def removeVarsTableInFunction(id):
  function_directory[id].vars_table = {}