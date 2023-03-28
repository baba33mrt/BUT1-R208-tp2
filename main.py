def add_person(people_table, first_name, last_name, gender, birth_date):
    new_person = {'first_name': first_name, 'last_name': last_name, 'gender': gender, 'birth_date': birth_date}
    people_table.append(new_person)


def select_person():
    person_id = int(input("Entrez le numéro de la personne : "))
    return person_id


def add_parent_child_link(link_table, parent_id, child_id):
    link_table.append((child_id, parent_id))


def get_ancestors(link_table, person_id):
    ancestors = []
    for link in link_table:
        if link[0] == person_id:
            ancestors.append(link[1])
            ancestors += get_ancestors(link_table, link[1])
    return ancestors


def get_descendants(link_table, person_id):
    descendants = []
    for link in link_table:
        if link[1] == person_id:
            descendants.append(link[0])
            descendants += get_descendants(link_table, link[0])
    return descendants


def get_siblings(link_table, person_id):
    siblings = []
    for link in link_table:
        if link[0] != person_id and link[1] in get_ancestors(link_table, person_id):
            siblings.append(link[0])
    return siblings


def sort_people_by_name(people_table):
    sorted_people = sorted(people_table, key=lambda x: (x['last_name'], x['first_name']))
    return sorted_people


def sort_people_by_age(people_table):
    sorted_people = sorted(people_table, key=lambda x: x['birth_date'])
    return sorted_people


