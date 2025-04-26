import time

def get_state_status(state):
    while True:
        status = input(f"Enter status for {state} (clean/dirty): ").lower()
        if status in ['clean', 'dirty']:
            return 'Clean' if status == 'clean' else 'Dirty'
        print("Invalid input! Please enter 'clean' or 'dirty'.")

def get_initial_position():
    while True:
        position = input("Enter initial vacuum position (left/right): ").lower()
        if position in ['left', 'right']:
            return position
        print("Invalid input! Please enter 'left' or 'right'.")

left_state = get_state_status("Left")
right_state = get_state_status("Right")
current_position = get_initial_position()
cost = 0

def clean_and_move():
    global left_state, right_state, current_position, cost

    while True:
        print(f"\nChecking {current_position} state...")

        if current_position == 'left':
            if left_state == 'Dirty':
                print("\nCleaning Left...")
                time.sleep(1)
                left_state = 'Clean'
                cost += 1
                print(f"Left: {left_state} Right: {right_state}")

            print("\nMoving to Right...")
            time.sleep(1)
            current_position = 'right'
            print(f"Moved to Right. Left: {left_state} Right: {right_state}")

        else:
            if right_state == 'Dirty':
                print("\nCleaning Right...")
                time.sleep(1)
                right_state = 'Clean'
                cost += 1
                print(f"Left: {left_state} Right: {right_state}")

            print("\nMoving to Left...")
            time.sleep(1)
            current_position = 'left'
            print(f"Moved to Left. Left: {left_state} Right: {right_state}")

        if left_state == 'Clean' and right_state == 'Clean':
            print("\nBoth rooms are clean, but still moving to show the process...")
            time.sleep(1)
            current_position = 'right' if current_position == 'left' else 'left'
            print(f"Moved to {current_position}. Left: {left_state} Right: {right_state}")
            break

    print("\nFinal Environment:")
    print(f"Left: {left_state} Right: {right_state}")
    print("\nAll rooms are clean. Task completed.")
    print(f"Total Cost (for cleaning only): {cost}")

clean_and_move()
