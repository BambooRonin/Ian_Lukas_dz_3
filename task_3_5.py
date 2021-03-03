nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(num_of_j, rep=0):
    """
    Функция для создания списка из случайных шуток, взятых из трех списков
    :param num_of_j: запрос необходимого кол-ва шуток
    :param rep: если аргумент равен 0 выдются неограниченное кол-во комбинаций, 1 - без повторений слов
    :return: возвращает список с шутками
    """
    jokes = []
    min_pos = min(nouns, adverbs, adjectives)
    from random import randrange
    r_n = randrange(len(nouns))
    r_adv = randrange(len(adverbs))
    r_adj = randrange(len(adverbs))
    i = randrange(len(min_pos))
    while len(jokes) < int(num_of_j):
        if int(rep) == 0:
            jokes.append(f'{nouns[r_n]} {adverbs[r_adv]} {adjectives[r_adj]}')
        elif int(rep) != 0 and int(num_of_j) > 4:
            print('Превышено количество возможных шуток без повторений!')
            break
    else:
        jokes.append(f'{nouns.pop(i)} {adverbs.pop(i)} {adjectives.pop(i)}')
    return jokes


print(get_jokes(input('Введите желаемое количество шуток: '),   # обращение к функции
                int(input('С повторениями - поставте 0, без - поставте 1 (не больше 4 шуток): '))))
