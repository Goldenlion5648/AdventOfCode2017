from collections import Counter
a='''set b 99
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23'''

positions = Counter([chr(i) for i in range(97, 97 + 8)])
for i in positions:
    positions[i] -= 1
print(positions)
instructs = a.split("\n")
curInstruct = 0
# for i in instructs:
count = 0
while curInstruct < len(instructs):
    i = instructs[curInstruct]
    inst, b, c = i.split(" ")
    jumped = False
    try:
        b = int(b)
    except:
        pass
    try:
        c = int(c)
    except:
        pass
    if inst == "set":
        if type(b) == type(2):
            positions[chr(b)+97] = c if type(c) == type(3) else positions[c]
        else:
            positions[b] = c if type(c) == type(3) else positions[c]
    elif inst == "sub":
        if type(b) == type(2):
            positions[chr(b)+97] -= c if type(c) == type(3) else positions[c]
        else:
            positions[b] -= c if type(c) == type(3) else positions[c]
    elif inst == "mul":
        if type(b) == type(2):
            positions[chr(b)+97] *= c if type(c) == type(3) else positions[c]
        else:
            positions[b] *= c if type(c) == type(3) else positions[c]
        count += 1
    elif inst == "jnz":
        if type(b) == type(2):
            if b != 0:
                curInstruct += c if type(c) == type(3) else positions[c]
                jumped = True
        else:
            if positions[b] != 0:
                curInstruct += c if type(c) == type(3) else positions[c]
                jumped = True
    if jumped == False:
        curInstruct += 1

print(count)
#part 1 done in 16:57, worked first try