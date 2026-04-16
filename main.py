def show_world(world):
    print(" +--- MAP ---+")
    for row in world:
        print(row)


if __name__ == "__main__":
    world = [["", "", ""], ["", "", ""], ["", "", ""]]

    player = "P"
    entity = "E"
    
    print("*" * 50)
    print(" --- TEST ---")

    show_world(world)

    world[0][1] = player
    world[2][2] = entity

    show_world(world)
