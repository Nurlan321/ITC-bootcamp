def go_to_cinema(genre, ticket_price):
    if genre == 'ужасы' or genre == 'детектив' or genre == 'комедия':
        if ticket_price < 500 and ticket_price >= 300:
            return "Идем в кинотеатр после 21:00"
        elif ticket_price < 300:
            return "Идем в кинотеатр с любым временем"
        else:
            return "Билеты слишком дорогие, лучше остаться дома"
    else:
        return "Жанр не подходит, лучше остаться дома"

# Пример использования
genre = input("Введите жанр фильма: ")
ticket_price = float(input("Введите стоимость билета: "))

result = go_to_cinema(genre, ticket_price)
print(result)


