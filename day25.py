from collections import defaultdict
'''Begin in state A.
Perform a diagnostic checksum after 12523873 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state E.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state C.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state F.

In state C:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state D.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state B.

In state D:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state E.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state C.

In state E:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state D.

In state F:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state C.'''
a='''Begin in state A.
Perform a diagnostic checksum after 12523873 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state E.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state C.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state F.

In state C:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state D.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state B.

In state D:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state E.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state C.

In state E:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state D.

In state F:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state C.'''

# conditions = dict()
# for i in a.split("\n"):
#     if "In state" in i:
#         conditions[i[-2]] = {} 

state = "A"
tape = [0] * 100000 
pos = len(tape) // 2
# print(tape)
for i in range(12523873):
    if state == "A":
        if tape[pos] == 0:
            tape[pos] = 1
            pos += 1
            state = "B"
        elif tape[pos] == 1:
            tape[pos] = 1
            pos -= 1
            state = "E"
    elif state == "B":
        if tape[pos] == 0:
            tape[pos] = 1
            pos += 1
            state = "C"
        elif tape[pos] == 1:
            tape[pos] = 1
            pos += 1
            state = "F"
    elif state == "C":
        if tape[pos] == 0:
            tape[pos] = 1
            pos -= 1
            state = "D"
        elif tape[pos] == 1:
            tape[pos] = 0
            pos += 1
            state = "B"
    elif state == "D":
        if tape[pos] == 0:
            tape[pos] = 1
            pos += 1
            state = "E"
        elif tape[pos] == 1:
            tape[pos] = 0
            pos -= 1
            state = "C"
    elif state == "E":
        if tape[pos] == 0:
            tape[pos] = 1
            pos -= 1
            state = "A"
        elif tape[pos] == 1:
            tape[pos] = 0
            pos += 1
            state = "D"
    elif state == "F":
        if tape[pos] == 0:
            tape[pos] = 1
            pos += 1
            state = "A"
        elif tape[pos] == 1:
            tape[pos] = 1
            pos += 1
            state = "C"
    if i % 10000 == 0:
        print(i)

print(sum(tape))
#part 1 done in 17:56, typo that led to double checking the whole thing