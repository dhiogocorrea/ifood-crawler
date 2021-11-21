from fastapi import FastAPI, Query, HTTPException, File, Depends, Body
from fastapi.middleware.cors import CORSMiddleware
import requests

# merchant ids de são paulo:
# 64006199-9343-47cc-a6ea-e7cd3450168d - ifood-mercado-by-extra-liberdade
# 37e7c9ac-2358-4a92-819e-73a8d9001e61 - pao-de-acucar---oscar-freire-cerqueira-cesar
# c7694a1c-b4f6-40d8-a528-4101f152c4fa - Korin - Vila Mariana

merchant_ids_sp = ['64006199-9343-47cc-a6ea-e7cd3450168d', '37e7c9ac-2358-4a92-819e-73a8d9001e61', 'c7694a1c-b4f6-40d8-a528-4101f152c4fa']

app = FastAPI(title='Ifoodonation - Ifood Crawler API', version='1.0.0', docs_url='/')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

_url_base = 'https://marketplace.ifood.com.br/v2/search/catalog-items?latitude=-23.5557714&longitude=-46.6395571&channel=IFOOD&term=<PLACEHOLDER>&size=36&page=0&item_from_merchant_ids='


@app.get('/find/{term}', tags=['ifood'])
def find_item(term):
    url = _url_base.replace('<PLACEHOLDER>', term) + ','.join(merchant_ids_sp)
    response = requests.get(url)
    result = []
    if response.status_code == 200:
        data = response.json()

        for item in data['items']['data']:
            new_item = {}
            new_item['id_'] = item['id']
            new_item['code'] = item['code']
            new_item['name'] = item['name']
            new_item['description'] = item['description']
            new_item['price'] = item['price']
            new_item['merchant_id'] = item['merchant']['id']
            new_item['merchant_name'] = item['merchant']['name']

            result.append(new_item)
    return result
