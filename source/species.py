

class Species:
    def __init__(self, species_code: str, common_name: str, scientific_name: str, order: str, extinct: bool):
        self.species_code = species_code
        self.common_name = common_name
        self.scientific_name = scientific_name
        self.order = order
        self.extinct = extinct

    def __repr__(self):
        return f'{self.__class__.__name__}({self.species_code}, {self.common_name}, {self.scientific_name}, {self.order}, {self.extinct})'

    def __str__(self):
        return f'{self.__class__.__name__}(Species code: {self.species_code!r}, Common English name: {self.common_name!r}, Scientific name: {self.scientific_name}, Order: {self.order!r}, Extinct: {self.extinct})'