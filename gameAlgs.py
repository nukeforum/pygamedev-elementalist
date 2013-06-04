import math

class alg:
    @staticmethod
    def w_avg(aset):
        slow = 3
        return ((aset[0] * (slow - 1)) + aset[1]) / slow

    @staticmethod
    def minus(aset):
        return (aset[0] - aset[1])
