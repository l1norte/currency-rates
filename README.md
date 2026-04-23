# currency-rates

Pulls official exchange rates from the National Bank of Ukraine and prints them as a formatted table right in your terminal. No third-party table libraries — just plain Python string formatting.

---

## What it does

The script hits [bank.gov.ua](https://bank.gov.ua/ua/markets/exchangerates), scrapes the exchange rate table with `requests` and `BeautifulSoup4`, and outputs it with five columns: numeric code, letter code, unit, currency name, and official rate.

```
| Код цифровий   | Код літерний   | Од.    | Назва валюти                   | Офіційний курс   |
---------------------------------------------------------------------------------------------------------
| 840            | USD            | 1      | Долар США                      | 43,8873          |
| 978            | EUR            | 1      | Євро                           | 51,4974          |
| 826            | GBP            | 1      | Фунт стерлінгів                | 59,2522          |
| 392            | JPY            | 10     | Єна                            | 2,7557           |
...
```

---

## Project structure

```
currency-rates/
├── main.py            # fetching and displaying rates
├── requirements.txt   # dependencies
└── README.md
```

---

## Requirements

Python 3.8 or higher. Everything else is in `requirements.txt`:

```
requests==2.33.0
beautifulsoup4==4.12.3
```

---

## Getting started

Clone the repo and step into it:

```bash
git clone https://github.com/l1norte/currency-rates.git
cd currency-rates
```

Set up a virtual environment:

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

---

## Branches

| Branch               | What's there                    |
|----------------------|---------------------------------|
| `main`               | Final working version           |
| `feature/parser`     | Data fetching and parsing logic |
| `feature/formatting` | Table formatting and output     |

---

## Author

Титаренко Богдан — 1st year, group ІК-8-25-Б1КНТ, speciality 122 Computer Science, MAUP, Kyiv 2026