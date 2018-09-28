from nex_tool import Nex_tool
from nex_key import Nex_key
from nex_encrypt import Nex_encrypt


if __name__ == "__main__":
    tool = Nex_tool()
    NK = Nex_key('ABC')
    NE = Nex_encrypt('ABCD')


    print(NE.encode("HELL"))
    print(NE.encode("0123"))
    print(NE.encode("HELL0123"))
    