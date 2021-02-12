from foo import Human


h= Human()
h.cap=int(input("enter no of caps"))
h.tshirt=int(input("enter no of tshirts"))
h.hoodie=input(" enter no of hoodies")

#print(h.showDetails(h))
#print(78.6)
print( "your total bill is "+h.CalculateBill(h))