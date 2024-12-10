import math
import os
from tracemalloc import Statistic

from constants.constants import *
from utils.statistics import StatisticsGenerator


class MarkDownGenerator:

    def __init__(self, year):
        self.graph_folder = "statistics"
        self.year = year

        self.generate_markdown()

    def generate_markdown(self):
        image_path = os.path.join(self.graph_folder, f"{self.year}_{artist_listen_time}.png")
        output_md_file = f"analysis_report_{self.year}.md"

        with open(output_md_file, 'w') as f:
            f.write("# The Statistics Spotify Should've gave us\n")
            f.write("## Below are a few Graphs showcasing some statistics:\n\n")

            f.write("### Your Top 5 Artists\n")
            self.graph_to_md(image_path, "Top 5 Artists", f)

            image_path = os.path.join(self.graph_folder, f"{self.year}_{artist_song_count}.png")
            f.write("\n\n ### Top 5 Artists You've Listened by Song Count\n")
            self.graph_to_md(image_path, "Top 5 Artists by Song Count", f)

            image_path = os.path.join(self.graph_folder, f"{self.year}_{song_listen_time}.png")
            f.write("\n\n ### Your Top 5 Songs\n")
            self.graph_to_md(image_path, "Top 5 Songs", f)

            image_path = os.path.join(self.graph_folder, f"{self.year}_{date_listen_time}.png")
            f.write("\n\n ### Your Top 5 Dates by Listening Time\n")
            self.graph_to_md(image_path, "Top 5 Dates by Listen Time", f)

            f.write("\n\n# Last But Not Least\n")
            f.write("## Your total listening time\n")

            listen_time = StatisticsGenerator(self.year, False).get_total_listen_time()
            f.write(f"### Total Listening Time: {math.trunc(listen_time.iloc[0]['mins_played'])} minutes.\n")
            f.close()

    @staticmethod
    def graph_to_md(image_path, text, f):
        image_markdown = f"![{text}]({image_path})\n"
        f.write(image_markdown)
