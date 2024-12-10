import csv
import math
import os
from constants.constants import *
import pandas as pd
from pandas import DataFrame


class DataProcessor:
    def __init__(self):
        self.data_folder = "dataset"
        self.gen_folder = "generated"
        self.columns = [
            ("date", "mins_played"),
            ("artist", "song_count"),
            ("artist", "mins_played"),
            ("song", "mins_played"),
            ("year","mins_played")
        ]
        self.data = {}

        os.makedirs(self.data_folder, exist_ok=True)
        self.runner()

    def data_gatherer(self, date, data: DataFrame):
        time_collection = {}
        artist_song_collection = {}
        artist_time_collection = {}
        top_songs = {}
        totall_listen_time = 0

        for index, row in data.iterrows():
            listening_in_mins = int(row['msPlayed']) / 60000
            totall_listen_time += listening_in_mins

            self.field_collecting(row, 'date', time_collection, listening_in_mins)
            self.field_collecting(row, 'artistName', artist_time_collection, listening_in_mins)
            self.field_collecting(row, 'artistName', artist_song_collection)
            self.field_collecting(row, 'trackName', top_songs, listening_in_mins)

        self.data[date] = {
            date_listen_time: time_collection,
            artist_song_count: artist_song_collection,
            artist_listen_time: artist_time_collection,
            song_listen_time: top_songs,
            total_listen_time: {date: totall_listen_time}
        }

    def save_data(self):
        for date in self.data:
            for index, key in enumerate(self.data.get(date).keys()):
                with open(os.path.join(self.gen_folder, f"{date}_{key}.csv"), mode='w', newline='',
                          errors="replace") as file:
                    df = DataFrame(self.data.get(date).get(key).items(), columns=self.columns[index])
                    df.to_csv(file, index=False, encoding="utf-8")

    def runner(self):
        for filename in os.listdir(self.data_folder):
            file_path = os.path.join(self.data_folder, filename)
            if os.path.isfile(file_path) and filename.endswith('.csv'):
                data = pd.read_csv(file_path)
                self.data_gatherer(filename.split(".")[0], data)
        self.save_data()

    @staticmethod
    def field_collecting(row, column, collection, value=None):
        value = math.floor(value) if value is not None else None
        if row[column] not in collection:
            collection[row[column]] = value if value is not None else 1
        else:
            collection[row[column]] += value if value is not None else 1
