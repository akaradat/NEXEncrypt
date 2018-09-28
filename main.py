from nex_tool import Nex_tool
from nex_key import Nex_key
from nex_encrypt import Nex_encrypt


if __name__ == "__main__":
    tool = Nex_tool()
    NK = Nex_key('ABC')
    NE = Nex_encrypt('ABCD')


    print(NE.encrypt("HELL"))
    print(NE.encrypt("0123"))
    print(NE.encrypt("HELL0123"))

    NE.set_key("BBBB")
    print(NE.encrypt("HELL0123"))

    NE.set_key("ABCD")
    print(NE.encrypt("HELL0123"))

    # print(Nex_encrypt('ABCD').encode("HELL0123"))
    