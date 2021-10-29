from random import randint
f = open("route", "w")
new = ""
for i in range(randint(100,150)):
    for i in range(359):
        new += f"{randint(2,7)},"
    new += f"{randint(2,7)}"
    new += "; \n"
f.write(new)
