
class VarCount:
  def __init__(self, int_type=0, float_type=0, char_type=0, string_type=0, dataframe_type=0):
    self.int_type = int_type
    self.float_type = float_type
    self.char_type = char_type
    self.string_type = string_type
    self.dataframe_type = dataframe_type
  
  def increment(self, var_type):
    if(var_type == "string"):
      self.string_type += 1
    elif(var_type == "int"):
      self.int_type += 1
    elif(var_type == "float"):
      self.float_type += 1
    elif(var_type == "char"):
      self.char_type += 1
    elif(var_type == "Dataframe"):
      self.dataframe_type += 1
  
  def __add__(self, var_counter): 
      string_type = self.string_type + var_counter.string_type
      int_type = self.int_type + var_counter.int_type
      float_type = self.float_type + var_counter.float_type
      char_type = self.char_type + var_counter.char_type
      dataframe_type = self.dataframe_type + var_counter.dataframe_type
      return VarCount(int_type, float_type, char_type, string_type, dataframe_type)

  def __repr__(self):
    return "VarCount({}, {}, {}, {}, {})".format(
      self.int_type,
      self.float_type,
      self.char_type,
      self.string_type,
      self.dataframe_type,
    )

def printQuads(quads):
  for (idx, quad) in enumerate(quads):
      print("{} - {}".format(idx, quad))