from engine import World, Entity, move_entity
from ui import show_movements, show_world


def main():
    size_world = 5
    w = World(size_world)

    player = Entity("Aragorn")
    player.position_x, player.position_y = w.add_entity_to_world(player)
    goblin = Entity("Goblin")
    goblin.position_x, goblin.position_y = w.add_entity_to_world(goblin)

    while True:
        show_world(w.world)
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
            move_entity(w, player, move_player)


if __name__ == "__main__":
    main()
