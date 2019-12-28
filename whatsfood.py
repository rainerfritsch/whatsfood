from bs4 import BeautifulSoup
from datetime import datetime
import requests, argparse,os



parser = argparse.ArgumentParser()
parser.add_argument('-d','--date', help='use date instead of today - format: Y-M-D')
args = parser.parse_args()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def whatsfood(fdate):
    cls()
    page = requests.get("https://www.studentenwerk-muenchen.de/mensa/speiseplan/speiseplan_411_-de.html")
    if page.status_code==200 :
        #print("page fetched")

        soup = BeautifulSoup(page.content, 'html.parser')
        try:
            result=soup.find("p", text="Leopoldstraße 13a, München").parent.find(class_=fdate).parent.findAll(class_="c-schedule__list-item")
            if len(result)>0:
                for r in result:
                    res=r.find(class_="js-schedule-dish-description")
                    print (res.text)
            else:
                print("Heute gibts nix!")
        except:
            print("Für diesen Tag existieren keine Daten :-(")

    else :
        print("page not reachable "  + page.status_code)

if __name__ == "__main__":
    if args.date is not None:
        fooddateStr="heute_"+args.date
    else:
        heute = datetime.now()
        fooddateStr=heute.strftime("heute_%Y-%m-%d");

    print(fooddateStr)
    whatsfood(fooddateStr)
