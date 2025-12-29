class Solution:
	def countOddEven(self, arr):
		odd_count = 0
    even_count = 0

    for l in arr:
        if l%2 == 0:
            even_count += 1
        elif l%2 == 1:
            odd_count += 1
    return odd_count, even_count
