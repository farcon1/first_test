# Задача №6 для распределительного теста
## Парсинг
Файл **G_parsing.py** отвечает за парсинг страниц(1-40 - настраиваемое), парсинг всех страниц книг и отзывов на них, а также последующее сохранение файлов, чтобы в дальнейшем отказаться от парсинга. В конце происходит валидация всех данных и удаляются все не полные строки 
## Выполнение заданий
Файл **G_progress.py** отвечает за выполнение всех заданий из списка:

#Запуск программы
Если у вас уже есть загруженные файлы в папке files, то парсинг делать заново не надо. Таким образом, необходимо запустить только файл **G_progress.py**

##Вывод работы программы **G_progress.py**
###1. Выведите первые 5 строк датасета. (0.25). Сколько в нём строк и столбцов (0.25)?
id 1
name Начинаем программировать на Python
author Тони Гэддис
link https://www.litres.ru/book/toni-geddis-32491161/nachinaem-programmirovat-na-python-68998912/
rating 5.0
rating_count 16
pages_count 875
price 599
age 12+
year 2021
review_count 6
text_reviews ['Шикарная книга! Начал изучать Python самостоятельно, пробежался по куче книг и ничего не было понятно, а эта книга изменила всё! Всем рекомендую', 'Главное берите в электроне. Печатное издание полное &quot;г&quot;. Пока дошёл до конца, вся книга развалилась и искать что-то очень проблематично. Выбросил печатное и сейчас в электроне перекупил. Книга супер,  даёт начальное представление, но после 800 страниц становится немного грустно, потому что понимаешь, что выучить синтаксис и умение программировать, это две разные вещи. После этой книги есть реальный шанс начать понимать более серьёзную литературу.', 'Лучшая книга для начинающих программировать на Python, и от издательства ZIP архив (~700Mb) (Состав архива: source-codes – исходные коды, VideoNotes – обучающие видео на английском языке).', 'Начинаем программировать на Python от Тони Гэддиса - это неплохая книга для изучения базового синтаксиса и концепций, которая раскрывает темы по их сложности. Сам по себе учебник не даст вам глубинного понимания о том, как работает язык. В плюсы хочу отнести то, что после каждой главы идут интересные задачи и вопросы, некоторые из которых заставят начинающего подумать.', 'Я по ней учусь, нашёл совет учиться по ней в интернете. Как для новичка-очень простая, подробная, много примеров и задач. Рекомендую всем начинать именно с неё!', 'PEkHn"Если вы начинающий программист, и не имели раньше дела с программированием вовсе, то эта книга поможет разобраться более чем поверхностноРазбираются основы языка программирования и проектирования ПО (совсем мельком)Но что важно - здесь есть задачки, которые я бы рекомендовал решать все, на все тесты отвечать и проверять себя. Без этого толку читать нет любую профессиональную книгу.Отзыв с Лайвлиба.01ОтветитьПожаловаться на отзывПоделиться отзывомОставьте отзыв']
__________________________________________________
id 2
name Изучаем DDD – предметно-ориентированное проектирование
author Влад Хононов
link https://www.litres.ru/book/vlad-hononov/izuchaem-ddd-predmetno-orientirovannoe-proektirovanie-70920895/
rating 0.0
rating_count 0
pages_count 319
price 549
age 0+
year 2022
review_count 1
text_reviews ['Эта книга из той лиги, в которой я пока не состою - лиги крутых разрабов и архитекторов. И я имею ввиду не какую-то субъективную оценку. Разработчикам с малым опытом нужно читать конкретику, изучать дальше фишки языка, алгоритмы. Какой смысл от джуна, который знает, что такое предметная область, но не может послать запрос на сервер? Как мне кажется, пользы от него мало. Прочитал я где-то 30% и решил отложить ее до лучших времен.']
__________________________________________________
id 3
name System Design. Подготовка к сложному интервью
author Алекс Сюй
link https://www.litres.ru/book/aleks-suy/system-design-podgotovka-k-slozhnomu-intervu-67193183/
rating 3.6
rating_count 17
pages_count 304
price 699
age 16+
year 2020
review_count 9
text_reviews ['Добротная книга по разработке архитектуры приложений. Замечательно подойдет программистам уровня Junior+ и выше. Умение проектировать дизайн приложения играет большую роль при разработке ПО, поэтому рекомендую ознакомиться с одержанием)', 'Отличная книга по дизайну систем – помимо примеров как решать задачи на интервью в ней присутствуют подробные описания какие решения могут быть приняты в различных ситуациях. Если кандидат её прочитает и поймёт почему определённые решения хороши в определённых ситуациях, то он сможет проити систем дизайн интервью со смной.', 'Отличная книга для тех, кто заинтересован в backend разработке высоконагруженных систем. Автор начитает с самых азов (объясняет для чего нужен CDN, кеш, реплицирование и что такое хеширование) и заканчивает сложными многокомпонентыми системами вроде ленты FB или облачного хранилища файлов (например google drive). Много схем и пояснений, а так же ссылок на дополнительный материал.', 'Для всех, кто интересуется проектированием систем (архитектурой) эта книга станет отличным стартом. Да, темы разобраны не очень подробно, но таков формат книги - азы для ответов на интервью по этой теме.', 'Полезная книга для всех, кто готовится проходить интервью по системному проектированию. В этой книге затронуты практически все аспекты, о которых спрашивают во время прохождения реального интервью. Однако надо понимать, что все темы затронуты очень поверхностно просто для того, чтобы у вас, во-первых, сложилось понимание, как выглядит алгоритм прохождения подобного вида интервью, какие в нём есть основные этапы, и в какой последовательности следует решать поставленную задачу. А во-вторых, у вас должно появиться понимание, какие в принципе существуют технологии для решения тех или иных проблем при проектировании высоконагруженных систем. Далее при желании вы всегда сможете углубить свои знания в этих технологиях. В книге кстати приводится внушительный список дополнительных источников информации по каждому разделу.', 'PEkHn"Для общего развития нормальноПочерпнуть какие-то концепции и идеи реализации популярных сервисов вполне можно, книга написана простым языком и понятна, думаю, будет всем.Отзыв с Лайвлиба.00ОтветитьПожаловаться на отзывПоделиться отзывомsafindanil2 августа', 'Книга проходится только по верхам, остальное предполагается, что человек либо сам знает, либо предлагается просто принять как данность. к примеру, в главе, посвященной сокращению ссылок, рассматривается только 2 варианта сокращения, а всё остальное просто описывется без какого либо объяснения, почему именно так. Тот же способ сокращения в итоге выбирается без каких-либо рассуждений о причине выбора в рамках рассматриваемой задачи. И во всем остальном книга такая же. Так же в книге спешано в кашу как всякие сложные темы, так и объяснение самых базовых понятий, которые по идее должен знать любой, даже самый начинающий разработчик', 'Разобраны все самые типовые задачи на проектирование. отдельное спасибо автору за большое количество ссылок для дополнительного изучения', 'Книга со своей задачей подготовить читателя к интервью справляется, но делает это отвратительно. Не читал оригинал, может дело в переводе, но повествование ужасное: постоянные повторы, разжевывание того, чего не надо, ну и вишенка на торте… ссылки и термины из Википедии!']
__________________________________________________
id 4
name Высоконагруженные приложения. Программирование, масштабирование, поддержка (pdf+epub)
author Мартин Клеппман
link https://www.litres.ru/book/martin-kleppman-1733/vysokonagruzhennye-prilozheniya-programmirovanie-mass-39100996/
rating 4.0
rating_count 51
pages_count 640
price 799
age 16+
year 2017
review_count 12
text_reviews ['Не могу что-либо про перевод сказать, читал данную книгу в оригинале. Очень толково и по делу описаны базы данных и интерфейсы. С другой же стороны – половину книги можно вырезать без какой либо потери в качестве и содержании…', 'Altmann Nicolas, hello world', 'Книга претендует на звание «must read» для разработчика отказоустойчивых систем. Представляет собой в первую очередь и в большей мере учебник, нежели справочник. Книга в полной мере раскрывает принципы функционирования самых разных баз данных. Но это далеко не всё, в книге описаны подходы и общие принципы к решению проблем отказов узлов в распределенных системах, выходящие за границы области баз данных. В русскоязычных сообществах книга зовется «кабанчик» и стала классикой в области разработки и проектирования распределенных отказоустойчивых решений. Отмечу высокий порог вхождения для некоторых деталей книги, в том числе B-деревья, алгоритмы консенсуса, и другие математические моменты.', 'Отличная книга, раскрывающая внутреннее устройство баз данных. Даёт понимание, в каких сценариях использовать БД того или иного класса.', 'Книга «с кабанчиком» обязательна к прочтению — это наиболее полное руководство к построению распределённых систем с фокусом на обработку данных (коими является большинство современных web-приложений), основные проблемы, с которыми приходится сталкиваться при проектировании и варианты их решений.', 'Книга стала настольной. Считаю ее необходимой практически любому разработчику или системному аналитику. Описаны все основные аспекты и лучшие практики. Рекомендую', 'Книга хорошая, но будьте внимательны, доступен только PDF формат, который проблематично читать на мобильном устройстве.', 'Антон Чеботарев, книга в epub формате есть в &quot;дополнительных материалах (февраль 24 года)', 'Когда только начинал заниматься бэкендом, хотел найти избыточный материал по БД и работе с данными. Мне кажется, эта книга является таковой. К идеалу можно только стремится, но книга действительно очень дотошная. Все начинается с обзорного и простого материала, а заканчивается хардовыми проблемами распределенных систем.', 'Невероятно дотошная книга о хранении и обработке данных, начиная от различных форматов хранения данных и индексов и заканчивая возможными реализациями распределенных транзакций. И все это в разрезах надежности/масштабируемости/удобстве сопровождения. Отдельные разделы посвящены таким редкоосвещаемым темам, как согласованность часов (и вообще виды и дискретность таймеров в современных ОС) и согласованность узлов (линеаризуемость и её практическая достижимость).\nMust read всем, кто хочет ориентироваться в современном (спасибо издательству за быстрый перевод) мире БД.', 'PEkHn"Читайте, если хотите, а если не хотите — не читайте :)Не для новчиковКнига тяжелая, местами душная, но полезная. Останутся ли у меня в голове все эти детали реализации LST или консенсусных алгоритмов? Нет, конечно. Редкому инженеру понадобятся эти знания, но соседствующие с ними рассказы про проблемы распределенных систем, потоковую и пакетную обработки данных и другое весьма хороши.На обратной стороне книги написано, что потребуются базовые знания работы БД и SQL. «Ага, поверил, ну и бредятина»Кабанчик возведён в некий культ, как я могу судить. Не дайте этому затмить ваш разум!Где-то видел сравнение данной книги с учебником. Не могу не согласитьсяХорошая книга. Но не идеал4/5Отзыв с Лайвлиба.00ОтветитьПожаловаться на отзывПоделиться отзывомАлександр Бизяев19\n        декабря 2021', 'Обязательно к прочтению, рассмотрен широкий круг вопросов, обозначены вопросы для дальнейшего изучения. ']
__________________________________________________
id 6
name Архитектура компьютера
author Эндрю Таненбаум
link https://www.litres.ru/book/endru-tanenbaum/arhitektura-komputera-66738078/
rating 4.2
rating_count 6
pages_count 816
price 699
age 16+
year 2015
review_count 3
text_reviews ['Большая, сложная, информативная книга. Рассказаны основы основ современного компьютера. не ищите в ней поверхностных знаний о актуальных вопросах, она освещает общую обстановку самого &quot;дна&quot; вычислительных машин - как работает то, о существовании чего обычный пользователь даже не догадывается. ', 'Если сосредоточенно погружаться, интересно. Иногда надо себя заставлять. Но все же это серьезная литература. автор (г-н Таненбаум) весьма опытный преподаватель и методист', 'Ну что же, прочитав половину этой книги могу с уверенностью рекомендовать каждому it специалисту. Несомненно буду перечитывать её езё раз.']
__________________________________________________
В датасете 687 строк и 12 столбцов
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
###2. Есть ли в датасете пропуски? (0.5)
Да, пропуски были в изначальном датасете. Например, цена можно быть null, год написания книги может быть неизвестен и были неизвестны количество страниц в некоторых книгах. Такие строки я удалил
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
###3. Проверьте типы данных. Если это необходимо, приведите к типам int и float те столбцы, с которыми понадобится работать как с числами. (1).
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
###4. Выведите описательные статистики переменных. Ответьте на следующие вопросы: 
Какая медианная цена книги в вашем датасете? (1) 
299.0
Какое возрастное ограничение встречается чаще всего? (1) 
0+
Какое среднее число отзывов в книге? (1) 
1.6273653566229986
Сколько книг имеют оценку ниже 4.25? (1) 
479 из 687 книг
В каком году было написано больше всего книг из датасета? (1)
2021 - 78 книг
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
###5. Если вы работаете с готовым датасетом, то попробуйте "достать" из столбца pages количество страниц. Если у вас не получилось, то далее при определении числа страниц пользуйтесь стольцов pages_count. Если вы парсили датасет сами, то вы получаете балл за этот пункт автоматически (1.5)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
###6. Создайте новое поле is_popular. Значение равно 1, если рейтинг книги не менее 4.6 и при этом у нее не менее 5 отзывов, и 0 в остальных случаях. (1)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
###7. Как отличается среднее число страниц среди популярных и непопулярных книг? (2)
Количество книг:
  - популярные: 179 книг 
  - не популярные: 508 книг
