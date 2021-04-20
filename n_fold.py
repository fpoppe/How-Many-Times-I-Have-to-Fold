import math

def main ():
    print("\n Welcome to 'HOW MANY TIMES DO I HAVE TO FOLD?' \n")
    distance = float(input("\n Give me the distance (a number) \n"))
    #usuário nao pode botar algo diferente de numero
    unit = input("Give me its unit (km, m or mm) \n")
    unit = unit.lower()
    while unit != "km" and unit != "m" and unit != "mm":
        print("\n Invalid Unit \n")
        unit = input()
        unit = unit.lower()
    n_fold = calculate_dist_fold(distance,unit)
    print("\n You have to fold your piece of paper " + str(n_fold) + " times to reach " + str(distance) + " " + unit + "\n\n")
    
def calculate_dist_fold(distance,unit):
    if unit == "km":
        thick = pow(10,-7)
        n_fold = math.log((distance/thick),2)
    elif unit == "m":
        thick = pow(10,-4)
        n_fold = math.log((distance/thick),2)
    else:
        thick = 0.1
        n_fold = math.log((distance/thick),2)
    n_fold = math.ceil(n_fold)
    return n_fold

main()
