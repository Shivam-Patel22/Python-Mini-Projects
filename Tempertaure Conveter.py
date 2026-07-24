class Converter():
    def Kel_cel(self):
        #1.Celsuis to Kelvin
        self.celsius=float(input("Enter Celsius="))
        self.kelvin=self.celsius+273.15
        print("="*40)
        print("Kelvin=",self.kelvin)
        print("="*40)
    def Cel_Kel(self):
        #Kelvin to Celsuis
        self.kelvin=float(input("Enter Kelvin="))
        self.celsius=self.kelvin-273.15
        print("="*40)
        print("Celsius=",self.celsius)
        print("="*40)
    def Kel_far(self):
        #Fareheit to Kelvin
        self.fareheit=float(input("Enter Farenheit="))
        self.kelvin=(self.fareheit+459.67)*5/9
        print("="*40)
        print("Kelvin=",self.kelvin)
        print("="*40)
    def Far_kel(self):
        #Kelvin to Fareheit
        self.kelvin=float(input("Enter Kelvin="))
        self.fareheit = (self.kelvin - 273.15) * 9/5 + 32
        print("="*40)
        print("Fareheit=",self.fareheit)
        print("="*40)
    def Cal_far(self):
        #Celsuis to Fareheit
        self.celsuis=float(input("Enter Celsius="))
        self.fareheit=(self.celsuis*9/5)+32
        print("="*40)
        print("Fareheit=",self.fareheit)
        print("="*40)
    def Far_cal(self):
        #Fareheit to Celsuis
        self.fareheit=float(input("Enter Farenheit="))
        self.celsuis=(self.fareheit-32)/(9/5)
        print("="*40)
        print("Celsuis=",self.celsuis)
x=1
c=Converter()
while x!=7:
    print("1.Celsuis to Kelvin")
    print("2.Kelvin to Celsuis")
    print("3.Fareheit to Kelvin")
    print("4.Kelvin to Fareheit")
    print("5.Celsuis to Fareheit")
    print("6.Fareheit to Celsuis")
    print("7.EXIT")
    x=int(input("Enter Your Choice From 1 to 6:"))
    match x:
        case 1:
            c.Kel_cel()
        case 2:
            c.Cel_Kel()
        case 3:
            c.Kel_far()
        case 4:
            c.Far_kel()
        case 5:
            c.Cal_far()
        case 6:
            c.Far_cal()
        case 7:
            x=7
        case _:
            print("Invalid Choice,Try Again")




