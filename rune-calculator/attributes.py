class Attributes:
    def __init__(self, attributes: dict):
        self.attributes = attributes

    def __getList__(self):
        return self.attributes.keys()
