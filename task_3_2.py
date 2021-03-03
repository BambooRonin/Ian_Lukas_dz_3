def thesaurus(*args):
    """Функция итерирует кортеж из имен, если существующего ключа нет, он создается из первой буквы слова"""
    names = {}
    for item in args:
        let = item[0]
        if let in names:
            names[let].append(item)
        else:
            names[let] = [item]
    return names


print(thesaurus(*input('Введите имена(без запятой): ').split()))  # ввод имен, их распаковка, и итерация в функции
