from json import JSONDecodeError
import requests


class EbirdAPI:

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = 'https://api.ebird.org/v2'
        self.header = {'x-ebirdapitoken': api_key}

    def __repr__(self):
        return f'{self.__class__.__name__}({self.api_key}, {self.base_url}, {self.header})'

    def __str__(self):
        return f'API key: {self.api_key!r}, Base URL: {self.base_url!r}, Header: {self.header!r}'

    def recent_observations_by_region(self, region_code):
        response = EbirdAPI.connection_exception_caller(
            requests.get(f'{self.base_url}/data/obs/{region_code}/recent', headers=self.header))
        return response.json()

    def recent_observations_by_species(self, region_code, species_code):
        response = EbirdAPI.connection_exception_caller(
            requests.get(f'{self.base_url}/data/obs/{region_code}/recent/{species_code}', headers=self.header))
        return response.json()

    def recent_nearby_observations(self, latitude, longitude):
        response = EbirdAPI.connection_exception_caller(
            requests.get(f'{self.base_url}/data/obs/geo/recent?lat={latitude}&lng={longitude}', headers=self.header))
        return response.json()

    def recent_nearby_observations_by_species(self, latitude, longitude, species_code):
        response = EbirdAPI.connection_exception_caller(
            requests.get(f'{self.base_url}/data/obs/geo/recent/{species_code}?lat={latitude}&lng={longitude}',
                         headers=self.header))
        return response

    def nearest_observation_of_species(self, latitude, longitude, species_code):
        response = EbirdAPI.connection_exception_caller(
            requests.get(f'{self.base_url}/data/nearest/geo/recent/{species_code}?lat={latitude}&lng={longitude}',
                         headers=self.header))
        return response.json()

    def nearby_notable_observations(self, latitude, longitude):
        response = EbirdAPI.connection_exception_caller(
            requests.get(f'{self.base_url}/data/obs/geo/recent/notable?lat={latitude}&lng={longitude}',
                         headers=self.header))
        return response.json()

    def recent_checklists_feed(self, region_code):
        response = EbirdAPI.connection_exception_caller(
            requests.get(f'{self.base_url}/product/lists/{region_code}', headers=self.header))
        return response

    def historic_observation_on_date(self, region_code, year, month, day):
        response = EbirdAPI.connection_exception_caller(
            requests.get(f'{self.base_url}/data/obs/{region_code}/historic/{year}/{month}/{month}/{day}',
                         headers=self.header))
        return response.json()

    def top_100_contributors_by_region_code_and_date(self, region_code, year, month, day):
        response = EbirdAPI.connection_exception_caller(
            requests.get(f'{self.base_url}/product/top100/{region_code}/{year}/{month}/{day}', headers=self.header))
        return response.json()

    def checklist_feed_on_date_by_region(self, region_code, year, month, day):
        response = EbirdAPI.connection_exception_caller(
            requests.get(f'{self.base_url}/product/stats/{region_code}/{year}/{month}/{day}', headers=self.header))
        return response

    def regional_statistics_on_date(self, region_code, year, month, day):
        response = EbirdAPI.connection_exception_caller(
            requests.get(f'{self.base_url}/product/top100/{region_code}/{year}/{month}/{day}', headers=self.header))
        return response.json()

    def species_code_list_of_region(self, region_code):
        response = EbirdAPI.connection_exception_caller(
            requests.get(f'{self.base_url}/product/spplist/{region_code}', headers=self.header))
        return response.json()

    def find_adjacent_regions(self, region_code):
        response = EbirdAPI.connection_exception_caller(
            requests.get(f'{self.base_url}/ref/adjacent/{region_code}', headers=self.header))
        return response.json()

    def find_hotspots_in_region(self, region_code):
        response = EbirdAPI.connection_exception_caller(
            requests.get(f'{self.base_url}/ref/hotspot/{region_code}', headers=self.header))
        return response.json()

    def hotspot_info(self, hotspot_id):
        response = EbirdAPI.connection_exception_caller(
            requests.get(f'{self.base_url}/ref/hotspot/info/{hotspot_id}', headers=self.header))
        return response.json()

    def region_info(self, region_code):
        response = EbirdAPI.connection_exception_caller(
            requests.get(f'{self.base_url}/ref/region/info/{region_code}', headers=self.header))
        return response.json()

    def sub_region_list(self, region_code, region_type):
        response = EbirdAPI.connection_exception_caller(
            requests.get(f'{self.base_url}/ref/region/list/{region_type}/{region_code}', headers=self.header))
        return response.json()

    @staticmethod
    def connection_exception_caller(request):
        try:
            return request
        except ConnectionError:
            print('Connection to the API failed.')
        except JSONDecodeError:
            print('JSON could not be decoded correctly.')
