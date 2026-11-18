#Nicole Ajjan, CMP-131, Week-09, Lab-01, November 17, 2026, Kinetic Energy

def kinetic_energy(m, v):
    ke = 0.5 * m * v * v
    return ke


def display(ke):
    print("The value for Kinetic Energy is", ke)


def main():
    m = float(input("Enter the mass: "))
    v = float(input("Enter the velocity: "))
    ke = kinetic_energy(m, v)
    display(ke)
		
		
main()
