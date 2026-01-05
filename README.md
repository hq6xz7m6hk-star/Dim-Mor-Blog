# Dim-Mor-Blog 

Установка
1. Установите Python 3
Убедитесь, что Python 3 установлен:

python --version
Если команда не работает, попробуйте:

python3 --version
2. Создайте папку проекта
mkdir mysite
cd mysite
3. Создайте виртуальное окружение
python -m venv venv
Активируйте окружение:

Windows:
venv\Scripts\activate
macOS / Linux:
source venv/bin/activate
4. Установите Django
pip install django

Создание и запуск проекта
1. Создайте Django‑проект
django-admin startproject config .
2. Примените миграции
python manage.py migrate
3. Запустите сервер разработки
python manage.py runserver
После запуска откройте:

http://127.0.0.1:8000/
