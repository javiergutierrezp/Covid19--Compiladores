SHOW_VIRTUAL = True

INT_SIZE = 2
FLOAT_SIZE = 4
CHAR_SIZE = 1
STRING_SIZE = 6
DATAFRAME_SIZE = 8

from grammar.covid19SemanticCube import semanticCube
from virtualmemory import getCompilationMemory
from utils import VarCount, pq

compilation_memory = getCompilationMemory()

class Quad:
  def __init__(self, operator, left_operand, right_operand, result_id):
    self.operator = operator
    self.left_operand = left_operand
    self.right_operand = right_operand
    self.result_id = result_id

  def __repr__(self):
    return "Quad({}, {}, {}, {})".format(
      self.operator,
      self.left_operand,
      self.right_operand,
      self.result_id,
    )
    
class Variable:
  def __init__(self, name, type, dimensions, memory_cell):
    self.name = name
    self.type = type
    self.dimensions = dimensions
    self.memory_cell = memory_cell

  def __repr__(self):
    return "Variable({}, {}, {}, {})".format(self.name, self.type, self.dimensions, self.memory_cell)

class Constant:
  def __init__(self, value, type, memory_cell):
    self.value = value
    self.type = type
    self.memory_cell = memory_cell
  def __repr__(self):
    return "CTE({} : {}, {})".format(self.type, self.value, self.memory_cell)

class Function:
  def __init__(self, name, var_type, params, first_quad, var_count, vars_table):
    self.name = name
    self.type = var_type
    self.params = params
    self.first_quad = first_quad
    self.var_count = var_count
    self.vars_table = vars_table

  def __repr__(self):
    return "Function({}, {}, {}, {}, {}, {})".format(self.name, self.type, str(self.params), self.first_quad, self.var_count, str(self.vars_table))

function_directory = {}
params_directory = {}
current_scope = ['principal']
var_directory = [{}]
cte_directory = [{}]
virtual_cte_directory = [{}]
quads = []
operators_stack = []
jump_stack = []
ids_stack = []
type_stack = []
jumps_stack = []
operators = ['+','-','*','/', ';'] #TODO: Implementar
received_param_counter = [0]
scope = [None]
semantic_cube = semanticCube()
global_var_counter = [VarCount(0,0,0,0,0)]
local_var_counter = [VarCount(0,0,0,0,0)]
temp_var_counter = [VarCount(0,0,0,0,0)]
cte_var_counter = [VarCount(0,0,0,0,0)]

########## Utils ##########

def getVirtualOperator(operator):
  if SHOW_VIRTUAL:
    return semantic_cube.id_of_oper[operator]
  else:
    return operator

def determineVarCounter(scope):
  final_var_counter = None
  if scope == 'global':
    final_var_counter = global_var_counter
  elif scope == 'local':
    final_var_counter = local_var_counter
  elif scope == 'temporary':
    final_var_counter = temp_var_counter
  elif scope == 'cte':
    final_var_counter = cte_var_counter
  return final_var_counter

def incrementVarCounter(scope, var_type):
  var_counter = determineVarCounter(scope)
  var_counter[0].increment(var_type)

def resetVarCounter(scope):
  if SHOW_VIRTUAL:
    for key in compilation_memory[scope]:
      compilation_memory[scope][key].used_space = 0
  else:
    var_counter = determineVarCounter(scope)
    var_counter[0] = VarCount(0,0,0,0,0)

def addMigajitaDePan():
  jump_stack.append(len(quads))

def getVarCountFromType(scope, var_type):
  final_var_counter = None
  if scope == 'global':
    final_var_counter = global_var_counter[0]
  elif scope == 'local':
    final_var_counter = local_var_counter[0]
  elif scope == 'temporary':
    final_var_counter = temp_var_counter[0]
  elif scope == 'cte':
    final_var_counter = cte_var_counter[0]
  
  if(var_type == "string"):
    return final_var_counter.string_type
  elif(var_type == "int"):
    return final_var_counter.int_type
  elif(var_type == "float"):
    return final_var_counter.float_type
  elif(var_type == "char"):
    return final_var_counter.char_type
  elif(var_type == "Dataframe"):
    return final_var_counter.dataframe_type

def getVirtualMemoryFrom(scope, var_type, param, extra = None):
  final_scope = None
  if scope != 'temporary' and scope != 'cte':
    if scope == 'principal':
      final_scope = 'global'
    else:
      final_scope = 'local'
  else:
    final_scope = scope

  compilation_memory_cell = None
  if not SHOW_VIRTUAL:
    if param == 'temp_num':
      compilation_memory_cell = getVarCountFromType(final_scope, var_type);
    elif param == 'id':
      compilation_memory_cell = extra
  else:
    # print(final_scope, var_type)
    compilation_memory_cell = compilation_memory[final_scope][var_type].incrementUsedSpace()
  # print(compilation_memory_cell)
  return compilation_memory_cell

