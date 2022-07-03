def find_duplicate(nums):
    newlist = []
    duplist = []
    for i in nums:
        if type(i) == int and i > 0:
            if i not in newlist:
                newlist.append(i)
            else:
                duplist.append(i)
    if len(duplist) > 0:
        return duplist[0]
    else:
        return False
