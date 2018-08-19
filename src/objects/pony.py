class Pony:
    def __init__(self, name, race, gender, url):
        self.name = name
        self.race = race
        self.gender = gender
        self.url = url

    def print(self):
        return {'name': self.name, 'race': self.race, 'gender': self.gender, 'url': self.url}
