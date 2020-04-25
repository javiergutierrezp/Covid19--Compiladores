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

function_directory = {}
