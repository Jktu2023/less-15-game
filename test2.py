import random

class Warrior:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self):
        damage = random.randint(1, self.attack_power)
        print(f"{self.name} наносит удар, нанося {damage} урона!")
        return damage

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} получил {damage} урона! Осталось здоровья: {self.health}")

def main():
    # Создаем экземпляры воинов
    player_warrior = Warrior("Ваш воин", 100, 20)
    computer_warrior = Warrior("Компьютерный воин", 100, 20)

    # Игровой цикл
    while player_warrior.is_alive() and computer_warrior.is_alive():
        # Ход игрока
        action = input("Выберите действие: 'атаковать' или 'сдаться': ").strip().lower()
        if action == 'атаковать':
            damage = player_warrior.attack()
            computer_warrior.take_damage(damage)
        elif action == 'сдаться':
            print("Вы сдались. Игра окончена.")
            break
        else:
            print("Некорректное действие. Попробуйте снова.")
            continue

        # Проверка, жив ли компьютерный воин
        if not computer_warrior.is_alive():
            print("Вы победили компьютерного воина!")
            break

        # Ход компьютера
        if computer_warrior.is_alive():
            damage = computer_warrior.attack()
            player_warrior.take_damage(damage)

        # Проверка, жив ли игрок
        if not player_warrior.is_alive():
            print("Ваш воин пал в бою. Игра окончена.")

if __name__ == "__main__":
    main()
