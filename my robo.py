
# import pyttsx3
# engin = pyttsx3.init()
# def speak (x):
#    if __name__ == '__main__':
#       print("wellcome to robo speaker 1.1 created by arth ")
# print("enter what you want me to prounce"  )
        

# engin.say(input("ent ter you want to say"))
# engin.runAndWait()
# print('you typed: ', )
# speak("how are you")

# import pyttsx3


# engine = pyttsx3.init()


# rate = engine.getProperty('rate')
# engine.setProperty('rate', rate - 50)  

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()
#     engine.stop()

# if __name__ == "__main__":
#     print("Welcome to Robo Speaker 1.1")
#     print("Created by Arth")
#     print("Type 'exit' to stop\n")

#     while True:
#         user_input = input("Enter what you want me to say: ")

#         if user_input.lower() == "exit":
#             speak("Goodbye")
#             break

#         speak(user_input)

import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)  # slow speed
    engine.say(text)
    engine.runAndWait()
    engine.stop()

if __name__ == "__main__":
    print("Welcome to Robo Speaker 1.1")
    print("Created by Arth")
    print("Type 'exit' to stop\n")

    while True:
        user_input = input("Enter what you want me to say: ")

        if user_input.lower() == "exit":
            speak("Goodbye")
            break

        speak(user_input)
