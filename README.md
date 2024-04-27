## Локальный запуск

1. Склонировать репозиторий  
`git clone https://github.com/eco-community-kpfu/eco-community.git`
2. Поднять базу данных для приложения  
`docker-compose up -d`
3. Создать виртуальное окружение  

4. Установить библиотеки  
`pip install -r requirements.txt`
5. Выполнить миграции в БД  
`python manage.py migrate`
6. Запустить веб-сервер  
`python manage.py runserver`
