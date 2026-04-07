# Sentiment Analysis Project

Проект содержит два способа работы с анализом тональности текста:
- API на FastAPI
- Web-интерфейс на Streamlit

## Структура проекта

- `main.py` — FastAPI приложение
- `services.py` — общая логика анализа текста
- `streamlit_app.py` — Web-интерфейс на Streamlit
- `logging_config.py` — настройка логирования

## Запуск проекта

Установить зависимости:

```bash
pip install fastapi uvicorn streamlit transformers torch
```

Запуск FastAPI:

```bash
uvicorn main:app --reload
```

Запуск Streamlit:

```bash
streamlit run streamlit_app.py
```

## Доступные API endpoints

- `GET /` - проверка запуска сервиса
- `GET /health` - healthcheck
- `POST /predict/` - анализ текста

Пример тела запроса:

```json
{
  "text": "I like this project"
}
```

## Реализованные улучшения

- бизнес-логика анализа вынесена в `services.py`;
- добавлены типизированные модели ответа FastAPI;
- валидация входных данных через Pydantic: отклонение пустых и whitespace-строк, ограничение длины 512 символов;
- корректная обработка ошибок: HTTP 400 вместо 500 при невалидном вводе;
- структурированное логирование с настройкой уровня через `LOG_LEVEL`;
- Streamlit UI: цветовая индикация результата, отображение confidence, история запросов.

## Настройка логирования

Уровень логирования задаётся через переменную окружения:

```bash
LOG_LEVEL=DEBUG uvicorn main:app --reload
```

По умолчанию используется `INFO`.

## Использованная схема GitFlow

- `main` - стабильная ветка проекта
- `feature/api-refactor` - доработка и рефакторинг API
- `feature/streamlit-ui` - разработка Streamlit-интерфейса
- `release/1` - подготовленная ветка для релиза проекта
- `bugfix/*` - ветки для исправления ошибок при необходимости

## Распределение работы

- Асадов Руслан (`RuslanAsadov`) — рефакторинг API, валидация входных данных, обработка ошибок.
- Курносов Константин (`SteepMans`) — структурированное логирование, настройка уровня через env.
- Кайгородова Оксана (`queenhellbabe`) — улучшение Streamlit UI, обновление документации.
