import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    #print(players[0].points)
    print("Oliot:")
    players.sort(key=take_points, reverse=True)
    for player in players:
        if player.nationality == "FIN":
            print(player)

def take_points(pelaaja):
        return pelaaja.points

if __name__ == "__main__":
    main()
