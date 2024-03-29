from random import choice

variant = {
    1: "камень",
    2: "ножницы",
    3: "бумага"
}

def variant_game(user_choise:int):
    computer_choice = choice(list(variant))
    if user_choise == computer_choice:
        return f"ничья,  выбрал {variant[computer_choice]}"
    
    elif user_choise == 1 and computer_choice == 2 or user_choise == 2 and computer_choice == 3 or user_choise == 3 and computer_choice == 1:
        return f"вы выйиграли,компьютер выбрал {variant[computer_choice]}"
    
    elif user_choise ==1 and computer_choice == 3 or user_choise == 2 and computer_choice == 1 or user_choise == 3 and computer_choice == 2:
        return f"Вы проиграли, компьютер выбрал {variant[computer_choice]}"

    else:
        return "выберите корректный ответ"
