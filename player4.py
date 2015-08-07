#Common base class for all Player0
class Player4:
    
   #This is the constructor for the class. It helps to allocate, instantiate,
   #each child in memory, and initializes the data members of the child object,
   #in this example, data members are model, color and passengerseats, mpg
   def __init__(self):
       pass
       
       
    
   #Defining functions for each child(instance) of class Car
   def strategy(self,history, opponent_history, score, opponent_score, getting_team_name):
        if getting_team_name:
            return 'reciprocator'
        else:
            # use history, opponent_history, score, opponent_score
            # to compute your strategy
            size = len(history)
            if(not ('b' in opponent_history) and size > 5):
                return 'c'
            elif(not ('c' in opponent_history) and size > 5):
                return 'b'
            elif(opponent_history[-1]=='c'): #the number of rounds played is a multiple of 3
                return 'c'
            else:
                return 'b'

   
