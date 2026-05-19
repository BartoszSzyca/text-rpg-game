import random


class World:
    def __init__(self, size=3):
        self.size = size
        self.world = self.generate_world(self.size)

    @staticmethod
    def generate_world(size=3):
        return [[" "] * size for _ in range(size)]

    def add_entity_to_world(self, entity):
        while True:
            position_x = random.randint(0, self.size - 1)
            position_y = random.randint(0, self.size - 1)
            if self._is_empty(position_x, position_y):
                self.world[position_y][position_x] = entity
                entity.position_x, entity.position_y = position_x, position_y
                break

    def _is_empty(self, position_x, position_y):
        return self.world[position_y][position_x] == " "


class Entity:
    def __init__(self, name):
        self.name = name
        self.position_x = None
        self.position_y = None

    def __repr__(self):
        return f"'{self.name[0].upper()}'"

    def move_entity(self, world, move):
        moves = {'up': [-1, 0], 'left': [0, -1], 'down': [1, 0], 'right': [0, 1]}
        new_coordinates = [self.position_y + moves[move][0], self.position_x + moves[move][1]]
        if self._can_move(len(world.world), new_coordinates):
            world.world[self.position_y][self.position_x] = " "
            self.position_y, self.position_x = new_coordinates
            world.world[self.position_y][self.position_x] = self


    def _can_move(self, size, new_entity_coordinates):
        return 0 <= new_entity_coordinates[0] < size and 0 <= new_entity_coordinates[1] < size
