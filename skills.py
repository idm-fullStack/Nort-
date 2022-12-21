import os
import webbrowser
import sys
import subprocess
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 180)  # скорость речи


def speaker(text):
    '''Озвучка текста'''
    engine.say(text)
    engine.runAndWait()


def browser():
    '''Открывает браузер заданнный по уполчанию в системе с url указанным здесь'''

    webbrowser.open('https://gogle.com', new=2)


def game():
    '''Нужно разместить путь к exe файлу любого вашего приложения'''
    try:
        subprocess.Popen('D:\Stronghold Crusader\Stronghold Crusader.exe')
    except:
        speaker('Путь к файлу не найден, проверьте, правильный ли он')


def offpc():
    # Эта команда отключает ПК под управлением Windows

    os.system('shutdown \s')
    print('пк был бы выключен, но команде # в коде мешает;)))')


def offBot():
    '''Отключает бота'''
    sys.exit()


def passive():
    '''Функция заглушка при простом диалоге с ботом'''
    pass
