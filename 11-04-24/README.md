# DP - Intro
###### Author: Alan Tao

## Fibonacci Sequence
We introduced dp with fibonacci sequence first
The sequence is:
1, 1, 2, 3, 5, 8, 13...

Recursion would give us $O(2^N)$, which is really slow

So we came up with dp (this one is very straightforward)

```python
dp[i] = dp[i-1] + dp[i-2]
```

And the time complexity becomes $O(N)$.

## 322. Coin Change
We then move on to a harder problem called [Coin Change](https://leetcode.com/problems/coin-change/description/).

The dp for that is:
```python
dp[i] = min(dp[i], dp[i-c] + 1)
```

where dp[i] means the smallest number of coins to make i dollars, and c means all the possible coins. We are trying every single coin and only keeping the minimum amount. 

For this one, we need to cycle through the coins while iterating through the dp array, resulting in a double for loop. 
```python
for i in range(1, amount):
  for c in coins:
    dp[i] = min(dp[i], dp[i-c] + 1)
```

Time complexity is $O(NC)$, where $N$ is the amount and $C$ is the number of coins. 

## Conclusion
Yeah that's pretty much it... dp is a relatively hard concept to grasp, but y'all chose it over graph theory so we'll just do an intro for this meeting. 