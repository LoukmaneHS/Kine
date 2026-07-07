import numpy as np

class Kimage:
    def __init__(self, row: int, column: int):
        if not (0 <= row <= 65535):
            raise ValueError(f"row must be between 0 and 65535, got {row}")
        if not (0 <= column <= np.iinfo(np.uint64).max):
            raise ValueError(f"column out of uint64 range, got {column}")

        self.row = np.uint16(row)
        self.column = np.uint64(column)
        self.kimage = np.zeros((row, column, 4), dtype=np.uint8, order='C')

    def __repr__(self):
        return f"Kimage(row={self.row}, column={self.column})"
