import numpy as np

class Ksign:
    def __init__(self, dof: int):
        self.dof_count = np.uint16(dof)
        self.values = np.zeros(dof, dtype=bool)

    def __repr__(self):
        return f"Ksign(dof={self.dof_count})"
