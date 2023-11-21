# #Task 1 
# def show_display_file_content(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             for line in file:
#                 print(line.strip())
#     except FileNotFoundError:
#         print(f"File '{file_path}' not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
# file_path = r"C:\Users\Aidar\Documents\text1.txt"
# show_display_file_content(file_path)


# #Task 2
# try:
#     import random
#     def read_random_line(file_path):
#         with open(file_path, 'r') as file:
#             lines = file.readlines()
#             if not lines:
#                 return None
#             random_line = random.choice(lines)
#             return random_line.strip()
#     file_path = r"C:\Users\Aidar\Documents\text1.txt"
#     random_line = read_random_line(file_path)
#     if random_line is not None:
#         print(f"Random line from the file: {random_line}")
#     else:
#         print("The file is empty.")
# except Exception as e:
#     print ("Error")


# #Task 3
# try:
#     def uppercase_characters_counter(file_path):
#         try:
#             with open(file_path, 'r') as file:
#                 content = file.read()
#                 uppercase_count = sum(1 for char in content if char.isupper())
#                 return uppercase_count
#         except FileNotFoundError:
#             print(f"The file '{file_path}' was not found.")
#         except Exception as e:
#             print(f"An error occurred: {e}")
#     file_path = r"C:\Users\Aidar\Documents\text1.txt"
#     result = uppercase_characters_counter(file_path)
#     print(f"Number of uppercase characters in the file: {result}")
# except Exception as e:
#     print ("Error")


# #Task 4
# def lines_not_starting_with_D(file_path):
#     count = 0
#     with open(file_path, 'r') as file:
#         for line in file:
#             if not line.startswith('D'):
#                 count += 1
#     return count
# file_path = r"C:\Users\Aidar\Documents\duracell.txt"
# result = lines_not_starting_with_D(file_path)
# print(f"Output: {result}")


# #Task 5
# def words_ending_with_f_counter(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             content = file.read()
#             words = content.split()
#             count = sum(1 for word in words if word.lower().endswith('f'))
#             return count
#     except FileNotFoundError:
#         print(f"Error: File '{file_path}' not found.")
#         return None
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return None
# file_path = r"C:\Users\Aidar\Documents\text1.txt"
# word_counter = words_ending_with_f_counter(file_path)
# if word_counter is not None:
#     print(f"The number of words ending with 'F' in the file is: {word_counter}")


# #Task 6
# try:
#     def words_counter(file_path):
#         try:
#             with open(file_path, 'r') as file:
#                 content = file.read()
#                 words = content.split()
#                 count_all = words.count("all")
#                 count_none = words.count("none")
#                 return count_all, count_none
#         except FileNotFoundError:
#             print(f"Error: File '{file_path}' not found.")
#             return None
#     file_path = r"C:\Users\Aidar\Documents\Kira.txt"
#     all_count, none_count = words_counter(file_path)
#     if all_count is not None:
#         print(f"Occurrences of 'all': {all_count}")
#         print(f"Occurrences of 'none': {none_count}")
# except Exception as e:
#     print ("Error")


# #Task 7
# try:
#     def word_frequency_counter(file_path):
#         with open(file_path, 'r') as file:  #Открываем файл по указанному пути в режиме чтения
#             content = file.read().lower()   #Читаем содержимое файла, преобразуя символы в нижний регистр
#             words = content.split()     #Разбиваем текст на слова
#             word_frequency = {}     #Словарь, который нужен для отслеживания частоты встречающихся слов
#             for word in words:      #Проходимся по каждому слову в файле
#                 word_frequency[word] = word_frequency.get(word, 0) + 1      #В случае если слово уже присутствует в словаре, то частота увеличивается на 1, если нет, то устанавливает частоту 1
#             for word, frequency in word_frequency.items():
#                 print(f"{word}: {frequency}")
#     file_path = file_path = r"C:\Users\Aidar\Documents\text1.txt"
#     word_frequency_counter(file_path)
# except Exception as e:
#     print ("Error")


# #Task 8
# def longest_word_finding(file_path):
#     try:
#         with open(file_path, 'r') as file:  #Открываем файл по указанному пути в режиме чтения
#             text = file.read()      #Читаем содержимое файла, преобразуя символы в нижний регистр
#             words = text.split()    #Разбиваем текст на слова
#             long_word = max(words, key=len)     #Находим самое длинное слово
#             return long_word
#     except FileNotFoundError:
#         print(f"Error: File '{file_path}' not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")
# file_path = r"C:\Users\Aidar\Documents\Kira.txt"
# longest_word = longest_word_finding(file_path)
# if longest_word:
#     print(f"The longest word in the file is: {longest_word}")


# #Task 9
# try:
#     def correct_and_save_file(file_path):
#         with open(file_path, 'r') as file: #Открываем файл по указанному пути в режиме чтения
#                 content = file.read() #Читаем файл
#                 correct_cont = content.replace('B', 'J').replace('b', 'j') #Заменяем букву "B" на "J"
#                 print(correct_cont) #Выводим результат на экран
#     file_path = r"C:\Users\Aidar\Documents\boy-next-door.txt"
#     correct_and_save_file(file_path)
# except FileNotFoundError:
#     print(f"Error: File '{file_path}' not found.")
# except Exception as e:
#     print(f"An error occurred: {e}")


# #Task 10
# def count_a_b_occur(file_path):
#    with open(file_path, 'r') as file:   #Открываем файл по указанному пути в режиме чтения
#       content = file.read().lower()     #Читаем содержимое файла, преобразуя символы в нижний регистр
#       count_a = content.count('a')      #Подсчет символа "а"
#       count_b = content.count('b')      #Подсчет символа "b"
#       print(f"a={count_a}, b={count_b}")
# file_path = r"C:\Users\Aidar\Documents\text1.txt"
# count_a_b_occur(file_path)