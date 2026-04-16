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


def show_world(world):
    print(" +--- MAP ---+")
    for row in world:
        print(row)
