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


def move_entity(world, entits_coordinates, entity, move):
    moves = {'up': [-1, 0], 'left': [0, -1], 'down': [1, 0], 'right': [0, 1]}
    entite_coordinates = entits_coordinates[entity]
    world[entite_coordinates[0]][entite_coordinates[1]] = " "
    new_coordinates = [entite_coordinates[0] + moves[move][0], entite_coordinates[1] + moves[move][1]]
    entits_coordinates[entity] = new_coordinates
    print(entity, new_coordinates)
    world[new_coordinates[0]][new_coordinates[1]] = entity


def show_movements():
    print("""
        +--- MOVE: ---+
        |1. UP    (W) |
        |2. LEFT  (A) |
        |3. DOWN  (S) |
        |4. RIGHT (D) |
        |0. EXIT  (Y) |
        +-------------+
        """)


if __name__ == "__main__":
    size_world = 5
    world = generate_world(size_world)
    entities = {"player": "P", "entity": "E"}
    entities_coordinates = add_entities_to_world(world, entities)
    show_world(world)

    print("*" * 50)
    print(" --- TEST ---")
    show_movements()
    move_player = input("Kierunek: ").lower()
    move_entity(world, entities_coordinates, entities["player"], move_player)

    show_world(world)


