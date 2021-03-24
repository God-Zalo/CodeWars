
def RowCalculator(n):
	# First number of each row
	a=(n*n)-(n-1)
	c = a

	# Calculate and sum remaining numbers
	for n in range(n-1):
		a = a+2
		c = c+a
	print('The total sum is: ' + str(c))

print('Select the row to be calculated')

n = int(input())

RowCalculator(n)
