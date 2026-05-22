from engine import World, Entity, spawn_entity
from ui import show_movements, show_world


def main():
    size_world = 5
    w = World(size_world)

    player = Entity("Aragorn")
    spawn_entity(w, player)
    goblin = Entity("Goblin")
    spawn_entity(w, goblin)

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
            player.move_entity(w, move_player)


if __name__ == "__main__":
    main()