Среднее количество страниц:
  - популярные: 351.8826815642458 страниц 
  - не популярные: 233.2263779527559 страниц
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
###8. Выведите топ-10 книг по числу отзывов. (2)
1С:Программирование для начинающих. Детям и родителям, менеджерам и руководителям. Разработка в системе «1С:Предприятие 8.3», 2-е стереотипное издание (+ epub) - 14 отзывов
Swift. Основы разработки приложений под iOS, iPadOS и macOS (pdf + epub) - 13 отзывов
Высоконагруженные приложения. Программирование, масштабирование, поддержка (pdf+epub) - 12 отзывов
Теоретический минимум по Computer Science. Все что нужно программисту и разработчику - 11 отзывов
Программирование на C++ в примерах и задачах - 11 отзывов
HTML и CSS. Разработка и дизайн веб-сайтов - 11 отзывов
1С:Предприятие 8.3. Практическое пособие разработчика. Примеры и типовые приемы. Издание 3-е - 10 отзывов
Программирование на Python в примерах и задачах - 10 отзывов
Выразительный JavaScript. Современное веб-программирование (pdf+epub) - 10 отзывов
Создание микросервисов (pdf+epub) - 10 отзывов
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
###9. Найдите среднюю длину отзыва (в символах). (2)
Средняя длина отзыва - 248.77101967799643 символов
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
###10. Постройте таблицу корреляций числовых переменных. (1) Прокомментируйте результаты. (1)
Среди аналилизируемых значений выберем следующие:
  - рейтинг
  - количество оценок
  - количество страниц
  - цена
  - количество отзывов
                rating  rating_count  pages_count     price  review_count