########## Cuadruplos funciones ##########

def rememberBeginingOfFunction(function_name):
  # print("************** DIMELOOOU **************")
  resetVarCounter('temporary')
  resetVarCounter('local')

  # print(temp_var_counter)
  # print(local_var_counter)
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
  function_directory[function_name].params.append(Variable(var_id, var_type, dimensions, None))

def incrementReceivedParamCounter():
  received_param_counter[0] += 1

def receivedFunctionParameters(function_name):
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
      definition_param_type = function_directory[function_name].params[
        len(function_directory[function_name].params) - 1 - i
      ].type
      given_param_type = type_stack.pop()
      if SHOW_VIRTUAL:
        generateAndAppendQuad(getVirtualOperator('PARAM'), ids_stack.pop(), None, i, False, given_param_type)
      else:
        generateAndAppendQuad(getVirtualOperator('PARAM'), ids_stack.pop(), None, "param{}".format(i + 1), False, given_param_type)
      if definition_param_type != given_param_type:
        raise EnvironmentError("""
          Given argument does not match the 
          parameter types of function '{}' - the argument #{} 
          was expecting type '{}' but received type '{}'
        """.format(
          function_name,
          len(function_directory[function_name].params) - i,
          definition_param_type,
          given_param_type
        ))
  received_param_counter[0] = 0
  

def insertERASize(function_name):
  generateAndAppendQuad(getVirtualOperator("ERA"), function_name, None, None, False, None)

def insertGOSUB(function_name):
  generateAndAppendQuad(getVirtualOperator("GOSUB"), function_name, None, None, False, None)
  # Sólo si la función que estamos llamando regresa algo, hacemos el buen
  # PARCHE GUADALUPANO WUWUWUW
  if function_name in function_directory['principal'].vars_table:
    function_type = function_directory['principal'].vars_table[function_name].type
    generateAndAppendQuad(getVirtualOperator("="), function_name, None, getVirtualMemoryFrom('temporary', function_type, 'temp_num'), True, function_type)

########## Cuadruplos estatutos no lineales ##########

def addGotoF():
  # print(quads)
  exp_type = type_stack.pop()
  if exp_type != 'int':
    raise EnvironmentError("Type missmatch")
  operand = ids_stack.pop()
  generateAndAppendQuad(getVirtualOperator('GOTOF'), operand, None, None, False, None)
  jump_stack.append(len(quads) - 1)

def addGotoA():
  last_goto_index = jump_stack.pop()
  generateAndAppendQuad(getVirtualOperator('GOTO'), None, None, None, False, None)
  jump_stack.append(len(quads) - 1)    
  quads[last_goto_index].result_id = len(quads)

def addGotoPrincipal():
  generateAndAppendQuad(getVirtualOperator('GOTO'), 'principal', None, None, False, None)

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
    generateAndAppendQuad(getVirtualOperator('+'), quads[iterator_index].result_id, getVirtualCte('1'), quads[iterator_index].result_id, False, "int")
    generateAndAppendQuad(getVirtualOperator('GOTO'), None, None, evaluation_index, False, None)
    # Decir que cuando N == M nos salimos del for
    quads[last_goto_index].result_id = len(quads)

def getVirtualCte(cte):
  if SHOW_VIRTUAL:
    return cte_directory[0][cte].memory_cell
  else:
    return 1

def forEvaluation():
  last_quad = quads[len(quads) - 1]
  type_stack.append('int')
  if SHOW_VIRTUAL:
    operators_stack.append(8)
  else:  
    operators_stack.append('==')
  ids_stack.append(last_quad.result_id)
  leaving('comparacion')
  jump_stack.append(len(quads) - 1)
  generateAndAppendQuad(getVirtualOperator('GOTOV'), ids_stack.pop(), None, None, False, None)
  jump_stack.append(len(quads) - 1)
  type_stack.pop()

########## Cuadruplos estatutos lineales ##########

def insertCteToStructs(cte, cte_type):
  type_stack.append(cte_type)
  if cte not in cte_directory[0]: # No existe...
    cte_virtual_memory = getVirtualMemoryFrom('cte', cte_type, 'cte', cte)
    value = cte
    if cte_type == 'int':
      value = int(cte)
    elif cte_type == 'float':
      value = float(cte)
      
    cte_directory[0][str(cte)] = Constant(value, cte_type, cte_virtual_memory)
    virtual_cte_directory[0][cte_virtual_memory] = Constant(value, cte_type, cte_virtual_memory)
  else: # Si existe, ocupamos buscarla...
    cte_virtual_memory = cte_directory[0][cte].memory_cell
  print(cte, cte_virtual_memory)
  
  if SHOW_VIRTUAL:
    ids_stack.append(cte_virtual_memory)
  else:
    ids_stack.append(cte)

