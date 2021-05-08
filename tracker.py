# Asin: B08R59YH7W
# URL Template: https://www.amazon.ca/dp/
# Simplied URL: https://www.amazon.ca/dp/B08R59YH7W
# Price: price_inside_buybox
# Price: priceblock_ourprice

import datetime
import nest_asyncio
from requests_html import HTMLSession
from requests_html import AsyncHTMLSession

nest_asyncio.apply()

class PandaTracker(object):
    
    def __init__(self, ASIN: str, desired_price: float = 0):
        self.ASIN = ASIN
        self.title = None
        self.URL = 'https://www.amazon.ca/dp/'+ self.ASIN
        self.desired_price = desired_price
        self.price = float(0)

    async def get_info(self):
    
        session = AsyncHTMLSession()
        request = await session.get(self.URL)
        await request.html.arender(sleep=1)
        
        self.title = request.html.find('#productTitle')[0].text.strip()
        
        try:
            self.price = request.html.find('#price_inside_buybox')[0].text.replace('$','').replace(',','').strip()
        except:
            self.price = request.html.find('#priceblock_ourprice')[0].text.replace('$','').replace(',','').strip()
    
    async def set_desired_price(self):
        
        self.desired_price = self.price


# async def get_info(ASIN):
    
#     ASIN = str(ASIN)
#     desired_price = 0
#     URL = 'https://www.amazon.ca/dp/'+ ASIN
    
#     session = AsyncHTMLSession()
#     request = await session.get(URL)
#     await request.html.arender(sleep=1)
    
#     title = request.html.find('#productTitle')[0].text.strip()
    
#     try:
#         price = request.html.find('#price_inside_buybox')[0].text.replace('$','').replace(',','').strip()
#     except:
#         price = request.html.find('#priceblock_ourprice')[0].text.replace('$','').replace(',','').strip()
    
#     return (title, price)
