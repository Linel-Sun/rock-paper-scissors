"""
Модуль статистики для "Камень-Ножницы-Бумага"
Участник 3 - Счёт, история игр, итоговая статистика
"""

# Счётчики
wins = 0
losses = 0
draws = 0

# История игр
history = []


def update_stats(winner):
    """
    Обновляет статистику после раунда.
    
    Args:
        winner (str): "игрок", "компьютер" или "ничья"
    """
    global wins, losses, draws
    
    if winner == "игрок":
        wins += 1
    elif winner == "компьютер":
        losses += 1
    else:
        draws += 1


def add_to_history(round_num, player_choice, computer_choice, winner):
    """
    Добавляет запись в историю игры.
    """
    history.append({
        "round": round_num,
        "player": player_choice,
        "computer": computer_choice,
        "result": winner
    })


def get_stats():
    """Возвращает текущий счёт (wins, losses, draws)."""
    return wins, losses, draws


def show_current_score():
    """Показывает текущий счёт."""
    print(f"\nСчёт: Победы: {wins} | Поражения: {losses} | Ничьи: {draws}")


def show_final_stats():
    """Показывает итоговую статистику."""
    total = wins + losses + draws
    print("\n" + "=" * 35)
    print("   ИТОГОВАЯ СТАТИСТИКА")
    print("=" * 35)
    print(f"  Всего раундов: {total}")
    print(f"  Победы:     {wins}")
    print(f"  Поражения:  {losses}")
    print(f"  Ничьи:      {draws}")
    
    if wins > losses:
        print("\n  Поздравляем! Вы выиграли серию!")
    elif wins < losses:
        print("\n  Неплохо! В следующий раз повезёт!")
    else:
        print("\n  Ничья - равные соперники!")
    
    print("=" * 35)


def show_history():
    """Показывает историю всех раундов."""
    if not history:
        print("История пуста")
        return
    
    print("\nИстория игр:")
    print("-" * 35)
    for record in history:
        if record["result"] == "игрок":
            result_text = "Победа"
        elif record["result"] == "компьютер":
            result_text = "Поражение"
        else:
            result_text = "Ничья"
        print(f"  Раунд {record['round']}: Вы - {record['player']}, "
              f"Компьютер - {record['computer']} -> {result_text}")


def reset_stats():
    """Сбрасывает всю статистику."""
    global wins, losses, draws, history
    wins = 0
    losses = 0
    draws = 0
    history = []