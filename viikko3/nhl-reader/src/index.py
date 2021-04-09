import requests
from player import Player
import datetime

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()
    timestamp = datetime.datetime.now()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []
    country = "FIN"

    for player_dict in response:
        player = Player(
            player_dict['name'], player_dict['nationality'], player_dict['assists'], player_dict['goals'], player_dict['team']
        )

        players.append(player)

    print(f"Players from {country} {timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')}\n")

    for player in players:
        if player.get_nationality() == country:
            print(player)


if __name__ == "__main__":
    main()
