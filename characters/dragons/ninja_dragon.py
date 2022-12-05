from .dragon import Dragon


class NinjaDragon(Dragon):
    """NinjaDragon does not block the path and damages all terminators in its place."""

    name = 'Ninja'
    damage = 1
    blocks_path=False
    food_cost=5
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.4
    implemented = True  # Change to True to view in the GUI

    # END 2.4

    def action(self, colony):
        # BEGIN 2.4
        "*** YOUR CODE HERE ***"
        tmt=[i for i in self.place.terminators]
        j=[]
        for i in tmt:
             i.reduce_armor(self.damage)
        for i in tmt:
            if i.armor>0:
                j.append(i)
        self.place.terminators=j
