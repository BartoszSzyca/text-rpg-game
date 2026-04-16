import random


def generate_world(size=3):
    world = []
    for i in range(size):
        row = []
        world.append(row)
        for j in range(size):
            row.append(" ")
    return world


def show_world(world):
    print(" +--- MAP ---+")
    for row in world:
        print(row)


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


if __name__ == "__main__":
    size_world = 5
    world = generate_world(size_world)
    show_world(world)

    print("*" * 50)
    print(" --- TEST ---")
    entities = {"player": "P", "entity": "E"}
    entities_coordinates = add_entities_to_world(world, entities)

    show_world(world)
