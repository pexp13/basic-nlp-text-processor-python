# 📝 Анализатор текста

Настольное приложение на Python / Tkinter для анализа частоты слов и определения **тональности** русскоязычного текста.

## Возможности

- **Частотный анализ** — подсчёт количества вхождений каждого слова, сортировка по убыванию.
- **Сентимент-анализ** — определение тональности текста (позитивная / негативная / нейтральная) с процентом уверенности. Используется модель [`blanchefort/rubert-base-cased-sentiment`](https://huggingface.co/blanchefort/rubert-base-cased-sentiment) на базе ruBERT.

## Требования

- Python 3.9+
- Зависимости из `requirements.txt`

## Установка

```bash
git clone https://github.com/<your-username>/text-analyzer.git
cd text-analyzer

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

## Запуск

```bash
python 3.py
```

При первом запуске функции тональности (~1–2 мин.) будет автоматически загружена модель (~700 МБ). После загрузки она кешируется локально.

## Структура проекта

```
text-analyzer/
├── 3.py              # Основной скрипт
├── requirements.txt  # Зависимости
├── .gitignore
└── README.md
```

## Технологии

| Компонент | Описание |
|---|---|
| `tkinter` | GUI (входит в стандартную библиотеку Python) |
| `transformers` | Загрузка и инференс NLP-моделей (Hugging Face) |
| `torch` | Бэкенд для модели |

## Лицензия

MIT
