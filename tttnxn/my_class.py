class my_class:
    def __init__(
            self,
            me="dave bobsteve",
            you="harry houdini",
            dims=3
    ):
        self.me = str(me)
        self.you = str(you)
        self.dims = 3
        self.combo = self.me + self.you

    def jumble_letters(self):
        import random as random
        _ = [x for x in (self.combo)]
        random.shuffle(_)
        self.combo = ''
        for letter in _:
            self.combo = self.combo + letter
        return self.combo

    def add_letters(self, letters_to_add=None):
        if letters_to_add == None:
            import random as random
            x = random.choice(range(0, 10))
            for i in range(0, x):
                import string
                lets = string.ascii_lowercase
                y = random.choice(lets)
                self.combo = self.combo + y
        else:
            self.combo = self.combo + str(letters_to_add)

        return self.combo