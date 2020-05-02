function_directory = {}
quads = []
operators_stack = []
ids_stack = []
type_stack = []
jumps_stack = []
operators = ['+','-','*','/', ';'] #TODO: Implementar
temp_number = [0]
scope = [None]

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

def receiveVar(var):
  print(var)

def setScope(s):
  print(s)
  if s != '':
    scope[0] = s
  else:
    scope[0] = None

def insertTypeToStack(type):
  type_stack.append(type)

def insertCteToStack(cte):
  ids_stack.append(cte)

def insertIdToStack(identificator):
  if scope[0]:
    print(function_directory)
    print(function_directory[scope[0]])
    print(function_directory[scope[0]].vars_table)
    print(function_directory[scope[0]].vars_table[identificator])
    print(function_directory[scope[0]].vars_table[identificator].type)
    type_stack.append(function_directory[scope[0]].vars_table[identificator].type)
  else:
    print("probably in principal -> global scope")
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
      left_operand = ids_stack.pop()
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
  print(new_quad)
  if type(temp_num) == int:
    temp_number[0] = temp_num + 1

def getVariable(var):
  name = var.getChild(2).getText()
  var_type = var.getChild(0).getText()
  dimensions = {}
  if name.count('[') == 1:
    dimensions['1'] = int(name[name.find('[') + 1:name.find(']')])
    name = name[:name.find('[')]
  elif name.count('[') == 2:
    dimensions['1'] = int(name[name.find('[') + 1:name.find(']')])
    dimensions['2'] = int(name[name.rfind('[') + 1:name.rfind(']')])
    name = name[:name.find('[')]

  return name, Variable(name, var_type, dimensions)

def extendVarDirectory(directory, varList):
  for i in range(len(varList)):
    name, variable = getVariable(varList[i])
    if name not in directory:
      directory[name] = variable
    else:
      print("La variable '{}' ya fue declarada anteriormente.".format(name))

def getVarDirectory(varList):
  var_directory = {}
  for i in range(len(varList)):
    name, variable = getVariable(varList[i])
    if name not in var_directory:
      var_directory[name] = variable
    else:
      print("La variable '{}' ya fue declarada anteriormente.".format(name))
  return var_directory

################# Cuadruplos #################

megaexpressions = []

def expressionInMegaExpressions(expression):
  ret = False
  for i in range(len(megaexpressions)):
    if expression in megaexpressions[i]:
      ret = True
  megaexpressions.append(expression)
  return ret

# def getRelativeLen(operators_stack):
#   print("getting relative len")
#   count = 0
#   print(operators_stack)
#   print(len(operators_stack) - 1)
#   for i in range(len(operators_stack) - 1, -1, -1):
#     print("inside for...")
#     if operators_stack[i] != '(':
#       count += 1
#     else:
#       break
#   return count


