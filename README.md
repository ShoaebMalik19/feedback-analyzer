<div align="center">

# 🧠 Feedback Analyzer

### Paste any feedback and get instant AI sentiment analysis with Django and Hugging Face Transformers.

<p>
  <img src="https://img.shields.io/badge/Python_3.10-1E293B?style=for-the-badge&logo=python&logoColor=FFD43B" alt="Python" />
  <img src="https://img.shields.io/badge/Django_5.2-0C2E1F?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
  <img src="https://img.shields.io/badge/Hugging_Face-1F1F1F?style=for-the-badge&logo=huggingface&logoColor=FFD21E" alt="Hugging Face" />
  <img src="https://img.shields.io/badge/PyTorch-1C1C1C?style=for-the-badge&logo=pytorch&logoColor=EE4C2C" alt="PyTorch" />
  <img src="https://img.shields.io/badge/Tailwind_CSS-0F172A?style=for-the-badge&logo=tailwindcss&logoColor=38BDF8" alt="Tailwind CSS" />
  <img src="https://img.shields.io/badge/SQLite-1A1A2E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
</p>

</div>

---

## ✨ Overview

**Feedback Analyzer** is a small Django web app that classifies user feedback as **POSITIVE** or **NEGATIVE** with a pre-trained Hugging Face `sentiment-analysis` pipeline. Each submission is saved to the database with its label and confidence score, so you can review it later in the Django admin.

## 🚀 Features

- **One-click sentiment analysis**: submit text and get the label with a confidence percentage (e.g. `Sentiment: POSITIVE (99.85%)`).
- **Model loaded once**: the Transformers pipeline loads at startup and is reused for every request.
- **Stored history**: every result is saved in a `Feedback` model (text, sentiment, confidence).
- **Admin panel**: browse past feedback at `/admin/`.
- **Deploy-ready**: Gunicorn `Procfile`, WhiteNoise static files and a pinned `runtime.txt` (Python 3.10.10).

## 🧱 Tech Stack

- **Backend:** Django 5.2, Gunicorn, WhiteNoise
- **AI/ML:** Hugging Face Transformers (`pipeline("sentiment-analysis")`), PyTorch
- **Database:** SQLite
- **Frontend:** Django templates with Tailwind CSS (CDN)

## 🗂️ Project Structure

```
feedback-analyzer/
├── analyzer/                 # app: model, view, template
│   ├── models.py             # Feedback(text, sentiment, confidence)
│   ├── views.py              # loads the pipeline, handles the form
│   └── templates/home.html
├── feedback_analyzer/        # project settings, urls, wsgi
├── manage.py
├── requirements.txt
├── Procfile                  # web: gunicorn feedback_analyzer.wsgi
└── runtime.txt               # python-3.10.10
```

## ⚡ Getting Started

```bash
git clone https://github.com/ShoaebMalik19/feedback-analyzer.git
cd feedback-analyzer

python -m venv venv
# Windows: venv\Scripts\activate   |   macOS / Linux: source venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser   # optional, for /admin
python manage.py runserver
```

Open `http://127.0.0.1:8000`. The first run downloads the default sentiment model from Hugging Face.

> `DEBUG` is set to `False` in `settings.py`. For local development, set it to `True` or run `python manage.py collectstatic` so static files are served.

## 🛣️ Roadmap

- Load `SECRET_KEY` and `DEBUG` from environment variables
- Add a history and analytics view of collected feedback

## 👤 Author

**Mohammed Shoaeb Malik** · AI & full-stack developer, Bengaluru
GitHub: [@ShoaebMalik19](https://github.com/ShoaebMalik19)
