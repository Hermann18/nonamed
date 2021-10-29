k = open("computerInput", "r").read()
with  open("computerInput", "w") as f:
    print(k)
    k = k.replace("diamat =True;", "diamat =False;")
    print(k)
    f.write(k)