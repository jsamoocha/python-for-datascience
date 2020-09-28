from collections import defaultdict

@dataclass
class ShapeGrouper:
    shapes: List[Shape2D]
    
    def __iter__(self):
        self.shape_type_dict = defaultdict(list)
        for shape in self.shapes:
            self.shape_type_dict[shape.__class__.__name__].append(shape)
        self.shape_type_iter = iter(self.shape_type_dict.items())
        return self
    
    def __next__(self):
        return next(self.shape_type_iter)
