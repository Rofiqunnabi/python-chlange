#conditional Statement [if,elif,else]
#candy_Buy
tk=int(input(" how much money do you have ?:"))
if(tk>=5):
    print("you can buy a candy")
    back= tk-5
    print (f"take a candy that is your current balance {back} " )
elif(tk<5):
    print(" you need to 5 tk for a candy")

print("thank you")
