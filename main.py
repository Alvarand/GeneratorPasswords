import random


class GeneratePasswords:
    '''
    Generating passwords
    '''

    def __init__(self):
        '''Generator initiation'''
        self.dictionary = 'qwertyuiopasdfghjklzxcvbnm' \
                          'QWERTYUIOPASDFGHJKLZXCVBNM' \
                          '1234567890!@#$%^&*()'

    def generate(self, lenght=8):
        '''Getting random password'''
        password = ''
        for i in range(lenght):
            c = random.choice(self.dictionary)
            password += c
        return password


password = GeneratePasswords()
print(password.generate())
