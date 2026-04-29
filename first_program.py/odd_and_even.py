import os

class ANSIFormatter:
    VIOLET = '\033[95m'
    AQUA = '\033[96m'
    EMERALD = '\033[92m'
    END = '\033[0m'
    BOLD = '\033[1m'
class DataStreamer:
    def __init__(self, target_file="numbers.txt"):
        self.target_file = target_file
        self.even_collection = []
        self.odd_collection = []
