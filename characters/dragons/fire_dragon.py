from .dragon import Dragon


class FireDragon(Dragon):
    """FireDragon cooks any Terminator in its Place when it expires."""

    name = 'Fire'
    damage = 3
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.2
    implemented = True  # Change to True to view in the GUI
    food_cost=5
    armor=3
    # END 2.2

    def __init__(self, armor=3):
        """Create a Dragon with a ARMOR quantity."""
        Dragon.__init__(self, armor)

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and remove the FireDragon from its place if it
        has no armor remaining.

        Make sure to damage each terminator in the current place, and apply the bonus
        if the fire dragon dies.
        """
        # BEGIN 2.2
        self.armor -= amount
        damge=amount
        place=self.place
        tmt=[i for i in place.terminators]
        j=[]
        if self.armor <= 0:
            damge=self.damage+amount
            self.place.remove_fighter(self)
            self.death_callback()
        for i in tmt:
             i.reduce_armor(damge)
        for i in tmt:
            if i.armor>0:
                j.append(i)
        place.terminators=j
