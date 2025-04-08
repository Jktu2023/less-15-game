# Разработать игру.
# Примеры игр:
# пинг-понг
# змейка
# тетрис
# игра на выживание с постоянным передвижением, где на поле постоянно появляются “враги”, которых нельзя касаться
# В поле для ответа загрузи видеозапись разработанной игры.
import pygame
import time
import  sys
pygame.init() # Для автоматической инициализации всех модулей Pygame

# ФПС
clock = pygame.time.Clock()
fps = 60

speed = 3 # задаем скорость
BLACK = (0, 0, 0)

image_snake = pygame.image.load("snake.png") # Загружаем изображение яблоко
image_apple = pygame.image.load("apple.png") # Загружаем изображение яблоко
image_rasp = pygame.image.load("rasp1.png") # Загружаем изображение клубника
image_rect_snake = image_snake.get_rect() #хитбокс — рамка вокруг каждой части персонажа
image_rect_apple = image_apple.get_rect() #хитбокс — рамка вокруг каждой части персонажа
image_rect_rasp = image_rasp.get_rect() #хитбокс — рамка вокруг каждой части персонажа

# Устанавливаем позицию изображений
image_rect_apple.topleft = (200, 200)  # Устанавливаем позицию для яблока
image_rect_rasp.topleft = (700, 400)  # Устанавливаем позицию для клубники

# Создаём окно с определёнными размерами, с заголовком
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Змейка")

# Переменные для отслеживания состояния яблока и клубники
apple_visible = True
rasp_visible = True

# Для создания игрового цикла создаём переменную и задаём цикл
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect_snake.x = mouseX - 22
            image_rect_snake.y = mouseY - 0

    if rasp_visible and image_rect_snake.colliderect(image_rect_rasp):
        print('Сьела  МАЛИНУ')
        rasp_visible = False  # Скрываем клубнику

    if rasp_visible and image_rect_snake.colliderect(image_rect_apple):
        print('Сьела  ЯБЛОКО')
        apple_visible = False  # Скрываем яблоко

    screen.fill(BLACK) # заливаем экран черным
    screen.blit(image_snake, image_rect_snake) # строим изображение картинки на слой выше заливки экрана

    # Отрисовка яблока и клубники, если они видимы
    if apple_visible:
        screen.blit(image_apple, image_rect_apple)  # строим изображение яблока
    if rasp_visible:
        screen.blit(image_rasp, image_rect_rasp)  # строим изображение клубники

    pygame.display.flip() # Чтобы обновлять содержимое экрана

    # Контроль ФПС
    clock.tick(fps)

pygame.quit()
sys.exit()