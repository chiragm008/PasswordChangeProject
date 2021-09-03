import re
from collections import Counter
from difflib import SequenceMatcher
from endPoint.EndPointFactory import EndPoint

class Password:
    def ChangePassword(oldPassword, newPassword):
        if not (oldPassword == EndPoint.systemPassword):
            return 0

        l = list((dict(Counter(newPassword))).values())
        l1 = [i for i in l if i != 1]

        if not (len(newPassword) >= 18) and (re.search('[a-z]', newPassword)) and (
        re.search('[A-Z]', newPassword)) and (
                re.search('[0-9]', newPassword)) and (
                re.search('[!@#$&*]', newPassword)) and (len(re.findall('[!@#$&*]', newPassword)) <= 4) and (
                len(newPassword) / 2 > len(re.findall('[0-9]', newPassword))) and (len(l1) <= 4):
            return 0

        if not (int(SequenceMatcher(None, oldPassword, newPassword).ratio() * 100) < 80):
            return 0

        return 1




