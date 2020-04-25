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

quads = []
temp_number = 1
operators_queue = []
ids_queue = []
jumps_queue = []
operators = [] #TODO: Implementar

def higherImportance(operator1, operator2):
  # TODO: Implementar funcion que determina si operator 1 es de
  # mayor importancia que operator 2
  return 0

def appendQuads(expression):
  for i in range(len(expression)):
    left_operand = None
    right_operand = None
    operator = None
    if expression[i] == '(':
      print('parentesisIzq')
    elif expression[i] == ')':
      print('parentesisDer')
    else: # o un operador, o un operando
      if expression[i] in operators: # operador
        if higherImportance(operators_queue[len(operators_queue) - 1], expression[i]):
          # En la pila encontramos a alguien con "mayor importancia" que tú...
          operator = operators_queue.pop()
        else:
          operators_queue.append(expression[i])
      else: # operando
        print("tbd")
  return "tbd"


