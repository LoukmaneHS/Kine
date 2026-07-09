import numpy as np

class Karacter:
    def __init__(self, name: str, dof: int):
        if not (0 <= dof <= 65535):
            raise ValueError(f"dof must be between 0 and 65535, got {dof}")
        
        self.model_name = name
        self.dof_count = np.uint16(dof)
        self.nacc = np.zeros(dof, dtype=np.uint32)
        self.oacc = np.zeros(dof, dtype=np.uint32)
        self.sacc = np.zeros(dof, dtype=bool)

    def __repr__(self):
        return f"Karacter(name={self.model_name!r}, dof={self.dof_count})"
