fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'kiwi']
fruits.append("orange")
fruits.append("avocado")
fruits.remove('avocado')
fruits.sort()
print(fruits[0:3])
for i, j in enumerate(fruits):
    print(f"{i}: {j}, ", end="")
print()
