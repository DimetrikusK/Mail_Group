class MappingAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee
        self.lights = list()
        self.obstacles = list()
        self.dim = [0, 0]

    def lighten(self, grid):
        self.dim = [len(grid[0]), len(grid)]

        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                if grid[j][i] > 0:
                    self.lights.append((i, j))
                elif grid[j][i] < 0:
                    self.obstacles.append((i, j))

        self.adaptee.set_dim(self.dim)
        self.adaptee.set_lights(self.lights)
        self.adaptee.set_obstacles(self.obstacles)

        return self.adaptee.generate_lights()
