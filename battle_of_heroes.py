'''
Создайте простую текстовую боевую игру, где игрок и компьютер управляют героями с различными характеристиками. Игра состоит из раундов,
в каждом раунде игроки по очереди наносят урон друг другу, пока у одного из героев не закончится здоровье.
Требования:
Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
Игра должна быть реализована как консольное приложение.

Классы:

Класс Hero:
Атрибуты:
Имя (name)
Здоровье (health), начальное значение 100
Сила удара (attack_power), начальное значение 20
Методы:
attack(other): атакует другого героя (other), отнимая здоровье в размере своей силы удара
is_alive(): возвращает True, если здоровье героя больше 0, иначе False

Класс Game:
Атрибуты:
Игрок (player), экземпляр класса Hero
Компьютер (computer), экземпляр класса Hero
Методы:
start(): начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет. Выводит информацию о каждом ходе
(кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.
'''

import random

from abc import ABC, abstractmethod
class Fighter(ABC): # создаем абстактный класс
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    @abstractmethod # создаем абстактный метод
    def attack(self):
        pass
    def is_alive(self):
        pass
    def take_damage(self, damage):
        pass

class Hero(Fighter): # Класс Hero
    def attack(self):
        damage = random.randint(1, self.attack_power)
        print(f"{self.name} наносит удар, причиняя {damage}% повреждений!")
        return damage

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):

        self.health -= damage
        print(f"{self.name} получил {damage}% повреждений! Осталось {self.health}% здоровья.")

def main():
    # Создаем экземпляры воинов
    hero = Hero('Наш Герой', 100, 20)
    gamer = Hero('Воин ПК', 100, 20)

    # игровой цикл
    while hero.is_alive() and gamer.is_alive():
        # наш ход
        action = input('Ваши действия: введите 1 - чтобы атаковать, 2 - чтобы сдаться').strip().lower()
        if action == '1':
            damage = hero.attack()
            gamer.take_damage(damage)
        elif action == '2':
            print("Вы сдались в плен добровольно. Игра окончена.")
            break
