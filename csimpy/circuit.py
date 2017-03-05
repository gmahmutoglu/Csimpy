from csimpy.physical import Physical

class Circuit(Physical):
    """A circuit class"""

    def __init__(self):
        super().__init__()

    def f(self):
        pass

    def q(self):
        pass

    def j(self):
        pass

    def d_f(self):
        pass

    def d_q(self):
        pass

class Subcircuit(Circuit):
    """A subcircuit class derived from the circuit class"""
