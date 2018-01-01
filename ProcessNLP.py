#-*- coding:utf-8 –*-
import re

split_mark = "#"
filtered_chars = u"[]「」『』［］〔〕"
split_chars = u"…《》，、。？！；：“”‘’'\n\r-=—()（）.【】"
input_file = open("C:/Users/Jovan/Desktop/new.txt", 'r')

def str_replace(string, str_from, str_to = ""):
    return str_to.join(string.split(str_from))


def str_replace_re(string, str_from, str_to = ""):
    return re.sub(str_from, str_to, string)

def preprocessing(string):
    string = str_replace_re(string, u"第.{1,5}回")

    for char in filtered_chars:
        string = str_replace(string, char)

    for char in split_chars:
        string = str_replace(string, char, split_mark)

    while split_mark + split_mark in string:
        string = str_replace(string, split_mark + split_mark, split_mark)

    return string

def main():
    output_file = open("C:/Users/Jovan/Desktop/new1.txt", "w")
    output_file.truncate()

    string = input_file.read()
    string = string.decode("utf8")
    print isinstance(string, unicode)


   # print string

    print isinstance(preprocessing(string),unicode)


    output_file.write(preprocessing(string).encode("utf8"))

if __name__ == "__main__":
    main()
