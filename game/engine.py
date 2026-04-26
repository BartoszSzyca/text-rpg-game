import random


def generate_world(size=3):
    world = []
    for i in range(size):
        row = []
        world.append(row)
        for j in range(size):
            row.append(" ")
    return world


def add_entities_to_world(world, entities: dict):
    entities_coordinates = {}
    size_world = len(world)
    x = list(range(size_world))
    y = x[:]
    random.shuffle(x)
    random.shuffle(y)
    for entity in entities.values():
        entities_coordinates[entity] = [y.pop(), x.pop()]
        world[entities_coordinates[entity][0]][entities_coordinates[entity][1]] = entity
    return entities_coordinates


def move_entity(world, entities_coordinates, entity, move):
    moves = {'up': [-1, 0], 'left': [0, -1], 'down': [1, 0], 'right': [0, 1]}
    entity_coordinates = entities_coordinates[entity]
    new_coordinates = [entity_coordinates[0] + moves[move][0], entity_coordinates[1] + moves[move][1]]
    if _can_move(len(world), new_coordinates):
        world[entity_coordinates[0]][entity_coordinates[1]] = " "
        entities_coordinates[entity] = new_coordinates
        world[new_coordinates[0]][new_coordinates[1]] = entity


def _can_move(size, new_entity_coordinates):
    return 0 <= new_entity_coordinates[0] < size and 0 <= new_entity_coordinates[1] < size
