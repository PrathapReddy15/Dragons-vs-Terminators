from .bodyguard_dragon import BodyguardDragon
from .dragon import Dragon


class TankDragon(BodyguardDragon):
    """TankDragon provides both offensive and defensive capabilities."""
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 3.3
    implemented = True
    is_container = True # Change to True to view in the GUI
    food_cost = 6
    damage = 1
    # END 3.3
    armor = 2
    contained_dragon = None
    def __init__(self, armor=2):
        """Create a Dragon with a ARMOR quantity."""
        Dragon.__init__(self, armor)
        

    def action(self, colony):
        tmt=[i for i in self.place.terminators]
        j=[]
        for i in tmt:
             i.reduce_armor(self.damage)
        for i in tmt:
            if i.armor>0:
                j.append(i)
        self.place.terminators=j
        if self.contained_dragon:
            self.contained_dragon.action(colony)
