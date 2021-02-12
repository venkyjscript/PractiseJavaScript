class Human:
    cap=0
    tshirt=0
    hoodie=0
    name=""
    age=0
    height=0.0
    #def __init__(self):--> Human()

    def showDetails(self,obj):
        return "Hello "+obj.name+" your age= "+obj.age+" and height ="+obj.height

    def CalcRW(self,obj):
        return "Your RW is "+str((float(obj.height) - 100 + int(obj.age) % 10) * 0.90)
    def CalculateBill(self,obj):
        return (obj.cap*5)+(obj.tshirt*10)+(int(obj.hoodie)*20)
