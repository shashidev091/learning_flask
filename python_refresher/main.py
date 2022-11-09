print(__name__)


def convert_sqrt_to_meter():
    inp = int(input("Enter your house in square feet"))
    square_meter = inp / 0.8
    print(f"{inp} square feet is {square_meter:.2f} square meters")


# convert_sqrt_to_meter()

fruits = {"🍎", "🥝", "🍉"}
basket = {"🍎", "🍉", "🍓", "🥝"}

# print(basket.difference(fruits))
# print(basket.union(fruits))
# print(basket.intersection(fruits))
# print(basket.difference_update(fruits))
print(fruits.intersection(basket))
tuple_ex = 11, 33,

print(tuple_ex)

print('🍇' in fruits)

double_fruits = []
for fruit in fruits:
    double_fruits.append(fruit * 2)

print(double_fruits)

list_comprehension = [fruit * 2 for fruit in fruits]
print(list_comprehension)


students_attendance = {
    "Rolf": 99,
    "Bablu": 33,
    "Raju": 89
}

print(students_attendance)

for student, attendance in students_attendance.items():
    print(f"{student}: {attendance}%")


# destructuing
list_numbers = [1, 2, 3, 4, 5]
head, *middle, tail = list_numbers

print(head)
print(middle)
print(tail)


def full_name(fname, lname):
    return f"{fname} {lname}"

