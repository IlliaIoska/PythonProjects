import requests
import bs4

def select_two_star_products():
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"
    for i in range(1, 51):
        res = requests.get(base_url.format(i))
        soup = bs4.BeautifulSoup(res.text, "lxml")
        books = soup.select(".product_pod")
        for book in books:
            if book.select(".star-rating.Two") != 0:
                print(book.select("a")[1]["title"])
        

    
                  
    
select_two_star_products()
