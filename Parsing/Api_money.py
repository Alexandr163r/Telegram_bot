import requests


def get_api():
    r = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    return r


def money(r=get_api()):
    r = r.json()
    return (
        f'{r["Valute"]["USD"]["Name"]}:'
        f' {round(r["Valute"]["USD"]["Value"],2)}р.\n'
        f'{r["Valute"]["EUR"]["Name"]}:'
        f' {round(r["Valute"]["EUR"]["Value"],2)}р.\n'
        f'{r["Valute"]["GBP"]["Name"]}: '
        f'{round(r["Valute"]["GBP"]["Value"],2)}р.\n'
        f'{r["Valute"]["CNY"]["Name"]}: '
        f'{round(r["Valute"]["CNY"]["Value"],2)}р.\n'
    )


money()
