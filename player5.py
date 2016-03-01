#Common base class for all Player0
class Player5:
    
   #This is the constructor for the class. It helps to allocate, instantiate,
   #each child in memory, and initializes the data members of the child object,
   #in this example, data members are model, color and passengerseats, mpg
   def __init__(self):
       pass
       
       
    
   #Defining functions for each child(instance) of class Car
   def strategy(self,history, opponent_history, score, opponent_score, getting_team_name):
        if getting_team_name:
            return 'I have no loyalty HAHAHAHAHA'
        else:
            # use history, opponent_history, score, opponent_score
            # to compute your strategy
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray is they were severely punished last time
            else:
                return 'c' #otherwise collude

   
#Common base class for all Player0
class Player6:
    
   #This is the constructor for the class. It helps to allocate, instantiate,
   #each child in memory, and initializes the data members of the child object,
   #in this example, data members are model, color and passengerseats, mpg
   def __init__(self):
       pass
       
       
    
   #Defining functions for each child(instance) of class Car
   def strategy(self,history, opponent_history, score, opponent_score, getting_team_name):
        if getting_team_name:
            return 'loyal vengeful'
        else:
            # use history, opponent_history, score, opponent_score
            # to compute your strategy
            if len(opponent_history)==0: #It's the first round: collude
                return 'c'
            elif history[-1]=='c' and opponent_history[-1]=='b':
                return 'b' # betray is they were severely punished last time
            else:
                return 'c' #otherwise collude
                collude #4
                
            return 'player 4'
                tuple 4
                get_action 'player 2'
                if player ==5 
                return 'c' 
                elif history [-2] == 'c' and opponent_history[-2] =='b':
                def_init_(self)
                    pass
                player6_ 
                if len(opponent
                class TitForTat(Player):
    """ A player starts by cooperating and then mimics previous move by opponent. """
    def strategy(self, opponent):
        """ Begins by playing 'C': This is affected by the history of the opponent: the strategy simply repeats the last action of the opponent """
        try:
            return opponent.history[-1]
        except IndexError:
            return 'C'

    def __repr__(self):
        """ The string method for the strategy. """
        return 'Tit For Tat'
            

    name = 'Punisher'

    def __init__(self):
        """
        Initialised the player
        """
        super(Punisher, self).__init__()
        self.history = []
        self.score = 0
        self.mem_length = 1
        self.grudged = False
        self.grudge_memory = 1

    def strategy(self, opponent):
        """
        Begins by playing C, then plays D for an amount of rounds proportional to the opponents historical '%' of playing 'D' if the opponent ever plays D
        """

        if self.grudge_memory >= self.mem_length:
            self.grudge_memory = 0
            self.grudged = False

        if self.grudged:
            self.grudge_memory += 1
            return 'D'
        elif 'D' in opponent.history[-1:]:
            self.mem_length = (sum([i == 'D' for i in opponent.history])*20)/len(opponent.history)
            self.grudged = True
            return 'D'
        return 'C'

    def reset(self):
        """
        Resets scores and history
        """
        self.history = []
        self.grudged = False
        self.grudge_memory = 0
        self.mem_length = 1


class InversePunisher(Player):
    if score<100==collude

    """

    name = 'Inverse Punisher'

    def __init__(self):
        """
        Initialised the player
        """
        super(InversePunisher, self).__init__()
        self.history = []
        self.score = 0
        self.mem_length = 1
        self.grudged = False
        self.grudge_memory = 1

    def strategy(self, opponent):
        """
        Begins by playing C, then plays D for an amount of rounds proportional to the opponents historical '%' of playing 'C' if the opponent ever plays D
        """

        if self.grudge_memory >= self.mem_length:
            self.grudge_memory = 0
            self.grudged = False

        if self.grudged:
            self.grudge_memory += 1
            return 'D'
        elif 'D' in opponent.history[-1:]:
            self.mem_length = ((sum([i == 'C' for i in opponent.history]))*20)/len(opponent.history)
            if self.mem_length == 0:
                self.mem_length += 1
            self.grudged = True
            return 'D'
        return 'C'

    def reset(self):
        """
        Resets scores and history
        """
        self.history = []
        self.grudged = False
        self.grudge_memory = 0
        self.mem_length = 1
        class Retaliate(Player):
    """
    A player starts by cooperating but will retaliate once the opponent
    has won more than 10 percent times the number of defections the player has.
    """
    retaliation_threshold = 0.1

    def __init__(self):
        """
        """
        Player.__init__(self)
        self.name = (
            'Retaliate (' +
            str(self.retaliation_threshold) + ')')

    def strategy(self, opponent):
        """
        If the opponent has played D to my C more often than x% of the time
        that I've done the same to him, play D. Otherwise, play C.
        """
        history = zip(self.history, opponent.history)
        if history.count(('C', 'D')) > (
           history.count(('D', 'C')) * self.retaliation_threshold):
            return 'D'
        return 'C'


class Retaliate2(Retaliate):
    """ :code:`Retaliate` player with a threshold of 8 percent.
    """
    retaliation_threshold = 0.08


class Retaliate3(Retaliate):
    """ :code:`Retaliate` player with a threshold of 5 percent.
    """
    retaliation_threshold = 0.05


class LimitedRetaliate(Player):
    """
 
    retaliation_limit = 20
    retaliation_threshold = 0.1
    retaliating = False
    retaliation_count = 0

    def __init__(self):
        """
        Uses the basic init from the Player class, but also set the name to
        include the retaliation setting.
        """
        Player.__init__(self)
        self.name = (
            'Limited Retaliate (' +
            str(self.retaliation_threshold) +
            '/' + str(self.retaliation_limit) + ')')

    def strategy(self, opponent):
        """
        If the opponent has played D to my C more often than x% of the time
        that I've done the same to him, retaliate by playing D but stop doing
        so once I've hit the retaliation limit.
        """
        history = zip(self.history, opponent.history)
        if history.count(('C', 'D')) > (
           history.count(('D', 'C')) * self.retaliation_threshold):
            self.retaliating = True
        else:
            self.retaliating = False
            self.retaliation_count = 0

        if self.retaliating:
            if self.retaliation_count < self.retaliation_limit:
                self.retaliation_count += 1
                return 'D'
            else:
                self.retaliation_count = 0
                self.retaliating = False

        return 'C'

    def reset(self):
        Player.reset(self)
        self.retaliating = False
        self.retaliation_count = 0

class LimitedRetaliate2(LimitedRetaliate):
    """ :code:`LimitedRetaliate` player with a threshold of 8 percent and a
    retaliation limit of 15.
    """
    retaliation_limit = 15
    retaliation_threshold = 0.08


class LimitedRetaliate3(LimitedRetaliate):
    """ :code:`LimitedRetaliate` player with a threshold of 5 percent and a
    retaliation limit of 20.
    """
    retaliation_limit = 20
    retaliation_threshold = 0.05
