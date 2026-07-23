class Converter():
    def __init__(self,celsius,kelvin,fareheit):
        self.celsius=celsius
        self.kelvin=kelvin
        self.fareheit=fareheit
    def Kel_cel(self):
        self.kelvin=self.celsius+273.15
        print("Kelvin=",self.kelvin)
    def Cel_Kel(self):
        self.celsius=self.kelvin-273.15
        print("Celsius=",self.celsius)
    def Kel_far(self):
        self.kelvin=(self.fareheit+459.67)*5/9
        print("Kelvin=",self.kelvin)
    def Far_kel(self):
        self.fareheit=(self.kelvin*5/9)-459.67
        print("Fareheit=",self.fareheit)
    def Far_cal(self):
        self.fareheit=(self.celsuis*9/5)+32
        print("Fareheit=",self.fareheit)
    def Cal_far(self):
        self.celsuis=(self.farenheit-32)/(9/5)
        print("Celsuis=",self.celsuis)
x=1
while x!=4:
    print("1.Celsuis to Kelvin")
    print("2.Kelvin to Celsuis")
    print("3.Kelvin to Fareheit")
    print("4.Fareheit to Kelvin")
    print("5.Fareheit to Celsuis")
    print("6.Celsuis to Fareheit")
    x=int(input("Enter Your Choice From 1 to 6:"))
    match x:
        case 1:
            celsuis



