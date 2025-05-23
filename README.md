# TPO auto tests

## Предварительные требования

- Python 3.11 или выше
- Google Chrome (последняя версия)

## Запуск

Клонирем репозиторий

```bash
git clone https://github.com/ElishaFlacon/top3kurs6lr.git .
```

Создаем .env

```bash
cp .env-example .env
```

Создаем виртуальное окружение

```bash
# Для Windows
python -m venv venv
venv\Scripts\activate

# Для macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

Устанавливаем зависимости

```bash
pip install -r requirements.txt
```

Запускаем скрипт для теста swaglabs
```bash
pytest -v test_swag_labs.py
```

Запускаем скрипт для теста github
```bash
pytest -v test_github_repos.py
```

Запускаем скрипт для теста lb4
```bash
pytest -v other/lb4.py
```

Запускаем скрипт для теста lb5
```bash
pytest -v other/lb5.py
```