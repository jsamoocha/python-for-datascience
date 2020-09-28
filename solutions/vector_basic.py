@dataclass
class Vector:
    values: List[float]
    
    def __mul__(self, scalar: float):
        return Vector([v * scalar for v in self.values])
    
    def __add__(self, other: 'Vector'):
        return Vector([v1 + v2 for v1, v2 in zip(self.values, other.values)])
