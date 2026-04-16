from engine import generate_world, add_entities_to_world, move_entity
from ui import show_movements, show_world


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
    main()
