#Write a program that takes names of 3 favorite
# foods from the user and stores them in a list
# Then print the list and its length
# add and food item on the list 
food1 =input("enter the frist food : ")
food2 =input("enter the second food : ")
food3 =input("enter the third food : ")

foods=[food1,food2,food3]
print("the food are " ,foods)
print("length of the is " ,len(foods))
foods.append("milk")
print(f"foods now {foods}")