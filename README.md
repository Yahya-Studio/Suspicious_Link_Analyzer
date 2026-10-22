# 🔍 محلل الروابط المشبوهة | Suspicious Link Analyzer

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109%2B-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![VirusTotal](https://img.shields.io/badge/API-VirusTotal%20v3-393B44?style=for-the-badge&logo=virustotal&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Server-Uvicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**أداة ويب ذكية وسريعة لفحص وتحليل الروابط المشبوهة واكتشاف التهديدات والبرمجيات الخبيثة بالاعتماد على محركات VirusTotal الرسمية.**

*A lightweight, asynchronous web-based URL safety scanner built with FastAPI and VirusTotal API v3. Detect phishing, malware, and suspicious domains in real-time.*

[المميزات](#-المميزات-الرئيسية--key-features) •
[التقنيات المستخدمة](#-التقنيات-المستخدمة--tech-stack) •
[طريقة التثبيت والتشغيل](#-طريقة-التثبيت-والتشغيل--getting-started) •
[الحصول على مفتاح VirusTotal](#-الحصول-على-مفتاح-virustotal-api--how-to-get-api-key) •
[هيكلية المشروع](#-هيكلية-المشروع--project-structure) •
[الأمان والخصوصية](#-الأمان-والخصوصية--security--privacy)

</div>

---

## 🌟 المميزات الرئيسية | Key Features

- 🛡️ **فحص شامل بمحركات متعددة (Multi-Engine Scanning):** تحليل الروابط ضد أكثر من 70 محرك أمني ومضاد فيروسات عالمي عبر **VirusTotal API v3**.
- ⚡ **أداء فائق السرعة وغير متزامن (Asynchronous):** مبني بالكامل على إطار عمل **FastAPI** ومكتبة **httpx** لمعالجة الطلبات بسرعة وكفاءة.
- 🎨 **واجهة مستخدم تفاعلية (Arabic RTL UI):** تصميم أنيق وجذاب يدعم اللغة العربية بالكامل، مع تأثيرات بصرية وبطاقات ملونة تعكس مستوى أمان الرابط:
  * 🔴 **خبيث (Malicious):** مواقع ضارة تم تأكيد خطرها.
  * 🟠 **مشبوه (Suspicious):** نطاقات غير موثوقة أو تحت الملاحظة.
  * 🟢 **آمن (Harmless):** مواقع موثوقة ونظيفة.
  * ⚪ **غير مكتشف (Undetected):** لم ترصد المحركات أي نشاط مشبوه.
- 🔌 **واجهة برمجية جاهزة (REST API Endpoint):** نقطة نهاية `POST /scan` تتيح دمج أداة الفحص مع تطبيقات أو بوتات تليجرام/ديسكورد أخرى بسهولة.

---

## 🛠 التقنيات المستخدمة | Tech Stack

| المجال | التقنية | الوصف |
| :--- | :--- | :--- |
| **Backend Framework** | [FastAPI](https://fastapi.tiangolo.com/) | إطار عمل بايثون فائق السرعة لبناء الواجهات البرمجية |
| **ASGI Server** | [Uvicorn](https://www.uvicorn.org/) | خادم تشغيل سريع وخفيف لتطبيقات بايثون الحديثة |
| **HTTP Client** | [HTTPX](https://www.python-httpx.org/) | عميل HTTP متقدم وغير متزامن للاتصال بـ VirusTotal |
| **Security Service** | [VirusTotal API v3](https://docs.virustotal.com/reference/overview) | خدمة فحص الروابط والملفات العالمية |
| **Frontend** | HTML5, Modern CSS, Vanilla JS | واجهة مستخدم خفيفة وسريعة بدون أي إطارات عمل ثقيلة |

---

## 🚀 طريقة التثبيت والتشغيل | Getting Started

### 📋 المتطلبات المسبقة (Prerequisites)
* تثبيت **Python** (الإصدار `3.9` أو أحدث).
* تثبيت **Git**.
* مفتاح API مجاني من منصة [VirusTotal](https://www.virustotal.com/gui/join-us).

### 📥 خطوات التثبيت (Installation Steps)

1. **استنساخ المستودع (Clone the Repository):**
   ```bash
   git clone https://github.com/Yahya-Studio/Suspicious_Link_Analyzer.git
   cd Suspicious_Link_Analyzer
   ```

2. **إنشاء وتفعيل البيئة الافتراضية (Virtual Environment):**
   * على Linux / macOS:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   * على Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **تثبيت الحزم المطلوبة (Install Dependencies):**
   ```bash
   pip install -r requirements.txt
   ```

4. **إعداد متغيرات البيئة (Configure Environment):**
   * انسخ ملف النموذج `.env.example` إلى `.env`:
     ```bash
     cp .env.example .env
     ```
   * افتح ملف `.env` وضع مفتاحك الخاص:
     ```env
     VIRUSTOTAL_API_KEY=your_actual_virustotal_api_key_here
     ```

5. **تشغيل الخادم (Run Server):**
   ```bash
   python main.py
   ```
   أو باستخدام Uvicorn مباشرة:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

6. **افتح المتصفح:**
   انتقل إلى الرابط: [http://localhost:8000](http://localhost:8000)

---

## 🔑 الحصول على مفتاح VirusTotal API | How to Get API Key

توفر منصة VirusTotal وصولاً مجانياً للـ API (يصل إلى 500 طلب/يوم بمعدل 4 طلبات/دقيقة):

1. ادخل إلى صفحة التسجيل: [VirusTotal Join Us](https://www.virustotal.com/gui/join-us).
2. قم بإنشاء حساب وتأكيد بريدك الإلكتروني.
3. بعد تسجيل الدخول، اضغط على اسم المستخدم أعلى يمين الشاشة ثم اختر **API Key**.
4. انسخ المفتاح والصقه داخل ملف `.env`.

---

## 📡 استخدام الـ API | REST API Usage

يمكنك فحص أي رابط برمجياً عبر إرسال طلب `POST` إلى `/scan`:

```bash
curl -X POST "http://localhost:8000/scan" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "url=https://example.com"
```

**نموذج الاستجابة (JSON Response):**
```json
{
  "url": "https://example.com",
  "malicious": 0,
  "suspicious": 0,
  "harmless": 72,
  "undetected": 15,
  "total_engines": 87,
  "is_safe": true
}
```

---

## 📁 هيكلية المشروع | Project Structure

```text
Suspicious_Link_Analyzer/
├── main.py               # خادم FastAPI ومنطق الفحص عبر VirusTotal
├── requirements.txt      # قائمة حزم ومكتبات بايثون
├── templates/
│   └── index.html        # واجهة المستخدم التفاعلية (HTML/CSS/JS)
├── .env.example          # نموذج توضيحي لمتغيرات البيئة
├── .gitignore            # الملفات المستثناة من التتبع وحماية الأسرار
├── LICENSE               # رخصة MIT مفتوحة المصدر
└── README.md             # دليل التوثيق والتشغيل
```

---

## 🔐 الأمان والخصوصية | Security & Privacy

* **فصل بيانات الاعتماد:** لا يحتوي الكود على أي مفاتيح صلبة. تتم قراءة مفتاح الـ API فقط من متغيرات البيئة عبر `dotenv`.
* **الحماية من تسريب الأسرار:** ملف `.gitignore` محصّن لمنع تتبع ورفع ملفات `.env` أو سجلات التشغيل (`server.log`) وملفات الكاش (`__pycache__`).

---

## 🤝 المساهمة | Contributing

نرحب بمساهمات المطورين لتحسين الأداة أو إضافة مميزات جديدة (مثل فحص ملفات أو عناوين IP):
1. قم بعمل **Fork** للمستودع.
2. أنشئ فرعاً لميزتك (`git checkout -b feature/NewFeature`).
3. سجّل التعديلات (`git commit -m 'Add NewFeature'`).
4. ارفع الفرع (`git push origin feature/NewFeature`).
5. افتح **Pull Request**.

---

## 📄 الترخيص | License

هذا المشروع متاح تحت رخصة **MIT**. راجع ملف `LICENSE` للمزيد من التفاصيل.

---

<div align="center">

صُنع بـ ❤️ بواسطة **[Yahya-Studio](https://github.com/Yahya-Studio)**

</div>
