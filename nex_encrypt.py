from nex_tool import Nex_tool
from nex_key import Nex_key
 
    
class Nex_encrypt:
    
    swap_patt = [32,33,34,35,36,37,38,39,
                 40,41,42,43,44,45,46,47,
                 0,1,2,3,4,5,6,7,
                 8,9,10,11,12,13,14,15,
                 48,49,50,51,52,53,54,55,
                 56,57,58,59,60,61,62,63,
                 16,17,18,19,20,21,22,23,
                 24,25,26,27,28,29,30,31]

    en_patt = {
        '00' : [0,7,11,1,
                13,2,8,12,
                9,3,5,15,
                14,6,4,10],

        '01' : [9,14,7,11,
                10,6,8,13,
                15,4,2,3,
                0,1,5,12],
            
        '10' : [9,14,8,10,
                0,5,6,7,
                2,1,4,13,
                15,3,11,12],

        '11' : [7,10,11,4,
                6,0,2,13,
                15,3,1,9,
                14,8,12,5]

    }

    def __init__(self, key, block_size=64, char_size=16, key_block_size=64, key_char_size=8):
        self.key = key
        self.block_size = block_size
        self.char_size = char_size
        self.nex_tool = Nex_tool(self.block_size,self.char_size)
        self.nex_key = Nex_key(self.key,key_block_size,key_char_size)

    def set_key(self, key):
        self.nex_key.set_key(key)

    def encrypt(self, plain_text):
        encrypted = ''
        str_list = self.nex_tool.split_len(plain_text,4)
        for i in range(len(str_list)):
            encrypted += self.encrypt_block(str_list[i])
        
        return encrypted

    def encrypt_block(self, plain_text):
        # self.plain_text = plain_text
        tmp_text = self.nex_tool.str_to_bi(plain_text)
        for i in range(1,9):
            tmp_text = self.nex_tool.permutate_str(tmp_text, self.swap_patt)
            tmp_list = self.nex_tool.split_len(tmp_text,16)
            key_list = self.nex_tool.split_len(self.nex_key.KR[i],16)
            for j in range(len(tmp_list)):
                if(key_list[j][-2:] == '00'):
                    tmp_list[j] = self.en00(tmp_list[j],key_list[j])
                elif(key_list[j][-2:] == '01'):
                    tmp_list[j] = self.en01(tmp_list[j],key_list[j])
                elif(key_list[j][-2:] == '10'):
                    tmp_list[j] = self.en10(tmp_list[j],key_list[j])
                elif(key_list[j][-2:] == '11'):
                    tmp_list[j] = self.en11(tmp_list[j],key_list[j])
            tmp_text = ''.join(tmp_list)

        return self.nex_tool.bi_to_str(tmp_text)

    def en00(self, str, tkey):
        return self.nex_tool.permutate_str( str, self.en_patt[tkey[:2]])

    def en01(self, str, tkey):
        return self.nex_tool.xor_str(str,tkey)

    def en10(self, str, tkey):
        return self.nex_tool.complement_str(str)

    def en11(self, str, tkey):
        return self.nex_tool.shift_str(str, -( self.nex_tool.bi_to_int(tkey[:2]) + 1 ) , self.char_size )