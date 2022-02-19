import random
import string


class RandomStr():

    def randomString():
        password_characters = string.ascii_letters + string.digits + "!"+"@"+"#"+"$"+"%" # alternative variant -> string.punctuation
        result = ''.join(random.choice(password_characters) for i in range(random.randint(6,20))) 
        with open('file.txt', "a", encoding='utf-8') as file:
            file.write(result + '\n') 



    if __name__ == '__main__':
        randomString()