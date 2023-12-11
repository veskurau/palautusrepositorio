from player_reader import PlayerReader

class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class All:
    def __init__(self):
        self.all_players = PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt")


    def test(self, player):
        return self.all_players.get_players


class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value

class Not:
    def __init__(self, what_class):
        self._what_class = what_class
        self._value = what_class._value
        self._attr = what_class._attr

    def test(self, player):
        player_value = getattr(player, self._attr)
        if isinstance(self._what_class, HasAtLeast):
            return player_value < self._value
        else:
            return player_value >= self._value

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True

        return False
