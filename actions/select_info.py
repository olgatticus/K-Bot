groups_info = [
    {"group": "BTS", "info": {"debut": "2013", "company": "BigHit", "members": "7", "activity": "inactive"}},
    {"group": "NCT", "info": {"debut": "2016", "company": "SM", "members": "23", "activity": "active"}},
    {"group": "Stray Kids", "info": {"debut": "2018", "company": "JYPE", "members": "8", "activity": "active"}},
    {"group": "Seventeen", "info": {"debut": "2015", "company": "Pledis", "members": "13", "activity": "active"}},
    {"group": "TXT", "info": {"debut": "2019", "company": "BigHit", "members": "4", "activity": "active"}},
    {"group": "Blackpink", "info": {"debut": "2016", "company": "YG", "members": "4", "activity": "active"}},
    {"group": "EXO", "info": {"debut": "2012", "company": "SM", "members": "9", "activity": "active"}},
]

def extract_info(group):
    if group == "BTS":
        return {"debut": "2013", "company": "BigHit", "members": "7", "activity": "inactive"}
    elif group == "NCT":
        return {"debut": "2016", "company": "SM", "members": "23", "activity": "active"}
    elif group == "Stray Kids":
        return {"debut": "2018", "company": "JYPE", "members": "8", "activity": "active"}
    elif group == "Seventeen":
        return {"debut": "2015", "company": "Pledis", "members": "13", "activity": "active"}
    elif group == "TXT":
        return {"debut": "2019", "company": "BigHit", "members": "4", "activity": "active"}
    elif group == "Blackpink":
        return {"debut": "2016", "company": "YG", "members": "4", "activity": "active"}
    elif group == "EXO":
        return {"debut": "2012", "company": "SM", "members": "9", "activity": "active"}

#group = "Stray Kids"
#info = extract_info(group)
#print(info["debut"])