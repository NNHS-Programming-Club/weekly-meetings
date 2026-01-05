import random
LEN = 5

def round(guesses):
  pos = random.randint(1, LEN)
  for g in guesses:
    if (pos == g):
      return True
    if (pos == 1):
      pos = 2
    elif (pos == LEN):
      pos = LEN-1
    else:
      if (random.randint(0, 1) == 0):
        pos -= 1
      else:
        pos += 1
  return False

guesses = list(map(int, input("Space seperated guesses: ").split()))
sim = int(input("How many simulations: "))


for _ in range(sim):
  if (not round(guesses)):
    print("Escaped")

