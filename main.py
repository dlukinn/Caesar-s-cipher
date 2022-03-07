print('Привет это программа шифрования по алгоритму Цезаря. \n')
continue_job = input('Если хотите начать напишите - (y): \n')

while continue_job == 'y':

    whats_task = input('Что мы должны сделать: (s) - шифровать или (d) - дешифровать? \n')
    while whats_task != 's' and whats_task != 'd':
        whats_task = input('Что-то ты ввел не то, напиши (s) - для шифрования или (d) - для дешифрования: \n')

    whats_language = input('Какой язык (rus) - русский или (eng) - английский? \n')
    while whats_language != 'rus' and whats_language != 'eng':
        whats_language = input('Что-то ты ввел не то, напиши (rus) или (eng): \n')

    whats_step = input('На сколько символов сдвигаем буквы алфавита? Ответ напиши числом: \n')
    while whats_step.isdigit() != True:
        whats_step = input('Что-то ты ввел не то, напиши число: \n')

    whats_text = input('Введите текст: \n')


    def cryption(direction, language, step, text):
        upper_eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lower_eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        upper_rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        lower_rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

        step = int(step)
        result = ''

        if language == 'eng':
            if direction == "s":
                for i in range(len(text)):
                    if text[i].lower() not in lower_eng_alphabet:
                        result += text[i]
                        continue
                    if text[i] == text[i].lower():
                        ind = lower_eng_alphabet.find(text[i])
                        result += lower_eng_alphabet[(ind + step) % 26]
                    if text[i] == text[i].upper():
                        ind = upper_eng_alphabet.find(text[i])
                        result += upper_eng_alphabet[(ind + step) % 26]

            if direction == "d":
                for i in range(len(text)):
                    if text[i].lower() not in lower_eng_alphabet:
                        result += text[i]
                        continue
                    if text[i] == text[i].lower():
                        ind = lower_eng_alphabet.find(text[i])
                        result += lower_eng_alphabet[(ind - step) % 26]
                    if text[i] == text[i].upper():
                        ind = upper_eng_alphabet.find(text[i])
                        result += upper_eng_alphabet[(ind - step) % 26]

        if language == 'rus':
            if direction == "s":
                for i in range(len(text)):
                    if text[i].lower() not in lower_rus_alphabet:
                        result += text[i]
                        continue
                    if text[i] == text[i].lower():
                        ind = lower_rus_alphabet.find(text[i])
                        result += lower_rus_alphabet[(ind + step) % 32]
                    if text[i] == text[i].upper():
                        ind = upper_rus_alphabet.find(text[i])
                        result += upper_rus_alphabet[(ind + step) % 32]

            if direction == "d":
                for i in range(len(text)):
                    if text[i].lower() not in lower_rus_alphabet:
                        result += text[i]
                        continue
                    if text[i] == text[i].lower():
                        ind = lower_rus_alphabet.find(text[i])
                        result += lower_rus_alphabet[(ind - step) % 32]
                    if text[i] == text[i].upper():
                        ind = upper_rus_alphabet.find(text[i])
                        result += upper_rus_alphabet[(ind - step) % 32]
        return result


    print(cryption(whats_task, whats_language, whats_step, whats_text))

    continue_job = input('Если хотите продолжить напишите - (y): \n')

print('Удачи, еще увидемся.')
