from __future__ import annotations

@dataclass
class Vector:
    values: list[float]
    
    def __mul__(self, scalar: float) -> Vector:
        return Vector([v * scalar for v in self.values])
    
    def __add__(self, other: Vector) -> Vector:
        return Vector([v1 + v2 for v1, v2 in zip(self.values, other.values)])
