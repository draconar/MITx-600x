def insert(atMe, newFrob):
    #Case1: newFrob comes before atMe
    if newFrob.myName() < atMe.myName():
        #atMe first in list
        if atMe.getBefore() == None:
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
        #element before atMe alphbetically before newFrob
        elif atMe.getBefore().myName()<newFrob.myName():
            atMe.getBefore().setAfter(newFrob)
            newFrob.setBefore(atMe.getBefore())
            atMe.setBefore(newFrob)
            newFrob.setAfter(atMe)
        #element before atMe alphbetically after newFrob    
        else:
            insert(atMe.getBefore(),newFrob)
    #Case 2: newFrob comes after atMe
    elif newFrob.myName() > atMe.myName():
        #atMe last in list
        if atMe.getAfter() == None:
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        #atMe not last in list and next element alphabetically after newFrob
        elif atMe.getAfter().myName()>newFrob.myName():
            atMe.getAfter().setBefore(newFrob)
            newFrob.setAfter(atMe.getAfter())
            atMe.setAfter(newFrob)
            newFrob.setBefore(atMe)
        #next element alphabetically before newFrob 
        else:
            insert(atMe.getAfter(),newFrob)
    #Case3: newFrob equals atMe
    elif newFrob.myName()==atMe.myName():
        if atMe.getAfter() != None:
            newFrob.setAfter(atMe.getAfter())
        newFrob.setBefore(atMe)
        if atMe.getAfter() != None:
            atMe.getAfter().setBefore(newFrob)
        atMe.setAfter(newFrob)
