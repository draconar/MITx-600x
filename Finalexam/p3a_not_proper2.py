def insert(atMe, newFrob):
    if atMe!=newFrob:
        if atMe.myName().lower()==newFrob.myName().lower():
            newFrob.setBefore(atMe)
            newFrob.setAfter(atMe.getAfter())
            atMe.getAfter().setBefore(newFrob)
            atMe.setAfter(newFrob)
        elif atMe.myName().lower()>newFrob.myName().lower():
            if atMe.getBefore()==None:
                atMe.setBefore(newFrob)
                newFrob.setAfter(atMe)
            elif newFrob.myName().lower()>atMe.getBefore().myName().lower():
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
            elif newFrob.myName().lower()<atMe.getAfter().myName().lower():
                newFrob.setAfter(atMe.getAfter())
                newFrob.setBefore(atMe)
                atMe.getAfter().setBefore(newFrob)
                atMe.setAfter(newFrob)
            else:
                insert(atMe.getAfter(),newFrob)
