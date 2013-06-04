import math
from gameAlgs import alg

def behavior1(pos, target_pos):
    ab = map(alg.minus, zip(pos, target_pos))
    c = math.hypot(abs(ab[0]), abs(ab[1]))
    
    return target_pos
