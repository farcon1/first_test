import json
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

with open(f"files/books/parsed_info.txt", "r", encoding="utf-8") as file:
    all_books = json.loads(file.read())
print("1. Выведите первые 5 строк датасета. (0.25). Сколько в нём строк и столбцов (0.25)?")
list_of_ids = []
for id in all_books:
    list_of_ids.append(id)
list_of_ids = sorted(list_of_ids, key= lambda s: int(s))
for num_id in range(5):
    id = list_of_ids[num_id]
    info = all_books[id]
    print(f"id {id}")
    for el in info:
        print(el, info[el])
    print("_" * 50)
print(f"В датасете {len(all_books)} строк и {len(all_books[list_of_ids[0]]) + 1} столбцов")
print("+" * 100)

print("2. Есть ли в датасете пропуски? (0.5)")
print("Да, пропуски были в изначальном датасете. Например, цена можно быть null, год написания книги может быть \
неизвестен и были неизвестны количество страниц в некоторых книгах. Такие строки я удалил")
print("+" * 100)
print("3. Проверьте типы данных. Если это необходимо, приведите к типам int и float те столбцы, с которыми понадобится работать как с числами. (1).")
all_books_new = {}
for i in range(len(list_of_ids)):
    id = int(list_of_ids[i])
    list_of_ids[i] = id
    all_books_new[id] = all_books[str(id)]
for id in list_of_ids:
    all_books_new[id]["rating"] = float(all_books_new[id]["rating"])
    all_books_new[id]["rating_count"] = int(all_books_new[id]["rating_count"])
    all_books_new[id]["pages_count"] = int(all_books_new[id]["pages_count"])
    if all_books_new[id]["price"] == 'null':
        all_books_new[id]["price"] = "0"
    all_books_new[id]["price"] = float(all_books_new[id]["price"])
    all_books_new[id]["age"] = int(all_books_new[id]["age"][:-1])
    all_books_new[id]["year"] = int(all_books_new[id]["year"])
    all_books_new[id]["review_count"] = int(all_books_new[id]["review_count"])
print("+" * 100)
print("4. Выведите описательные статистики переменных. Ответьте на следующие вопросы: ")
print("Какая медианная цена книги в вашем датасете? (1) ")
list_of_prices = []
for el in list_of_ids:
    list_of_prices.append(all_books_new[el]["price"])
list_of_prices.sort()
mid = len(list_of_prices) // 2
print((list_of_prices[mid] + list_of_prices[~mid]) / 2)
print("Какое возрастное ограничение встречается чаще всего? (1) ")
list_of_ages = []
for el in list_of_ids:
    list_of_ages.append(all_books_new[el]["age"])
print(str(max(set(list_of_ages), key = list_of_ages.count)) + "+")
print("Какое среднее число отзывов в книге? (1) ")
list_of_reviews_count = []
for el in list_of_ids:
    list_of_reviews_count.append(all_books_new[el]["review_count"])
print(sum(list_of_reviews_count) / len(list_of_reviews_count))
print("Сколько книг имеют оценку ниже 4.25? (1) ")
count = 0
for el in list_of_ids:
    if all_books_new[el]["rating"] < 4.5:
        count += 1
print(f"{count} из {len(list_of_ids)} книг")
print("В каком году было написано больше всего книг из датасета? (1)")
list_of_years = []
for el in list_of_ids:
    list_of_years.append(all_books_new[el]["year"])
year_max = max(set(list_of_years), key = list_of_years.count)
print(str(year_max) + " - " + str(list_of_years.count(year_max)) + " книг")
print("+" * 100)
print("5. Если вы работаете с готовым датасетом, то попробуйте \"достать\" из столбца pages количество страниц. Если у вас не получилось, то далее при определении числа страниц пользуйтесь стольцов pages_count. Если вы парсили датасет сами, то вы получаете балл за этот пункт автоматически (1.5)")
print("+" * 100)
print("6. Создайте новое поле is_popular. Значение равно 1, если рейтинг книги не менее 4.6 и при этом у нее не менее 5 отзывов, и 0 в остальных случаях. (1)")
for id in list_of_ids:
    if all_books_new[id]["rating"] >= 4.6:
        all_books_new[id]["is_popular"] = 1
    else:
        all_books_new[id]["is_popular"] = 0
print("+" * 100)
print("7. Как отличается среднее число страниц среди популярных и непопулярных книг? (2)")
sum_popular = 0
count_popular = 0
sum_not_popular = 0
count_not_popular = 0
for book in all_books_new:
    if all_books_new[book]["is_popular"] == 1:
        count_popular += 1
        sum_popular += all_books_new[book]["pages_count"]
    else:
        count_not_popular += 1
        sum_not_popular += all_books_new[book]["pages_count"]
print(f"Количество книг:\n  - популярные: {count_popular} книг \n  - не популярные: {count_not_popular} книг")
print(f"Среднее количество страниц:\n  - популярные: {sum_popular/count_popular} страниц \n  - не популярные: {sum_not_popular/count_not_popular} страниц")
print("+" * 100)
print("8. Выведите топ-10 книг по числу отзывов. (2)")
book_count_review = {}
for id in list_of_ids:
    book_count_review[all_books_new[id]["name"]] = all_books_new[id]["review_count"]
