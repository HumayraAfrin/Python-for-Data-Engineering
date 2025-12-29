# Function should return an integer value
class Solution:
    def convertFive(self, n):
        return int(str(n).replace('0', '5'))
