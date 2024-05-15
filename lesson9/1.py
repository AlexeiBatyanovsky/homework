# Написать функцию printn() которая будет печатать переданный текст, 
# но при этом перед этим текстом выводить строку с номером отражающим 
# кокай раз по счету выполняется эта функция.

str1 = input('Enter string: ')
n = 0
def printn(str1):
    global n
    n += 1
    if str1:
        print(n, str1)
        printn(str1)
printn(str1)