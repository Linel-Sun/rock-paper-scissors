"""
Главный файл игры "Камень-Ножницы-Бумага"
Объединяет логику, интерфейс и статистику
"""

import ui
import game
import stats


def main():
    """Главная функция игры."""
    ui.show_welcome()
    
    round_number = 1
    
    while True:
        player_choice = ui.get_player_choice()
        
        if player_choice is None:
            break
        
        computer_choice = game.get_computer_choice()
        

        winner = game.determine_winner(player_choice, computer_choice)
        
        # Показываем результат
        ui.show_round_result(player_choice, computer_choice, winner, round_number)
        

        stats.update_stats(winner)
        stats.add_to_history(round_number, player_choice, computer_choice, winner)
        stats.show_current_score()
        
        round_number += 1
    

    if round_number > 1:  
        stats.show_final_stats()
        stats.show_history()
    
    ui.show_goodbye()


if __name__ == "__main__":
    main()