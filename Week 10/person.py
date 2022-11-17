class Person:
    def __init__(self,name,address):
        self._name=name
        self._address = address

    def getName(self):
        return self._name

    def getNumber(self):
        return self._address

    def toString(self):
        return self._name , self._address
