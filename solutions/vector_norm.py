@dataclass
class Vector:
    components: list[float]  # for Python < 3.9, you need to import List from typing
    
    def norm(self) -> float:
        return sum(x ** 2 for x in self.components) ** .5
