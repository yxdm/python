#Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”.
#Once “done” is entered, print out the total, count, and average of the numbers.
#If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

total=0 #表示总数（sum）
average=0 #表示平均值

count=0 #计数，看输入多少个数

input_num=[]

while True:
    num=input("please input a number: ")

    if num=='done':
        break
    else:
        try:
            num=float(num)
            input_num.append(num)
        except:
            print("Invalid input!")

for i in input_num:
    total=total+i
    count=count+1

average=total/count
print(total,count,average)
