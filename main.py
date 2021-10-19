def unique_words():
    with open('files/input.txt', "r", encoding="utf8") as file:
        contents = file.readlines()
        unique_words = []
        for row in contents:
            words_in_row = row.split()
            for word in words_in_row:
                if word not in unique_words:
                    unique_words.append(word)
        print(f'Уникальных слов в тексте {len(unique_words)}')


def quantity_every_word():
    with open('files/input.txt', "r", encoding="utf8") as file:
        contents = file.readlines()
        unique_words = {}
        for row in contents:
            words_in_row = row.split()
            for word in words_in_row:
                if word in unique_words:
                    unique_words[word] += 1
                else:
                    unique_words[word] = 1

        quantity_every_word = dict((sorted(unique_words.items(), key=lambda x: x[1], reverse=True)))

        words_string = ''

        for word in quantity_every_word.keys():
            words_string += word + ' '

        print(words_string)


def longest_rows():
    with open('files/input (4).txt', "r", encoding="utf8") as file:
        contents = file.readlines()
        rows_lenghth = {}
        for i in range(len(contents)):
            rows_lenghth[i] = len(contents[i])


quantity_every_word()
