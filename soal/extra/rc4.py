from django.conf import settings

def rc4_crypt( data , key ):
    S = list(range(256))
    j = 0
    out = []

    #KSA Phase
    for i in list(range(256)):
        j = (j + S[i] + ord( key[i % len(key)] )) % 256
        S[i] , S[j] = S[j] , S[i]

    #PRGA Phase
    i = j = 0
    for char in data:
        i = ( i + 1 ) % 256
        j = ( j + S[i] ) % 256
        S[i] , S[j] = S[j] , S[i]
        out.append(chr(char ^ S[(S[i] + S[j]) % 256]))

    return out

class NewFileRC4(object):
    
    def __init__(self, data_file, password, nama_file):
        self.data = data_file
        self.nama_file = nama_file
        self.data_encrypt = []
        self.password = password
        self.__reader()
        self.__encrypt()
        self.__create()
        
    def __reader(self):
        #with open()
        #print(list(self.data))
        pass

    def __encrypt(self):
        self.data_encrypt = rc4_crypt(self.data, self.password)
        #print(self.data_encrypt)
        
    def __create(self):
        
        with open(self.nama_file, "w+") as f:
            f.writelines(self.data_encrypt)
        return True
        