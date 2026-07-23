def Tip():
    bill=int(input("Enter Bill Ammount="))
    tip_per=float(input("Enter Tip Percentage="))
    print("Bill Without Tip=",bill)
    tip=bill*(tip_per/100)
    bill=bill+tip
    print("Bill With Tip=",bill)
Tip()