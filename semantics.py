function_directory = {}
current_scope = ['principal']
var_directory = [{}]
quads = []
operators_stack = []
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
    return "{}, {}, {}, {}".format(
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
    return "{}, {}, {}".format(self.name, self.type, self.dimensions)

class Function:
  def __init__(self, name, type, vars_table):
    self.name = name
    self.type = type
    self.vars_table = vars_table

  def __repr__(self):
    return "{}, {}, {}".format(self.name, self.type, str(self.vars_table))

def insertTypeToStack(t):
  type_stack.append(t)

def insertCteToStack(cte):
  ids_stack.append(cte)

def insertIdToStack(identificator):
  type_stack.append(function_directory[current_scope[0]].vars_table[identificator].type)
  ids_stack.append(identificator)

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
      print(result_type)
      if (origin != 'asignacion'):
        generateQuad(operator, left_operand, right_operand, temp_number[0], True)
      else:
        generateQuad(operator, right_operand, None, left_operand, False)

def readId(identificator):
  generateQuad('lee', identificator, -1, temp_number[0], False)

def writeExpression():
  write("t{}".format(temp_number[0] - 1))

def write(idOrCte):
  generateQuad('escribe', idOrCte, -1, temp_number[0], False)

def generateQuad(operator, left_operand, right_operand, temp_num, append_temp):
  if type(temp_num) == int:
    new_quad = Quad(operator, left_operand, right_operand, "t{}".format(temp_num))
  else: 
    new_quad = Quad(operator, left_operand, right_operand, temp_num)
  quads.append(new_quad)
  if append_temp:
    ids_stack.append("t{}".format(temp_num))
  if type(temp_num) == int:
    temp_number[0] = temp_num + 1

def addVarToVarsTable(type, id):
  print("Adding var...")
  print(id, type)
  name = str(id)
  dimensions = {}
  if name.count('[') == 1:
    dimensions['1'] = int(name[name.find('[') + 1:name.find(']')])
    name = name[:name.find('[')]
  elif name.count('[') == 2:
    dimensions['1'] = int(name[name.find('[') + 1:name.find(']')])
    dimensions['2'] = int(name[name.rfind('[') + 1:name.rfind(']')])
    name = name[:name.find('[')]
  var_directory[0][name] = Variable(name, type, dimensions)
  print(var_directory)

def setScope(id):
  current_scope[0] = id

def addFunctionToDirectory(id, type):
  function_directory[id] = Function(id, type, {})

def includeVarsTableInFunction(id):
  function_directory[id].vars_table = var_directory[0]
  var_directory[0] = {}

################# Cuadruplos #################

megaexpressions = []

def expressionInMegaExpressions(expression):
  ret = False
  for i in range(len(megaexpressions)):
    if expression in megaexpressions[i]:
      ret = True
  megaexpressions.append(expression)
  return ret