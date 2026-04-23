import requests
from bs4 import BeautifulSoup


url = "https://bank.gov.ua/ua/markets/exchangerates"


def get_rates():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0.0.0 Safari/537.36"
    }

    r = requests.get(url, headers=headers)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")
    table = soup.find("table")

    if not table:
        return []

    result = []
    for row in table.find_all("tr")[1:]:
        cells = row.find_all("td")
        if len(cells) >= 4:
            result.append((
                cells[0].get_text(strip=True),
                cells[1].get_text(strip=True),
                cells[2].get_text(strip=True),
                cells[3].get_text(strip=True),
            ))

    return result


def show_table(data):
    w = [14, 14, 30, 16]

    def line(a, b, c, d):
        return f"| {a:<{w[0]}} | {b:<{w[1]}} | {c:<{w[2]}} | {d:<{w[3]}} |"

    header = line("Код цифровий", "Код літерний", "Назва валюти", "Офіційний курс")
    print(header)
    print("-" * len(header))

    for item in data:
        print(line(*item))


if __name__ == "__main__":
    data = get_rates()
    if data:
        show_table(data)
    else:
        print("Не вдалось отримати дані")