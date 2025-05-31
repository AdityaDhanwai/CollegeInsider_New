from bardapi import Bard
from dotenv import load_dotenv
load_dotenv()

token='cwhow3usnEBaFFkRz6LusxgCoAD6_hsOeK8NnG9kpHdQpCcUBvwtKRWqxSIpzoBpKZ40XQ.'
bard=Bard(token=token)
result=bard.get_answer("Who are you?")
print(result)