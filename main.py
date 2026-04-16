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


if __name__ == "__main__":
    player = "P"
    entity = "E"

    print("*" * 50)
    print(" --- TEST ---")
    size_world = 5
    world = generate_world(size_world)

    show_world(world)

    world[0][1] = player
    world[2][2] = entity

    show_world(world)
