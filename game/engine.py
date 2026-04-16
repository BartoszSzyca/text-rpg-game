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


def move_entity(world, entitis_coordinates, entity, move):
    moves = {'up': [-1, 0], 'left': [0, -1], 'down': [1, 0], 'right': [0, 1]}
    entity_coordinates = entitis_coordinates[entity]
    world[entity_coordinates[0]][entity_coordinates[1]] = " "
    new_coordinates = [entity_coordinates[0] + moves[move][0], entity_coordinates[1] + moves[move][1]]
    entitis_coordinates[entity] = new_coordinates
    print(entity, new_coordinates)
    world[new_coordinates[0]][new_coordinates[1]] = entity
