from settings import classes
import os
import time

def is_valid(value, is_role = False):
    if len(value) == 0:
        print("Ошибка ввода! Вы ввели пустую строку!")
        return False
    if is_role:
        try:
            value = int(value)
        except:
            print("Ошибка ввода. Вы ввели текст вместо числа.")
            return False
        if value > len(classes) or value < 1:
            print("Ошибка ввода. Нет такого номера роли.")
            return False
    return True

def pause():
    time.sleep(3)
def enter_to_continue():
    input("Нажмите на любую клавишу для продолжения!")

def clear():
    os.system("cls")