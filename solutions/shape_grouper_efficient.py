from collections import defaultdict

@dataclass
class ShapeGrouper:
    shapes: list[Shape2D]

    def __init__(self, shapes: list[Shape2D]):
        self.shapes = shapes
        self.shape_type_dict = defaultdict(list)
        for shape in self.shapes:
            self.shape_type_dict[shape.__class__.__name__].append(shape)

    def __iter__(self):
        self.shape_type_iter = iter(self.shape_type_dict.items())
        return self
    
    def __next__(self):
        return next(self.shape_type_iter)

    def total_size(self):
        return {
            shape_type: sum([shape.circumference() for shape in shapes])
            for shape_type, shapes in self
        }
