import pyttsx3 as speak

if __name__ == '__main__':
    print("Welcome to Robo speaker 1.1. created by Sumit")
    engine = speak.init()
    while True:
        x = input("Say: ")
        if x == 'q':
            engine.say("Good bye friends")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
