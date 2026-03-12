print("Hello")
print("5回繰り返し")
for i in range(5):
    print(i)
print("3~10繰り返し")
for i in range(3,10):
    print(i)
print("0~10を3で繰り返し")
for i in range(0,30,3):
    print(i)
animals = ["猫","犬","狸",]
for animal in animals:
    print(animal)
fruits = ["梨","リンゴ","バナナ"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
mixed_list = ["ぶどう",1000,True]
print(mixed_list)
student = {"name":"田中","age":"20","grade":"A"}
print(student)
print(student["name"])
score = 75
if score >= 60:
    print("合格")
elif score >= 50:
    print("もう少し")
else:
    print("不合格")
animals.append("熊")
print(animals)
print(animals[3])