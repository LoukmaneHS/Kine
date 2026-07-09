import numpy as np

class Karacter:
    def __init__(self, name: str, dof: int):
        if not (0 <= dof <= 65535):
            raise ValueError(f"dof must be between 0 and 65535, got {dof}")
        
        self.dof_count = np.uint16(dof)
        self.n_acc = np.zeros(dof, dtype=np.uint32)
        self.o_acc = np.zeros(dof, dtype=np.uint32)

    def __repr__(self):
        return f"Karacter(name={self.model_name!r}, dof={self.dof_count})"
