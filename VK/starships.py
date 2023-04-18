import requests

urls = [
    "https://swapi.dev/api/starships/?page=1",
    "https://swapi.dev/api/starships/?page=2",
    "https://swapi.dev/api/starships/?page=3",
    "https://swapi.dev/api/starships/?page=4",
]

def ship(api):
    max_speed = 0
    max_ship = ''
    for api in urls:
        response = requests.get(api).json()
        for ship in response['results']:
            sh = (ship["name"])
            s = ship.get('max_atmosphering_speed')
            if s and s != 'unknown' and s != '0' and s != 'n/a' and s != '1000km':
                s = float(s)
                if s > max_speed:
                    max_speed = s
                    max_ship = ship.get('name')
    return (f"Корабль {max_ship} имеет наибольшую скорость - {max_speed}.")

if __name__ == '__main__':
    print(ship(urls))