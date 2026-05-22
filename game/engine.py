import random


class World:
    def __init__(self, size=3):
        self.size = size
        self.world = self.generate_world(self.size)

    @staticmethod
    def generate_world(size=3):
        return [[{} for _ in range(size)] for _ in range(size)]

    def add_entity_to_world(self, entity, position_x, position_y):
        self.world[position_y][position_x][entity.name] = entity
        entity.position_x, entity.position_y = position_x, position_y

    def remove_entity_from_world(self, entity, position_x, position_y):
        self.world[position_y][position_x].pop(entity.name)

    def is_empty(self, position_x, position_y):
        return self.world[position_y][position_x] == {}


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
        if self._can_move(world.size, new_coordinates):
            world.remove_entity_from_world(self, self.position_x, self.position_y)
            self.position_y, self.position_x = new_coordinates
            world.add_entity_to_world(self, self.position_x, self.position_y)

    def _can_move(self, size, new_entity_coordinates):
        return 0 <= new_entity_coordinates[0] < size and 0 <= new_entity_coordinates[1] < size

    def is_empty(self, world):
        return world[self.position_y][self.position_x] == {}


def spawn_entity(world, entity):
    while True:
        position_x = random.randint(0, world.size - 1)
        position_y = random.randint(0, world.size - 1)
        if world.is_empty(position_x, position_y):
            world.add_entity_to_world(entity, position_x, position_y)
            break
