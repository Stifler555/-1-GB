text_varitable = "John Doe"
integer_varitable = 10
float_aritable = 13.7
boolean_aritable = False

user_name = input("Введите ваше имя >>> ")
print(user_name)

user_age = input("Введите ваш возраст >>> ")
print(user_age)









user_input = input("Введите время в секундах >>> ")

if not user_input.isdigit():
    print("Неверный формат числа")
    exit()

user_seconds = int(user_input)

hours = user_seconds // 3600
minutes = (user_seconds % 3600) // 60
seconds = (user_seconds % 3600) % 60

hours, minutes, seconds = user_seconds // 3600, (user_seconds % 3600) // 60, (user_seconds % 3600) % 60

print(f"{hours:>02}:{minutes:02}:{seconds:>02}")







user_input = input("Введите число >>> ")

if not user_input.isdigit():
    print("Неверный формат числа")
    exit()

result = 0
for x in range(1, 4):
    result += int(user_input * x)

print(result)

user_number = int(user_input)
characters_count = 0
temp_numder = user_number

while temp_number:
    temp_number //= 10
    characters_count += 1

first_level_multiplication = (10 ** characters_count) + 1
second_level_multiplication = (10 ** (haracters_count * 2)) + first_level_multiplication

result = user_number + (user_number * first_level_multiplication) + (user_number * second_level_multiplication)
print(result)








user_input = input("Введите число >>> ")

if not user_input.isdigit():
    print("Неверный формат числа")
    exit()

number = int(user_input)
max_num = 0

while number and max_num != 9:
    print(number)
    current = number % 10
    number = number // 10
    max_num = current if current > max_num else max_num

print(max_num)






revenue = int(input("Введите сумму выручки >>> "))
costs = int(input("Введите сумму издержек >>> "))

profit = revenue - costs

if profit:
    profitability = profit / revenue
    print(f"Прибыль = {profit}, рентабельность = {profitability}")

    workers_cout = int(input("Укажите количество сотрудников >>> "))

    profit_pet_worker = profit / workers_count
    print(f"Прибыль на одного сотрудника = {profit_pet_worker}")
else:
    print(f"Убыток = {profit}")






start = int(input("Укажите количество КМ за первый день >>> "))
goal = int(input("Укажите желаемое количество КМ >>> "))

day_counter = 1 

while start < goal:
    day_counter += 1
    start += start * .10
else:
    print(f"День достижения = {day_counter}")


