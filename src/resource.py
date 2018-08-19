from src.objects.episode import Episode
from src.objects.pony import Pony


class PonyResource:
    pones = []
    episodes = []
    movies = []

    def __init__(self):
        try:
            with open('./data/episodes.txt', 'r', encoding='utf-8') as f:
                line = f.readline().strip()
                while line:
                    self.parse_episode(line)
                    line = f.readline().strip()
            with open('./data/ponies.txt', 'r', encoding='utf-8') as f:
                line = f.readline().strip()
                while line:
                    self.parse_pony(line)
                    line = f.readline().strip()
            # self.episodes = sorted(self.episodes, key=lambda x: (x.season, x.episode))
            self.episodes = sorted(self.episodes, key=lambda x: x.air_date)
            self.movies = sorted(self.movies, key=lambda x: (x.season, x.episode))
            self.pones = sorted(self.pones, key=lambda x: x.name)
        except IOError as ex:
            print('Something went wrong.\n\n{}'.format(ex))

    def parse_episode(self, raw):
        raw_ep = raw.split('|')
        # SHOW - TIMESTAMP - SEASON - EPISODE - TITLE
        if raw_ep[0] == 'FIM':
            ep_create = Episode(raw_ep[4], raw_ep[1], raw_ep[2], raw_ep[3], raw_ep[5] if len(raw_ep) > 5 else None)
            if raw_ep[2].isnumeric():
                # TV Episode
                self.episodes.append(ep_create)
            else:
                # Movie
                self.movies.append(ep_create)

    def parse_pony(self, raw):
        raw_pone = raw.split('|')
        # NAME - RACE - GENDER - URL
        pone_create = Pony(raw_pone[0], raw_pone[1], raw_pone[2], raw_pone[3])
        self.pones.append(pone_create)
