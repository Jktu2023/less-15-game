# Разработать игру.
# Примеры игр:
# пинг-понг
# змейка
# тетрис
# игра на выживание с постоянным передвижением, где на поле постоянно появляются “враги”, которых нельзя касаться
# В поле для ответа загрузи видеозапись разработанной игры.
import pygame
pygame.init() # Для автоматической инициализации всех модулей Pygame

speed = 3 # задаем скорость
image_snake = pygame.image.load("snake.png") # Загружаем изображение яблоко
image_apple = pygame.image.load("apple.jpg") # Загружаем изображение яблоко
image_rasp = pygame.image.load("rasp.jpg") # Загружаем изображение клубника
image_rect_snake = image_snake.get_rect() #хитбокс — рамка вокруг каждой части персонажа
image_rect_apple = image_apple.get_rect() #хитбокс — рамка вокруг каждой части персонажа
image_rect_rasp = image_rasp.get_rect() #хитбокс — рамка вокруг каждой части персонажа

# Устанавливаем позицию изображений
image_rect_apple.topleft = (100, 100)  # Устанавливаем позицию для яблока
image_rect_rasp.topleft = (200, 200)  # Устанавливаем позицию для клубники

# Создаём окно с определёнными размерами, с заголовком
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Змейка")

# Для создания игрового цикла создаём переменную и задаём цикл
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        screen.fill((0, 0, 0)) # заливаем экран черным
        screen.blit(image_snake, image_rect_rasp) # строим изображение картинки на слой выше заливки экрана
        screen.blit(image_rasp, image_rect_rasp) # строим изображение картинки на слой выше заливки экрана
        screen.blit(image_apple, image_rect_apple) # строим изображение картинки на слой выше заливки экрана

        pygame.display.flip() # Чтобы обновлять содержимое экрана

pygame.quit()