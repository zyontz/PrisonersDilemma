#Common base class for all Player0
class Player14:
    
   
   #This is the constructor for the class. It helps to allocate, instantiate,
   #each child in memory, and initializes the data members of the child object,
   #in this example, data members are model, color and passengerseats, mpg
   def __init__(self):
       pass
       
       
    
   #Defining functions for each child(instance) of class Car
   def strategy(self,history, opponent_history, score, opponent_score, getting_team_name):
        import random
        if getting_team_name:
            return 'our branch is the best branch, your edits are unworthy'
        else:
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray is they were severely punished last time
            else:
                if random.random()<0.1: #10% of the other rounds
                    return 'b'         #betray
                else:
                    return 'c'         #otherwise collude
