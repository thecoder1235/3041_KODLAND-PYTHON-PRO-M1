from time import sleep

def time_txt(text):
    [print(harf, end='', flush=True) or sleep(.05) for harf in text]
    print(" ")

time_txt("puanımı ver kodland!")