def insertIdToStack(identificator):
  # print('insertIdToStack {}'.format(identificator))
  # Busca en donde está esta variable...
  if identificator in function_directory[current_scope[0]].vars_table: # Current scope
    type_stack.append(function_directory[current_scope[0]].vars_table[identificator].type)
    ids_stack.append(function_directory[current_scope[0]].vars_table[identificator].memory_cell)
  elif identificator in function_directory['principal'].vars_table: # Global
    type_stack.append(function_directory['principal'].vars_table[identificator].type)
    # print("************* ")
    # print(function_directory['principal'].vars_table[identificator])
    ids_stack.append(function_directory['principal'].vars_table[identificator].memory_cell)
  else:
    raise EnvironmentError("Hubo un error al intentar utilizar '{}' ¿Tal vez no fue declarado?".format(identificator))
    quit()

def insertOperator(operator):
  if SHOW_VIRTUAL:
    operators_stack.append(semantic_cube.id_of_oper[operator])
  else:
    operators_stack.append(operator)

def deleteParenthesis():
  operators_stack.pop()

def insertParenthesis():
  operators_stack.append('(')

def getAllowedOperators(origin):
  allowed_operators = []
  if SHOW_VIRTUAL:
    if origin == 'factor':
      allowed_operators = [0, 1]
    elif origin == 'termino':
      allowed_operators = [2, 3]
    elif origin == 'comparacion':
      allowed_operators = [6, 5, 9, 10, 8, 7]
    elif origin == 'union':
      allowed_operators = [11, 12]
    elif origin == 'asignacion':
      allowed_operators = [4]
  else:
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
  return allowed_operators

def leaving(origin):
  allowed_operators = getAllowedOperators(origin)
  if len(operators_stack) >= 1 and len(ids_stack) >= 2 and operators_stack[len(operators_stack) - 1] in allowed_operators:
      operator = operators_stack.pop()
      right_operand = ids_stack.pop()
      right_operand_type = type_stack.pop()
      left_operand = ids_stack.pop()
      left_operand_type = type_stack.pop()

      final_operator = operator
      if SHOW_VIRTUAL:
        final_operator = semantic_cube.id_to_oper[operator]

      result_type = semantic_cube.cube[left_operand_type][final_operator][right_operand_type]
      if 'Error:' in result_type:
        raise EnvironmentError(result_type[7:])
      if (origin != 'asignacion'):
        print("{} {} {} = {}".format(left_operand, operator, right_operand, result_type))
        generateAndAppendQuad(operator, left_operand, right_operand, getVirtualMemoryFrom('temporary', result_type, 'temp_num'), True, result_type)
      else:
        generateAndAppendQuad(operator, right_operand, None, left_operand, False, result_type)

def readId(identificator):
  if identificator in function_directory[current_scope[0]].vars_table: #local
    id_type = function_directory[current_scope[0]].vars_table[identificator].type
    generateAndAppendQuad(getVirtualOperator('LEE'), function_directory[current_scope[0]].vars_table[identificator].memory_cell, None, None, False, id_type)
  elif identificator in function_directory['principal'].vars_table: #global
    id_type = function_directory['principal'].vars_table[identificator].type
    generateAndAppendQuad(getVirtualOperator('LEE'), function_directory['principal'].vars_table[identificator].memory_cell, None, None, False, id_type)
  else: #no existe
    raise EnvironmentError("The ID {}, that was intended to be received in 'lee()', was not found. Perhaps it hasn't been declared yet?".format(identificator))


def write(id_or_cte):
  #TODO: Necesitamos traducir estas id's y CTE's a memory cells
  # Determinar si es una variable o un string
  if not id_or_cte: # expresion
    generateAndAppendQuad(getVirtualOperator('ESCRIBE'), ids_stack.pop(), None, None, False, "string")
    type_stack.pop()
  elif id_or_cte[0] == "'" or id_or_cte[0] == '"': # String
    if SHOW_VIRTUAL:
      generateAndAppendQuad(getVirtualOperator('ESCRIBE'), ids_stack.pop() , None, None, False, "string")
    else:
      generateAndAppendQuad(getVirtualOperator('ESCRIBE'), id_or_cte, None, None, False, "string")
    type_stack.pop()
  else:
    if id_or_cte in function_directory[current_scope[0]].vars_table: #local
      generateAndAppendQuad(getVirtualOperator('ESCRIBE'), function_directory[current_scope[0]].vars_table[id_or_cte].memory_cell, None, None, False, "string")
    elif id_or_cte in function_directory['principal'].vars_table: #global
      generateAndAppendQuad(getVirtualOperator('ESCRIBE'), function_directory['principal'].vars_table[id_or_cte].memory_cell, None, None, False, "string")
    else: #no existe
      raise EnvironmentError("The ID {}, that was intended to be written, was not found. Perhaps it hasn't been declared yet?".format(id_or_cte))

