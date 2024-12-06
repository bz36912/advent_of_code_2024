import numpy as np
file1 = open("day3/input.txt", "r")

answer = 0
toEnd = False
text = "   "
text2 = "       "
toContinue = False
enable = True

while not toEnd:
    toContinue = False
    while True:
        c = file1.read(1)
        if c == "":
            toEnd = True
            break
        text = text[1:] + c
        if text == "mul":
            break

        text2 = text2[1:] + c
        if text2 == "don't()":
            enable = False
        elif text2[-4:] == "do()":
            enable = True
    
    if toEnd:
        break

    content = ""
    while True:
        c = file1.read(1)
        if c == "":
            toEnd = True
            break
        text = text[1:] + c
        content += c
        text2 = text2[1:] + c
        if text2 == "don't()":
            enable = False
        elif text2[-4:] == "do()":
            enable = True
        if c == ")":
            break
        if text == "mul":
            content = ""
        
    
    print(content)
    try:
        t = eval(content)
        if enable:
            answer += int(t[0]) * int(t[1])
    except:
        pass

print(f"ans: {answer}")
print("end")