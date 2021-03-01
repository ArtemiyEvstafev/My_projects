import random
import colorama

def right():
    print("\033[32m {}".format("Правильно!"))


def NotRight():
    print("\033[31m {}".format("Неправильно!"))


numbers = [" ", " ", "zwanzig", "dreisig", "vierzig", "feunfzig", "sechzig", "siebzig", "achtzig", "neunzig"]
numbers2 = [" ", "eins", "zwei", "drei", "vier", "funf", "sechs", "sieben", "acht", "neun"]
for i in range(100):
    print(" ")
while True:
    OurNumber = random.randint(20, 99)
    NumberLetters = ""
    if OurNumber % 10 != 0:
        NumberLetters += numbers2[OurNumber % 10]
        NumberLetters += "und"
    NumberLetters += numbers[OurNumber // 10]
    print("\033[37m {}" .format(OurNumber))
    InputNumber = str(input())
    if InputNumber == NumberLetters:
        right()
    else:
        NotRight()
        print(NumberLetters)
    print("\033[37m {}" .format("Повторить?"))
    a = str(input())
    for i in range(100):
        print(" ")
    if len(a) != 0:
        quit()
