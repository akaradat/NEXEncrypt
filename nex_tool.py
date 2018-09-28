from collections import deque

class Nex_tool:

    def __init__(self, block_size, char_size):
        self.block_size = block_size
        self.char_size = char_size


    def permutate(self,input,pattern):
        """Permutate this block with the specified table"""
        return list(map(lambda x: input[x], pattern))

    def permutate_str(self,str, patt):
        return ''.join( self.permutate(self.split_len(str,1),patt) )
        
    def shift(self,str,num):
        #from collections import deque
        tmp = deque(list(str))
        tmp.rotate(num)
        return ''.join(tmp)

    def shift_str(self,str,num,block):
        tmp = self.split_len(str,block)
        for i in range(len(tmp)):
            tmp[i] = self.shift(tmp[i],num)
        return ''.join(tmp)

    def str_to_bi(self,str):
        return ''.join(format(ord(x), 'b').zfill(self.char_size) for x in str)

    def bi_to_str(self,bi):
        list_bi = self.split_len(bi,self.char_size)
        return ''.join( "{0:c}".format(int(x,2)) for x in list_bi)

    def int_to_bi(self,inte):
        return ('{:0'+str(self.char_size)+'b}').format(inte)
    
    def bi_to_int(self,bi):
        return int("{0:d}".format(int(bi,2)))

    def split_len(self,seq, length):
        return [seq[i:i+length] for i in range(0, len(seq), length)]

    def xor_str(self,str1,str2):
        l = len(str1)
        y = int(str1,2) ^ int(str2,2)
        return '{0:b}'.format(y).zfill(l)

    def complement_str(self,str):
        pw = 2**self.char_size - 1
        str_int = self.bi_to_int(str)
        return self.int_to_bi(pw - str_int)



    


    