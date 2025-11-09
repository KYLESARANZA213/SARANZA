print("Welcome to SARANZA's Maze")

maze = [
    "#########",
    "#P     G#",
    "# ### ###",
    "#   #   #",
    "#########"
]

player_row, player_col = 1, 1  # Starting position

def print_maze():
    for row in maze:
        print(row)
    print("Use W/A/S/D to move. Q to quit.\n")

while True:
    print_maze()
    move = input("Move: ").lower()
    if move == 'q':
        print("Goodbye!")
        break

    new_row, new_col = player_row, player_col
    if move == 'w': new_row -= 1
    elif move == 's': new_row += 1
    elif move == 'a': new_col -= 1
    elif move == 'd': new_col += 1
    else:
        print("Invalid input.")
        continue

    if maze[new_row][new_col] == '#':
        print("You hit a wall!\n")
        continue
    elif maze[new_row][new_col] == 'G':
        print("🎉 You reached the goal! You win!")
        break
    else:
        maze[player_row] = maze[player_row][:player_col] + ' ' + maze[player_row][player_col+1:]
        maze[new_row] = maze[new_row][:new_col] + 'P' + maze[new_row][new_col+1:]
        player_row, player_col = new_row, new_col



