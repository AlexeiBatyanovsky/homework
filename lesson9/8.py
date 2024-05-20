# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы 
#  - остались только строки.
#  - остался только логический тип.

l = [1, 2, "hello", "123", True, False]

l2 = list(filter(lambda x: isinstance(x, str), l))
l3 = list(filter(lambda x: isinstance(x, bool), l))

print(l2)
print(l3)