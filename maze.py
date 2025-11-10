player_x = 0
player_y = 0

treasure_x = 7
treasure_y = 3
game_running = True


print(f"Find the treasure at ({treasure_x}, {treasure_y})!")


while game_running:
    move = input("Enter move (up/down/right/left for movement, q to quit): ").lower()

    if move == 'up':
        player_y += 1
    elif move == 'down':
        player_y -= 1
    elif move == 'left':
        player_x -= 1
    elif move == 'right': 
        player_x += 1
    elif move == 'q':
        game_running = False
        print("You quit the game.")
    else:
        print("Invalid move. Please use up/down/right/left for movement, or q to quit.")

    
    print(f"Player position: ({player_x}, {player_y})")