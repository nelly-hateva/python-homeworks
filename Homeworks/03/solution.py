class Person:
    def __init__(self, name, gender, birth_year, father=None, mother=None):
        self.name, self.gender, self.birth_year = name, gender, birth_year
        self.father, self.mother = father, mother
        if(self.father is not None):
            self.father.successor.append(self)
        if(self.mother is not None):
            self.mother.successor.append(self)
        self.successor = []

    def children(self, gender=None):
        if(gender == 'M'):
            return [child for child in self.successor if child.gender == 'M']
        elif(gender == 'F'):
            return [child for child in self.successor if child.gender == 'F']
        else:
            return self.successor

    def is_direct_successor(self, child):
        return child in self.successor

    def get_sisters(self):
        sisters_from_mother, sisters_from_father = [], []
        if(self.mother is not None):
            sisters_from_mother = \
            [child for child in self.mother.children('F') if self is not child]
        if(self.father is not None):
            sisters_from_father = \
            [child for child in self.father.children('F') if self is not child]
        return list(set(sisters_from_mother + sisters_from_father))

    def get_brothers(self):
        brothers_from_mother, brothers_from_father = [], []
        if(self.mother is not None):
            brothers_from_mother = \
            [child for child in self.mother.children('M') if self is not child]
        if(self.father is not None):
            brothers_from_father = \
            [child for child in self.father.children('M') if self is not child]
        return list(set(brothers_from_mother + brothers_from_father))
