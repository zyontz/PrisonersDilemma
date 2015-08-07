#Common base class for all Player0
class Player2:
    
   #This is the constructor for the class. It helps to allocate, instantiate,
   #each child in memory, and initializes the data members of the child object,
   #in this example, data members are model, color and passengerseats, mpg
   def __init__(self):
       pass
       
       
    
   #Defining functions for each child(instance) of class Car
   def strategy(self,history, opponent_history, score, opponent_score, getting_team_name):
        if getting_team_name:
            return 'loyal most of the time'
       else:
            if len(opponent_history) == 0: #It's the first round: collude
                return 'c'
            elif  len(opponent_history) > 3 and opponent_history[-1]=='b'and opponent_history[-2]=='b' :
                return 'b' # patient and optimistic
            else:
                return 'c' #otherwise collude

   
