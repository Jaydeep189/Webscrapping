#This is Algorithm for truth
sub_obj = '' 
print("The Truth Finder!")
def Truth_step_1():
    q1 = input("Do you know the concept of objective/Subjective things? (y/n) : ")
    if q1 == 'n' or q1 == 'N':
        print("Subjective : based on or influenced by personal feelings, tastes, or opinions.\nObjective : not influenced by personal feelings or opinions in considering and representing facts")
        sub_obj = input("The Truth you want to find is objective or Subjective (O = Objective / S = Subjective) :")
        
    elif q1 == 'y' or q1 == 'Y':    
        sub_obj = input("The Truth you want to find is objective or Subjective (O = Objective / S = Subjective) :")
    else:
        print("Enter in y/n Format")  
        Truth_step_1() 
    return sub_obj         


def Truth_step_2():     
    if sub_obj == 'S' or sub_obj == 's':
        print("All that you feel subjectively is merely a byproduct of your attachments to people and object that you love or hate\n" + 
        "The subjective truth that you want to find lies within you, There is no other forces in the world that can answer those question other than you.")  
          
    elif sub_obj == 'O' or sub_obj == 'o':
        Truth_step_3()

    else:
        print("Enter in y/n format")
        Truth_step_2()        
 
def Truth_step_3():
    q2 = input("Does the objective truth stay true across multiple oberservations? (y/n)")
    if q2 == 'y' or q2 == 'Y':
        Truth_step_4()

    elif q2 == 'n' or q2 == 'N':    
            print("If it does'nt repeat itself across obervations, then it won't be considered truth. \nHence it's not true.")
    else:
        print("Enter in y/n format")
        Truth_step_3()

def Truth_step_4():
    q3 = input("Your Obervations are golbally True? \nAcross different cultures and races? (y/n)")
    if q3 == 'y' or q3 == 'Y':
        print("It's True")
    elif q3 == 'n' or q3 == 'N':
        print("It's not True")    
    else:
        print("Enter in y/n format")
        Truth_step_4()        

Truth_step_1()        
Truth_step_2()