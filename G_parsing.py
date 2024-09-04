import json
import time
import requests
import re

def get_html(link):
    st_accept = "text/html"
    st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
    headers = {
        "Accept": st_accept,
        "User-Agent": st_useragent
    }
    req = requests.get(link, headers)
    src = req.text
    time.sleep(1)
    return src

def clean_author(author):
    while True:
        if len(author) == 0:
            return ''
        if re.search('[а-яА-ЯёЁa-zA-Z]', author[0]) and re.search('[а-яА-ЯёЁa-zA-Z]', author[-1]):
            return author
        if not re.search('[а-яА-ЯёЁa-zA-Z]', author[0]):
            author = author[1:]
            continue
        if not re.search('[а-яА-ЯёЁa-zA-Z]', author[-1]):
            author = author[:-1]
            continue


def get_info_first_part(src):
    result = []
    searcher = "<div class=\"ArtDefault_cover__text__HKF_g\">"
    all_books = src.split(searcher)
    all_books.pop(0)
    for info_book in all_books:
        link = info_book[info_book.find("href=\"")+6:]
        link = link[:link.find("\"")]
        link = "https://www.litres.ru" + link
        info_book = info_book[info_book.find("p class=\"")+10:]
        info_book = info_book[info_book.find("\">")+2:]
        name = info_book[:info_book.find("</")]
        info_book = info_book[info_book.find("author"):]
        info_book = info_book[info_book.find("\">")+2:]
        author = info_book[:info_book.find("<")]
        info_book = info_book[info_book.find("art__ratingAvg\">") + len("art__ratingAvg\">"):]
        rating = info_book[:info_book.find("</")]
        info_book = info_book[info_book.find("ratingCount\">") + len("ratingCount\">"):]
        rating_count = info_book[:info_book.find("</")]
        info_book = info_book[info_book.find("art_price--value\">") + len("art_price--value\">"):]
        price = info_book[:info_book.find("</")]
        price = re.sub('\D', '', price)
        if rating == "0":
            rating_count = "0"
        result.append({
            "name": name,
            "author": author,
            "link": link,
            "rating": rating,
            "rating_count": rating_count,
            "price": price})
    return result


def get_info_second_part(text):
    base_text = text
    searched_text = "BookAuthor_author__name"
    #print(0, searched_text in text)
    text = text[text.find("<link href=\"")+12:]
    link = text[:text.find("\"")]
    #print(1, searched_text in text)
    text = text[text.find("BookCard_book__mainInfo__title"):]
    text = text[text.find(">")+1:]
    name = text[:text.find("</")]

    text = text[text.find("BookAuthor_author__name"):]
    text = text[text.find("<span itemProp=\"name\">")+22:]
    author = clean_author(text[:text.find("<")])
    #print(text)

    #print(2, searched_text in text)
    text = base_text[base_text.find("ratingValue")+22:]
    rating = text[:text.find("\"")]

    #print(3, searched_text in text)
    text = base_text[base_text.find("ratingCount")+20:]
    text = text[text.find("\"")+1:]
    rating_count = text[:text.find("\"")]


    #print(4, searched_text in text)
    #print(text)
    #print(text)
    #text = text[text.find("data-testid=\"art__authorName\" class=\"ArtInfoTile_person"):]


    #print(text)
    #print(text)
    #text = text[text.find("itemProp=\"name\">")+16:]
    #author = text[:text.find("<")]

    #text = text[text.find("CommentSystem_commentsCount"):]
    #text = text[text.find("\"")+2:]
    #review_count = text[:text.find("<")]

    text = text[text.find("Возрастное ограничение"):]
    text = text[text.find("<span>")+6:]
    age = text[:text.find("<")]

    #print(5, searched_text in text)
    text = text[text.find("Дата написания"):]
    text = text[text.find("<span>") + 6:]
    year = text[:text.find("<")]

    #print(6, searched_text in text)
    text = base_text[base_text.find("numberOfPages") + 15:]
    pages = text[:text.find("<")]

    #print(7, searched_text in text)
    text = text[text.find("final_price")+14:]
    price = text[:text.find("inapp_price")]
    price = text[:price.rfind(",")]
    result = {
        "name": name,
        "author": author,
        "link": link,
        "rating": rating,
        "rating_count": rating_count,
        #"review_count": review_count,
        "pages_count": pages,
        "price": price,
        "age": age,
        "year": year}
    #for el in result:
    #    print(el, result[el])
    return result

def delete_attrs(st):
    is_delete = False
    st = list(st)
    deleted_indexes = []
    for i in range(len(st)):
        if st[i] == "<":
            is_delete = True
            deleted_indexes.append(i)
            continue
        if st[i] == ">":
            is_delete = False
            deleted_indexes.append(i)
            continue
        if is_delete:
            deleted_indexes.append(i)
    for i in range(len(deleted_indexes) - 1 , -1, -1):
        st.pop(deleted_indexes[i])
    res = ""
    for el in st:
        res += el
    return res

