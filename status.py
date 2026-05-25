wins = 0
losses = 0
draws = 0

history = []


def update_stats(winner):
  
    global wins, losses, draws
    
    if winner == "игрок":
        wins += 1
    elif winner == "компьютер":
        losses += 1
    else:
        draws += 1


def add_to_history(round_num, player_choice, computer_choice, winner):
  
    history.append({
        "round": round_num,
        "player": player_choice,
        "computer": computer_choice,
        "result": winner
    })


def get_stats():
   
    return wins, losses, draws


def show_current_score():
   
    print(f"\n Счёт: Победы: {wins} | Поражения: {losses} | Ничьи: {draws}")


def show_final_stats():
    print("\n" + "=" * 35)
    print("   ИТОГОВАЯ СТАТИСТИКА")
    print("=" * 35)
    print(f"  Всего раундов: {wins + losses + draws}")
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
   
    if not history:
        print("История пуста")
        return
    
    print("\n История игр:")
    print("-" * 35)
    for record in history:
        result_text = "Победа" if record["result"] == "игрок" else \
                      "Поражение" if record["result"] == "компьютер" else "Ничья"
        print(f"  Раунд {record['round']}: Вы - {record['player']}, "
              f"Компьютер - {record['computer']} -> {result_text}")


def reset_stats():
   
    global wins, losses, draws, history
... (осталось: 4 строки)
