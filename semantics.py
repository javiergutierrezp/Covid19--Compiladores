class Variable:
  def __init__(self, name, type):
    self.name = name
    self.type = type

  def __repr__(self):
    return "{}, {}".format(self.name, self.type)

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

def extendVarDirectory(directory, varList):
  for i in range(len(varList)):
    name = varList[i].getChild(2).getText()
    var_type = varList[i].getChild(0).getText()
    if name not in directory:
      directory[name] = Variable(name, var_type)
    else:
      print("intentas declarar la misma variable dos veces!")

def getVarDirectory(varList):
  var_directory = {}
  for i in range(len(varList)):
    name = varList[i].getChild(2).getText()
    var_type = varList[i].getChild(0).getText()
    if name not in var_directory:
      var_directory[name] = Variable(name, var_type)
    else:
      print("intentas declarar la misma variable dos veces!")
  return var_directory

function_directory = {}
