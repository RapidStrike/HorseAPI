class Episode:
    def __init__(self, title, air_date, season, episode, synopsis):
        self.title = title
        self.air_date = air_date
        self.season = int(season) if season.isnumeric() else season
        self.episode = int(episode)
        self.synopsis = synopsis
        self.is_movie = not season.isnumeric() and season != 'SPECIAL'

    def print(self):
        if not self.is_movie and self.synopsis:
            return {'title': self.title, 'air_date': self.air_date, 'season': self.season, 'episode': self.episode, 'synopsis': self.synopsis}
        elif self.is_movie:
            return {'title': self.title, 'air_date': self.air_date, 'series': self.season, 'number': self.episode, 'synopsis': self.synopsis}
        return {'title': self.title, 'air_date': self.air_date, 'season': self.season, 'episode': self.episode}
