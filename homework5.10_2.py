# Exercise 2: Write another program that prompts for a list of numbers as above and
# at the end prints out both the maximum and minimum of the numbers instead of the average
# 编写另一个程序，提示输入上述数字列表，以及在最后打印出数字的最大值和最小值，而不是平均值

max1 = 0
min1 = 0

input_num = []


while True:
    num = input("please input a number: ")

    if num == 'done':
        break
    else:
        try:
            num = float(num)
            input_num.append(num)
        except:
            print("Invalid input!")

for i in num:
    max1 = int(max(input_num))
    min1 = int(min(input_num))

print(max1)
print(min1)
