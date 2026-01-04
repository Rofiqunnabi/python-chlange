#oprator 
#:Write a program that takes two numbers and prints:
#Their sum, difference, and product  
 #Whether the first number is greater than the second

# Get two numbers from user
num1 = float(input("Enter first number: "))

num2 = float(input("Enter second number: "))

# Calculate sum, difference, and product
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2

# Check if first number is greater
is_greater = num1 > num2 

# Print results
print(f"\nSum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Is {num1} greater than {num2}? {is_greater}")


