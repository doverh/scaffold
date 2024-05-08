import random
import string

def getRandomPwd(pwdLength):
    pwdCharacteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(pwdCharacteres, k=pwdLength))