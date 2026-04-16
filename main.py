world = [["","",""], ["","",""], ["","",""]]

print(world[0])
print(world[1])
print(world[2])

player = "P"
entity = "E"

world[0][1] = player
world[2][2] = entity

print(" --- TEST ---")
print("*" * 50)

print(world[0])
print(world[1])
print(world[2])