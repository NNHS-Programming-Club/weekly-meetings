# USACO 2023 February Bronze - Hungry Cow
###### Author: Alan Tao

## Problem
The full problem is [here](https://usaco.org/index.php?page=viewproblem2&cpid=1299). 

Bessie the cow eats one haybale every day during dinner. There are `N` haybale deliveries that bessie will recieve on day $d_i$ with $b_i$ haybales. How many haybales will Bessie eat in `T` days?

### Constraints
$1 <= N <= 10^5$ <br />
$1 <= T <= 10^{14}$ <br />
$1 <= d_i <= 10^{14}$ <br />
$1 <= b_i <= 10^9$ <br />

## Solution 1 (Simulation)
We can solve the problem using simulation by cycling through all the days and checking if we have haybales to eat on day `i`. We can keep track of the haybales by putting $b_i$ haybales on day $d_i$ in a dictionary. We make a variable called `hay` that keeps track of how many haybales we have. We can update `hay` in the loop accordingly. This gives a time complexity of $O(T)$. Check solution1.py for more information. 

## Solution 2 (Optimized Simulation)
This solution is also siulation, but it doesn't simulate the days. We notice that we can only cycle through the `N` deliveries, which is at most $10^5$. We can do this by checking if we have enough haybales until the next delivery, and update our answer and current haybales accordingly. For example, if there are 4 days until the next delivery, and Bessie has 10 haybales, Bessie will eat 4, leaving her with 6 haybales. If Bessie had 2 haybales, she will eat 2 and starve on the next two days. This gives a complexity of $O(N)$. Check solution2.py for more information. 

## Conclusion
Although this problem didn't involve any algorithms, we still need to be careful about the time complexity. Specifically, we need to focus on the variables that are smaller and take advantage of those. 