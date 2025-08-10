import os
os.environ['NUMBA_USE_LEGACY_TYPE_SYSTEM'] = '0'

import numba as nb

@nb.njit
def makestring():
    return 'J'

@nb.njit
def testprint():
    print(f"{makestring()}")

testprint()
