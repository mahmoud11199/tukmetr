# Tukmetr

هيكل مشروع أولي (Starter Scaffold) بلغة Python يوفّر:

- حزمة أساسية داخل `src/tukmetr`
- دوال بسيطة للبدء السريع
- اختبارات ابتدائية داخل `tests`

## المتطلبات

- Python 3.10+

## التشغيل السريع

```bash
python -m unittest discover -s tests -v
```

## هيكل المجلدات

```text
.
├── README.md
├── src/
│   └── tukmetr/
│       ├── __init__.py
│       └── core.py
└── tests/
    └── test_core.py
```

## الخطوة القادمة المقترحة

- إضافة واجهة CLI أو API بسيطة.
- إضافة أداة إدارة بيئة مثل `venv` + `requirements.txt`.
- إضافة CI لتشغيل الاختبارات تلقائيًا.
