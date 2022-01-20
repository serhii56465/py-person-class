class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for i in people:
        for key in i:
            Person(i["name"], i["age"])
    for j in people:
        for key in j:
            try:
                if j["wife"] is not None:
                    Person.people[j["name"]].wife = Person.people[j["wife"]]
            except KeyError:
                pass
            try:
                if j["husband"] is not None:
                    Person.people[j["name"]].husband = \
                        Person.people[j["husband"]]
            except KeyError:
                pass

    return [Person.people[i] for i in Person.people]