def incrementTempCounter(var_type):
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
  megaexpresion_return_type = None
  return_value = None
  if (any(operator in megaexpresion for operator in operators)): # Operation
    return_value = ids_stack.pop()
    megaexpresion_return_type = type_stack.pop()
  elif ('(' in megaexpresion): # Function
    megaexpresion_return_type = type_stack.pop()
    return_value = ids_stack.pop()
  else: # CTE or ID
    megaexpresion_return_type = type_stack.pop()
    return_value = ids_stack.pop()
  if (megaexpresion_return_type == function_directory['principal'].vars_table[current_scope[0]].type):
    final_return = None
    if SHOW_VIRTUAL:
      if type(return_value) == int: #Memory cell return
        print("CTE (Memory cell) return {}".format(return_value))
        final_return = return_value
      else: #id return
        print("ID return {}".format(return_value))
        final_return = function_directory[current_scope[0]].vars_table[return_value].memory_cell
    else:
      final_return = return_value
    generateAndAppendQuad(getVirtualOperator('REGRESA'), current_scope[0], None, final_return, False, megaexpresion_return_type)
  else:
    raise EnvironmentError("""
        The return type the function '{}' expected was '{}' but received '{}'.
      """.format(
        current_scope[0],
        function_directory['principal'].vars_table[current_scope[0]].type,
        megaexpresion_return_type
      ))

def isGoto(operator):
  first_goto = semantic_cube.id_of_oper['GOTO']
  if SHOW_VIRTUAL:
    if type(operator) == int:
      return operator >= first_goto
    else:
      return False
  else:
    return 'GOTO' in operator or 'REGRESA' in operator

def generateAndAppendQuad(operator, left_operand, right_operand, temp_num, append_temp, result_type):
  if isGoto(operator):
    new_quad = Quad(operator, left_operand, right_operand, temp_num)
    quads.append(new_quad)
  else:
    if type(temp_num) == int: # No asignacion
      memory_cell = None
      if SHOW_VIRTUAL:
        memory_cell = temp_num
      else:
        memory_cell = "t{}{}".format(result_type[0], temp_num)
      new_quad = Quad(operator, left_operand, right_operand, memory_cell)
      incrementVarCounter('temporary', result_type)
      if append_temp:
        ids_stack.append(memory_cell)
        type_stack.append(result_type)
    else: # Asignacion
      new_quad = Quad(operator, left_operand, right_operand, temp_num)
    quads.append(new_quad)

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
  if var_id in function_directory: # It's a function's id
      raise EnvironmentError("""
        The id '{}' has already been declared as a function.
      """.format(
        var_id
      ))
  elif not last_var:
    final_type = var_type
  else:
    final_type = last_var[:last_var.find(':')]
  dimensions, id_string = getDimensions(var_id)
  var_directory[0][id_string] = Variable(id_string, final_type, dimensions, getVirtualMemoryFrom(current_scope[0], final_type, 'id', id_string))

def setScope(id):
  current_scope[0] = id
  if id == 'principal':
    function_directory['principal'].first_quad = len(quads)
    resetVarCounter('temporary')
    resetVarCounter('local')

def addFunctionToDirectory(function_id, function_type):
  function_directory[function_id] = Function(function_id, function_type, [], None, None, {})
  if function_type:
    function_directory['principal'].vars_table[function_id] = Variable(function_id, function_type, {}, compilation_memory['global'][function_type].incrementUsedSpace())

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

def getVarCountFromVarsTable(vars_table):
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
  
  return VarCount(
    int_counter,
    float_counter,
    char_counter,
    string_counter,
    dataframe_counter,
  )

def reachedFunctionDefinitionEnd(id):
  # Save ERA Size on function_directory
  function_directory[id].var_count = getVarCountFromVarsTable(function_directory[id].vars_table) + temp_var_counter[0]
  # Release varstable
  function_directory[id].vars_table = {}
  # Generate ENDFUNC quad
  generateAndAppendQuad(getVirtualOperator('ENDFUNC'), None, None, None, False, None)