import os
import sys
import requests as rq
from bs4 import BeautifulSoup
from plyer import notification as nt
import time



def main():
    while True:
            time.sleep(1)
            # time.sleep()

            url = 'https://www.worldometers.info/coronavirus/'
            res = rq.get(url)
            soup=BeautifulSoup(res.text, 'html.parser')

            mydata = ""
            for tr in soup.find_all('tbody')[0].find_all('tr'):
                mydata += tr.get_text()
                data = tr.get_text().split("\n\n")

                if data[0].startswith('\nBangladesh'):
                    items=[]
                    for i in data:
                        item = i.split('\n')
                        for it in item:
                            if it != '':
                                print(it)
                                items.append(it)
            time.sleep(10)

            nt.notify(
                title=items[0],
                message=f'''Total Cases: {items[1]}
                \nTotal Deaths: {items[2]}
                \nTotal Recovered: {items[3]}
                \nNew Deaths: {items[6]}''',
                app_name='Corona Update'
                # app_icon = None,
            )



if __name__ == "__main__":
    main()



