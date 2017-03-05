from nose.tools import *
from csimpy.circuit import *


def setup_module():
    print(__name__, ': setup_module() ~~~~~~~~~~~~~~~~~~~~~~')

def teardown_module():
    print(__name__, ': teardown_module() ~~~~~~~~~~~~~~~~~~~')

class TestCircuit():

    @classmethod
    def setup_class(cls):
        print(__name__, ': TestClass.setup_class() ----------')

    @classmethod
    def teardown_class(cls):
        print(__name__, ': TestClass.teardown_class() -------')

    def setup(self):
        print(__name__, ': TestClass.setup()  - - - - - - - -')
        self.ckt = Circuit()

    def teardown(self):
        print(__name__, ': TestClass.teardown() - - - - - - -')

    def test_circuit(self):
        print("Started circuit test.")
