import click
import requests

BASE_URL = "https://api.coinmarketcap.com/v1/ticker/"
ETHEREUM_URL = BASE_URL + "ethereum/"

@click.command()
@click.argument('currencies', nargs=-1)
def cli(currencies):
    """Fetch prices"""
    if len(currencies) == 0:
        return

    res = requests.get(ETHEREUM_URL)
    btc_eth = 1 / float(res.json()[0]['price_btc'])

    results = []
    for currency in currencies:
        res = requests.get(BASE_URL + currency)
        cur_btc = float(res.json()[0]['price_btc'])
        cur_eth = btc_eth * cur_btc
        results.append("{0:.8f}".format(cur_eth))

    click.echo("\n".join(results))

