import numpy as np
from ..classes.karacter import Karacter


def state(karacter: Karacter) -> np.ndarray:
    return karacter.accumulator.copy()
