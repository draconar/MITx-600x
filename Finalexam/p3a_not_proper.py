def insert(atMe, newFrob):
    inListName = atMe.myName()
    newName = newFrob.myName()

    if(atMe.getBefore() == None and atMe.getAfter() == None):
        if(inListName >= newName):
            atMe.setBefore(newName)
            newFrob.setAfter(inListName)
        else:
            atMe.setAfter(newName)
            newFrob.setBefore(inListName)
    elif(inListName > newName):
        temp = atMe.getBefore()
        if(temp < newName):
            atMe.setBefore(newName)
            temp.setAfter(newName)
            newFrob.setBefore(temp)
            newFrob.setAfter(inListName)
        else:
            while(temp > newName and temp.getBefore() != None):
                temp = temp.getBefore()
            temp.setBefore(newName)
            newFrob.setAfter(temp)
    elif(inListName < newName):
        temp = atMe.getAfter()
        if(temp > newName):
            atMe.setAfter(newName)
            temp.setBefore(newName)
            newFrob.setBefore(inListName)
            newFrob.setAfter(temp)
        else:
            while(temp < newName and temp.getAfter() != None):
                temp = temp.getAfter()
            temp.setAfter(newName)
            newFrob.setBefore(temp)
    else:
        temp = atMe.getAfter()
        atMe.setAfter(newName)
        temp.setBefore(newName)
        newFrob.setBefore(inListName)
        newFrob.setAfter(temp)