def get_text_reviews(num):
    with open(f"files/books/reviews/book_{num}.txt", "r", encoding="utf-8") as file:
        text = file.read()
    text = text[text.find("AllComments_comments"):]
    list_comments = text.split("Comment_reviewText")
    if len(list_comments) == 0:
        return []
    list_comments.pop(0)
    result = []
    for el in list_comments:
        el = el[el.find("<p>")+3:]
        el = el[:el.find("</p>")]
        result.append(delete_attrs(el))
    return result


def validate_result(all_books):
    result = []
    for id in all_books:
        problems = []
        info = all_books[id]
        if info["name"].isspace():
            problems.append("name is empty")
        if info["author"].isspace():
            problems.append("author is empty")
        if not re.search(r'(https?://[^\s]+|www\.[^\s]+)', info["link"]):
            problems.append("link is not valid")
        if not (info["rating"][0].isdigit() and info["rating"][2].isdigit() and info["rating"][1] == '.'):
            problems.append("rating is not valid")
        if not info["rating_count"].isdigit():
            problems.append("rating_count is not valid")
        if not info["pages_count"].isdigit():
            problems.append("pages_count is not valid")
        if not info["price"].replace(".", "").isdigit() and info["price"] != 'null':
            problems.append("price is not valid")
        if info["age"][-1] != '+' or not info["age"][:-1].isdigit():
            problems.append("age is not valid")
        if not info["year"].isdigit() or len(info["year"]) != 4:
            problems.append("year is not valid")
        if len(problems) != 0:
            result.append(id)
    return result


NEED_TO_DOWNLOAD_FILES = False
if NEED_TO_DOWNLOAD_FILES:
    NUM_OF_ALL_PAGES = 40

    print("Процесс скачивания страниц (1/3)...")
    for num in range(1, NUM_OF_ALL_PAGES + 1):
        print(f"{num*100/NUM_OF_ALL_PAGES}%")
        src = get_html("https://www.litres.ru/genre/programmirovanie-5272/?page=" + str(num))
        with open('files/page_' + str(num) + ".txt", 'a+', encoding="utf-8") as f:
            f.write(src)
    count = 0
    links_of_books = []
    print("Процесс скачивания книг (2/3)...")
    for num in range(1, NUM_OF_ALL_PAGES + 1):
        with open(f"files/page_{num}.txt", "r", encoding="utf-8") as file:
            src = file.read()
            info = get_info_first_part(src)
            for el in info:
                count += 1
                print(f"{count * 100 / (24 * NUM_OF_ALL_PAGES)}%")
                link = el["link"]
                links_of_books.append(link)
                with open(f"files/books/book_{count}.txt", "a+", encoding="utf-8") as book:
                    book.write(get_html(link))
    print("Процесс скачивания отзывов (3/3)...")
    count = 0
    for link in links_of_books:
        count += 1
        link = link + "otzivi/"
        with open(f"files/books/reviews/book_{count}.txt", "a+", encoding="utf-8") as review:
            print(f"{count * 100 / (24 * NUM_OF_ALL_PAGES)}%")
            review.write(get_html(link))

    print("Файлы скачаны")
NEED_TO_PARSE_FILES = False
if NEED_TO_PARSE_FILES:
    all_books = {}
    for num in range(1, 961):
        with open(f"files/books/book_{num}.txt", "r", encoding="utf-8") as file:
            src = file.read()
            info = get_info_second_part(src)
            text_reviews = get_text_reviews(num)
            info["review_count"] = len(text_reviews)
            info["text_reviews"] = text_reviews
            all_books[num] = info
    with open(f"files/books/parsed_info.txt", "w", encoding="utf-8") as file:
        file.write(json.dumps(all_books))
with open(f"files/books/parsed_info.txt", "r", encoding="utf-8") as file:
    all_books = json.loads(file.read())
    print("Файлы готовы к валидации")
bad_books = validate_result(all_books)
if (len(bad_books) == 0):
    print('Успех! \"Плохих\" книг нет')
else:
    print(f"Всего {len(bad_books)} плохих книг. Их удалим") #272 книги
    for bad_id in bad_books:
        all_books.pop(bad_id)
    with open(f"files/books/parsed_info.txt", "w", encoding="utf-8") as file:
        file.write(json.dumps(all_books))
#print(all_books)
"""
for el in all_books:
    print(el)
    for el1 in all_books[el]:
        print("----", el1, all_books[el][el1])
    print("_______________")"""