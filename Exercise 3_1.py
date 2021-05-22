dict_eng = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
dict_rus = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
            6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять'}
print(dict_eng)

def num_translate():
    """Translate number from english to russian"""
    number = int(input('enter a number :'))
    if number <= 10 and number >= 0:
        print(dict_eng[number], 'is mean', dict_rus[number], 'in russia')
    else:
        print(None)

num_translate()

