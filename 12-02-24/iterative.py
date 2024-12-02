class Solution:
  def asteroidCollision(self, asteroids):
    # this array will change
    curAsteroids = asteroids
    go = True
    while go:
      go = False
      n = len(curAsteroids)

      # new array after collision
      newAsteroids = []

      i = 0
      while i < n:
        if i < n-1 and curAsteroids[i] > 0 and curAsteroids[i+1] < 0:
          # found target pair
          go = True
          if curAsteroids[i] > curAsteroids[i+1]*-1:
            # skip the next one
            newAsteroids.append(curAsteroids[i])
            i+=1
          elif curAsteroids[i] == curAsteroids[i+1]*-1:
            # skip both
            i+=1
          # if we want to skip this one we just do nothing

        else:
          # no need to skip anything
          newAsteroids.append(curAsteroids[i])

        i+=1
      
      # replace old array with new array
      curAsteroids = newAsteroids

    return curAsteroids
