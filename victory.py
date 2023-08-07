import random
from datetime import datetime

# Известные люди и их даты рождения
people = {
    'John': '02.01.1988',
    'Alice': '15.04.1992',
    'Bob': '30.07.1985',
    'Emma': '18.12.1976',
    'Mike': '09.06.1999',
    'Kate': '21.03.1983',
    'Tom': '11.11.1990',
    'Linda': '25.09.1979',
    'David': '07.05.1981',
    'Sophia': '29.08.1995'
}

while True:
        # Выбираем 5 случайных людей
        random_people = random.sample(list(people.keys()), 5)

        correct_count = 0  # Счетчик правильных ответов

        for person in random_people:
            birthday = datetime.strptime(people[person], '%d.%m.%Y')
            formatted_birthday = birthday.strftime('%d %B %Y')

            user_input = input(f"Введите дату рождения {person}: ")

            try:
                user_birthday = datetime.strptime(user_input, '%d.%m.%Y')
                formatted_user_birthday = user_birthday.strftime('%d %B %Y')

                if user_birthday == birthday:
                    correct_count += 1
                else:
                    print(f"Неверно. Правильная дата рождения {person}: {formatted_birthday}")
            except ValueError:
                print("Ошибка: неверный формат даты. Введите дату в формате 'dd.mm.yyyy'.")

        incorrect_count = 5 - correct_count
        print(f"\nПравильных ответов: {correct_count}, Неправильных ответов: {incorrect_count}\n")

        restart = input("Хотите начать снова? (да/нет): ")
        if restart.lower() != 'да':
            break

if __name__ == "__main__":
    main()