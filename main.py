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
    entity_coordinates = entits_coordinates[entity]
    world[entity_coordinates[0]][entity_coordinates[1]] = " "
    new_coordinates = [entity_coordinates[0] + moves[move][0], entity_coordinates[1] + moves[move][1]]
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


def main():
    size_world = 5
    world = generate_world(size_world)
    entities = {"player": "P", "entity": "E"}
    entities_coordinates = add_entities_to_world(world, entities)

    while True:
        show_world(world)
        show_movements()
        user_choice = input("Kierunek: ").lower()
        match user_choice:
            case "1" | "w" | "up":
                move_player = "up"
            case "2" | "a" | "left":
                move_player = "left"
            case "3" | "s" | "down":
                move_player = "down"
            case "4" | "d" | "right":
                move_player = "right"
            case "0" | "y" | "yes" | 't' | "tak":
                print("Koniec!")
                break
            case _:
                user_choice = None
                print("Nie prawidlowy wybor! Spróbuj ponownie.")
        if user_choice:
            move_entity(world, entities_coordinates, entities["player"], move_player)


if __name__ == "__main__":
    print("*" * 50)
    print(" --- TEST ---")
    main()
