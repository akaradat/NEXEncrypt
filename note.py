from collections import deque

# output = __permutate(pattern,input)
# def __permutate(self, table, block):
def permutate(input,pattern):
    """Permutate this block with the specified table"""
    return list(map(lambda x: input[x], pattern))

def permutate_str(str, patt):
    return ''.join( permutate(split_len(str,1),patt) )

    
def shift(str,num):
    #from collections import deque
    tmp = deque(list(str))
    tmp.rotate(num)
    return ''.join(tmp)

def shift_str(str,num):
    tmp = split_len(str,16)
    for i in range(len(tmp)):
        tmp[i] = shift(tmp[i],num)
    return ''.join(tmp)

def str_to_bi(str):
    return ''.join(format(ord(x), 'b').zfill(16) for x in str)

def bi_to_str(bi):
    list_bi = split_len(bi,16)
    return ''.join( "{0:c}".format(int(x,2)) for x in list_bi)

def split_len(seq, length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]

def xor_str(str1,str2):
    l = len(str1)
    y = int(str1,2) ^ int(str2,2)
    return '{0:b}'.format(y).zfill(l)

def foxie_1():
    en_pat = [37,35,54,7,24,9,28,11,
              36,19,34,25,6,23,22,39,
              18,32,3,10,1,5,30,29,
              33,31,8,0,26,12,21,45,
              20,2,40,17,4,43,44,46,
              53,41,13,38,27,56,55,47,
              52,60,42,57,50,48,14,62,
              51,59,58,16,49,15,61,63]

    de_pat = [27,20,33,18,36,21,12,3,
              26,5,19,7,29,42,54,61,
              59,35,16,9,32,30,14,13,
              4,11,28,44,6,23,22,25,
              17,24,10,1,8,0,43,15,
              34,41,50,37,38,31,39,47,
              53,60,52,56,48,40,2,46,
              45,51,58,57,49,62,55,63]

    test_pat = [0,1,2,3,4,5,6,7,
              8,9,10,11,12,13,14,15,
              16,17,18,19,20,21,22,23,
              24,25,26,27,28,29,30,31,
              32,33,34,35,36,37,38,39,
              40,41,42,43,44,45,46,47,
              48,49,50,51,52,53,54,55,
              56,57,58,59,60,61,62,63]

    plain = "HEกข"
    plain_bi = str_to_bi(plain)
    # print(plain_bi)
    sh = shift_str(plain_bi,3)
    en = bi_to_str(sh)
    # print("...",en,"...")

    sh2 = shift_str(sh,-3)
    # print(bi_to_str(sh2))

    perm_bi = permutate_str(sh,en_pat)

    print(bi_to_str(perm_bi))

    perm_de = permutate_str(perm_bi,de_pat)

    sh2 = shift_str(perm_de,-3)
    print(bi_to_str(sh2))

    # print(bi_to_str(perm_de))



if __name__ == "__main__":
    # print(str_to_binary("HELLOWORLD"))
    foxie_1()

    
    