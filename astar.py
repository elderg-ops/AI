import heapq

class Puzzle:
    def __init__(self, puzzle, g_value=0):
        self.puzzle = puzzle
        self.size = len(puzzle)
        self.goal = "1238_4765"
        self.h_value = self.heuristic()
        self.g_value = g_value
        self.f_value = self.h_value + self.g_value

    def __lt__(self, other):
        return self.f_value < other.f_value

    def display(self):
        for i in range(0, self.size, 3):
            print(self.puzzle[i], self.puzzle[i+1], self.puzzle[i+2])

    def move(self, direction):
        index = self.puzzle.index("_")
        puzzle_list = list(self.puzzle)

        if direction == "up":
            if index not in [0, 1, 2]:
                puzzle_list[index], puzzle_list[index - 3] = puzzle_list[index - 3], puzzle_list[index]
                return Puzzle("".join(puzzle_list), self.g_value + 1)

        elif direction == "down":
            if index not in [6, 7, 8]:
                puzzle_list[index], puzzle_list[index + 3] = puzzle_list[index + 3], puzzle_list[index]
                return Puzzle("".join(puzzle_list), self.g_value + 1)

        elif direction == "left":
            if index not in [0, 3, 6]:
                puzzle_list[index], puzzle_list[index - 1] = puzzle_list[index - 1], puzzle_list[index]
                return Puzzle("".join(puzzle_list), self.g_value + 1)

        elif direction == "right":
            if index not in [2, 5, 8]:
                puzzle_list[index], puzzle_list[index + 1] = puzzle_list[index + 1], puzzle_list[index]
                return Puzzle("".join(puzzle_list), self.g_value + 1)

        return None

    def get_children(self):
        directions = ["up", "down", "left", "right"]
        children = []
        for direction in directions:
            child = self.move(direction)
            if child:
                children.append((direction, child))
        return children

    def heuristic(self):
        h_value = 0
        for i in range(self.size):
            if self.puzzle[i] != self.goal[i] and self.puzzle[i] != "_":
                h_value += 1
        return h_value

    def is_goal(self):
        return self.puzzle == self.goal

def main():
    user_input = input("Enter the initial puzzle state (use _ for blank space, e.g., 2831647_5): ").strip()

    if len(user_input) != 9 or set(user_input) != set("12345678_"):
        print("Invalid input. Please enter exactly 9 characters using 1-8 and _ (underscore).")
        return

    start_puzzle = Puzzle(user_input)
    open_list = []
    closed_list = set()

    heapq.heappush(open_list, start_puzzle)
    counter = 0

    while open_list:
        current_puzzle = heapq.heappop(open_list)
        print(f"-------------------------------------------------------------------")
        print(f"\nStage: {counter}")
        current_puzzle.display()
        print(f"h: {current_puzzle.h_value}, g: {current_puzzle.g_value}, f: {current_puzzle.f_value}")

        if current_puzzle.is_goal():
            print("Goal reached!")
            return

        closed_list.add(current_puzzle.puzzle)
        children = current_puzzle.get_children()

        for direction, child in children:
            if child.puzzle in closed_list:
                continue
            if child not in open_list:
                heapq.heappush(open_list, child)
                print(f"\nDirection: {direction}")
                child.display()
                print(f"h: {child.h_value}, g: {child.g_value}, f: {child.f_value}")

        counter += 1

if __name__ == "__main__":
    main()
