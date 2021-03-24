
def RowCalculator(x):
	# First number of each row
	n=(x*x)-(x-1)
	c = n

	# Calculate and sum remaining numbers
	for x in range(x-1):
		n = n+2
		c = c+n
	print('The total sum is: ' + str(c))

print('Select the row to be calculated')

a = int(input())

RowCalculator(a)
