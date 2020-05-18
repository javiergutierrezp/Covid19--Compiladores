class MemorySegment():
    def __init__(self, name, beginning, size, sub_segments):
        self.name = name
        self.beginning = beginning
        self.size = size
        self.sub_segments = sub_segments

virtual_memory = MemorySegment('memory', 0, 40000, [
    MemorySegment('global', 0, 16000, [
        MemorySegment('variables', 0, 6000, [
            MemorySegment('int', 0, 1800, None),
            MemorySegment('float', 1800, 1800, None),
            MemorySegment('char', 3600, 600, None),
            MemorySegment('string', 4200, 600, None),
            MemorySegment('Dataframe', 4800, 1200, None),
        ]),
        MemorySegment('temporary', 6000, 10000, [
            MemorySegment('int', 6000, 3000, None),
            MemorySegment('float', 9000, 3000, None),
            MemorySegment('char', 12000, 1000, None),
            MemorySegment('string', 13000, 1000, None),
            MemorySegment('Dataframe', 14000, 2000, None),
        ])
    ]),
    MemorySegment('local', 16000, 24000, [
        MemorySegment('variables', 16000, 9000, [
            MemorySegment('int',   16000, 2700, None),
            MemorySegment('float', 18700, 2700, None),
            MemorySegment('char', 21400, 900, None),
            MemorySegment('string', 22300, 900, None),
            MemorySegment('Dataframe', 23200, 1800, None),
        ]),
        MemorySegment('temporary', 25000, 15000, [
            MemorySegment('int', 25000, 4500, None),
            MemorySegment('float', 29500, 4500  , None),
            MemorySegment('char', 34000, 1500, None),
            MemorySegment('string', 35500, 1500, None),
            MemorySegment('Dataframe', 37000, 3000, None),
        ])
    ])
])