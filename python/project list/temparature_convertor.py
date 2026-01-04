#Take input in Celsius and print its equivalent in Fahrenheit and Kelvin. 
#(Use explicit type conversion and arithmetic operators.) 
#Formula: Fahrenheit = (C × 9/5) + 32 ; Kelvin = C + 273.15 
clesius = float(input("enter the value of Celsius converted to Fahrenheit: "))
fer = (clesius*9/5)+32
print(" the value of Fahrenheit is :" , fer)
print(" done \n")
clesius = float(input("enter the value of Celsius converted to kelvin: "))
Kelvin = clesius + 273.15
print("the velue of kelvin is :" ,Kelvin) 