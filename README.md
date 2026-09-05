# Панелька — сайт для чтения комиксов

Учебное Django-приложение по варианту «Веб-сайт для чтения комиксов с настройками внешнего вида».

## Возможности

- библиотека из трёх выпусков комиксов;
- страница чтения с панелями, текстом и SVG-иллюстрациями;
- форма настроек внешнего вида;
- темы «Бумага», «Ночь» и «Неон»;
- три размера текста;
- русский и английский язык интерфейса;
- сохранение темы, размера текста, языка и последнего выпуска в cookies;
- данные каталога хранятся в Python-списках и словарях, без моделей и базы данных;
- адаптивная внешняя CSS-стилизация;
- автоматические тесты основных маршрутов и cookies.

## Установка локально

Понадобятся Python 3.10+ и Git.

```bash
git clone <ссылка-на-репозиторий>
cd django-comics

python -m venv .venv
```

Активация окружения:

```bash
# Linux / macOS
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Установка зависимостей и запуск:

```bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Откройте в браузере: http://127.0.0.1:8000/

## Тестирование

```bash
python manage.py test
```

## Структура

```text
comic_reader/       настройки и маршруты проекта
comics/             приложение, формы, представления и данные
templates/          HTML-шаблоны
static/css/         внешний файл стилей
static/images/      SVG-иллюстрации комиксов
```

## Git

Пример последовательности коммитов:

```bash
git init
git add .
git commit -m "Создан Django-проект и базовая структура"
git add .
git commit -m "Добавлен каталог комиксов и чтение выпусков"
git add .
git commit -m "Добавлены cookies-настройки, стили и тесты"
```

Для публикации на GitHub создайте пустой репозиторий и выполните:

```bash
git branch -M main
git remote add origin https://github.com/<username>/django-comics.git
git push -u origin main
```