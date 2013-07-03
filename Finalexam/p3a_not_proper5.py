class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        self.before = before
    def setAfter(self, after):
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
 
def insert(atMe, newFrob):
    def insertAfter(atMe, newFrob):
        a = atMe.getAfter()
        newFrob.setAfter(a)
        newFrob.setBefore(atMe)
        atMe.setAfter(newFrob)
        if a is not None:
            a.setBefore(newFrob)
            
    def insertBefore(atMe, newFrob):
        b = atMe.getBefore()
        newFrob.setBefore(b)
        newFrob.setAfter(atMe)
        atMe.setBefore(newFrob)
        if b is not None:
            b.setAfter(newFrob)
        
    if atMe is not None and atMe.myName() is not None and newFrob is not None and newFrob.myName() is not None:
        current = atMe
        if current.myName() == newFrob.myName():
            insertAfter(current, newFrob)
        else:
            if current.myName() < newFrob.myName():
                while current.myName() < newFrob.myName() and current.getAfter() is not None:
                    current = current.getAfter()
                insertBefore(current, newFrob)
            else:
                while current.myName() > newFrob.myName() and current.getBefore() is not None:
                    current = current.getBefore()
                insertAfter(current, newFrob)
 
def printList(e):
    print "Forward:"
    c = e
    while c is not None:
        print "this: " + c.myName()
        print "before:"
        if c.getBefore() is not None:
            print "       "+ c.getBefore().myName()
        print "after:"
        if c.getAfter() is not None:
            print "       "+ c.getAfter().myName()
        c = c.getAfter()
    print "Backward:"
    c = e
    while c is not None:
        print c.myName()
        c = c.getBefore()
    print "---------------------"
 
eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
fred2 = Frob('fred')
fred3 = Frob('fred')
martha = Frob('martha')
 
insert(eric, andrew)
 
insert(eric, ruth)
 
insert(eric, fred)
insert(ruth, martha)
insert(ruth, fred2)
 
printList(andrew)
