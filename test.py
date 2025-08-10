import os
os.environ['NUMBA_USE_LEGACY_TYPE_SYSTEM'] = '0'

import numba as nb
from numba.core import types
if not hasattr(types, 'intp'):
    types.intp = types.c_intp
if not hasattr(types, 'uintp'):
    types.uintp = types.c_uintp
if not hasattr(types, 'int32'):
    types.int32 = types.c_int32
if not hasattr(types, 'uint32'):
    types.uint32 = types.c_uint32

@nb.njit
def makestring():
    return "Hello from Numba"

@nb.njit
def testprint():
    print(makestring())

testprint()
