import requests

base_url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api"

hero_intelligence = {}

def get_hero_list(hero_name):
    uri = '/all.json'
    request_url = base_url + uri
    response = requests.get(request_url)
    response.json()
    for hero in response.json():
        if hero ["name"] == hero_name:
            intelligence = hero["powerstats"]["intelligence"]
            hero_intelligence[hero_name] = int(intelligence)
            print(hero_intelligence)

if __name__ == '__main__':

    get_hero_list("Hulk")
    get_hero_list("Captain America")
    get_hero_list("Thanos")

int_max = max(list(hero_intelligence.values()))
rev = dict(map(reversed, hero_intelligence.items()))
pers_max = rev[int_max]
print(f"Наибольший интеллект {int_max} у персонажа {pers_max}")