rating        1.000000      0.324846     0.533671  0.452529      0.474459
rating_count  0.324846      1.000000     0.310405  0.253921      0.752373
pages_count   0.533671      0.310405     1.000000  0.664039      0.454236
price         0.452529      0.253921     0.664039  1.000000      0.371654
review_count  0.474459      0.752373     0.454236  0.371654      1.000000
Комментарий:
Наибольшая корреляция наблюдается между количеством отзывов и количеством оценок
Наименьшая корреляция наблюдается между ценой и количеством оценок
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
###11. Постройте диаграмму рассеяния (scatterplot) количества страниц и количества отзывов. Не забудьте подписать график и оси. (1) Прокомментируйте полученные результаты. (1)
Комментарий:
Количество оценок уменьшается по ходу увеличения количества страниц
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
###12. Постройте линейный график: по оси Х год, по оси Y количество книг. (1) Прокомментируйте. (1)
Комментарий:
Рост книг по программированию начался в 2006 году. В 2016 году было снижение тренда. В 2021 году был резкий пик по количеству книг, связанных с программированием
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
###13. Постройте еще любые два графика по вашему усмотрению. (2) Прокомментируйте полученные результаты. (1.5)
Комментарий:
  График 1: цена вне зависимости от количества страниц держится на уровне около 700-800 рублей. Книги с высокой ценой встречаются только среди книг с большим количеством страниц
  График 2: книги с высокой ценой не отличаются высоким рейтингом, что подтверждает то, что дешевая книга != плохая книга
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
###14. Постройте таблицу с авторами книг с именем автора, количество книг в датасете, средней оценкой книг, средним количеством отзывов. (2).
                 Имя  Количество книг  Средний рейтинг  \
0        Тони Гэддис                1              5.0   
1       Влад Хононов                1              0.0   
2          Алекс Сюй                2              4.3   
3    Мартин Клеппман                1              4.0   
4    Эндрю Таненбаум                1              4.2   
..               ...              ...              ...   
516  А. В. Кучуганов                1              0.0   
517  А. М. Пеленицын                1              0.0   
518     А. А. Салтан                1              0.0   
519   Ю. В. Трифонов                1              3.0   
520  М. В. Зенькович                1              0.0   

     Среднее количество отзывов  
0                           6.0  
1                           1.0  
2                           4.5  
3                          12.0  
4                           3.0  
..                          ...  
516                         0.0  
517                         0.0  
518                         0.0  
519                         0.0  
520                         0.0  

[521 rows x 4 columns]
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
###15. Что еще интересного можно увидеть в этом датасете? Просмотрите на данные и ответьте на какие-нибудь вопросы, на которые не ответили в предыдущим пункте. Мы никак не ограничиваем вашу фантазию! (3).