class User:
    def __init__(self):
        self.data = {}

    def set_data(self, data):
        self.data = data

    def update_data(self, data):
        for key in data:
            if key in self.data:
                self.data[key] = data[key]
