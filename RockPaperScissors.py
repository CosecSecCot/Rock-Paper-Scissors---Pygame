import pygame
import random
import time

pygame.init()
display_res = (640, 480)
pygame.display.set_caption("Rock-Paper-Scisors")
pygame.display.set_icon(pygame.image.load("data/images/icon.png"))
display = pygame.display.set_mode(display_res)

# Variables
choice_list = ['rock', 'paper', 'scissors']
computer = random.choice(choice_list)
player_choice = None
click = False
game_over = False

rock_rect = pygame.Rect((16, 288, 105, 193))
paper_rect = pygame.Rect((144, 288, 106, 230))
scissors_rect = pygame.Rect((272, 288, 113, 238))
computer_win_pos = (470, 390)
player_win_pos = (490, 390)
tie_pos = (540, 390)

# Images
rock_img = pygame.image.load('data/images/rock.png')
paper_img = pygame.image.load('data/images/paper.png')
scissors_img = pygame.image.load('data/images/scissors.png')
bg_img = pygame.image.load('data/images/background.png')


#Font
pygame.font.init()
_Font = pygame.font.Font('data/font/Cafe Francoise_D.otf', 36)
_FontSmall = pygame.font.Font('data/font/Cafe Francoise_D.otf', 24)

WHITE = (255, 255, 255)
player_text = _Font.render("Player", True, WHITE)
computer_text = _Font.render("Computer", True, WHITE)
tie = _FontSmall.render("Tie", True, WHITE)
player_win = _FontSmall.render("Player Wins", True, WHITE)
computer_win = _FontSmall.render("Computer Wins", True, WHITE)


# Basic Logic
# player = None
# while player not in choice_list:
#     player = input("Enter Choice : ")

# if player == computer:
#     print("Computer : ", computer)
#     print('Tie')

# elif player == 'rock':
#     if computer == 'paper':
#         print("Computer : ", computer)
#         print('Lost')
#     elif computer == 'scissors':
#         print("Computer : ", computer)
#         print('Won')
#
# elif player == 'paper':
#     if computer == 'scissors':
#         print("Computer : ", computer)
#         print('Lost')
#     elif computer == 'rock':
#         print("Computer : ", computer)
#         print('Won')

# elif player == 'scissors':
#     if computer == 'rock':
#         print("Computer : ", computer)
#         print('Lost')
#     elif computer == 'paper':
#         print("Computer : ", computer)
#         print('Won')


# Game Loop
running = True
while running:
    display.blit(bg_img, (0, 0))

    display.blit(rock_img, (16, 288))
    display.blit(paper_img, (144, 288))
    display.blit(scissors_img, (272, 288))
    display.blit(player_text, (32, 6))
    display.blit(computer_text, (440, 6))

    mouse_loc = pygame.mouse.get_pos()
    mouse_x, mouse_y = mouse_loc[0], mouse_loc[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                click = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                click = False
        if game_over == True:
            time.sleep(1)
            player_choice = None
            computer = random.choice(choice_list)
            game_over = False
                
    
    # Game logic
    if not game_over:
        if rock_rect.collidepoint(mouse_x, mouse_y):
            if click == True:
                player_choice = 'rock'
        elif paper_rect.collidepoint(mouse_x, mouse_y):
            if click == True:
                player_choice = 'paper'
        elif scissors_rect.collidepoint(mouse_x, mouse_y):
            if click == True:
                player_choice = 'scissors'
    
    if player_choice != None:
        if player_choice == computer:
            if player_choice == 'rock':
                display.blit(pygame.transform.rotate(rock_img, -90), (0, 88))
                display.blit(pygame.transform.rotate(rock_img, 90), (447, 88))
                display.blit(tie, tie_pos)
                game_over = True
            elif player_choice == 'paper':
                display.blit(pygame.transform.rotate(paper_img, -90), (0, 88))
                display.blit(pygame.transform.rotate(paper_img, 90), (447, 88))
                display.blit(tie, tie_pos)
                game_over = True
            else:
                display.blit(pygame.transform.rotate(scissors_img, -90), (0, 88))
                display.blit(pygame.transform.rotate(scissors_img, 90), (447, 88))
                display.blit(tie, tie_pos)
                game_over = True

        elif player_choice == 'rock':
            if computer == 'paper':
                display.blit(pygame.transform.rotate(rock_img, -90), (0, 88))
                display.blit(pygame.transform.rotate(paper_img, 90), (447, 88))
                display.blit(computer_win, computer_win_pos)
                game_over = True
            elif computer == 'scissors':
                display.blit(pygame.transform.rotate(rock_img, -90), (0, 88))
                display.blit(pygame.transform.rotate(scissors_img, 90), (447, 88))
                display.blit(player_win, player_win_pos)
                game_over = True
        
        elif player_choice == 'paper':
            if computer == 'scissors':
                display.blit(pygame.transform.rotate(paper_img, -90), (0, 88))
                display.blit(pygame.transform.rotate(scissors_img, 90), (447, 88))
                display.blit(computer_win, computer_win_pos)
                game_over = True
            elif computer == 'rock':
                display.blit(pygame.transform.rotate(paper_img, -90), (0, 88))
                display.blit(pygame.transform.rotate(rock_img, 90), (447, 88))
                display.blit(player_win, player_win_pos)
                game_over = True
        
        elif player_choice == 'scissors':
            if computer == 'rock':
                display.blit(pygame.transform.rotate(scissors_img, -90), (0, 88))
                display.blit(pygame.transform.rotate(rock_img, 90), (447, 88))
                display.blit(computer_win, computer_win_pos)
                game_over = True
            elif computer == 'paper':
                display.blit(pygame.transform.rotate(scissors_img, -90), (0, 88))
                display.blit(pygame.transform.rotate(paper_img, 90), (447, 88))
                display.blit(player_win, player_win_pos)
                game_over = True

    pygame.display.update()

pygame.quit()
