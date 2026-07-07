import numpy as np
from ..classes.karacter import Karacter


def acc_reset(karacter: Karacter) -> None:
    karacter.accumulator.fill(0)


def acc_state(karacter: Karacter) -> np.ndarray:
    return karacter.accumulator.copy()


def kar_rename(karacter: Karacter, new_name: str) -> None:
    if not new_name or not isinstance(new_name, str):
        raise ValueError("Name must be a non-empty string")
    karacter.model_name = new_name


def kar_info(karacter: Karacter) -> None:
    print(f"Karacter: {karacter.model_name}")
    print(f"  DOF   : {karacter.dof_count}")
    print(f"  Acc   : shape={karacter.accumulator.shape}, "
          f"dtype={karacter.accumulator.dtype}")
