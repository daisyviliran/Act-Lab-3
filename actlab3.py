def check_number(num):
	if num == 0:
		print("the number is zero")
	elif num % 2 == 0:
		print(f"{num} is even.")
	else:
		print(f"{num} is odd.")
		
while True:
	num = int(input("enter your number: "))
	check_number(num)