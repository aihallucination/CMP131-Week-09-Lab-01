#Nicole Ajjan, CMP-131, Week-09, Lab-01, Celsius Temp Table, 11/17/26

def celsius(fahrenheit):
	cel=(fahrenheit -32) * (5/9)
	return cel 
	
	
def display (cel, farenheit):
	print("Given the Farenheit temperature: ", farenheit, ", the converted temperature is: ", "Celsius", cel) 


def main(): 
	for farenheit in range(21): 
		celsius(farenheit) 
	farenheit=float(input("Enter the temperature in Farenheit: ")) 
	cel=celsius(farenheit) 
	display(cel,farenheit)
	
	 
main()