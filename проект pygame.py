import pygame
import time
import random

pygame.init()

white = (255, 255, 255)  # белый цвет
yellow = (255, 255, 102)  # желтый цвет
black = (0, 0, 0)  # черный цвет
red = (213, 50, 80)  # красный цвет
green = (1, 50, 30)  # зеленый цвет
green2 = (0, 128, 0)  # ярко зеленый цвет
blue = (50, 153, 213)  # синий цвет
orange = (255, 160, 0)  # оранжевый цвет

dis_width = 800  # длина
dis_height = 600  # высота

dis = pygame.display.set_mode((dis_width, dis_height))  # создаем главный экран
pygame.display.set_caption('Игра змейка!(Дельмухаметов Данила)')  # создаем надпись

pygame.mixer.music.load('Techno_Music_Bed_6.mp3')  # музыка когда мы играем
pygame.mixer.music.set_volume(0.05)  # громкость музыки
eat_sound = pygame.mixer.Sound('z_uk-kushaet.mp3')  # музыка когда змейка кушает еду
eat_sound.set_volume(0.06)  # громкость музыки когда змейка кушает еду

clock = pygame.time.Clock()  # время

background = pygame.image.load('grassss.jpg').convert()  # задний фон
background2 = pygame.image.load('snake.jpg').convert()  # задний фон в конце игры
icon = pygame.image.load('broccoli.png')  # иконка еды
icon2 = pygame.image.load('snake.png')  # иконка змеи

snake_block = 10  # размер змейки
snake_speed = 15  # скорость змейки

font_style = pygame.font.SysFont("bahnschrift", 50)  # размер и шрифт надписи в конце игры
score_font = pygame.font.SysFont("cmmi10", 42)  # размер и шрифт надписи во время игры


def Your_score(score):  # функия, которая считает размер змейки и результат
    value = score_font.render("Размер змейки " + str(score + 1), True, blue)  # наша надпись во время игры
    dis.blit(value, [0, 0])  # количество еды съеденных змейкой


def our_snake(snake_block, snake_list):  # функия, которая выводит змейку на экран
    for x in snake_list:
        dis.blit(icon2, [x[0], x[1], snake_block, snake_block])


def gameLoop():
    game_over = False
    game_close = False

    pygame.mixer.music.play(-1)  # музыка проигрывается до конца игры

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []  # список где находится змейка
    Length_of_snake = 1  # длина змейки

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0  # x еды
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0  # y еды

    while not game_over:
        while game_close:
            dis.blit(background2, (0, 0))  # выводиться фон конца игры

            mesg = font_style.render("Ты проиграл!!!", True, yellow)  # надпись в конце игры
            dis.blit(mesg, [dis_width / 8, dis_height / 8])  # позиция надписи
            Your_score(Length_of_snake)  # вызов функции
            pygame.display.update()  # обновление экрана
            while pygame.event.wait().type != pygame.QUIT:  # проверка на выход из игры
                pass
            pygame.quit()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if pygame.event.wait().type == pygame.QUIT:
                        pygame.quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:  # проверка на нажатия стрелочки влево
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:  # проверка на нажатия стрелочки вправо
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:  # проверка на нажатия стрелочки вверх
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:  # проверка на нажатия стрелочки вниз
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.blit(background, (0, 0))  # загружаем наш фон
        dis.blit(icon, [foodx, foody, snake_block, snake_block])  # выводим иконку змейки
        snake_Head = []  # позиции змейки
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)  # вызов функции
        Your_score(Length_of_snake - 1)  # вызов функции

        pygame.display.update()  # обновление экрана

        if x1 == foodx and y1 == foody:  # проверка, съела ли змейка еду
            pygame.mixer.Sound.stop(eat_sound)  # останавливаем музыку если она была включена
            pygame.mixer.Sound.play(eat_sound)  # включаем музыку
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0  # x новой еды
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0  # y новой еды
            Length_of_snake += 1  # прибавляем 1 к длине змейки

        clock.tick(snake_speed)  # скорость времени

    pygame.quit()


gameLoop()
