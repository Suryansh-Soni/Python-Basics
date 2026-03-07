# Rule base chat assistant


import datetime
import time 
currentHour=datetime.datetime.now().hour
fname=input("Please enter your first name : ")
lname=input("Please enter your last name : ")
name=fname+" "  +lname
if(5<=currentHour<=11):
    print(f"Good Morning ,{name} ")
elif(11<=currentHour<=17):
    print(f"Good Afternoon ,{name}")
elif(17<=currentHour<=20):
    print("Good evening ",name)
else:
    print("Good Night",name)

print('Namaste I am your personal Chat Bot ')
print("You can ask me basic question , Type 'bye' to exit")

# chatbot memory 
responses={
    "hello":"Hi,welcome. How can I help you.",
    "how are you":"I am fine. How about you .",
    "who are you":"I am you personal Chat Bot",
    "motivate me":f"Keep going . Every bug you face make you a better coder {name}."
}

# Function to get responses
def getResponse(userQuestion):
    userQuestion=userQuestion.lower()
    for i in responses:
        if i in userQuestion:
            return responses[i]
    return ""
# take input from user
while(True):
    userQuestion=input("Please enter your query: ")
    reply=getResponse(userQuestion)
    print("Bot:",reply)
    if "bye" in userQuestion.lower():
        print(" Bot:Hope i had been usefull to you ,bye.")
        break
