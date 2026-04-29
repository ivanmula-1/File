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
def _validate_source(self):
        if not os.path.exists(self.target_file):
            raise FileNotFoundError(f"Missing: {self.target_file}")
def _yield_integers(self):
        self._validate_source()
        with open(self.target_file, 'r') as stream:
            for line in stream:
                if line.strip():
                    yield int(line.strip())
def distribute_data(self):
        for val in self._yield_integers():
            if val % 2 == 0:
                self.even_collection.append(str(val))
            else:
                self.odd_collection.append(str(val))
        self._finalize_outputs()
def _finalize_outputs(self):
        mapping = {
            "even_results.txt": self.even_collection,
            "odd_results.txt": self.odd_collection
        }
        for path, contents in mapping.items():
            with open(path, "w") as f:
                f.write("\n".join(contents))
                
def generate_terminal_summary(self):
        print(f"{ANSIFormatter.EMERALD}--- TASK COMPLETE ---{ANSIFormatter.END}")
        print(f"{ANSIFormatter.VIOLET}Evens: {len(self.even_collection)}")
        print(f"{ANSIFormatter.AQUA}Odds:  {len(self.odd_collection)}{ANSIFormatter.END}")

def distribute_data(self):
        self._finalize_outputs()
        self.generate_terminal_summary()
