from queue import Queue

A, B, C = 4, 5, 6
combo = {0:0, 1:1, 2:2, 3:3, A:30899381, B:0, C:0}
# 117440
output = []
def adv(operand):
    dem = 2**combo[operand]
    combo[A] //= dem

def bxl(operand):
    combo[B] = operand ^ combo[B]

def bst(operand):
    combo[B] = combo[operand] % 8

def jnz(operand):
    print("shouldn't reach here")
    pass

def bxc(operand):
    combo[B] = combo[C] ^ combo[B]

def out(operand):
    output.append(combo[operand] % 8)

def bdv(operand):
    dem = 2**combo[operand]
    combo[B] = combo[A] // dem

def cdv(operand):
    dem = 2**combo[operand]
    combo[C] = combo[A] // dem

operations = {0:adv, 1:bxl, 2:bst, 3:jnz, 4:bxc, 5:out, 6:bdv, 7:cdv}

file = open("day17/input.txt", "r")
text = file.read()
vals = [int(c) for c in text.split(",")]

def oneCycle2(a:int, b:int):
    global vals, output
    output = []
    i = 0
    combo = {0:0, 1:1, 2:2, 3:3, A:a, B:b, C:0}
    while i < len(vals) - 2:
        if vals[i] == 3: # the jump (jnz) opcode
            if combo[A] == 0:
                i += 2
            else:
                i += 2
                # i = vals[i+1]
            continue
        operations[vals[i]](vals[i+1])
        i += 2
    return output

# 2,4, 1,1, 7,5, 4,0, 0,3, 1,6,5,5,3,0
# {0:adv, 1:bxl, 2:bst, 3:jnz, 4:bxc, 5:out, 6:bdv, 7:cdv}
def oneCycle(a:int, b:int):
    global combo
    combo = {0:0, 1:1, 2:2, 3:3, A:a, B:b, C:0}
    bst(4)
    bxl(1)
    cdv(5)
    bxc(0)
    adv(3)
    bxl(6)
    return combo[B] % 8

# toSearch = Queue()
# toSearch.put((0, len(vals) - 1))
# while not toSearch.empty():
#     aOffset, idx = toSearch.get()
#     if idx < 0:
#         continue
#     for a in range(aOffset, aOffset + 8):
#         if idx == 0:
#             ans = oneCycle(a, 0)
#             if ans == vals[idx]:
#                 print(f"when idx = 0, a = {a}, b = 0")
#         else:
#             ans = oneCycle(a, vals[idx - 1])
#             if ans == vals[idx]:
#                 toSearch.put((a * 8, idx - 1))

ans = []
combo = {0:0, 1:1, 2:2, 3:3, A:247839653009594, B:0, C:0}
for a in range(16-0):
    ans.append(oneCycle(combo[A], combo[B]))
print(ans)

# output = [str(c) for c in output]
# joined = ",".join(output)

# print(joined == text, joined)
print("end")
# 2,4,1,1,7,5,4,0,0,3,1,6,5,5,3,0

# length of 16 from: 33989319100000 to 304350642697910