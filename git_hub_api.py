import pprint
import requests

token = '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'

url='https://api.github.com/search/code?q=eval+users:ubi22'
session = requests.session()
session.auth = ('olyakir', token)
result = session.get(url)
pprint.pprint(result.json())