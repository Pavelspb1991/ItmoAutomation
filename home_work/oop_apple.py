class apple:
    grow_stage = ["flower", "green", "red"]
    index = 1

    def __init__(self):
        self.index = apple.index
        apple.index += 1
        self.stage = 0

    def ripe(self):
        self.stage += 1

    def is_ripe(self):
        if self.stage > 2:
            return True
        else:
            return  False

    def ripe_stage(self):
        if 2 < self.stage < 5:
            return apple.grow_stage[2]
        elif self.stage >= 5:
            return False
        else:
            return apple.grow_stage[self.stage]

        # def grow
            #если возрт >10 умирают плоды

