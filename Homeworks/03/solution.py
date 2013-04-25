class Person:
    def __init__(self, name, gender, birth_year, father=None, mother=None):
        self.name, self.gender, self.birth_year = name, gender, birth_year
        self.father, self.mother = father, mother
        if(self.father is not None):
            self.father.successors.append(self)
        if(self.mother is not None):
            self.mother.successors.append(self)
        self.successors = []

    def children(self, gender=None):
        if(gender is None):
            return self.successors
        else:
            return \
                [child for child in self.successors if child.gender == gender]

    def is_direct_successor(self, child):
        return child in self.successors

    def get_relatives_by_parent(self, parent, gender):
        if parent == 'mother':
            mothers_children = self.mother.children(gender)
            return [child for child in mothers_children if self is not child]
        if parent == 'father':
            fathers_children = self.father.children(gender)
            return [child for child in fathers_children if self is not child]

    def get_relatives(self, gender):
        from_mother_side, from_father_side = [], []
        if(self.mother is not None):
            from_mother_side = self.get_relatives_by_parent('mother', gender)
        if(self.father is not None):
            from_father_side = self.get_relatives_by_parent('father', gender)
        return list(set(from_mother_side + from_father_side))

    def get_sisters(self):
        return self.get_relatives('F')

    def get_brothers(self):
        return self.get_relatives('M')
