from nex_tool import Nex_tool


class Nex_key:
    gen_key_patt = [0,16,32,48,1,17,33,49,
                    2,18,34,50,3,19,35,51,
                    4,20,36,52,5,21,37,53,
                    6,22,38,54,7,23,39,55,
                    8,24,40,56,9,25,41,57,
                    10,26,42,58,11,27,43,59,
                    12,28,44,60,13,29,45,61,
                    14,30,46,62,15,31,47,63]

    KR = {}

    def __init__(self, key, block_size = 64, char_size = 8):
        self.key = key
        self.block_size = block_size
        self.char_size = char_size
        self.nex_tool = Nex_tool(block_size,char_size)
        self.gen_all_key()

    def set_key(self, key):
        self.key = key
        self.gen_all_key()
        
        
    def gen_all_key(self):
        tmp = ('{:<0'+str(self.block_size)+'}').format(self.nex_tool.str_to_bi(self.key))
        tmp = tmp[:64]  
        self.KR[0] = self.nex_tool.permutate_str( tmp , self.gen_key_patt)
        for i in range(1,9):
            self.KR[i] = self.gen_key(i) 

    def gen_key(self,n):
        # self.KR[n] = self.nex_tool.shift( self.KR[n-1], self.nex_tool.bi_to_int(self.KR[n-1][-2:]) + 1 )
        return self.nex_tool.shift( self.KR[n-1], self.nex_tool.bi_to_int(self.KR[n-1][-2:]) + 1 )



        