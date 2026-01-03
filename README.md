# Todo List REST API

Простой и функциональный RESTful API для управления списком задач (To-Do List), реализованный на Django и Django REST Framework.

## 📌 Функциональность
- Полный CRUD (Create, Read, Update, Delete) для задач.
- Поддерживаемые статусы: `todo`, `in_progress`, `done`.
- Стандартные HTTP-методы и коды ответа.
- Данные в формате JSON.

## 🚀 Быстрый старт

### Предварительные требования
- Python 3.10+
- pip

### Установка и запуск
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Nahlebnick/CollocOS.git
   cd todo-list-api

2. Клонируйте репозиторий:
   ```bash
   python -m venv venv
   source venv/bin/activate  # На Windows: venv\Scripts\activate
   
3. Установите зависимости
   ```bash
   pip install -r requirements.txt
   
4. Примените миграции
   ```bash
   python manage.py migrate
   
5. Запустите сервер
   ```bash
   python manage.py runserver
   
6. API будет доступно по адресу: http://127.0.0.1:8000/api/v1/