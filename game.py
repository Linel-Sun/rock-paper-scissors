"""
Модуль игровой логики для "Камень-Ножницы-Бумага"
Участник 1 - Логика сравнения и определения победителя
"""

import random


def get_computer_choice():
    """
    Компьютер делает случайный выбор.
    
    Returns:
        str: "камень", "ножницы" или "бумага"
    """
    choices = ["камень", "ножницы", "бумага"]
    return random.choice(choices)


def determine_winner(player_choice, computer_choice):
    """
    Определяет победителя раунда.
    
    Args:
        player_choice (str): выбор игрока
        computer_choice (str): выбор компьютера
    
    Returns:
        str: "игрок", "компьютер" или "ничья"
    """
    if player_choice == computer_choice:
        return "ничья"
    

    winning_combinations = {
        "камень": "ножницы",
        "ножницы": "бумага",
        "бумага": "камень"
    }
    
    if winning_combinations[player_choice] == computer_choice:
        return "игрок"
    else:
        return "компьютер"


def get_choice_from_number(num):
    """
    Конвертирует номер (1, 2, 3) в текстовый выбор.
    
    Args:
        num (int): число 1, 2 или 3
    
    Returns:
        str: текстовый выбор или None если число неверное
    """
    choices = {1: "камень", 2: "ножницы", 3: "бумага"}
    return choices.get(num)