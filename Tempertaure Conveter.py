class Converter():
    def cel_to_kel(self):
        # Celsius to Kelvin
        self.celsius = float(input("Enter Celsius = "))
        self.kelvin = self.celsius + 273.15
        print("="*40)
        print("Kelvin =", self.kelvin)
        print("="*40)

    def kel_to_cel(self):
        # Kelvin to Celsius
        self.kelvin = float(input("Enter Kelvin = "))
        self.celsius = self.kelvin - 273.15
        print("="*40)
        print("Celsius =", self.celsius)
        print("="*40)

    def far_to_kel(self):
        # Fahrenheit to Kelvin
        self.fahrenheit = float(input("Enter Fahrenheit = "))
        self.kelvin = (self.fahrenheit + 459.67) * 5/9
        print("="*40)
        print("Kelvin =", self.kelvin)
        print("="*40)

    def kel_to_far(self):
        # Kelvin to Fahrenheit
        self.kelvin = float(input("Enter Kelvin = "))
        self.fahrenheit = (self.kelvin - 273.15) * 9/5 + 32
        print("="*40)
        print("Fahrenheit =", self.fahrenheit)
        print("="*40)

    def cel_to_far(self):
        # Celsius to Fahrenheit
        self.celsius = float(input("Enter Celsius = "))
        self.fahrenheit = (self.celsius * 9/5) + 32
        print("="*40)
        print("Fahrenheit =", self.fahrenheit)
        print("="*40)

    def far_to_cel(self):
        # Fahrenheit to Celsius
        self.fahrenheit = float(input("Enter Fahrenheit = "))
        self.celsius = (self.fahrenheit - 32) * 5/9
        print("="*40)
        print("Celsius =", self.celsius)
        print("="*40)


x = 1
c = Converter()
while x != 7:
    print("1. Celsius to Kelvin")
    print("2. Kelvin to Celsius")
    print("3. Fahrenheit to Kelvin")
    print("4. Kelvin to Fahrenheit")
    print("5. Celsius to Fahrenheit")
    print("6. Fahrenheit to Celsius")
    print("7. EXIT")
    x = int(input("Enter Your Choice From 1 to 7: "))
    match x:
        case 1:
            c.cel_to_kel()
        case 2:
            c.kel_to_cel()
        case 3:
            c.far_to_kel()
        case 4:
            c.kel_to_far()
        case 5:
            c.cel_to_far()
        case 6:
            c.far_to_cel()
        case 7:
            print("Exiting...")
        case _:
            print("Invalid Choice, Try Again")
