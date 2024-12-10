import os
import pandas as pd
from matplotlib import pyplot as plt
from pandas import DataFrame

from constants.constants import *


class StatisticsGenerator():
    def __init__(self, year):
        self.data_folder = 'generated'
        self.year = year
        self.stat_folder = "statistics"
        os.makedirs(self.stat_folder, exist_ok=True)
        self.gen_stats()

    def gen_stats(self):
        self.gen_top_artists_graph()
        self.gen_top_songs_graph()
        self.gen_top_artist_song_count_graph()
        self.gen_top_date_listen_time_graph()

    def get_top_artists(self) -> DataFrame:
        file_path = os.path.join(self.data_folder, f"{self.year}_{artist_listen_time}.csv")
        if os.path.isfile(file_path):
            df = pd.read_csv(file_path, encoding='latin-1')
            return df.nlargest(5, 'mins_played')

    def gen_top_artists_graph(self):
        top_artists = self.get_top_artists()
        fig, ax = plt.subplots(figsize=(15, 8), facecolor='black')
        ax.set_facecolor('black')
        plt.tight_layout(pad=2)
        bars = plt.bar(top_artists['artist'], top_artists['mins_played'], color='#444444')

        plt.xlabel('Artist Name', color='white')
        plt.ylabel('Minutes Played', color='white')
        plt.title('Top 5 Artists by Minutes Played', color='white')

        for spine in ax.spines.values():
            spine.set_edgecolor('white')

        self.graph_indicator(bars)
        plt.savefig(os.path.join(self.stat_folder, f"{self.year}_{artist_listen_time}.png"), bbox_inches='tight',
                    facecolor='black')
        plt.close()

    def get_top_songs(self) -> DataFrame:
        file_path = os.path.join(self.data_folder, f"{self.year}_{song_listen_time}.csv")
        if os.path.isfile(file_path):
            df = pd.read_csv(file_path, encoding='latin-1')
            return df.nlargest(5, 'mins_played')

    def gen_top_songs_graph(self):
        top_songs = self.get_top_songs()
        fig, ax = plt.subplots(figsize=(15, 8), facecolor='black')
        ax.set_facecolor('black')
        plt.tight_layout()
        bars = plt.bar(top_songs['song'], top_songs['mins_played'], color='#444444')

        plt.xlabel('Song Name', color='white')
        plt.ylabel('Minutes Played', color='white')
        plt.title('Top 5 Songs by Minutes Played', color='white')

        self.graph_indicator(bars)
        for spine in ax.spines.values():
            spine.set_edgecolor('white')
        plt.savefig(os.path.join(self.stat_folder, f"{self.year}_top_songs.png"), bbox_inches='tight',
                    facecolor='black')
        plt.close()

    def get_total_listen_time(self) -> DataFrame:
        file_path = os.path.join(self.data_folder, f"{self.year}_{total_listen_time}.csv")
        if os.path.isfile(file_path):
            df = pd.read_csv(file_path, encoding='latin-1')
            return df

    def get_artist_song_count(self) -> DataFrame:
        file_path = os.path.join(self.data_folder, f"{self.year}_{artist_song_count}.csv")
        if os.path.isfile(file_path):
            df = pd.read_csv(file_path, encoding='latin-1')
            return df.nlargest(5, 'song_count')

    def gen_top_artist_song_count_graph(self):
        top_songs = self.get_artist_song_count()
        fig, ax = plt.subplots(figsize=(15, 8), facecolor='black')
        ax.set_facecolor('black')
        plt.tight_layout()
        bars = plt.bar(top_songs['artist'], top_songs['song_count'], color='#444444')

        plt.xlabel('Artist Name', color='white')
        plt.ylabel('Songs Played', color='white')
        plt.title('Top 5 Artists', color='white')
        self.graph_indicator(bars)
        for spine in ax.spines.values():
            spine.set_edgecolor('white')
        plt.savefig(os.path.join(self.stat_folder, f"{self.year}_{artist_song_count}.png"), bbox_inches='tight',
                    facecolor='black')
        plt.close()

    def top_date_listen_time(self) -> DataFrame:
        file_path = os.path.join(self.data_folder, f"{self.year}_{date_listen_time}.csv")
        if os.path.isfile(file_path):
            df = pd.read_csv(file_path, encoding='latin-1')
            return df.nlargest(5, 'mins_played')

    def gen_top_date_listen_time_graph(self):
        top_songs = self.top_date_listen_time()
        fig, ax = plt.subplots(figsize=(15, 8), facecolor='black')
        ax.set_facecolor('black')
        plt.tight_layout()
        bars = plt.bar(top_songs['date'], top_songs['mins_played'], color='#444444')

        plt.xlabel('Date', color='white')
        plt.ylabel('Minutes Played', color='white')
        plt.title('Top 5 Dates by Minutes Played', color='white')
        for spine in ax.spines.values():
            spine.set_edgecolor('white')

        self.graph_indicator(bars)
        plt.savefig(os.path.join(self.stat_folder, f"{self.year}_{date_listen_time}.png"), bbox_inches='tight',
                    facecolor='black')
        plt.close()

    @staticmethod
    def graph_indicator(bars, ax=None):
        for bar in bars:
            if ax is None:
                ax = plt.gca()
            yval = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,  # X position: center of the bar
                yval + 1,  # Y position: slightly above the bar
                f"{yval:.1f}",  # Text: formatted value
                ha='center',  # Horizontal alignment
                va='bottom',  # Vertical alignment
                fontsize=10,
                color='white'  # White text for visibility
            )
        plt.xticks(color="white", rotation=45)
        plt.yticks(color="white")

        plt.grid(color='gray', linestyle='--', linewidth=0.5)
