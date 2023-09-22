

# List

# Exercise 1

number = input(int("Enter number: ")

ones = number % 10

tens = number//10

# print(ones + tens)

# Exercise 2

number = input(int("Enter number: ")

hundreds = number//100

ones = number % 10

tens = ((number//10) % 10)

# print(ones + tens + hundreds)


# Exercise 3


student_list = []

for i in range(4):
    student_name = input(f'Student {i+1} enter your name: ')
    if student_name in student_list:
        print(f'"{student_name}" already exists, try again')
    else:
        student_list.append(student_name)
        print(f'Welcome {student_name} !')


# Exercise 4

total_cost = 0

for i in range(3):
   item_cost = float(input(f'Enter cost of item number {i + 1} in your shopping list: '))

   total_cost += item_cost
print(total_cost)
