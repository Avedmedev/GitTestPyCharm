class Floor:
    def __init__(self):
        self.name = 'floor'

    def build(self):
        print(f'Build: {self.name}')


class Ceiling:
    def __init__(self):
        self.name = 'ceiling'

    def build(self):
        print(f'Build: {self.name}')


class Wall:
    def __init__(self):
        self.name = 'wall'

    def build(self):
        print(f'Build: {self.name}')


class Building:
    def __init__(self):
        self.floor = None
        self.ceiling = None
        self.walls = None

    def floor_injection(self):
        self.floor = Floor()

    def wall_injection(self):
        self.ceiling = Ceiling()

    def ceiling_injection(self):
        self.ceiling = Ceiling()


def build():
    house = Building()
    house.floor_injection()
    house.wall_injection()
    house.ceiling_injection()
    return house



if __name__ == '__main__':
    build()
