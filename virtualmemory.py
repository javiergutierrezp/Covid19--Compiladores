class MemorySegment():
    def __init__(self, beginning, size, used_space = 0):
        self.beginning = beginning
        self.size = size
        self.used_space = used_space

    def setUsedSpace(self, var_count):
        current_memory_cell = self.beginning + var_count
        return current_memory_cell

class MemorySegmentTwo():
    def __init__(self, var_count):
        self.int_space = [None] * var_count.int_type
        self.float_space = [None] * var_count.float_type
        self.char_space = [None] * var_count.char_type
        self.string_space = [None] * var_count.string_type
        self.dataframe_space = [None] * var_count.dataframe_type