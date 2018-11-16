# Django 習作

練習Django用的小專案。

## 練習內容概述

1. / : 抓到db中Person的資料，並列出來。

2. /polls/archive/ : 抓到Article的資料，並列出，有設定動態網址，可以點進去只看該年份的資料。

3. /hello : 打招呼，顯示時間，不用db

4. /admin : 可以顯示出登入登出畫面

## 建置方法

- ```docker-compose up --build```
- ```docker-compose exec web python manage.py migrate```
- ```docker-compose exec web python manage.py loaddata data/person_data.json```


## 建置日記

未整理，暫不公開：放在Paper的「人臉辨識研究文件」。