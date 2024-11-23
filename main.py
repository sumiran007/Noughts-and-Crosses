import pygame
import random

width, height = 900, 900
grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
# This sets up the 3 by 3 grid and can be changed
pygame.init()
screen = pygame.display.set_mode((width, height))
running = True
current_player = 1
# This alternates to help it be player 1 then player 2
# Ask the user whether they want to play against an AI or another player
mode = input("Enter '1' to play against another player or '2' to play against AI: ")

# Load images
x_img = pygame.image.load('x.png')
o_img = pygame.image.load('o.png')

def is_grid_full(grid):
    for row in grid:
        if 0 in row:
            return False
    return True

# Checks if the grid is full and stops game below if it is True
def check_winner(grid):
    # Check rows and columns
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != 0:
            return grid[i][0]
        if grid[0][i] == grid[1][i] == grid[2][i] != 0:
            return grid[0][i]
    # Check diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] != 0:
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] != 0:
        return grid[0][2]
    return None

# Checks to see if someone has won
def draw_grid(screen):
    screen.fill((255, 255, 255))
    for i in range(1, 3):
        pygame.draw.line(screen, (0, 0, 0), (i * 300, 0), (i * 300, 900), 10)
        pygame.draw.line(screen, (0, 0, 0), (0, i * 300), (900, i * 300), 10)
    for row in range(3):
        for col in range(3):
            if grid[row][col] == 1:
                screen.blit(x_img, (col * 300, row * 300))
            elif grid[row][col] == 2:
                screen.blit(o_img, (col * 300, row * 300))
    pygame.display.flip()

# Prints in the x or o respectively
def handle_mouse_click(grid, mouse_x, mouse_y, current_player):
    col, row = mouse_x // 300, mouse_y // 300
    if grid[row][col] == 0:
        grid[row][col] = current_player
        return True
    return False

# Goes to the correct row or column
def print_grid(grid):
    for row in grid:
        print(row)

def ai_move(grid):
    available_moves = [(i, j) for i in range(3) for j in range(3) if grid[i][j] == 0]
    if available_moves:
        move = random.choice(available_moves)
        grid[move[0]][move[1]] = 2
        return True
    return False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print(mouse_x, mouse_y)
            if handle_mouse_click(grid, mouse_x, mouse_y, current_player):
                print_grid(grid)
                if is_grid_full(grid):
                    print("The grid is full!")
                    running = False
                winner = check_winner(grid)
                if winner:
                    print(f"Player {winner} wins!")
                    running = False
                else:
                    if mode == '1':
                        current_player = 2 if current_player == 1 else 1
                    elif mode == '2':
                        current_player = 2
    # Checks winner and if there is no winner then it switches the player
    if mode == '2' and current_player == 2 and running:
        if ai_move(grid):
            print_grid(grid)
            if is_grid_full(grid):
                print("The grid is full!")
                running = False
            winner = check_winner(grid)
            if winner:
                print(f"Player {winner} wins!")
                running = False
            else:
                current_player = 1
    # Final check for winner vs full grid which is a draw
    draw_grid(screen)