# from semantics import *

class CompilationMemorySegment():
    def __init__(self, beginning, size, used_space = 0):
        self.beginning = int(beginning)
        self.size = int(size)
        self.used_space = int(used_space)

    def incrementUsedSpace(self):
        current_memory_cell = self.beginning + self.used_space
        self.used_space += 1
        return current_memory_cell

    def __repr__(self):
        return "CompilationMemorySegment({}, {}, {})".format(
        self.beginning,
        self.size,
        self.used_space,
        )

class RuntimeMemorySegment():
    def __init__(self, var_count):
        self.int_space = [None] * var_count.int_type
        self.float_space = [None] * var_count.float_type
        self.char_space = [None] * var_count.char_type
        self.string_space = [None] * var_count.string_type
        self.dataframe_space = [None] * var_count.dataframe_type
    
    def set(self, value, runtime_memory_index, variable_type):
        if variable_type == 'int':
            self.int_space[runtime_memory_index] = value
        elif variable_type == 'float':
            self.float_space[runtime_memory_index] = value
        elif variable_type == 'char':
            self.char_space[runtime_memory_index] = value
        elif variable_type == 'string':
            self.string_space[runtime_memory_index] = value
        elif variable_type == 'Dataframe':
            self.dataframe_space[runtime_memory_index] = value

class VirtualMachine():
    def __init__(self, quads, cte_directory, functions_directory):
        self.quads = quads
        self.cte_directory = cte_directory
        self.functions_directory = functions_directory
        
        # Global memory se inicializa con "todo el espacio que tenemos para globales"
        self.global_memory = RuntimeMemorySegment(VarCount(
            compilation_memory['global']['int'].size,
            compilation_memory['global']['float'].size,
            compilation_memory['global']['char'].size,
            compilation_memory['global']['string'].size,
            compilation_memory['global']['Dataframe'].size))

        # Temporary memory inicia con "todo el espacio que tenemos para temporales"
        # Cuando vamos a llamar a una función, se instancia con un espacio limitado dependiendo de ERA
        # Cuando salimos de una función, la igualamos a "todo el espacio que tenemos para temporales"
        self.temporary_memory = RuntimeMemorySegment(VarCount(
            compilation_memory['temporary']['int'].size,
            compilation_memory['temporary']['float'].size,
            compilation_memory['temporary']['char'].size,
            compilation_memory['temporary']['string'].size,
            compilation_memory['temporary']['Dataframe'].size))

        # Local memory inicia como un arreglo vacio
        # Cada que entramos a una función, agregamos una instancia de RuntimeMemorySegment
        # En el inter, cada cosa que ocupe memoria "local" irá al último elemento del arreglo de locales
        # Cada que salimos de una función, sacamos el último RuntimeMemorySegment del arreglo
        self.local_memory = []

    def getCte(self, virtual_memory):
        if virtual_memory in self.cte_directory:
            return self.cte_directory[virtual_memory].value
        else:
            return None
    
    def setMemorySegmentValue(self, scope, value, runtime_memory_index, variable_type):
        if scope == 'global':
            self.global_memory.set(value, runtime_memory_index, variable_type)
        elif scope == 'local':
            self.local_memory[len(self.local_memory) - 1].set(value, runtime_memory_index, variable_type)
        elif scope == 'temporary':
            self.temporary_memory.set(value, runtime_memory_index, variable_type)
    
    def getValueOfOperand(self, virtual_memory):
        runtime_memory_index, variable_type, scope = interpretVirtualMemory(virtual_memory)
        return accessMemory(scope, runtime_memory_index, variable_type)
    
    def accessMemory(self, scope, runtime_index, var_type):
        # Accesar memoria...
        print("not defined yet")
        return 0


    def execute(self):
        # Iterar por los quads
        instruction_pointer = 0
        current_quad = None
        while instruction_pointer < len(quads) - 1:
            # Leer quad
            current_quad = self.quads[instruction_pointer]

            left_operand = self.getValueOfOperand(current_quad.left_operand)
            right_operand = self.getValueOfOperand(current_quad.right_operand)

            if current_quad.operator == 0:  # *
                print("found a *")
                self.setMemorySegmentValue()
            elif current_quad.operator == 1:  # /
                print("found a /")
            elif current_quad.operator == 2:  # +
                print("found a +")
            elif current_quad.operator == 3:  # -
                print("found a -")
            elif current_quad.operator == 4:  # =
                print("found a =")
            elif current_quad.operator == 5:  # <
                print("found a <")
            elif current_quad.operator == 6:  # >
                print("found a >")
            elif current_quad.operator == 7:  # !=
                print("found a !=")
            elif current_quad.operator == 8:  # ==
                print("found a ==")
            elif current_quad.operator == 9:  # >=
                print("found a >=")
            elif current_quad.operator == 10: # <=
                print("found a <=")
            elif current_quad.operator == 11: # AND
                print("found a AND")
            elif current_quad.operator == 12: # OR
                print("found a OR")
            elif current_quad.operator == 13: # Goto
                print("found a Goto")
            elif current_quad.operator == 14: # GotoV
                print("found a GotoV")
            elif current_quad.operator == 15: # GotoF
                print("found a GotoF")
        return 0;
# Determinar que operacion es
# Dependiendo de la operacion, lo que hacemos...

def interpretVirtualMemory(virtual_memory):
    runtime_memory_index = None
    variable_type = None
    scope = None

    return runtime_memory_index, variable_type, scope

# * global (donde estamos por default) -> Con toño
# * stack de memorias? para siempre utilizar la final...
# * local (para funciones) -> ERA
# * cte (en todas partes...) -> Expandirla dependiendo de ERA
# * temporal (en todas partes...) -> Inicializarla desde el inicio

def getScopeMemory(base, total_space):
    floor = base
    scope_memory = {}
    ceil = total_space * .3
    scope_memory['int'] = CompilationMemorySegment(floor, ceil, 0)

    floor += ceil
    ceil = total_space * .3
    scope_memory['float'] = CompilationMemorySegment(floor, ceil, 0)

    floor += ceil
    ceil = total_space * .1
    scope_memory['char'] = CompilationMemorySegment(floor, ceil, 0)

    floor += ceil
    ceil = total_space * .1
    scope_memory['string'] = CompilationMemorySegment(floor, ceil, 0)

    floor += ceil
    ceil = total_space * .2
    scope_memory['DataFrame'] = CompilationMemorySegment(floor, ceil, 0)
    floor += ceil
    return floor, scope_memory

def getCompilationMemory():
    base = 0
    compilation_memory = {}
    new_base, compilation_memory['global'] = getScopeMemory(base, 6000)
    base = new_base
    new_base, compilation_memory['temporary'] = getScopeMemory(base, 10000)
    base = new_base
    new_base, compilation_memory['local'] = getScopeMemory(base, 9000)
    base = new_base
    new_base, compilation_memory['cte'] = getScopeMemory(base, 6000)
    return compilation_memory