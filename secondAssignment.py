from random import randrange
import sys

input_str = input("Guess the number: ")
try:
	input_int = int(input_str)
	if input_int >10 or input_int<1:
		print("Only 1 to 10 is accepted")
		sys.exit()
except Exception as e:
	print("only accept integer.")
	# print "Error happened in script with %s"%e
	sys.exit()

irand = randrange(1, 10)
if irand == input_int:
	print("Correct!")
else:
	print("Wrong, try again! ")
	# print irand