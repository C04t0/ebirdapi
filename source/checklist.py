
class Checklist:

    def __init__(self, checklist_id: int, date: str, location_id: int, num_of_observers: int, num_of_species: int, comment: str):
        self.id = checklist_id
        self.date = date
        self.location_id = location_id
        self.num_of_observers = num_of_observers
        self.num_of_species = num_of_species
        self.comment = comment

    def __repr__(self):
        return f'{self.__class__.__name__!r}({self.id}, {self.date!r}, {self.location_id}, {self.num_of_observers}, {self.num_of_species}, {self.comment})'

    def __str__(self):
        return f'{self.__class__.__name__!r}(Id: {self.id}, Date: {self.date}, Location_id: {self.location_id}, Number of observers: {self.num_of_observers}, Number of species: {self.num_of_species}, Comment: {self.comment})'

