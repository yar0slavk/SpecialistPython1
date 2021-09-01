# Напишите функцию log() принимающую в качестве аргумента строку и дописывающую это строку в конец файла
import os


def log(text, file="log.txt"):
    path = os.path.join('data', file)
    with open(path, 'a', encoding='UTF-8') as f:
        f.write(text + '\n')


log("hello world")  # дописывает "hello world" в конец файла log.txt
log("message", "log01.txt")  # дописывает "message" в конец файла log01.txt
