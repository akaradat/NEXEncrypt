from nex_tool import Nex_tool
from nex_key import Nex_key
from nex_encrypt import Nex_encrypt
from nex_decrypt import Nex_decrypt


if __name__ == "__main__":
    NE = Nex_encrypt('ABCD')
    ND = Nex_decrypt('ABCD')

    txt_en = NE.encrypt("Hello WORLD สวัสดีชาวโลก 00123 /*-")

    print(txt_en)
    # print(len(txt_en))

    txt_de = ND.decrypt(txt_en)

    print(txt_de)
    print(repr(txt_de))



    