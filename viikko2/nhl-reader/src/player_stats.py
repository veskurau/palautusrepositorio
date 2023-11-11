class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = self.reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        top_scorers = []
        self.players.sort(key=self.take_points, reverse=True)
        for player in self.players:
            if player.nationality == nationality:
                top_scorers.append(player)
        return top_scorers

    def take_points(self, pelaaja):
        return pelaaja.points
