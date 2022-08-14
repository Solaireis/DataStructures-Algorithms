list = ['Bougainvillea','Orchids','Hibiscus','Frangipani','Honeysuckle']

def front_H(list):
    hList = []
    otherList = []
    for i in list:
        if i.startswith('H'):
            hList.append(i)
        else:
            otherList.append(i)

    return sorted(hList) + sorted(otherList)

print(front_H(list))