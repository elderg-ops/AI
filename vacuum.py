rooms = {'left': input("Left (clean/dirty): "), 'right': input("Right (clean/dirty): ")}
pos = input("Initial position (left/right): ")
cost = 0

for _ in range(2):
    print(f"\nVacuum at {pos}")
    if rooms[pos] == 'dirty':
        print(f"Cleaning {pos}...")
        rooms[pos] = 'clean'
        cost += 1
    print(f"State: Left={rooms['left']} Right={rooms['right']}")
    pos = 'right' if pos == 'left' else 'left'
    print(f"Moving to {pos}...")

print(f"\nFinal: Left={rooms['left']} Right={rooms['right']}\nTotal Cost: {cost}")
