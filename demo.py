from nex_tool import Nex_tool
from nex_key import Nex_key
from nex_encrypt import Nex_encrypt
from nex_decrypt import Nex_decrypt
import os,time

def cls():
	if(os.name=='nt'):
		os.system('cls')
	else :
		os.system('clear')

def yes_or_no(question):
    while True:
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False

def export_file(text):
    output_file_header = open("output.txt", "w")
    output_file_header.write("Your ciphertext is:")
    output_file_header.close()
    output_file = open("output.txt", "ab")
    for i in text:
        try:
            output_file.write(i.encode('utf-8'))
        except UnicodeEncodeError:
            print("The cyphertext contain some special character that can't be encoded")
            print("Please try another input")
    output_file.close()

if __name__ == "__main__":
    x=''
    while(x!='#'):
        cls()
        print(" Welcome to NEX encrypt ".center(50,'-'))
        print("\t[1].Encrypt")
        print("\t[2].Decrypt")
        print("\t #  Exit")
        x=input("Select your option: ")

        if (x=='1'):
            msg = input("Input your text(more than 32 character): ")
            while(len(msg) < 32):
                msg = input("Input your text(more than 32 character): ")
            NE = Nex_encrypt(input("Key: "))
            en = NE.encrypt(msg)
            try:
                print("\nYour encrypted text is : "+en)
                print("repr : "+repr(en))
            except UnicodeEncodeError:
                print("\nrepr : "+repr(en))
                print("***The cyphertext contain some special character that can't be encoded")
                if(yes_or_no("Do you want to export as file?")):
                    export_file(repr(en))
                
        elif (x=='2'):
            msg = input("Input your encrypted text: ")
            ND = Nex_decrypt(input("Key: "))
            de = ND.decrypt(msg)
            try:
                print("\nYour decrypted text is : "+de)
                print("repr : "+repr(de))
            except UnicodeEncodeError:
                print("\nrepr : "+repr(de))
                print("***The cyphertext contain some special character that can't be encoded")
                if(yes_or_no("Do you want to export as file?")):
                    export_file(repr(en))
                

        if(x!='#'):
            input("\npress any button to continue")
    
    cls()
    print(" GOODBYE ".center(50,'-'))
    time.sleep(1)
    cls()


    


    