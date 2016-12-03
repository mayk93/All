class LibMacls(object):
    def __init__(self,
                 value=0):
        self.value = 0
        self.val_gen = self.get_val_gen()

    def get_val_gen(self):
        initial_value = self.value

        def val_gen(initial_value):
            while True:
                yield initial_value
                initial_value += 1

        return val_gen

    def new_val_gen(self, new_value):
        old_value = self.value
        self.value = new_value
        self.val_gen = self.get_val_gen()
        self.value = old_value

    def __str__(self):
        #  - Return statement -
        return " -> Current value is: %s" % self.value