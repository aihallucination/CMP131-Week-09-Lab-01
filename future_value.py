#Nicole Ajjan, CMP-131, Week-09, Lab-01, November 17, 2026, Future Value

def future_value (P, i, t):
	F= P * (1 + i)**t
	return (F)


def display (F):
	print ("The future value is ", F)
	

def main():
	P = (int(input("Please enter the present value: ")))
	i = (float(input("Please enter the monthly interest rate: ")))	
	t = (int(input ("Please enter the number of months: ")))
	F = future_value (P, i, t)
	display (F)
	
	
	main()