sorted_dict = sorted(book_count_review.items(), key=lambda x: x[1], reverse=True)
for i in range(10):
    print(f"{sorted_dict[i][0]} - {sorted_dict[i][1]} отзывов")
print("+" * 100)
print("9. Найдите среднюю длину отзыва (в символах). (2)")
all_reviews = []
for id in list_of_ids:
    for review in all_books_new[id]["text_reviews"]:
        all_reviews.append(len(review))
print(f"Средняя длина отзыва - {sum(all_reviews)/len(all_reviews)} символов")
print("+" * 100)
print("10. Постройте таблицу корреляций числовых переменных. (1) Прокомментируйте результаты. (1)")
print("Среди аналилизируемых значений выберем следующие:\n  - рейтинг\n  - количество оценок\n  - количество страниц\n  - цена\n  - количество отзывов")

new_rating = []
new_rating_count = []
new_pages_count = []
new_price = []
new_review_count = []
for id in list_of_ids:
    new_rating.append(all_books_new[id]["rating"])
    new_rating_count.append(all_books_new[id]["rating_count"])
    new_pages_count.append(all_books_new[id]["pages_count"])
    new_price.append(all_books_new[id]["price"])
    new_review_count.append(all_books_new[id]["review_count"])
new_table = {"rating": new_rating,
             "rating_count": new_rating_count,
             "pages_count": new_pages_count,
             "price": new_price,
             "review_count": new_review_count}
df = pd.DataFrame(new_table, columns=['rating', 'rating_count', 'pages_count', 'price', 'review_count'])
print(df.corr())
print("Комментарий:\nНаибольшая корреляция наблюдается между количеством отзывов и количеством оценок\nНаименьшая корреляция наблюдается между ценой и количеством оценок")
print("+" * 100)
print("11. Постройте диаграмму рассеяния (scatterplot) количества страниц и количества отзывов. Не забудьте подписать график и оси. (1) Прокомментируйте полученные результаты. (1)")
sns.scatterplot(data=new_table, x="pages_count", y="review_count")
plt.show()
print("Комментарий:\nКоличество оценок уменьшается по ходу увеличения количества страниц")
print("+" * 100)
print("12. Постройте линейный график: по оси Х год, по оси Y количество книг. (1) Прокомментируйте. (1)")

years_count_books = {}
for id in list_of_ids:
    year = all_books_new[id]["year"]
    if year in years_count_books:
        years_count_books[year] += 1
    else:
        years_count_books[year] = 1
years_count_books = dict(sorted(years_count_books.items()))
list_of_new_years = []
list_of_new_count_books = []
for el in years_count_books:
    list_of_new_years.append(el)
    list_of_new_count_books.append(years_count_books[el])
table_tmp = {"year": list_of_new_years,
             "count_of_books": list_of_new_count_books}
sns.lineplot(data=table_tmp, x="year", y="count_of_books")
plt.show()
print("Комментарий:\nРост книг по программированию начался в 2006 году. В 2016 году было снижение тренда. В 2021 году был резкий пик по количеству книг, связанных с программированием")
print("+" * 100)
print("13. Постройте еще любые два графика по вашему усмотрению. (2) Прокомментируйте полученные результаты. (1.5)")
sns.scatterplot(data=new_table, x="pages_count", y="price")
plt.show()
sns.scatterplot(data=new_table, x="rating", y="price")
plt.show()
print("Комментарий:\n  График 1: цена вне зависимости от количества страниц держится на уровне около 700-800 рублей. Книги с высокой ценой встречаются только среди книг с большим количеством страниц\n"
      "  График 2: книги с высокой ценой не отличаются высоким рейтингом, что подтверждает то, что дешевая книга != плохая книга")
print("+" * 100)
print("14. Постройте таблицу с авторами книг с именем автора, количество книг в датасете, средней оценкой книг, средним количеством отзывов. (2).")
def get_info_about_books(all_books, need_books):
    count_books = len(need_books)
    ratings = []
    num_reviews = []
    for id in need_books:
        book_info = all_books[id]
        ratings.append(book_info["rating"])
        num_reviews.append(book_info["review_count"])
    return {"count_books": count_books,
            "avg_rating": round(sum(ratings)/len(ratings), 1),
            "avg_count_reviews": round(sum(num_reviews)/len(num_reviews), 1)}
authors_and_books = {}
for id in all_books_new:
    author = all_books_new[id]["author"]
    if author == "":
        continue
    if author in authors_and_books:
        authors_and_books[author].append(id)
    else:
        authors_and_books[author] = [id]
data = []
for el in authors_and_books:
    info_main = get_info_about_books(all_books_new, authors_and_books[el])
    data.append([el, info_main["count_books"], info_main["avg_rating"], info_main["avg_count_reviews"]])
df = pd.DataFrame(data, columns=['Имя', 'Количество книг', 'Средний рейтинг', 'Среднее количество отзывов'])
pd.set_option('display.max_rows', 30)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
print(df)
print("+" * 100)
print("15. Что еще интересного можно увидеть в этом датасете? Просмотрите на данные и ответьте на какие-нибудь вопросы, на которые не ответили в предыдущим пункте. Мы никак не ограничиваем вашу фантазию! (3).")