import binascii
from gmpy2 import iroot

def xgcd(a, b):
    """
    Extented Euclid GCD algorithm.
    Return (x, y, g) : a * x + b * y = gcd(a, b) = g.
    """
    if a == 0: return 0, 1, b
    if b == 0: return 1, 0, a

    px, ppx = 0, 1
    py, ppy = 1, 0

    while b:
        q = a // b
        a, b = b, a % b
        x = ppx - q * px
        y = ppy - q * py
        ppx, px = px, x
        ppy, py = py, y

    return ppx, ppy, a

def invmod(a, n):
    """
    Return 1 / a (mod n).
    a and n must be co-primes.
    """
    if n < 2:
        raise ValueError("modulus must be greater than 1")

    x, y, g = xgcd(a, n)

    if g != 1:
        raise ValueError("no invmod for given @a and @n")
    else:
        return x % n

def nroot(x, n):
    """
    Return truncated n'th root of x.
    """
    if n < 0:
        raise ValueError("can't extract negative root")

    if n == 0:
        raise ValueError("can't extract zero root")

    sign = 1
    if x < 0:
        sign = -1
        x = -x
        if n % 2 == 0:
            raise ValueError("can't extract even root of negative")

    high = 1
    while high ** n <= x:
        high <<= 1

    low = high >> 1
    while low < high:
        mid = (low + high) >> 1
        mr = mid ** n
        if mr == x:
            return (mid, True)
        elif low < mid and mr < x:
            low = mid
        elif high > mid and mr > x:
            high = mid
        else :
            return (sign * mid, False)
    return (sign * (mid + 1) , False)


def fermat_factorization(N):
    a = iroot(N,2)[0]
    b2 = a*a - N
    b = iroot(N,2)[0]
    count = 0
    while b*b != b2:
        a = a + 1
        b2 = a*a - N
        b = iroot(b2,2)[0]
        count += 1
    p=a+b
    q=a-b
    return p, q

intToBytes = lambda x: binascii.unhexlify(hex(x)[2:])

e = 670708811
# n1 : r * next_prime(r)
n1 = 1445996106672795658014837677785551023248936972910686021347266433727666047353070921847230451546002345944283339548492109265556498740954239558888098348112238931171876231003264798569273
# n2 : p * q
n2 = 34568362683447146470933991590843730934193905484315988168903637059272116982282817804370662024105270529532518829384638265622710170832825979019152207027686730233580553331596804775271843952485179781695017034212344202606559719618472298367898264478055948042854773306315738907164284541070523483745279798108232560469149163467451873615032837829992110612676842455165389951351903461282330810985927123596992899230689725951464761356123796491539296209437661445967669667859903239781154581635366990822139999800199129989533981404823992417749136200150754701189236858963042967549956348050557957950793395048369192364000916096397237383549440954750353603730161576656716191404068808393764330105791685853479217071782816932634014007606977011465253
# enc : pow(FLAG1, e, n1)
enc1 = 367487901269053030058214287045120184472448456102757119240854405634734835246705008573601630186268564301666439366101414000135776808248600044909221537287929293781132827570693279203546
# enc : pow(FLAG2, e, n2)
enc2 = 21379502969808259200899386201498432466847715448699510452145470116136992957739596668986751651513143936243211370674231907531334137894009261498251851141601264660269230787977965177851517489422594445572124562056947738741935775730153121427396043094927992264841260138366516921738164703549213007662709527943442861300257860141065601747495372244129816171602762881002195876799538075391702867514657806885086349611481531787317946733234127979187945675894323958788028497412276863415475540086000121442074303557365199069849137550019853846578590202324220326658771972221518475201718777715002150047277228408717953379283466525666170414681650969955710401592379220954288720155272480561298387988080608778220590353625814938885453819339432778374314
s,r = fermat_factorization(n1)

d1 = invmod(e,(r-1)*(s-1))
flag1 = intToBytes(pow(enc1,d1,n1))

p = r**4 + r**3 + r**2 + r +1
q = n2 // p 

assert n2 == p*q

d2 = invmod(e,(p-1)*(q-1))
flag2 = intToBytes(pow(enc2,d2,n2))

print(flag1+flag2)