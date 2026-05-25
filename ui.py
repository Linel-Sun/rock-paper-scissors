"""
Модуль интерфейса для "Камень-Ножницы-Бумага"
Участник 2 - Меню, ввод игрока, вывод результатов
"""

import game


def show_welcome():
    """Показывает приветственное сообщение."""
    print("\n" + "=" * 35)
    print("   КАМЕНЬ - НОЖНИЦЫ - БУМАГА")
    print("=" * 35)
    print("Добро пожаловать в игру!")
    print()


def show_menu():
    """Показывает меню выбора."""
    print("Выберите действие:")
    print("  1 - Камень")
    print("  2 - Ножницы")
    print("  3 - Бумага")
    print("  0 - Выход из игры")
    print("-" * 35)


def get_player_choice():
    """
    Получает выбор игрока с валидацией.
    
    Returns:
        str: выбор игрока или None для выхода
    """
    while True:
        show_menu()
        user_input = input("Ваш выбор: ")
        
        try:
            choice_num = int(user_input)
        except ValueError:
            print("Пожалуйста, введите число (0, 1, 2 или 3)")
            continue
        
        if choice_num == 0:
            return None
        
        if choice_num in [1, 2, 3]:
            return game.get_choice_from_number(choice_num)
        else:
            print("Введите число от 0 до 3")


def show_round_result(player_choice, computer_choice, winner, round_num):
    """
    Показывает результат раунда.
    
    Args:
        player_choice (str): выбор игрока
        computer_choice (str): выбор компьютера
        winner (str): победитель
        round_num (int): номер раунда
    """
    print("\n" + "-" * 35)
    print(f"   РАУНД {round_num}")
    print("-" * 35)
    print(f"  Вы выбрали:    {player_choice}")
    print(f"  Компьютер выбрал: {computer_choice}")
    
    if winner == "ничья":
        print("\n  Результат: НИЧЬЯ!")
    elif winner == "игрок":
        print("\n  Результат: ВЫ ПОБЕДИЛИ!")
    else:
        print("\n  Результат: ВЫ ПРОИГРАЛИ!")
    print()


def show_goodbye():
    """Показывает прощание."""
    print("=" * 35)
    print("Спасибо за игру! До встречи!")
    print("=" * 35 + "\n")