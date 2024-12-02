# Asteroid Collision
###### Author: Alan Tao

The link to the problem is: [https://leetcode.com/problems/asteroid-collision/description/](https://leetcode.com/problems/asteroid-collision/description/)

## Summary of Problem
Given an array of $N$ asteroids represented by integers, simulate the collisions. A positive integer means that the asteroid is moving right, and negative means that it is moving left. All asteroids move at the same speed. If two asteroids $a$ and $b$ collide, then the asteroid with a higher absolute value stays and the other asteroid disappears. 

Constraints:
$2 <= N <= 10^4$
`-1000 <= asteroids[i] <= 1000`
`asteroids[i] != 0`

## First Thoughts
Given that $N$ is no larger than $10^4$, we can have the time complexity of $N^2$. Some useful questions to ask ourselves are:
- What is the largest number of collisions we can have?
- How do we know if a collision is going to happen?
- How would we solve the problem as a human?
- What algorithms can we use to solve the problem? (binary search, two pointers, simulation, greedy)

## Observations
- We can have at most $N$ collisions because we remove an asteroid from each collision
- The first asteroids that would collide are the ones that are adjacent to each other, and the left one is positive and the right one is negative, like [..., 2, -4, ...]. 
- We can just use simulation to solve the problem in $N^2$ time. 

## Solution
Iterate through the array and find instances where two adjacent asteroids follow the pattern described above (left positive, right negative). Do this repeatedly until there are no asteroids left, or they are all facing the same way. It is also possible to do this recursively. Here is the pseudo-code for the iterative solution:

```
curAsteroids = asteroids
go = true
while go:
  go = false
  newAsteroids = []
  for i from 0 to N-1:
    if curAsteroids[i] is positive and curAsteroids[i+1] is negative:
      push the bigger asteroid to newAsteroids
      go = true
  curAsteroids = newAsteroids

return curAsteroids
```

See the two methods written in Python in this repo. 

## Conclusion
This is a slightly tricky and annoying simulation problem because we need to modify the array and keep track of when to stop. Sometimes the problem-makers are just interested in testing people's coding skills. It's important to always first check the constraints so you don't get off-track trying to think of a perfectly efficient solution. 
