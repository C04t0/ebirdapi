import sqlite3


class Database:

    def __init__(self, db_name):
        self.db_name = db_name

    def connect(self):
        connection = sqlite3.connect(self.db_name)
        connection.row_factory = sqlite3.Row
        return connection

    def get_all_species(self):
        with self.connect() as connection:
            cursor = connection.cursor()
            return cursor.execute(
                'select species_code, common_name, scientific_name, scientific_order, extinct from species').fetchall()

    def get_locations(self):
        with self.connect() as connection:
            cursor = connection.cursor()
            return cursor.execute(
                'select id, name, latitude, longitude, sub_national_code from locations').fetchall()
    def get_species_by_species_code(self, species_code):
        with self.connect() as conn:
            cursor = conn.cursor()
            return cursor.execute(
                'select species_code, common_name, scientific_name, scientific_order, extinct from species where species_code = ?',
                (species_code,)).fetchone()

    def find_species_by_common_name(self, common_name):
        common_name = '%' + common_name + '%'
        with self.connect() as conn:
            cursor = conn.cursor()
            return cursor.execute(
                'select species_code, common_name, scientific_name, scientific_order, extinct from species where common_name like ?',
                (common_name,)).fetchall()

    def find_species_by_scientific_name(self, scientific_name):
        scientific_name = '%' + scientific_name + '%'
        with self.connect() as conn:
            cursor = conn.cursor()
            return cursor.execute(
                'select species_code, common_name, scientific_name, scientific_order, extinct from species where scientific_name like ?',
                (scientific_name,)).fetchall()
