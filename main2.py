import random


pass_length = int(input("Enter pass length: "))


def gen_pass(uzunluk):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(uzunluk):
        password += random.choice(elements)

    return password

x = gen_pass(pass_length)
print(x)
