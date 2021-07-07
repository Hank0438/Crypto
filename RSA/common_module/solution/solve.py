import gmpy2
from Crypto.Util.number import getPrime


class RSAModuli:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.m = 0
        self.i = 0
    def gcd(self, num1, num2):
        """
        This function os used to find the GCD of 2 numbers.
        :param num1:
        :param num2:
        :return:
        """
        if num1 < num2:
            num1, num2 = num2, num1
        while num2 != 0:
            num1, num2 = num2, num1 % num2
        return num1
    def extended_euclidean(self, e1, e2):
        """
        The value a is the modular multiplicative inverse of e1 and e2.
        b is calculated from the eqn: (e1*a) + (e2*b) = gcd(e1, e2)
        :param e1: exponent 1
        :param e2: exponent 2
        """
        self.a = gmpy2.invert(e1, e2)
        self.b = (float(self.gcd(e1, e2)-(self.a*e1)))/float(e2)
    def modular_inverse(self, c1, c2, N):
        """
        i is the modular multiplicative inverse of c2 and N.
        i^-b is equal to c2^b. So if the value of b is -ve, we
        have to find out i and then do i^-b.
        Final plain text is given by m = (c1^a) * (i^-b) %N
        :param c1: cipher text 1
        :param c2: cipher text 2
        :param N: Modulus
        """
        i = gmpy2.invert(c2, N)
        mx = pow(c1, self.a, N)
        my = pow(i, int(-self.b), N)
        self.m= mx * my % N
    def print_value(self):
        print("Plain Text: ", (int(self.m)).to_bytes(0x40, byteorder='big').strip(b'\x00'))


def main():
    # m = int.from_bytes(b'Crypto{AAAAAAAAAAAAAA}', byteorder='big')
    # p = getPrime(256)
    # q = getPrime(256)
    # N = p*q
    # e1 = getPrime(10)
    # e2 = getPrime(10)
    # c1 = pow(m, e1, N) 
    # c2 = pow(m, e2, N)

    N = 7267635112341452069442513069212622057735567000533112364576621364649054503735406200368062759475588499921026069945425401749161569237613133564677597077561917
    e1 = 971
    c1 = 7087522869831400610482525751505139686127248792540422690112164226615957641426941176123612273484760199661752957658895180635437547195461745309086224871943227
    e2 = 557
    c2 = 2591269816650585112647277175810508267690752461061316312062558549360631337706175763152798885455497815234029334980049753916396211908755164422220358041789757


    c = RSAModuli()
    c.extended_euclidean(e1, e2)
    c.modular_inverse(c1, c2, N)
    c.print_value()

if __name__ == '__main__':
    main()
