def task_1(a=3, b=5):
    return max(a, b)


print(task_1())

a = 150
b = 5
if (a - b) > 135:
    print('yes')
else:
    print("no")

a = 12
if a in [1, 2, 12]:
    print("зима")
elif a in [3, 4, 5]:
    print("весна")
elif a in [6, 7, 8]:
    print("лето")
elif a in [9, 10, 11]:
    print("осень")
else:
    print("введите правильное число от 1 до 12")

a = 5
b = 7
c = 10
if a > 10 and b > 10 and c > 10:
    print("yes")
else:
    print("no")
