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
    
    def pipe(self, fn: Callable[['Vector'], 'Vector'], *args, **kwargs) -> 'Vector':
        return fn(self, *args, **kwargs)

def rotate(v: Vector, direction=None) -> Vector:
    if direction in ['right', 'clockwise']:
        return Vector([v[1], -v[0]])
    elif direction in ['left', 'counterclockwise']:
        return Vector([-v[1], v[0]])
    else:
        print(f'Invalid rotation argument')
        return v
