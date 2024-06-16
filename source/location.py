
class Location:
    def __init__(self, region_id: str, name: str, latitude: float, longitude: float, sub_national_code: str):
        self.region_id = region_id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.sub_national_code = sub_national_code

    def __repr__(self):
        return f'{self.__class__.__name__}({self.region_id}, {self.latitude}, {self.longitude})'

    def __str__(self):
        return f'Region_code: {self.region_id!r}, Latitude: {self.latitude!r}, Longitude: {self.longitude!r}'