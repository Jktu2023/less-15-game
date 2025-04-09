import pygame
import random
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

# Создаём окно с определёнными размерами, с заголовком
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Змейка")

# Переменная для хранения позиций яблок и клубники
apple_positions = []
rasp_positions = []

# Генерация позиций для яблок и клубники
def generate_positions(image_rect, count):
    positions = []
    for _ in range(count):
        x = random.randint(0, window_size[0] - image_rect.width)
        y = random.randint(0, window_size[1] - image_rect.height)
        positions.append(pygame.Rect(x, y, image_rect.width, image_rect.height))
    return positions

# Заполняем позиции
apple_positions = generate_positions(image_apple.get_rect(), 4)
rasp_positions = generate_positions(image_rasp.get_rect(), 4)

# Переменная для отслеживания состояния змеи
snake_rect = image_snake.get_rect(center=(400, 300))

# Инициализируем mouseX и mouseY
mouseX, mouseY = 0, 0

# Для создания игрового цикла создаём переменную и задаём цикл
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            snake_rect.x = mouseX - 22
            snake_rect.y = mouseY

    # Создаем прямоугольник для курсора
    cursor_rect = pygame.Rect(mouseX, mouseY, 1, 1)  # Устанавливаем минимальный размер прямоугольника

    # Проверка на столкновение с клубникой
    for rasp_rect in rasp_positions[:]:
        if cursor_rect.colliderect(rasp_rect):
            print('Съела МАЛИНУ')
            rasp_positions.remove(rasp_rect)  # Удаляем клубнику, если съели

    # Проверка на столкновение с яблоком
    for apple_rect in apple_positions[:]:
        if cursor_rect.colliderect(apple_rect):
            print('Съела ЯБЛОКО')
            apple_positions.remove(apple_rect)  # Удаляем яблоко, если съели

    screen.fill(BLACK)  # заливаем экран черным
    screen.blit(image_snake, snake_rect)  # строим изображение змеи

    # Отрисовка яблок и клубники
    for apple_rect in apple_positions:
        screen.blit(image_apple, apple_rect)  # строим изображение яблока
    for rasp_rect in rasp_positions:
        screen.blit(image_rasp, rasp_rect)  # строим изображение клубники

    pygame.display.flip()  # Чтобы обновлять содержимое экрана

    # Контроль ФПС
    clock.tick(fps)

pygame.quit()
sys.exit()