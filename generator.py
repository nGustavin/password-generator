import string
from random import choice, randint

def passwordGenerator():
    passLenght = int(input("Password Lenght: "))
    characters = string.ascii_letters + string.punctuation  + string.digits
    password =  "".join(choice(characters) for x in range(randint(passLenght, passLenght)))

    print(password)


passwordGenerator()