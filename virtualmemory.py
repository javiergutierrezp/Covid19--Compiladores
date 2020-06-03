from utils import VarCount, pq

class CompilationMemorySegment():
    def __init__(self, beginning, size, used_space = 0):
        self.beginning = int(beginning)
        self.size = int(size)
        self.used_space = int(used_space)

    def incrementUsedSpace(self, space):
        current_memory_cell = self.beginning + self.used_space
        self.used_space += space
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

    def setFirstAvail(self, value, variable_type):
        if variable_type == 'int':
            self.int_space[self.int_space.index(None)] = value
        elif variable_type == 'float':
            self.float_space[self.float_space.index(None)] = value
        elif variable_type == 'char':
            self.char_space[self.char_space.index(None)] = value
        elif variable_type == 'string':
            self.string_space[self.string_space.index(None)] = value
        elif variable_type == 'Dataframe':
            self.dataframe_space[self.dataframe_space.index(None)] = value


class VirtualMachine():
    def __init__(self, quads, cte_directory, function_directory):
        self.quads = quads
        self.cte_directory = cte_directory
        self.function_directory = function_directory
        self.compilation_memory = getCompilationMemory()
        
        # Global memory se inicializa con "todo el espacio que tenemos para globales"
        self.global_memory = RuntimeMemorySegment(VarCount(
            self.compilation_memory['global']['int'].size,
            self.compilation_memory['global']['float'].size,
            self.compilation_memory['global']['char'].size,
            self.compilation_memory['global']['string'].size,
            self.compilation_memory['global']['Dataframe'].size))

        # Temporary memory inicia con "todo el espacio que tenemos para temporales"
        # Cuando vamos a llamar a una función, se instancia con un espacio limitado dependiendo de ERA
        # Cuando salimos de una función, la igualamos a "todo el espacio que tenemos para temporales"
        self.temporary_memory = RuntimeMemorySegment(VarCount(
            self.compilation_memory['temporary']['int'].size,
            self.compilation_memory['temporary']['float'].size,
            self.compilation_memory['temporary']['char'].size,
            self.compilation_memory['temporary']['string'].size,
            self.compilation_memory['temporary']['Dataframe'].size))

        # Local memory inicia como un arreglo vacio
        # Cada que entramos a una función, agregamos una instancia de RuntimeMemorySegment
        # En el inter, cada cosa que ocupe memoria "local" irá al último elemento del arreglo de locales
        # Cada que salimos de una función, sacamos el último RuntimeMemorySegment del arreglo
        self.local_memory = []

        self.param_stack = []
        self.current_scope = None

    def getCte(self, virtual_memory):
        # print("entering getCte")
        # print(self.cte_directory)
        # print(virtual_memory)
        # print(virtual_memory in self.cte_directory)
        # print(self.cte_directory)
        if virtual_memory in self.cte_directory:
            return self.cte_directory[virtual_memory].value
        else:
            return None

    def setMemorySegmentValue(self, scope, value, runtime_memory_index, variable_type):
        # print("setMemorySegmentValue")
        # print(scope, value, runtime_memory_index, variable_type)
        if scope == 'global':
            self.global_memory.set(value, runtime_memory_index, variable_type)
        elif scope == 'local':
            if runtime_memory_index:
                self.local_memory[len(self.local_memory) - 1].set(value, runtime_memory_index, variable_type)
            else:
                self.local_memory[len(self.local_memory) - 1].setFirstAvail(value, variable_type)
        elif scope == 'temporary':
            self.temporary_memory.set(value, runtime_memory_index, variable_type)

    def accessMemory(self, virtual_memory):
        final_virtual_memory = virtual_memory
        value = None

        if type(virtual_memory) == str and 'lit' in virtual_memory:
            value = int(virtual_memory[virtual_memory.find('(') + 1 :-1])
        elif type(virtual_memory) == str and 'meta' in virtual_memory:
            value = self.accessMemory(int(virtual_memory[virtual_memory.find('(') + 1:-1]))
        else:
            # print("Entreing access memory...")
            runtime_memory_index, variable_type, scope = self.interpretVirtualMemory(virtual_memory)
            # print("runtime_memory_index=({})\n variable_type=({})\n scope=({})\n".format(runtime_memory_index, variable_type, scope))
            value = None
            if scope != 'cte':
                # print("about to get memory")
                memory = self.accessScopeMemory(scope, runtime_memory_index, variable_type)
                # print("***memory***")
                # print(memory)
                # print("about to get value")
                value = self.accessTypeMemory(memory, variable_type, runtime_memory_index)
                # print("***value***")
                # print(value)
            else:
                value = self.getCte(virtual_memory)
                # print("returned value from getCte = {}".format(value))
        return value

    def accessTypeMemory(self, memory, var_type, runtime_index):
        # print("Trying to accessTypeMemory of...")
        # print(self.global_memory.int_space)
        # print(runtime_index)
        # print(memory, var_type, runtime_index)
            
        if var_type == 'int':
            return memory.int_space[runtime_index]
        elif var_type == 'float':
            return memory.float_space[runtime_index]
        elif var_type == 'char':
            return memory.char_space[runtime_index]
        elif var_type == 'string':
            return memory.string_space[runtime_index]
        elif var_type == 'Dataframe':
            return memory.dataframe_space[runtime_index]

    def accessScopeMemory(self, scope, runtime_index, var_type):
        # Accesar memoria...
        if scope == 'local':
            # print("{}, {}".format(self.local_memory, len(self.local_memory)))
            return self.local_memory[len(self.local_memory) - 1]
            # self.accessTypeMemory('local', var_type, runtime_index)
        elif scope == 'temporary':
            return self.temporary_memory
            # self.accessTypeMemory('temporary', var_type, runtime_index)
        elif scope == 'global':
            return self.global_memory
            # return self.accessTypeMemory('global', var_type, runtime_index)

    def execute(self):
        # Iterar por los quads
        instruction_pointer = 0
        current_quad = None
        previousIP_stack = []
        while instruction_pointer < len(self.quads):
            # print('instruction_pointer: {}'.format(instruction_pointer))
            # Leer quad
            current_quad = self.quads[instruction_pointer]
            if current_quad.operator >= 0 and current_quad.operator <= 12 and current_quad.operator != 4: # Arithmetic operation
                left_operand = self.accessMemory(current_quad.left_operand)
                right_operand = self.accessMemory(current_quad.right_operand)
                destination_runtime_memory_index,\
                destination_variable_type,\
                destination_scope = self.interpretVirtualMemory(current_quad.result_id)
                # print("left = {}".format(left_operand))
                # print("right = {}".format(right_operand))
                if current_quad.operator == 0:  # *
                    # print("found a *")
                    computed_value = left_operand * right_operand
                elif current_quad.operator == 1:  # /
                    # print("found a /")
                    computed_value = left_operand / right_operand
                elif current_quad.operator == 2:  # +
                    computed_value = left_operand + right_operand
                elif current_quad.operator == 3:  # -
                    # print("found a -")
                    computed_value = left_operand - right_operand
                elif current_quad.operator == 5:  # <
                    # print("found a <")
                    computed_value = boolToInt(left_operand < right_operand)
                elif current_quad.operator == 6:  # >
                    # print("found a >")
                    computed_value = boolToInt(left_operand > right_operand)
                elif current_quad.operator == 7:  # !=
                    # print("found a !=")
                    computed_value = boolToInt(left_operand != right_operand)
                elif current_quad.operator == 8:  # ==
                    # print("found a ==")
                    computed_value = boolToInt(left_operand == right_operand)
                elif current_quad.operator == 9:  # >=
                    computed_value = boolToInt(left_operand >= right_operand)
                elif current_quad.operator == 10: # <=
                    computed_value = boolToInt(left_operand <= right_operand)
                elif current_quad.operator == 11: # AND
                    computed_value = boolToInt(left_operand and right_operand)
                elif current_quad.operator == 12: # OR
                    computed_value = boolToInt(left_operand or right_operand)
                self.setMemorySegmentValue(destination_scope, computed_value, destination_runtime_memory_index, destination_variable_type)
                instruction_pointer += 1
            elif current_quad.operator == 4:  # =
                final_left_operand = None
                if type(current_quad.left_operand) == int:
                    final_left_operand = self.accessMemory(current_quad.left_operand)
                else:
                    if type(current_quad.left_operand) == str and 'meta' in current_quad.left_operand:
                        final_left_operand = self.accessMemory(self.accessMemory(current_quad.left_operand))
                    else:
                        final_left_operand = self.accessMemory(self.function_directory['principal'].vars_table[current_quad.left_operand].memory_cell)
                computed_value = final_left_operand

                final_result_id = current_quad.result_id
                if type(current_quad.result_id) == str and 'meta' in current_quad.result_id:
                    final_result_id = self.accessMemory(current_quad.result_id)
                
                destination_runtime_memory_index, destination_variable_type, destination_scope = self.interpretVirtualMemory(final_result_id)

                self.setMemorySegmentValue(destination_scope, computed_value, destination_runtime_memory_index, destination_variable_type)
                instruction_pointer += 1
            else:
                if current_quad.operator == 13: # Goto
                    if current_quad.result_id == None: #estamos accesando a principal
                        instruction_pointer = self.function_directory['principal'].first_quad
                    else:
                        instruction_pointer = current_quad.result_id
                elif current_quad.operator == 14: # GotoV
                    # print("found a GotoV")
                    condition = self.accessMemory(current_quad.left_operand)
                    if condition == 1:
                        instruction_pointer = current_quad.result_id
                    else:
                        instruction_pointer += 1
                elif current_quad.operator == 15: # GotoF
                    condition = self.accessMemory(current_quad.left_operand)
                    if condition == 0:
                        instruction_pointer = current_quad.result_id
                    else:
                        instruction_pointer += 1
                    # print("found a GotoF")
                elif current_quad.operator == 16: # GOSUB
                    print("IN GOSUB")
                    self.processing_param = False
                    self.current_scope = None
                    print("deleting current_scope")
                    previousIP_stack.append(instruction_pointer + 1)
                    instruction_pointer = self.function_directory[current_quad.left_operand].first_quad
                elif current_quad.operator == 17: # ERA
                    print("IN ERA")
                    self.processing_param = True
                    self.current_scope = current_quad.left_operand
                    print("updating current_scope: {}".format(self.current_scope))
                    var_count = self.function_directory[current_quad.left_operand].var_count
                    print("creating new local memory with var_count: {}".format(var_count))
                    self.local_memory.append(RuntimeMemorySegment(var_count))
                    instruction_pointer += 1

                elif current_quad.operator == 18: # ENDFUNC
                    # printNotNone("enfunc... removing last local memory", self.local_memory[len(self.local_memory) - 1])
                    print("deleting last local memory")
                    self.local_memory.pop()
                    instruction_pointer = previousIP_stack.pop()
                elif current_quad.operator == 19: # LEE
                    destination_runtime_memory_index, destination_variable_type, destination_scope = self.interpretVirtualMemory(current_quad.left_operand)
                    computed_value = input("Input ({}): ".format(destination_variable_type))
                    computed_value = castTo(destination_variable_type, computed_value)
                    self.setMemorySegmentValue(destination_scope, computed_value, destination_runtime_memory_index, destination_variable_type)
                    instruction_pointer += 1
                elif current_quad.operator == 20: # ESCRIBE
                    # import pdb; pdb.set_trace()
                    if type(current_quad.left_operand) == str:
                        computed_value = current_quad.left_operand
                        print(computed_value)
                    else:
                        _, var_type, _ = self.interpretVirtualMemory(current_quad.left_operand)
                        computed_value = self.accessMemory(current_quad.left_operand)
                        print(prettyDisplay(var_type, computed_value))
                    instruction_pointer += 1
                elif current_quad.operator == 21: # REGRESA
                    # import pdb; pdb.set_trace()
                    computed_value = self.accessMemory(current_quad.result_id)
                    function_memory_cell = self.function_directory['principal'].vars_table[current_quad.left_operand].memory_cell
                    destination_runtime_memory_index, destination_variable_type, destination_scope = self.interpretVirtualMemory(function_memory_cell)
                    self.setMemorySegmentValue(destination_scope, computed_value, destination_runtime_memory_index, destination_variable_type)
                    instruction_pointer += 1
                elif current_quad.operator == 22: # PARAM
                    print("IN PARAM")
                    if current_quad.result_id: # Not the last param yet...
                        param_definition_type = self.function_directory[self.current_scope].params[current_quad.result_id].type
                    else: # Last param...
                        param_definition_type = self.function_directory[self.current_scope].params[0].type
                    
                    computed_value = self.accessMemory(current_quad.left_operand)

                    _, param_given_type, _ = self.interpretVirtualMemory(current_quad.left_operand)
                    if param_given_type != param_definition_type:
                        raise EnvironmentError('Type of param missmatch when calling {}'.format(self.current_scope))
                        
                    self.param_stack.append({
                        "value": computed_value,
                        "type": param_given_type,
                    })

                    if not current_quad.result_id: # Last param! Let's set them all...
                        import pdb; pdb.set_trace()
                        while self.param_stack:
                            param = self.param_stack.pop()
                            self.setMemorySegmentValue('local', param['value'], None, param['type'])
                        import pdb; pdb.set_trace()
                    instruction_pointer += 1

                elif current_quad.operator == 23: # VER
                    computed_value = self.accessMemory(current_quad.left_operand)
                    if computed_value < current_quad.right_operand or computed_value >= current_quad.result_id:
                        raise EnvironmentError('Index out of range')
                    instruction_pointer += 1                 

        # printNotNone("global_memory.int_space", self.global_memory.int_space)
        # printNotNone("global_memory.float_space", self.global_memory.float_space)
        # printNotNone("local_memory", self.local_memory)
        # printNotNone("temporary_memory.int_space", self.temporary_memory.int_space)
        # printNotNone("temporary_memory.float_space", self.temporary_memory.float_space)
        return 0;

    def determineScope(self, virtual_memory):
        scope = None
        # print(virtual_memory, self.compilation_memory['local']['int'])
        # print(type(virtual_memory), self.compilation_memory['local']['int'].beginning)
        if virtual_memory >= self.compilation_memory['cte']['int'].beginning:
            scope = 'cte'
        elif virtual_memory >= self.compilation_memory['local']['int'].beginning:
            scope = 'local'
        elif virtual_memory >= self.compilation_memory['temporary']['int'].beginning:
            scope = 'temporary'
        elif virtual_memory >= self.compilation_memory['global']['int'].beginning:
            scope = 'global'
        return scope

    def determineRuntimeIndex(self, virtual_memory, scope_floor, variable_floor):
        # print(virtual_memory, scope_floor, variable_floor)
        runtime_memory_index = None
        runtime_memory_index = virtual_memory % variable_floor if variable_floor != 0 else virtual_memory
        # print(runtime_memory_index)
        return runtime_memory_index

    def determineType(self, virtual_memory, scope):
        # print("determineType...")
        # print(virtual_memory)
        # print(self.compilation_memory)
        var_type = None
        if virtual_memory < self.compilation_memory[scope]['int'].beginning + self.compilation_memory[scope]['int'].size:
            var_type = 'int'
            # print("found int")
        elif virtual_memory < self.compilation_memory[scope]['float'].beginning + self.compilation_memory[scope]['float'].size:
            var_type = 'float'
            # print("found float")
        elif virtual_memory < self.compilation_memory[scope]['char'].beginning + self.compilation_memory[scope]['char'].size:
            var_type = 'char'
            # print("found char")
        elif virtual_memory < self.compilation_memory[scope]['string'].beginning + self.compilation_memory[scope]['string'].size:
            var_type = 'string'
            # print("found string")
        elif virtual_memory < self.compilation_memory[scope]['Dataframe'].beginning + self.compilation_memory[scope]['Dataframe'].size:
            var_type = 'Dataframe'
            # print("found Dataframe")
        return var_type

    def interpretVirtualMemory(self, virtual_memory):
        if virtual_memory != None:
            # print("Entering interpretVirtualMemory -> {}".format(virtual_memory))
            compilation_memory = getCompilationMemory()
            runtime_memory_index = None
            variable_type = None
            scope = None

            # print("determineScope({},\n {},\n {})".format(virtual_memory, compilation_memory, compilation_memory))
            scope = self.determineScope(virtual_memory)
            variable_type = self.determineType(virtual_memory, scope)
            runtime_memory_index = self.determineRuntimeIndex(virtual_memory,
            self.compilation_memory[scope]['int'].beginning,
            self.compilation_memory[scope][variable_type].beginning)
            return runtime_memory_index, variable_type, scope
        else:
            return None
    
def boolToInt(operation):
    if operation:
        return 1
    else:
        return 0
# * global (donde estamos por default) -> Con toño
# * stack de memorias? para siempre utilizar la final...
# * local (para funciones) -> ERA
# * cte (en todas partes...) -> Expandirla dependiendo de ERA
# * temporal (en todas partes...) -> Inicializarla desde el inicio

def prettyDisplay(var_type, value):
    if var_type == 'char':
        return "'{}'".format(value)
    elif var_type == 'string':
        if value[0] != '"':
            return '"{}"'.format(value)
        else:
            return value
    else:
        return value

def castTo(var_type, value):
    if var_type == 'int':
        return int(value)
    elif var_type == 'float':
        return float(value)
    elif var_type == 'char':
        if len(value) > 1:
            raise EnvironmentError('Error: las variables de tipo char sólo pueden contener 1 caracter')
        return value
    else:
        return value

def printNotNone(name, list):
    print(name)
    print(['({}: {})'.format(idx,x) for (idx, x) in enumerate(list) if x is not None])

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
    scope_memory['Dataframe'] = CompilationMemorySegment(floor, ceil, 0)
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
