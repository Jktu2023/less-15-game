import pygame
import sys

pygame.init()  # Для автоматической инициализации всех модулей Pygame

# ФПС
clock = pygame.time.Clock()
fps = 60

speed = 3  # задаем скорость
BLACK = (0, 0, 0)

image_snake = pygame.image.load("snake.png")  # Загружаем изображение змеи
image_apple = pygame.image.load("apple.png")  # Загружаем изображение яблока
image_rasp = pygame.image.load("rasp1.png")  # Загружаем изображение клубники

# Устанавливаем позицию изображений
image_rect_apple = image_apple.get_rect(topleft=(200, 200))  # Устанавливаем позицию для яблока
image_rect_rasp = image_rasp.get_rect(topleft=(700, 400))  # Устанавливаем позицию для клубники

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

    # Получаем позицию курсора мыши
    mouseX, mouseY = pygame.mouse.get_pos()

    # Создаем прямоугольник для курсора
    cursor_rect = pygame.Rect(mouseX, mouseY, 1, 1)  # Устанавливаем минимальный размер прямоугольника

    # Проверка на столкновение с клубникой
    if rasp_visible and cursor_rect.colliderect(image_rect_rasp):
        print('Съела МАЛИНУ')
        rasp_visible = False  # Скрываем клубнику

    # Проверка на столкновение с яблоком
    if apple_visible and cursor_rect.colliderect(image_rect_apple):
        print('Съела ЯБЛОКО')
        apple_visible = False  # Скрываем яблоко

    screen.fill(BLACK)  # заливаем экран черным

    # Отрисовка яблока и клубники, если они видимы
    if apple_visible:
        screen.blit(image_apple, image_rect_apple)  # строим изображение яблока
    if rasp_visible:
        screen.blit(image_rasp, image_rect_rasp)  # строим изображение клубники

    pygame.display.flip()  # Чтобы обновлять содержимое экрана

    # Контроль ФПС
    clock.tick(fps)

pygame.quit()
sys.exit()