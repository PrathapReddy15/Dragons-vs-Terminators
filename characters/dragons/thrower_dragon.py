from .dragon import Dragon
from utils import random_or_none


class ThrowerDragon(Dragon):
    """ThrowerDragon throws a stone each turn at the nearest Terminator in its range."""

    name = 'Thrower'
    implemented = True
    damage = 1
    food_cost = 3
    min_range=0
    max_range=float('inf')
    def nearest_terminator(self, skynet):
        min_range=self.min_range
        max_range=self.max_range
        j=0
    # ADD/OVERRIDE CLASS ATTRIBUTES HERE

        temp = self.place
        if min_range!=0:
            for i in range(0,min_range):
                temp=temp.entrance
        while(temp!= skynet):
            if len(temp.terminators)!= 0:
                return random_or_none(temp.terminators)
            else:
                if j!=(max_range-min_range):
                    temp=temp.entrance
                    j=j+1
                else:
                    break
                
        if temp == skynet:
            return None 

    def throw_at(self, target):
        """Throw a stone at the TARGET Terminator, reducing its armor."""
        if target is not None:
            target.reduce_armor(self.damage)

    def action(self, colony):
        """Throw a stone at the nearest Terminator in range."""
        self.throw_at(self.nearest_terminator(colony.skynet))
