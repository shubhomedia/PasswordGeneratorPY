import random
def passwordGenerator():
    lowerChars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    upperChars = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    specialChars = ['!','"','#','$','%','&','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','^','`',',','~'];
    numericChars = ['0','1','2','3','4','5','6','7','8','9']
    password = random.choice(lowerChars) + random.choice(upperChars) + random.choice(specialChars) + random.choice(numericChars) + random.choice(numericChars) + random.choice(specialChars) + random.choice(lowerChars) + random.choice(specialChars)
    print(password)
    return password

passwordGenerator()