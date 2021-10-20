import csv
import openpyxl


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
        max_length = max(len(row) for row in contents)

        for row in contents:
            if len(row) == max_length:
                print(row)


def reverse_text():
    with open('files/input (6).txt', "r", encoding="utf8") as file:
        contents = file.readlines()
        contents.reverse()
        for row in contents:
            print(''.join(reversed(row)))


def sort_salary():
    with open('files/input.csv') as file:
        file_reader = csv.reader(file, delimiter=";")
        company_salary = {}
        for row in file_reader:
            company_salary[row[0]] = int(row[1])

        sorted_by_names = dict((sorted(company_salary.items(), key=lambda x: x[0])))
        sorted_by_salary = dict((sorted(sorted_by_names.items(), key=lambda x: x[1])))

        for company in sorted_by_salary:
            print(f'{company}: {sorted_by_salary[company]}')


def sort_calories():
    book = openpyxl.open('files/trekking1.xlsx', read_only=True)
    sheet = book.active
    product_calories = {}
    for row in range(1, sheet.max_row):
        if row == 1: continue
        product_calories[sheet[row][0].value] = int(sheet[row][1].value)

    sorted_by_names = dict((sorted(product_calories.items(), key=lambda x: x[0])))
    sorted_by_calories = dict((sorted(sorted_by_names.items(), key=lambda x: x[1], reverse=True)))

    for product in sorted_by_calories:
        print(f'{product}: {sorted_by_calories[product]}')


unique_words()

quantity_every_word()

longest_rows()

reverse_text()

sort_salary()

sort_calories()