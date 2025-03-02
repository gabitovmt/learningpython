"""Модуль wo. Содержит функцию: words_occur()"""


# Функции интерфейса
def words_occur():
    """words_occur() - подсчитывает вхождения слов в файле."""
    # Запросить у пользователя имя файла.
    file_name = input("Enter the name of the file: ")
    # Открыть файл, прочитать его и сохранить слова в списке.
    f = open(file_name, 'r')
    word_list = f.read().split()
    f.close()
    # Подсчитать количество вхождений каждого слова в файле.
    occurs_dict = {}
    for word in word_list:
        # Увеличить счетчик для данного слова.
        occurs_dict[word] = occurs_dict.get(word, 0) + 1
    # Вывести результаты.
    print("File %s has %d words (%d are unique)"
          % (file_name, len(word_list), len(occurs_dict)))
    print(occurs_dict)


if __name__ == '__main__':
    words_occur()
