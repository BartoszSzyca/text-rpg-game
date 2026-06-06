def show_movements():
    print("""
        +----- MOVE: -----+
        |1. UP        (W) |
        |2. LEFT      (A) |
        |3. DOWN      (S) |
        |4. RIGHT     (D) |
        |0. MENU      (Y) |
        +-----------------+
        """)


def show_world(world):
    print(" +--- MAP ---+")
    for row in world:
        print()
        for d in row:
            print(list(d.values()), end="")


def show_combat_options():
    print("""
        +----- MOVE: -----+
        |1. ATTACK    (A) |
        |2. DEFENSE   (D) |
        |3. INVENTORY (I) |
        |4. RUN       (R) |
        |0. MENU      (Y) |
        +-----------------+
        """)


def show_menu():
    print("""
        +----- MOVE: -----+
        |1. CONTINUE  (C) |
        |2. SAVE      (S) |
        |3. LOAD      (L) |
        |0. EXIT      (Y) |
        +-----------------+
        """)
