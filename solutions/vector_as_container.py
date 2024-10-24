from __future__ import annotations

@dataclass
class Vector:
    values: list[float]
    
    def __getitem__(self, index: int) -> float:
        return self.values[index]
    
    def __len__(self) -> int:
        return len(self.values)
    
    def __mul__(self, scalar: float) -> Vector:
        return Vector([v * scalar for v in self.values])
    
    def __add__(self, other: Vector) -> Vector:
        return Vector([self[i] + other[i] for i in range(len(self))])
