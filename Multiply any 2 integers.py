def tt(table,startn,endn):
    for i in range(startn,endn+1):
        tt = table*i
        print(table,"times",i, "=",tt)
name = input("what is your name?")
print("Hi,",name)
while True:
    try:
        table = int(input("enter the times table you would like me to display:"))
        startnw = int(input("enter the first number you would like me to multiply:"))    
        endnw = int(input("enter the last number you would like me to multiply:"))
        tt(table,startnw,endnw)
        endorc = input("enter yes to continue,anything else to end")
        if endorc == "yes" or endorc =="Yes":
            continue
        else:
            print("Thank you for using this program")
            break
    except ValueError:
        print("You must enter an integer")
     
