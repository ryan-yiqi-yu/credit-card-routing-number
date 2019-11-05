"""This program allows us to determine if user entered
credit card and routing numbers are valid"""


def is_valid_CC(ccnum: str) -> bool:
    """This function determines if credit card numbers are valid"""
    tot = tot2 = 0
    l = list(ccnum)
    for i in l[-1::-2]:
        tot += int(i)
    for j in l[-2::-2]:
        list2 = []
        list2 = [int(d) for d  in str(2*int(j))]
        tot2 += sum(list2)
    return (tot2 + tot) % 10 == 0

def is_valid_RN(rn: str) -> bool:
    """This function determines if routing numbers are valid"""
    if len(rn) != 9:
        return false
    l = list(rn)
    tot = tot2 = tot3 = 0
    for i in l[-1::-3]:
        tot += int(i)
    for i in l[-2::-3]:
        tot2 += 7*int(i)
    for i in l[-3::-3]:
        tot3 += 3*int(i)
    return (tot+tot2+tot3)%10 == 0
    
    
if __name__ == "__main__":
    
    print (__doc__)
    print()
    
    user = input("enter credit card number ")

    while user != "q":
        
        if is_valid_CC(user):
            print(user + " is valid")
        else:
            print(user + " is not valid")
        print()
        user = input("enter credit card number ")

    user = input("enter routing number ")

    while user != "q":
        
        if is_valid_RN(user):
            print(user + " is valid")
        else:
            print(user + " is not valid")
        print()
        user = input("enter routing number ")

    print()
    input("press enter to continue...")
    functions = [is_valid_RN, is_valid_CC]
    for x in functions:
        print()
        print (x.__name__)
        print (x.__doc__)
        print (x.__annotations__)
        
    
            


      
    
