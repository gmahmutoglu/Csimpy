from abc import ABCMeta, abstractmethod

class Physical(metaclass=ABCMeta):
    """Abstract class representing physical objects like circuits and devices.

    Subclasses: Pysical
                 |_ Circuit
                 |   |_ SubCircuit
                 |_ CircuitComponent
                    |_ Device

    n_u: This is the number of "time dependent inputs". However, these are not
         inputs in the usual sense. I.e., they are not something like a node
         voltage which is supplied to a model from the outside world. The u
         inputs communicate the time information with time dependent objects.
         However, because we are not always inspect objects in a way in which
         time makes sense (e.g., AC analysis), we cannot directly supply the
         absolute time information. Instead, we let devices register their time
         dependent functions with higher order objects (e.g., a circuit) and
         then let the circuit decide what to do with them.
    """

    def __init__(self):
        self.name = None           # Name of the device.
        self.n_x = 0;              # Number of inputs.
        self.n_y = 0;              # Number of internal unknowns.
        self.n_u = 0;              # Number of time dependent inputs.
        self.n_out = 0             # Number of outputs.
        self.n_int = 0             # Number of internal equations.
        self.gnd_node = None       # Ground node of the circuit.
        self.gnd_node_num = 0      # Number of the ground node in the node_list.
        self.component_list = None # A list of components.
        self.n_component = 0       # Number of circuit components.

    @abstractmethod
    def f(self):
        """Return the current value vector."""

    @abstractmethod
    def q(self):
        """Return the charge value vector."""

    @abstractmethod
    def j(self):
        """Return the source value vector."""

    @abstractmethod
    def d_f(self):
        """Return the current Jacobian matrix."""

    @abstractmethod
    def d_q(self):
        """Return the charge Jacobian matrix."""
