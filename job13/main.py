# asks five numbers to the user
numbers = []
for i in range(5):
    number = int(input("Entrez cinq nombres entiers : "))
    numbers.append(number)

# sorts numbers in ascending order
numbers.sort()

# prints numbers in order
print("Voici les numbers triés : ")
for number in numbers:
    print(number)
