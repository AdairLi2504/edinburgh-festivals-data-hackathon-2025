memberships = ["Friend","Silver Friend","Gold Friend",
                "Ambassador","Silver Ambassador","Gold Ambassador","Non"]

def isAP(raw:str|float)->bool:
    if raw != raw:
        return False
    else:
        return ("Access Pass" in raw)

def deformat_membership(raw:str|float)->str:
    if raw != raw:
        return "Non"
    membership_c=["Friend Membership","Silver Friend Membership","Gold Friend Membership",
                  "Ambassador Membership","Silver Ambassador Membership","Gold Ambassador Membership"]
    if raw == "Ambassador Membership - Monthly, Silver Ambassador Membership":
        return "Silver Ambassador"
    if raw == "Friend Membership, Gold Friend Membership":
        return "Gold Friend"
    if "Friend Membership, Silver Friend Membership" in raw:
        return "Silver Friend"
    if raw == "Festival Society Life Membership, Ambassador Membership":
        return "Ambassador"
    for i in membership_c:
        if raw[:len(i)]==i:
            return i[:-11]
    return "Non"

def isYMP(raw:str|float)->bool:
    if raw != raw:
        return False
    else:
        return ("Young Musician's Pass" in raw)