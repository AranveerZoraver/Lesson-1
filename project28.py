class DailyDataHelper:
    def __init__(self, name="Daily Helper", values=None):
        self.name = name
        self.values = values if values is not None else []
        print(f"{self.name} created with {len(self.values)} values.")

    def add_value(self, value):
        self.values.append(value)
        print(f"Added: {value}")

    def show_values(self):
        for index, value in enumerate(self.values):
            print(f"Index {index}: {value}")

    def find_by_index(self, index):
        if 0 <= index < len(self.values):
            return self.values[index]
        return None

    def find_by_value(self, target):
        positions = []
        for index, value in enumerate(self.values):
            if value == target:
                positions.append(index)
        return positions

    def __del__(self):
        print(f"{self.name} is being removed.")


helper = DailyDataHelper("Study Tracker", ["math", "python", "science"])
helper.add_value("history")
helper.show_values()
print(helper.find_by_index(1))
print(helper.find_by_value("science"))
del helper