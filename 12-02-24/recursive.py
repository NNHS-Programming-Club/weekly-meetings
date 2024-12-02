class Solution:
  def asteroidCollision(self, asteroids):
    n = len(asteroids)
    found = False

    # new array after collisions
    result = []

    # we don't use for loop because we want to change the i to skip some asteroids
    i = 0
    while (i < n):
      if i < n-1 and asteroids[i] > 0 and asteroids[i+1] < 0:
        # found target pair
        found = True
        if asteroids[i] > asteroids[i+1]*-1:
          # skip the next one
          result.append(asteroids[i])
          i+=1
        elif asteroids[i] == asteroids[i+1]*-1:
          # skip both
          i+=1
        # if we want to skip this one we just do nothing

      else:
        # no need to skip anything
        result.append(asteroids[i])

      i+=1
    
    # found keeps track of if we are done or not
    if not found:
      return result
    else:
      return self.asteroidCollision(result)
