from nex_tool import Nex_tool
from nex_key import Nex_key
 
    
class Nex_decrypt:
    
    de_swap_patt = [16,17,18,19,20,21,22,23,
                    24,25,26,27,28,29,30,31,
                    48,49,50,51,52,53,54,55,
                    56,57,58,59,60,61,62,63,
                    0,1,2,3,4,5,6,7,
                    8,9,10,11,12,13,14,15,
                    32,33,34,35,36,37,38,39,
                    40,41,42,43,44,45,46,47]

    de_patt = {
        '00' : [0,3,5,9,
                14,10,13,1,
                6,8,15,2,
                7,4,12,11],

        '01' : [12,13,10,11,
                9,14,5,2,
                6,0,4,3,
                15,7,1,8],
            
        '10' : [4,9,8,13,
                10,5,6,7,
                2,0,3,14,
                15,11,1,12],

        '11' : [5,10,6,9,
                3,15,4,0,
                13,11,1,2,
                14,7,12,8]

    }

    def __init__(self, key, block_size=64, char_size=16, key_block_size=64, key_char_size=8):
        self.key = key
        self.block_size = block_size
        self.char_size = char_size
        self.nex_tool = Nex_tool(self.block_size,self.char_size)
        self.nex_key = Nex_key(self.key,key_block_size,key_char_size)

    def set_key(self, key):
        self.nex_key.set_key(key)

    def decrypt(self, encrypted_text):
        plain_text = ''
        str_list = self.nex_tool.split_len(encrypted_text,4)
        for i in range(len(str_list)):
            plain_text += self.decrypt_block(str_list[i])
        
        return plain_text.rstrip()

    def decrypt_block(self, encrypted_text):
        # self.plain_text = plain_text
        tmp_text = self.nex_tool.str_to_bi(encrypted_text)
        for i in range(8,0,-1):
            tmp_list = self.nex_tool.split_len(tmp_text,self.char_size)
            key_list = self.nex_tool.split_len(self.nex_key.KR[i],self.char_size)
            for j in range(len(tmp_list)):
                if(key_list[j][-2:] == '00'):
                    tmp_list[j] = self.de00(tmp_list[j],key_list[j])
                elif(key_list[j][-2:] == '01'):
                    tmp_list[j] = self.de01(tmp_list[j],key_list[j])
                elif(key_list[j][-2:] == '10'):
                    tmp_list[j] = self.de10(tmp_list[j],key_list[j])
                elif(key_list[j][-2:] == '11'):
                    tmp_list[j] = self.de11(tmp_list[j],key_list[j])
            tmp_text = ''.join(tmp_list)
            tmp_text = self.nex_tool.permutate_str(tmp_text, self.de_swap_patt)

        return self.nex_tool.bi_to_str(tmp_text)

    def de00(self, str, tkey):
        return self.nex_tool.permutate_str( str, self.de_patt[tkey[:2]])

    def de01(self, str, tkey):
        return self.nex_tool.xor_str(str,tkey)

    def de10(self, str, tkey):
        return self.nex_tool.complement_str(str)

    def de11(self, str, tkey):
        return self.nex_tool.shift_str(str, ( self.nex_tool.bi_to_int(tkey[:2]) + 1 ) , self.char_size )