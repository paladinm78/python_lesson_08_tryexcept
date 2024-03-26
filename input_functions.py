
def yes_or_no(answer):
    return answer in ('да', 'lf', 'y', 'yes')


def confirmation(message='Выполнить действие? (да/нет): '):
    answer = ''
    while answer not in ('да', 'нет', 'lf', 'ytn', 'y', 'n', 'yes', 'no'):
        answer = input(message).lower()

    if answer == 'lf':
        print('Получен ответ "да"')
    if answer == 'ytn':
        print('Получен ответ "нет"')

    return yes_or_no(answer)


def input_correct_float(prompt='Введите дробное число: '):
    while True:
        number_str = input(prompt)
        if (number_str.replace('.', '', 1).replace('-', '', 1).isdigit()
                and number_str.count('.') <= 1
                and number_str.count('-') <= 1):
            number_float = float(number_str)
            if number_float > 0:
                return number_float
            else:
                print("Пожалуйста, введите положительное число.")
        else:
            print("Это не число. Пожалуйста, введите число.")