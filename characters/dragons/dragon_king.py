from .dragon import Dragon
from .scuba_thrower import ScubaThrower
from ..fighter import Fighter
from utils import terminators_win

class DragonKing(ScubaThrower):  # You should change this line
    # END 4.3
    """The King of the colony. The game is over if a terminator enters his place."""

    name = 'King'
    instanciated = False
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 4.3
    implemented = True # Change to True to view in the GUI
    food_cost = 7
    armor = 1
    # END 4.3
    buffed_list = []
    def __init__(self, armor=1):
        # BEGIN 4.3
        Dragon.__init__(self, armor)
        self.isdragonking=False
        if DragonKing.instantiated==False:
            self.isdragonking=True
            DragonKing.instantiated=True
        # END 4.3

    def action(self, colony):
        """A dragon king throws a stone, but also doubles the damage of dragons
        in his tunnel.

        Impostor kings do only one thing: reduce their own armor to 0.
        """
        # BEGIN 4.3
        if not self.isdragonking:
            self.reduce_armor(self.armor)
        else:
            temp = self.place.exit 
            while(temp!=None):
                if temp.dragon is not None:
                    if temp.dragon not in self.buffed_list:
                        temp.dragon.damage=2*temp.dragon.damage
                        self.buffed_list.append(temp.dragon)
                    if temp.dragon.is_container:
                        if temp.dragon.contained_dragon is not None:
                            if temp.dragon.contained_dragon not in self.buffed_list:
                                temp.dragon.contained_dragon.damage=2*temp.dragon.contained_dragon.damage
                                self.buffed_list.append(temp.dragon.contained_dragon)
                temp=temp.exit
            super().action(colony)
        # END 4.3

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and if the True DragonKing has no armor
        remaining, signal the end of the game.
        """
        Fighter.reduce_armor(self, amount)
        if self.armor <= 0 and self.isdragonking:
            terminators_win()
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
