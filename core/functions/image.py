import numpy as np
from ..classes.kinematrix import Kinematrix
from ..classes.kimage import Kimage


def encode_image(kinematrix: Kinematrix) -> Kimage:
    img = Kimage(row=int(kinematrix.row), column=int(kinematrix.column))

    raw = kinematrix.kinematrix.astype('>i4')
    byte_view = raw.view(np.uint8).reshape(raw.shape[0], raw.shape[1], 4)

    img.kimage[:] = byte_view

    return img


def decode_image(kimage: Kimage) -> Kinematrix:
    row = int(kimage.row)
    column = int(kimage.column)

    raw = kimage.kimage.reshape(row, column, 4).view('>i4').reshape(row, column)

    mat = Kinematrix(row=row, column=column)
    mat.kinematrix[:] = raw.astype(np.int32)

    return mat
