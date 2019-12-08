class Area:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def rectangle(self):
        return self.a*2*self.b
    def square(self):
        return self.a**2
    def trainagle(self):
        return 0.5*self.a*self.b

fn=float(input("enter first number: "))
sn=float(input("enter second number "))
area=Area(fn,sn)

def main():
    print "enter choice to find area for \n 1.rectangle \n 2.square \n 3.triangle"
    choice=int(input("enter your choice"))
    while choice!=0:
        if choice==1:
            print "rectangle area is: ", area.rectangle()
        elif choice==2:
            print "square area is: ", area.square()
        elif choice==3:
            print "triangle area is: ", area.trainagle()
        else:
            print "invalid choice"
        break

    print "do you want to continue? (y/n) "
    option = input("enter y if you want to continue:")

    if option == 'y':
        main()
    else:
        print "thank you for playing"

main()





"""print "do you want to continue? (y/n) "
option=input("enter y if you want to continue:")
while option!='n':
    main()"""
