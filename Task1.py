'''Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
passed to the constructor. The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.'''

class Email:

    def __init__(self, name):
        self.validate(name)
        self.name = name

    def validate(self, s):
        if s.find('@') == -1:
            raise ValueError('Invalid email')
        for i in range(len(s)):
            if s[i] not in '@abcdefghijklmnopqrstuvwxyz01234567869_-.':
                raise ValueError('Invalid email')
            elif s[i] in '_-.' and (i == 0 or s[i+1] == '@'):
                raise ValueError('Invalid email')

mail = Email('something@smth.com')
print(mail.name)