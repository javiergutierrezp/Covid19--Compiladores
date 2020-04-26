function_directory = {}

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

def printDirectory(directory):
  for key in directory:
    print(directory[key])

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

# def getRelativeLen(operators_queue):
#   print("getting relative len")
#   count = 0
#   print(operators_queue)
#   print(len(operators_queue) - 1)
#   for i in range(len(operators_queue) - 1, -1, -1):
#     print("inside for...")
#     if operators_queue[i] != '(':
#       count += 1
#     else:
#       break
#   return count

quads = []
operators_queue = []
ids_queue = []
jumps_queue = []
operators = ['+','-','*','/', ';'] #TODO: Implementar
temp_number = 0
  
def generateQuad(temp_number):
  operator = operators_queue.pop()
  right_operand = ids_queue.pop()
  left_operand = ids_queue.pop()
  temp_number += 1
  ids_queue.append("t{}".format(temp_number))
  quads.append(Quad(operator, left_operand, right_operand, "t{}".format(temp_number)))

def appendQuads(expression):
  # print(expressionInMegaExpressions(expression))
  if not expressionInMegaExpressions(expression):
    expression = expression + ';'
    print(expression)
    variable = ""
    for i in range(len(expression)):
      left_operand = None
      right_operand = None
      operator = None
      if expression[i] == '(':
        operators_queue.append(expression[i])
        ids_queue.append(expression[i])
      elif expression[i] == ')':
        ids_queue.append(variable)
        variable = ""
        generateQuad(temp_number)
      else: # o un operador, o un operando
        if expression[i] in operators: # operador
          ids_queue.append(variable)
          variable = ""
          char = expression[i]
          if expression[i] == ';':
            char = operators_queue[len(operators_queue) - 1]
          print("operators_queue: {}".format(operators_queue))
          print("ids_queue: {}".format(ids_queue))
          print("RelativeLen: {}".format(len(operators_queue)))
          if len(operators_queue) >= 1 and len(ids_queue) >= 2:
            if char in ['*','/']:
              while len(operators_queue) >= 1 and operators_queue[len(operators_queue) - 1] in ['*','/']: # Hay operadores de mayor o igual importancia
                print("inside while...")
                print(operators_queue)
                print(operators_queue[len(operators_queue) - 1])
                print(operators_queue[len(operators_queue) - 1] in ['*','/'])
                # print(operators_queue)
                generateQuad(temp_number)
              # No hay operadores de mayor o igual importancia
              if char != ';':
                operators_queue.append(char)
            elif char in ['-','+']:
              while len(operators_queue) >= 1 and operators_queue[len(operators_queue) - 1] in ['*','/','-','+']: # Hay operadores de mayor o igual importancia
                print("inside while...")
                print(operators_queue)
                generateQuad(temp_number)
              # No hay operadores de mayor o igual importancia
              operators_queue.append(char)
          else:
            operators_queue.append(expression[i])
        else: # operando
          variable += expression[i]
    print("-----------")
    for i in range(len(quads)):
      print(quads[i])
      print("***********")
  return "tbd"


