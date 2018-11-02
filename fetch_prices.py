import click
import requests

URL = 'https://{}-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

@click.command()
@click.argument('env')
@click.argument('api_key')
@click.argument('target_currency')
@click.argument('currencies', nargs=-1)
def cli(env, api_key, target_currency, currencies):
    """Fetch prices"""
    if len(currencies) == 0:
        return
    currencies = [str(int(float(currency))) for currency in currencies]

    url = URL.format(env)
    headers = {'X-CMC_PRO_API_KEY': api_key}
    payload = {'id': ','.join(currencies), 'convert': target_currency}
    res = requests.get(url, headers=headers, params=payload).json()
    #click.echo(res)
    for currency in currencies:
        #click.echo(currency)
        price = res['data'][currency]['quote'][target_currency]['price']
        click.echo("{0:.9f}".format(price))

