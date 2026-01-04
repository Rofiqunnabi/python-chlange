#Convert text-based emotions into emojis.
msg =input("enter the text with emoji: ") 

msg = msg.replace(":)", "😊")
msg = msg.replace(":(", "☹️")
msg = msg.replace(":D", "😃")
msg = msg.replace(";)", "😉")
print(msg)