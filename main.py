from utils.data_processor import DataProcessor
from utils.data_set_prep import DataPrep
from utils.markdown_generator import MarkDownGenerator
from utils.statistics import StatisticsGenerator


def main():
    DataPrep()
    DataProcessor()
    StatisticsGenerator(2024)
    MarkDownGenerator(2024)

if __name__ == '__main__':
    main()
