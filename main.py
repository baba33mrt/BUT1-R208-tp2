def add(array, FirstName, LastName, gender, birth_date):
    array.append([FirstName, LastName, gender, birth_date])


def select_person(array, firstName, LastName):
    i = 0
    while i < len(array):
        if array[i][0] == firstName and array[i][1] == LastName:
            return i


def viewTab(array):
    i = 0
    string = 'Nom\t\tPrénom\tSex\tDate de naissance\n'
    while i < len(array):
        j = 0
        while j < len(array[i]):
            string = string + f'{array[i][j]}\t'
            j = j + 1
        i = i + 1
        string = string + '\n'
    print(string)


def link(link_table, parent_id, child_id):
    link_table.append([child_id, parent_id])


def getAscendants(link_table, person_id):
    ancestors = []
    for link in link_table:
        if link[0] == person_id:
            ancestors.append(link[1])
            ancestors += getAscendants(link_table, link[1])
    return ancestors


def getDescendants(link_table, person_id):
    descendants = []
    for link in link_table:
        if link[1] == person_id:
            descendants.append(link[0])
            descendants += getDescendants(link_table, link[0])
    return descendants


def getFrere(link_table, person_id):
    siblings = []
    for link in link_table:
        if link[0] != person_id and link[1] in getAscendants(link_table, person_id):
            siblings.append(link[0])
    return siblings



tab1, tab2 = [], []
add(tab1, 'John', 'Fern', 'H', (1, 3, 1993))

viewTab(tab1)
