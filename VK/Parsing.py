import requests

urls = [
    "https://swapi.dev/api/planets/?page=1",
    "https://swapi.dev/api/planets/?page=2",
    "https://swapi.dev/api/planets/?page=3",
    "https://swapi.dev/api/planets/?page=4",
    "https://swapi.dev/api/planets/?page=5",
    "https://swapi.dev/api/planets/?page=6",
]

def planet(api):
    max_diameter = 0
    max_planet = ''
    for api in urls:
        response = requests.get(api).json()
        for planet in response['results']:
            pl = (planet["name"])
            d = planet.get('diameter')
            if d and d != 'unknown' and d != '0':
                d = float(d)
                if d > max_diameter:
                    max_diameter = d
                    max_planet = planet.get('name')
            a = (max_diameter, max_planet)
    return (f"Планета {max_planet} имеет наибольший диаметр - {max_diameter} км.")

if __name__ == '__main__':
    print(planet(urls))