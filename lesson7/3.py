latin = "abcdefghijklmnopqrstuvwxyz"
text = input("Введите строку: ")
print(text)
i = 0
s = ""
for a in text:
    if "0" <= a <= "9":
        s += a
        continue
    elif s != "":
        text = text.replace(s, latin[int(s)-1])
    s = ""
print(text)