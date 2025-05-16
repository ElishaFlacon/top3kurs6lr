# Swag Labs E2E Test

Автоматизированный E2E тест для проверки процесса покупки на сайте [Swag Labs](https://www.saucedemo.com/) с использованием Python и Selenium.

## Предварительные требования

- Python 3.11 или выше
- Google Chrome (последняя версия)

## Запуск

Клонирем репозиторий

```bash
git clone https://github.com/yourusername/swag-labs-test.git
cd swag-labs-test
```

Создаем .env

```bash
cp .env.example .env
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
python test_swag_labs.py
```

Запускаем скрипт для теста github
```bash
python test_swag_labs.py
```
