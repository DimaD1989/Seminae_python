# ✔Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# ✔Первое число int, второе - float разделены вертикальной чертой.
# ✔Минимальное число - -1000, максимальное - +1000. ✔Количество строк и имя файла передаются как аргументы функции
# import random
#
#
# def new_file(strings_number, file_name):
#     with open(file_name, "a", encoding="utf-8") as f:
#         for _ in range(strings_number):
#             intput_numbers = (str(random.randint(-1000, 1001)), str(random.uniform(-1000, 1001)))
#
#             f.write("|".join(intput_numbers) + "\n")
#
#
# new_file(10, "file.txt")
from random import random


# ✔Напишите функцию, которая генерирует псевдоимена. ✔Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные. ✔Полученные имена сохраните в файл.
#
# def names_generator():
#     name_lenght = random.randint(4,8)
#     letters="ауоыэяюёиебвгджзйклмнпрстфхцчшщ"
#     created_name = []
#     for i in range(name_lenght / 2):
#         letter = random.choice(letters[0:9])
#         created_name.append(letter)
#     for i in range(name_lenght// 2 + 1, name_lenght):
#         letter = random.choice(letters[10:])
#         created_name.append(letter)
#     random.shuffle(created_name)
#
#     return "".join(created_name).title()
#
#
# def write_names(file_name,number_of_names):
#     with open(file_name,"a",encoding='utf-8') as f:
#
#
# print(names_generator())

#
# ✔Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами. ✔Перемножьте пары чисел. В новый файл сохраните имя и произведение: ✔если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю ✔если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого. ✔В результирующем файле должно быть столько же строк, сколько в более длинном файле. ✔При достижении конца более короткого файла, возвращайтесь в его начало.
#
#
# def something_strange(new_file):
#     massive_multiplied_numbers = []
#     massive_of_names = []
#     length_of_first_file = 0
#     length_of_second_file = 0
#
#
#     with (
#     open('file.txt', 'r', encoding='utf-8') as f1,
#     open('file_with_names.txt', 'r', encoding='utf-8') as f2,
#     open(new_file, 'w', encoding='utf-8') as f3
#     ):
#         while numbers := f1.readline():
#             int_number, float_number = numbers.strip().split("|")
#             massive_multiplied_numbers.append(int(int_number) * float(float_number))
#             length_of_first_file += 1
#         while name := f2.readline():
#             massive_of_names.append(name[:-1])
#             length_of_second_file += 1
#
#         lengths = sorted([length_of_first_file, length_of_second_file])
#
#         for i in range(lengths[0]):
#             if massive_multiplied_numbers[i] < 0:
#                 f3.write(massive_of_names[i].lower() + " " + str(abs(massive_multiplied_numbers[i])) + "\n")
#             else:
#                 f3.write(massive_of_names[i].upper() + " " + str(round(massive_multiplied_numbers[i])) + "\n")
#
#         for i in range(lengths[1] - lengths[0]):
#             if massive_multiplied_numbers[i] < 0:
#                 f3.write(massive_of_names[i].lower() + " " + str(abs(massive_multiplied_numbers[i])) + "\n")
#             else:
#                 f3.write(massive_of_names[i].upper() + " " + str(round(massive_multiplied_numbers[i])) + "\n")
#
# something_strange("appended_file.txt")
#
# ✔Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры: ✔расширение ✔минимальная длина случайно сгенерированного имени, по умолчанию 6 ✔максимальная длина случайно сгенерированного имени, по умолчанию 30 ✔минимальное число случайных байт, записанных в файл, по умолчанию 256 ✔максимальное число случайных байт, записанных в файл, по умолчанию 4096 ✔количество файлов, по умолчанию 42 ✔Имя файла и его размер должны быть в рамках переданного диапазона.
#
# import random
# from random import randint, randbytes, sample, choice
# from string import ascii_letters
# import os
#
#
# def random_extension(list_ext: list[str]) -> str:
#     return random.choice(list_ext)
#
#
# def create_files(extension: list[str], min_name: int = 6, max_name: int = 30,
#                  min_size: int = 256, max_size: int = 4096, amount: int = 42):
#     for _ in range(amount):
#         name_size = randint(min_name, max_name)
#         ext = random_extension(extension)
#         file_name = ''.join(sample(ascii_letters, name_size)) + '.' + ext
#         file_name = os.path.join('data', file_name)
#         with open(file_name, 'ab') as file:
#             size = randint(min_size, max_size)
#             result = randbytes(size)
#             file.write(result)
#
#
# create_files(['txt', 'doc', 'md', 'rtf'], amount=12)
#
# def sort_files(dir_path: str, video_dir: str = 'Video', image_dir: str = 'Image', music_dir: str = 'Music',
#                doc_dir: str = 'Documents'):
#     if not os.path.isdir(dir_path):
#         return False
#     file_list = os.listdir(dir_path)
#     video_extensions = ['mov', 'mp4', 'mkv', 'avi']
#     image_extensions = ['png', 'jpg', 'bmp', 'psd']
#     music_extensions = ['mp3', 'wav', 'ogg']
#     documents_extensions = ['txt', 'doc', 'rtf']
#     all_extensions = {video_dir: video_extensions,
#                       image_dir: image_extensions,
#                       music_dir: music_extensions,
#                       doc_dir: documents_extensions}
#
#     def sort_files(current_file: str, dist_dir: str):
#         _, cur_ext = current_file.split('.')
#         if cur_ext in all_extensions.get(dist_dir):
#             if not os.path.isdir(os.path.join(dir_path, dist_dir)):
#                 os.mkdir(os.path.join(dir_path, dist_dir))
#             os.replace(os.path.join(dir_path, current_file), os.path.join(dir_path, dist_dir, current_file))
#
#     for cur_file in file_list:
#         for directory in all_extensions:
#             if '.' in cur_file:
#                 sort_files(cur_file, directory)
#
#     return f'Файлы в папке {dir_path} отсортированы по типам'
#
# sort_files('test')