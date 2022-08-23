import winsound
from random import randint

def create_music():
    count = 10
    while count > 0:
        winsound.Beep(randint(50 , 2000), randint(200 ,1000))
        count -= 1
create_music()
