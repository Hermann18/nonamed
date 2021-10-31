from random import randint
f = open("routeDegrees", "w")
k = open("routeGyroscopes", "w")
new = ""
degrees = ""
for x in range(randint(100,150)):
    for i in range(359):
        new += f"{randint(2,7)},"
    new += f"{randint(2,7)}"
    new += f";\n"
    degrees += f"{randint(0,360)};"
degrees += f"{randint(0,360)}"
k.write(degrees)

for i in range(359):
        new += f"{randint(2,7)},"
    new += f"{randint(2,7)}"
f.write(new)
