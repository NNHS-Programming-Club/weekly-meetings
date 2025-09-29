# problem: https://leetcode.com/problems/coin-change/

# don't worry about the imports
from typing import List


class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    # create dp array
    # dp[i] = minimum number of coins to make i dollars
    # in this case, 100000 means cannot find a case
    dp = [100000] * (amount+1)

    # base case
    dp[0] = 0

    # cycle through all the amounts
    for i in range(1, amount+1):
      # cycle through all coins
      for c in coins:
        # check if c is smaller or equal to i
        # if it's bigger we cannot use c (it would give runtime error)
        if c <= i:
          # dp formula
          dp[i] = min(dp[i], dp[i-c]+1)
    
    # we want to know the minimum number of coins to make "amount" dollars
    # the problem asks for -1 if cannot find a way
    if (dp[amount] == 100000):
      return -1
    else:
      return dp[amount]


# testing code    
coins = [1, 2, 5]
amount = 11

s = Solution()
print(s.coinChange(coins, amount))
