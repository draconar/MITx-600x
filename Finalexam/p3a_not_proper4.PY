def insert(atMe, newFrob):
    if atMe!=newFrob:
        if atMe.myName() == newFrob.myName():
            newFrob.setBefore(atMe)
            newFrob.setAfter(atMe.getAfter())
            atMe.getAfter().setBefore(newFrob)
            atMe.setAfter(newFrob)
        elif atMe.myName()>newFrob.myName():
            if atMe.getBefore()==None:
                atMe.setBefore(newFrob)
                newFrob.setAfter(atMe)
            elif newFrob.myName()>atMe.getBefore().myName():
                newFrob.setBefore(atMe.getBefore())
                newFrob.setAfter(atMe)
                atMe.getBefore().setAfter(newFrob)
                atMe.setBefore(newFrob)
            else:
                insert(atMe.getBefore(),newFrob)
        else:
            if atMe.getAfter()==None:
                atMe.setAfter(newFrob)
                newFrob.setBefore(atMe)
            elif newFrob.myName()<atMe.getAfter().myName():
                newFrob.setAfter(atMe.getAfter())
                newFrob.setBefore(atMe)
                atMe.getAfter().setBefore(newFrob)
                atMe.setAfter(newFrob)
            else:
                insert(atMe.getAfter(),newFrob)
    return
