class Solution:

  def addStrings(self, num1: str, num2: str) -> str:
    maxLen = max(len(num1), len(num2))

    # Normalize two number to the same number of elements
    for index in range(maxLen):
      if index >= len(num1):
        num1 = '0' + num1
      if index >= len(num2):
        num2 = '0' + num2

    print('num1', num1)
    print('num2', num2)

    ans = ''
    add = 0
    # Sum two numbers
    for index in range(maxLen):
      n1 = int(num1[index])
      n2 = int(num2[index])

      sumNum = n1 + n2 + add

      if n1 + n2 + add > 9:
        add = 1
      else:
        add = 0

      ans = str(sumNum % 10) + ans

    # Add last digit if exists
    if add > 0:
      ans = str(add) + ans

    return ans


my = Solution()

n1 = '650'
n2 = '55'
trueAns = '705'

n1 = '1000'
n2 = '9000'
trueAns = '10000'

ans = my.addStrings(n1, n2)
print("ans", ans, ans == trueAns)
"""

55
55
 0
1

60
50

"""
