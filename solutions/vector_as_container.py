@dataclass
class Vector:
    values: List[float]
    
    def __getitem__(self, index: int):
        return self.values[index]
    
    def __len__(self):
        return len(self.values)
    
    def __mul__(self, scalar: float):
        return Vector([v * scalar for v in self.values])
    
    def __add__(self, other: 'Vector'):
        return Vector([self[i] + other[i] for i in range(len(self))])
