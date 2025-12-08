# introductory function
def rec(a, b, n):
    if (n == 1):
        return a
    else:
        return rec(b, (a + b), (n - 1))
print(rec(1, 1, 6))

# Leetcode problem 390: Elimination Game
def elimination(start, end, step, direction):
    if direction > 0:
        direction = 1
    else:
        direction = -1

    if (((((end - start)/step*direction) + 1) % 2) == 1): # if the amount of numbers are odd
        if (start == end):
            return start
        else:
            newEnd = end - step*direction
    else:
        newEnd = end

    return(elimination(newEnd, (start + (step * direction)), (step * 2), (direction * -1)))

print(elimination(1, 8, 1, 1))