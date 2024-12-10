import csv
import json
import os

from constants.constants import *


class DataPrep:
    def __init__(self) -> None:
        self.data_gen_folder = "dataset"
        self.data_keys_shape = {"endTime", "artistName", "trackName", "msPlayed"}
        self.data = {}

        os.makedirs(self.data_gen_folder, exist_ok=True)
        self.data_prep(target)

    def data_prep(self, path) -> None:
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path) and filename.endswith('.json'):
                if "music" in filename:
                    for item in self.load_json(file_path):
                        self.data_year_splitter(item)

        self.save_data()

    def data_year_splitter(self, item: dict):
        years = self.data.keys()
        year = item["date"][:4]

        if year in years:
            self.data[year].append(item)
        else:
            self.data[year] = [item]

    def save_data(self) -> None:
        for year in self.data:
            with open(os.path.join(self.data_gen_folder, f"{year}.csv"), mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=self.data.get(year)[0].keys())
                writer.writeheader()
                writer.writerows(self.data.get(year))

    def data_checker(self, data: dict) -> bool:
        if self.data_keys_shape != set(data.keys()):
            return False
        return True

    def load_json(self, path) -> dict:
        with open(path) as file:
            data = json.load(file)
            for item in data:
                if not self.data_checker(item):
                    raise KeyError("Invalid data format")

                yield {
                    "date": item["endTime"][:-6],
                    "artistName": item["artistName"],
                    "trackName": item["trackName"],
                    "msPlayed": item["msPlayed"]
                }
