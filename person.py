from settings import classes
from utils import is_valid, clear, enter_to_continue, pause
import random


class Person:

    def __init__(self):
        self.name = ""
        self.role = ""
        self.characterictics = {}
        self.health = 0
        self.attack = 0
        self.protect = 0
        self.skills = {}
        self.is_alive = True

    def set_class_properties(self):
        self.health = self.characterictics["здоровье"]
        self.attack = self.characterictics["атака"]
        self.protect = self.characterictics["защита"]
        self.skills = self.characterictics["навыки"]

    def show_info(self):
        print(
            f"{self.name} - {self.role}, имеет характеристики:\nздоровье - {self.health},\nзащита - {self.protect},\nатака - {self.attack}")

    def attack_enemy(self, enemy):
        enter_to_continue()
        clear()
        print(f"{self.name} атакует {enemy.name}")
        damage = self.attack - enemy.protect
        if damage <= 0:
            damage = 0
            self.apply_skill()
        enemy.health -= damage
        print(f"{self.name} нанес {damage} урона и у {enemy.name} осталось {enemy.health} здоровья.")

    def fight_for_the_win(self, attacker, defender):
        clear()
        while self.is_alive:
            if attacker.health > 0:
                attacker.attack_enemy(defender)
            else:
                pause()
                print(f"Здоровье {attacker.name} - {attacker.health}.\nБой завершен победой {defender.name}!")
                enter_to_continue()
                clear()
                break
            if defender.health > 0:
                defender.attack_enemy(attacker)
            else:
                pause()
                print(f"Здоровье {defender.name} - {defender.health}.\nБой завершен победой {attacker.name}!")
                enter_to_continue()
                clear()
                break

    def apply_skill(self):
        a = random.random()
        if a > 0.7:
            skill_keys = list(self.skills.keys())
            skill = random.choice(skill_keys)
            self.health += self.skills[skill]
            print(f"{self.name} применяет навык {skill} и восстановливает свое здоровье на {self.skills[skill]}")


class Player(Person):

    def __init__(self):
        super().__init__()
        self.set_person_class()
        self.characterictics = classes[self.role]
        self.set_class_properties()
        self.money = random.randint(0, 10000)
        self.inventory = self.characterictics["инвентарь"]
        self.set_name()
        self.show_info()

    def set_name(self):
        while True:
            name = input("Введите имя для своего персонажа>> ")
            if is_valid(name):
                self.name = name
                break

    def set_person_class(self):
        roles = list(classes.keys())
        while True:
            role_number = int(input("Введите номер роли (1-Воин, 2-Лучник, 3-Маг)>> "))
            if is_valid(str(role_number), True):
                self.role = roles[role_number - 1]
                break

    def increase_money(self, amount):
        enter_to_continue()
        clear()
        self.money += amount
        print(f"Заработано {amount} руб. Осталось: {self.money} руб.")

    def decrease_money(self, amount):
        enter_to_continue()
        clear()
        if amount > self.money:
            print("Герой не может себе этого позволить.")
            return
        else:
            self.money -= amount
            print(f"Потрачено {amount} руб. Осталось: {self.money} руб.")


class Enemy(Person):

    def __init__(self):
        super().__init__()
        self.set_name()
        self.set_person_class()
        self.characterictics = classes[self.role]
        self.set_class_properties()
        self.show_info()

    def set_name(self):
        first_name = ['Доктор', 'Летающий', 'Профессор', 'Скучный', 'Мега', 'Железный', 'Голодный', 'Капитан',
                      'Быстрый',
                      'Мистер', 'Горячий', 'Звездный', 'Космический', 'Просто', 'Восхитительный', 'Непобедимый']
        second_name = ['слесарь', 'мухомор', 'пепел', 'лемур', 'шаман', 'пельмень', 'слизень', 'алхимик', 'крот',
                       'фикус',
                       'кролик', 'танцор', 'пингвин', 'викинг', 'паук', 'плащ']
        self.name = random.choice(first_name) + " " + random.choice(second_name)

    def set_person_class(self):
        roles = list(classes.keys())
        self.role = random.choice(roles)
