import requests
import json


headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36"
}


faculties = ["ФМТ", "ФПТ", "ФІС", "ФЕМ"]


def collect_schedule():  # Метод для знаходження парсинг всіх груп
    with open("info.json", "r", encoding="utf8") as file:
        reading = json.load(file)
    s = requests.Session()  # Створення сесії
    for faculty in faculties:
        response = s.get(  # Відправлення запиту до сайту
            url=f"https://tntu.edu.ua/q.php?m=schedule&c=groups&state=active&faculty={faculty}",
            headers=headers)
        groups = response.json()["Groups"]
        reading[faculty] = {}
        for group in groups:
            response = s.get(
                url=f"https://tntu.edu.ua/q.php?m=schedule&c=get&group={group}",
                headers=headers)
            reading[faculty][group] = response.json()["Schedule"]["Lessons"]["Items"]
    with open("info.json", "w", encoding="utf8") as file:  # Записуємо зібрані дані у файл
        json.dump(reading, file, indent=4, ensure_ascii=False)
