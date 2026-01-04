#Write a program that takes your favorite food name as input and prints:
# 1.The middle 3 characters & 2.The last 2 characters
food = input("enter your fevorite food:")

print("the length" ,len(food))#banana
mid=len(food)//2 #6/2=3 [mid-1=2 no ] [mid+2 =5]
output=food[mid-1:mid+2]
print("midil 3 chr is :" , output)
print("midil 3 chr is :" , food[2:5])
print("last 2 chr is :" , food[-2:])
