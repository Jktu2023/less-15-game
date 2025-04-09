# Разработать игру.
# Примеры игр:
# пинг-понг
# змейка
# тетрис
# игра на выживание с постоянным передвижением, где на поле постоянно появляются “враги”, которых нельзя касаться
# В поле для ответа загрузи видеозапись разработанной игры.
import pygame
import random
import  sys

pygame.init() # Для автоматической инициализации всех модулей Pygame, это команда, которая запускает pygame
pygame.mixer.init()  # Инициализация модуля звука

# Загрузка звуковых эффектов
eat_sound = pygame.mixer.Sound("eat_.wav")  # Путь к  звуковому файлу

# ФПС
clock = pygame.time.Clock() # clock, чтобы убедиться, что игра работает с заданной частотой кадров.
fps = 60 # частота кадров в секунду

speed = 3 # задаем скорость
BLACK = (0, 0, 0)
WIDTH = 800  # ширина игрового окна
HEIGHT = 600

image_snake = pygame.image.load("snake.png") # Загружаем изображение яблоко
image_apple = pygame.image.load("apple.png") # Загружаем изображение яблоко
image_rasp = pygame.image.load("rasp1.png") # Загружаем изображение клубника

# image_rect_snake = image_snake.get_rect() #хитбокс — рамка вокруг каждой части персонажа
# image_rect_apple = image_apple.get_rect() #хитбокс — рамка вокруг каждой части персонажа
# image_rect_rasp = image_rasp.get_rect() #хитбокс — рамка вокруг каждой части персонажа
#
# # Устанавливаем позицию изображений
# image_rect_apple.topleft = (200, 200)  # Устанавливаем позицию для яблока
# image_rect_rasp.topleft = (700, 400)  # Устанавливаем позицию для клубники

# Создаём окно с определёнными размерами, с заголовком
window_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(window_size) #После этого создаем графическое окно, передав в качестве аргумента в функцию set_mode() его разрешение в виде пары целых чисел. В свою очередь функция вернет нам объект типа Surface, используемый для представления изображений:
pygame.display.set_caption("Змейка")

# Переменная для хранения позиций яблок и клубники
apple_positions = []
rasp_positions = []

# # Переменные для отслеживания состояния яблока и клубники
# apple_visible = True
# rasp_visible = True

# Генерация позиций для яблок и клубники (генератор рандома в установленом окне)
def generate_positions(image_rect, count):
    positions = []
    for _ in range(count):
        x = random.randint(0, window_size[0] - image_rect.width)
        y = random.randint(0, window_size[1] - image_rect.height)
        positions.append(pygame.Rect(x, y, image_rect.width, image_rect.height))
    return positions

# Определяем рандомные позиции генератором
apple_positions = generate_positions(image_apple.get_rect(), 4)
rasp_positions = generate_positions(image_rasp.get_rect(), 4)

# Переменная для отслеживания состояния змеи
snake_rect = image_snake.get_rect(center=(400, 300))

# Инициализируем mouseX и mouseY
mouseX, mouseY = 0, 0

# Для создания игрового цикла создаём переменную и задаём цикл
run = True

while run:
    # Ввод процесса (события)
    # Обновление
    # Визуализация (сборка)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #pygame.QUIT — событие, которое стартует после нажатия крестика и передает значение False переменной running, в результате чего игровой цикл заканчивается.
            run = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            snake_rect.x = mouseX - 22
            snake_rect.y = mouseY

    # Создаем прямоугольник для курсора
    cursor_rect = pygame.Rect(mouseX, mouseY, 1, 1)  # Устанавливаем минимальный размер прямоугольника

    # Проверка на столкновение с клубникой
    for rasp_rect in rasp_positions[:]:
        if cursor_rect.colliderect(rasp_rect):
            eat_sound.play()  # Воспроизводим звук поедания
            print('Съела МАЛИНУ')
            rasp_positions.remove(rasp_rect)  # Удаляем клубнику, если съели

    # Проверка на столкновение с яблоком
    for apple_rect in apple_positions[:]:
        if cursor_rect.colliderect(apple_rect):
            eat_sound.play()  # Воспроизводим звук поедания
            print('Съела ЯБЛОКО')
            apple_positions.remove(apple_rect)  # Удаляем яблоко, если съели

    # Рендеринг
    screen.fill(BLACK) # заливаем экран черным
    screen.blit(image_snake, snake_rect) # строим изображение картинки на слой выше заливки экрана

    # Отрисовка яблок и клубники
    for apple_rect in apple_positions:
        screen.blit(image_apple, apple_rect)  # строим изображение яблока
    for rasp_rect in rasp_positions:
        screen.blit(image_rasp, rasp_rect)  # строим изображение клубники

    # Рендеринг
    pygame.display.flip() # Чтобы обновлять содержимое экрана. Нужно всего лишь сказать доске, чтобы она перевернулась, когда отрисовка завершена. Эта команда называется flip()
    #Главное — сделать так, чтобы функция flip() была в конце. Если попытаться отрисовать что-то после поворота, это содержимое не отобразится на экране.

    # Контроль ФПС # держим игорвой цикл на правильной скорости
    clock.tick(fps) #нужно убедиться, что настройка FPS контролирует скорость игры.

pygame.quit() # выходим так
sys.exit() # и эдак