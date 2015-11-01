from soal.models import Soal

def rc4_crypt( data , key ):
    S = range(256)
    j = 0
    out = []

    #KSA Phase
    for i in range(256):
        j = (j + S[i] + ord( key[i % len(key)] )) % 256
        S[i] , S[j] = S[j] , S[i]

    #PRGA Phase
    i = j = 0
    for char in data:
        i = ( i + 1 ) % 256
        j = ( j + S[i] ) % 256
        S[i] , S[j] = S[j] , S[i]
        out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))

    return ''.join(out)


class RC4File(object):

    resources = ""
    target = ""
    password = ""
    data = ""
    mix_data = ""
    
    def __init__(self, resources, password, target=True):
        self.resources = resources
        if target and isinstance(target, bool):
            self.target = self.resources
        else:
            self.target = target
        self.password = password

    def __read(self):
        with open(self.resources, "r+") as f:
            self.data = f.read()

    def __write(self):
        with open(self.target, "w+") as f:
            f.write(self.mix_data)

    def run(self):
        self.__read()
        self.mix_data = rc4_crypt(self.data, self.password)
        self.__write()
        
    def to_byte(self):
        return [ord(i) for i in list(self.data)]

    def to_char(self):
        return [chr(ord(i)) for i in list(self.data)]



class InstanceRC4File(object):

    instance = ""
    
    def __init__(self, instance):
        if not isinstance(instance, Soal):
            raise BaseException("instance bukan dari objek model Soal")
        self.instance = instance
        
    @staticmethod
    def run(instance):
        irc = InstanceRC4File(instance)
        resources = irc.instance.file_soal.path
        password = irc.instance.guru.passwordmanager.password
        RC4File(resources, password).run()

        
            