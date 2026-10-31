<p align="center">
  <picture>
    <img src="assets/hero.svg" alt="TibaTech · Vixona Technologies" width="100%">
  </picture>
</p>

# TibaTech — المحفظة التقنية | Tech Portfolio

> بنينا أدوات **نستخدمها نحن أولاً** — ثم فتحناها للعالم. كل مشروع هنا مفتوح المصدر، عربي في صميمه، ومحكوم ببوابات جودة آلية.

<p align="center">
  <a href="https://github.com/orgs/tibatechapp-ship-it/repositories"><img src="https://img.shields.io/badge/%D8%A7%D9%84%D9%85%D8%B3%D8%AA%D9%88%D8%AF%D8%B9%D8%A7%D8%AA-%D8%A7%D9%84%D9%83%D9%84-0A66C2?logo=github" alt="All repos"></a>
  <img src="https://img.shields.io/badge/%D8%A7%D9%84%D8%AA%D8%B1%D8%AE%D9%8A%D8%B5-MIT-yellow" alt="MIT">
  <img src="https://img.shields.io/badge/CI-gated%20on%20main-success?logo=githubactions&logoColor=white" alt="CI gated">
  <img src="https://img.shields.io/badge/%D8%A7%D9%84%D8%B1%D8%A6%D9%8A%D8%A9-%D8%B9%D8%B1%D8%A8%D9%8A%20RTL-2EA043" alt="Arabic RTL first">
</p>

---

## 🚀 المشاريع النشطة | Active Projects

| المشروع | ما هو | المجال | الحالة |
|---|---|---|---|
| **[Nexus Core](https://github.com/tibatechapp-ship-it/nexus-core)** | نظام وكلاء AI موحّد: ذاكرة + تعلّم + أمن + 20 وكيل | 🧠 AI Framework | `v1.9.3` |
| **[Rasan — رسن](https://github.com/tibatechapp-ship-it/Rasan)** | دردشة E2EE بلا رقم هاتف — ~7KB gzipped | 💬 Communication | `PWA` |
| **[LifeLink](https://github.com/tibatechapp-ship-it/lifelink-app)** | شبكة إنقاذ وتبرع بالدم — خصوصية أولاً | 🩸 Health | `v1.0.0` |
| **[Raqib — راقب](https://github.com/tibatechapp-ship-it/raqib)** | لوحة تحليلات فورية بـRunbooks ذكية (لا تنفّذ أوامر) | 📊 Analytics | `v0.4.3` |
| **[Pharma SDL](https://github.com/tibatechapp-ship-it/pharma-sdl)** | منصة عربية لتعليم واكتشاف الأدوية بالذكاء الاصطناعي | 🧬 Biotech Edu | `sprint 8` |
| **[NexHub](https://github.com/tibatechapp-ship-it/nexhub)** | منصة Git محلية عربية — بلا حساب، بلا سحابة | 🛠️ Developer Tool | `v0.3.0` |
| **[Chess CLI](https://github.com/tibatechapp-ship-it/chess-cli)** | شطرنج الطرفية ببايثون نقي + واجهة ويب FastAPI — وُلد من Nexus Studio | ♟️ Showcase | `0.1.0` |

### 🎯 التركيز الحالي — النواة الخمسة | Core Five

> مراجعة محفظة 2026-10-31 خلصت إلى: **القيمة في التركيز**. هذه الخمسة تحصل على الجهد الهندسي الكامل؛ ما عداهم إما داعم أو مؤرشف. **الدليل الكامل خلف كل رقم**: [بطاقة الأداء 📊](docs/scorecard.md) · [خارطة المنتَجة 🗺️](docs/productization-plan.md)

| الترتيب | المشروع | فكرة | تنفيذ | سوق | جاهزية | المركّب | الفجوة الوحيدة نحو المنتج |
|---|---|---|---|---|---|---|---|
| 1 | **Nexus Core** | 9.5 | 9.0 | 8.0 | 6.0 | **8.2** | لوحة تحكم + trace logs + benchmarks + demo مستضاف |
| 2 | **Rasan — رسن** | 9.0 | 8.5 | 8.5 | 6.5 | **8.1** | نشر على المتاجر (AAB موقّع) + MLS الجماعي + اختبار ميداني |
| 3 | **LifeLink** | 8.5 | 8.0 | 7.5 | 6.0 | **7.5** | مطابقة متبرعين جغرافية + حزمة ثقة للمشغّل |
| 4 | **NexHub** | 7.5 | 8.0 | 6.5 | 5.5 | **7.0** | هوية محسومة (مساحة عمل مطور محلية) + onboarding سرد ذاتي |
| 5 | **BASIRAH-AI — بصيرة** | 8.5 | 6.5 | 7.5 | 5.0 | **6.8** | من pipeline إلى platform: مقياس استرجاع + لوحة بيانات |

> **منهجية الدرجات**: كل رقم خلفه دليل قابل للتحقق بتاريخ 2026-10-31 — `nexus-core`: **3,680 حالة اختبار مجمّعة** في 210 ملفات + CI مزدوج أخضر؛ `Rasan`: **312 اختبار زمني خضراء** (265 خادم vitest + 47 جوال flutter)؛ `lifelink-app`: **70/70 pytest** + هجرات Alembic مثبتة على Postgres حقيقي؛ `nexhub`: **38/38 + analyze صفر** + نشر Pages؛ `BASIRAH-AI`: CI أخضر بكامل مكدس pgvector + Docker stack. تفصيل المنهجية والأوزان وإعادة إنتاج كل رقم: [docs/scorecard.md](docs/scorecard.md).

### 🧩 النواة الخمسة كمنتجات | The Core Five as Products

> لكل مشروعٍ جملةٌ واحدة تجيب الأسئلة التي يسألها أي زائر في أول 30 ثانية: **ما هذا المنتج؟ لمن؟ ما الذي يعمل فعلاً اليوم؟ وكيف أجرّبه الآن؟**

#### 1. Nexus Core — نظام وكلاء AI تدقّقه بنفسك

- **المنتج**: نظام وكلاء ذكاء اصطناعي موحّد يعمل على جهازك — ذاكرة طويلة المدى، تعلّم مستمر، أمن offline، ومجلس قرارات حيّ. النواة بايثون قياسي خالص بلا أي تبعية.
- **لمن**: مهندسو وباحثو AI يبنون وكلاء مستقلين ويريدون وقت تشغيل يدقّقونه بأنفسهم سطراً بسطر — لا صندوقاً أسود سحابياً.
- **MVP اليوم**: 20 وكيلاً يعملون فعلاً + 3,680 حالة اختبار + CI مزدوج أخضر + Docker.
- **جرّبه الآن**: `git clone https://github.com/tibatechapp-ship-it/nexus-core && cd nexus-core && make check` — ثم `python zyvo-telegram.py` أو واجهة TUI بلا أي تثبيت.

#### 2. Rasan — رسن: دردشة E2EE بلا رقم هاتف

- **المنتج**: دردشة جماعية مشفّرة طرفاً-لطرف بهوية مستخدم فقط — واجهة ~7KB مضغوطة، عربية RTL أولاً، قابلة للاستضافة الذاتية.
- **لمن**: مجتمعات عربية تحتاج خصوصية كاملة (صحفيون، فِرق ميدانية، عائلات) بلا أرقام ولا سحابة مزوّد.
- **MVP اليوم**: 312 اختباراً زمنياً (265 خادم + 47 جوال) + مكالمات وقصص وإشراف وتصويت + نداء طوارئ معياري.
- **جرّبه الآن**: `git clone https://github.com/tibatechapp-ship-it/Rasan && cd Rasan/server && npm install && npm start` → افتح `http://localhost:3000` — وعلى الـWiFi عنوان جهازك مباشرة.

#### 3. LifeLink — شبكة إنقاذ دم بخصوصية مصمَّمة

- **المنتج**: منصة تربط المتبرعين بالمستشفيات والمرضى — نداءات استغاثة بفصيلة ومدينة واستعجال، وقوائم PII-minimal: التفاصيل تُجلب عند الطلب فقط.
- **لمن**: بنوك دم ومراكز نقل ومبادرات طلابية تحتاج مشغّلاً يستطيع تبرير الثقة به — ومتبرعون يريدون أن يساعدوا فوراً.
- **MVP اليوم**: 70/70 اختبار عقد + JWT وتحديد معدل + هجرات idempotent على Postgres حقيقي + Docker + إصدار v1.0.0.
- **جرّبه الآن**: `docker build -t lifelink https://github.com/tibatechapp-ship-it/lifelink-app && docker run -p 5000:5000 -e SECRET_KEY=$(openssl rand -hex 32) lifelink` → `http://localhost:5000` — رحلة النداء الاستعجالي تعمل للزائر.

#### 4. NexHub — مساحة عمل المطوّر العربية offline

- **المنتج**: عميل Git كامل + لوحة مستودعات + أدوات يومية + وكيل AI — في تطبيق واحد يعمل بلا حساب ولا سحابة ولا إنترنت. الكود لا يترك جهازك.
- **لمن**: المطوّر العربي في بيئة اتصال ضعيف أو مقيّد، والمبتدئ الذي تخيفه واجهات Git الإنجليزية.
- **MVP اليوم**: `flutter analyze` صفر + 38/38 اختبار + CI وBuild أخضران + موقع توثيق منشور + إصدارات جاهزة.
- **جرّبه الآن**: حمّل الإصدار من [Releases](https://github.com/tibatechapp-ship-it/nexhub/releases) — أو من المصدر: `flutter pub get && flutter run -d windows` (أو linux/android).

#### 5. BASIRAH-AI — بصيرة: ذكاء الوثائق العربية

- **المنتج**: من أرشيف مبعثر وممسوح ضوئياً إلى قاعدة معرفية مصنّفة قابلة للبحث الدلالي — OCR عربي حقيقي + embeddings على pgvector، كله على جهازك.
- **لمن**: مكتبات وجامعات ومراكز بحث وناشرون يريدون تحويل أرشيفهم إلى أصل معرفي — بأدوات مفتوحة لا تقرأ وثائقهم في سحابة غريبة.
- **MVP اليوم**: خط معالجة كامل (OCR → تصنيف هجين → pgvector) + Docker stack جاهز + ثلاث واجهات (CLI/سطح مكتب/ويب RTL).
- **جرّبه الآن**: `git clone https://github.com/tibatechapp-ship-it/BASIRAH-AI && cd BASIRAH-AI && docker compose up --build` → `http://localhost:8000/docs` — أو `PYTHONPATH=src python -m basirah.cli` لتنظيم مكتبة كاملة من سطر واحد.

### 🧱 الطبقات الأخرى | Other Tiers

- **درجة ثانية قريبة من النواة**: [Raqib](https://github.com/tibatechapp-ship-it/raqib) (E2E + Integration Postgres أخضر + ADRs — ينقصه قصة سوق) و[Pharma SDL](https://github.com/tibatechapp-ship-it/pharma-sdl) (إصدارات سطح مكتب 3 منصات — يحتاج فريق بحث وبيانات).
- **مكوّنات داعمة**: [qubhub telemetry](https://github.com/tibatechapp-ship-it/qubhub) (خادم إحصاءات يحترم الخصوصية — جزء من منظومة QubHub لا منتج مستقل).
- **أرشيف موحّد**: `wifi-chat` → وحدة sila داخل رسن · `NexunGu` → qubhub · `tyb-zyv-ai` → nexus-core · `novasphere` مؤرشف · `olmo` مُدمج في NexHub · `seekfeek` fork لمرجع DeepSeek Harness.

### 📊 شارات المشاريع | Project Badges

| المشروع | CI | الترخيص | الإصدار | التقنية |
|---|---|---|---|---|
| **Nexus Core** | [![CI](https://github.com/tibatechapp-ship-it/nexus-core/actions/workflows/ci.yml/badge.svg)](https://github.com/tibatechapp-ship-it/nexus-core/actions/workflows/ci.yml) [![Tests](https://github.com/tibatechapp-ship-it/nexus-core/actions/workflows/test.yml/badge.svg)](https://github.com/tibatechapp-ship-it/nexus-core/actions/workflows/test.yml) | [![MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/tibatechapp-ship-it/nexus-core/blob/main/LICENSE) | [![Release](https://img.shields.io/github/v/release/tibatechapp-ship-it/nexus-core)](https://github.com/tibatechapp-ship-it/nexus-core/releases) | ![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white) |
| **Rasan** | [![CI](https://github.com/tibatechapp-ship-it/Rasan/actions/workflows/ci.yml/badge.svg)](https://github.com/tibatechapp-ship-it/Rasan/actions/workflows/ci.yml) | [![MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/tibatechapp-ship-it/Rasan/blob/main/LICENSE) | — | ![Node](https://img.shields.io/badge/Node-%E2%89%A520-339933?logo=node.js&logoColor=white) |
| **LifeLink** | [![CI](https://github.com/tibatechapp-ship-it/lifelink-app/actions/workflows/ci.yml/badge.svg)](https://github.com/tibatechapp-ship-it/lifelink-app/actions/workflows/ci.yml) | [![MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/tibatechapp-ship-it/lifelink-app/blob/main/LICENSE) | [![Release](https://img.shields.io/github/v/release/tibatechapp-ship-it/lifelink-app)](https://github.com/tibatechapp-ship-it/lifelink-app/releases) | ![Python](https://img.shields.io/badge/Flask-3.1-000000?logo=flask&logoColor=white) |
| **Raqib** | [![CI](https://github.com/tibatechapp-ship-it/raqib/actions/workflows/ci.yml/badge.svg)](https://github.com/tibatechapp-ship-it/raqib/actions/workflows/ci.yml) | [![MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/tibatechapp-ship-it/raqib/blob/main/LICENSE) | [![Release](https://img.shields.io/github/v/release/tibatechapp-ship-it/raqib)](https://github.com/tibatechapp-ship-it/raqib/releases) | ![Python](https://img.shields.io/badge/FastAPI-WS-009688?logo=fastapi&logoColor=white) |
| **Pharma SDL** | [![Tests](https://github.com/tibatechapp-ship-it/pharma-sdl/actions/workflows/tests.yml/badge.svg)](https://github.com/tibatechapp-ship-it/pharma-sdl/actions/workflows/tests.yml) | [![MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/tibatechapp-ship-it/pharma-sdl/blob/main/LICENSE) | — | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white) |
| **NexHub** | [![CI](https://github.com/tibatechapp-ship-it/nexhub/actions/workflows/ci.yml/badge.svg)](https://github.com/tibatechapp-ship-it/nexhub/actions/workflows/ci.yml) [![Build](https://github.com/tibatechapp-ship-it/nexhub/actions/workflows/build.yml/badge.svg)](https://github.com/tibatechapp-ship-it/nexhub/actions/workflows/build.yml) | [![MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/tibatechapp-ship-it/nexhub/blob/main/LICENSE) | [![Release](https://img.shields.io/github/v/release/tibatechapp-ship-it/nexhub)](https://github.com/tibatechapp-ship-it/nexhub/releases) | ![Flutter](https://img.shields.io/badge/Flutter-%E2%89%A53.24-02569B?logo=flutter&logoColor=white) |
| **Chess CLI** | [![CI](https://github.com/tibatechapp-ship-it/chess-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/tibatechapp-ship-it/chess-cli/actions/workflows/ci.yml) | [![MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/tibatechapp-ship-it/chess-cli/blob/main/LICENSE) | — | ![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white) |

---

## 🖼️ المشاريع بنظرة | Projects at a Glance

<table>
  <tr>
    <td width="50%">
      <a href="https://github.com/tibatechapp-ship-it/nexus-core"><img src="assets/nexus-core.svg" alt="nexus-core"></a>
      <p align="center"><sub>المحرك الجامع لمنظومة Nexus</sub></p>
    </td>
    <td width="50%">
      <a href="https://github.com/tibatechapp-ship-it/Rasan"><img src="assets/rasan.svg" alt="Rasan"></a>
      <p align="center"><sub>دردشة E2EE بلا رقم هاتف</sub></p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <a href="https://github.com/tibatechapp-ship-it/lifelink-app"><img src="assets/lifelink.svg" alt="LifeLink"></a>
      <p align="center"><sub>شبكة إنقاذ وتبرع بالدم</sub></p>
    </td>
    <td width="50%">
      <a href="https://github.com/tibatechapp-ship-it/raqib"><img src="assets/raqib.svg" alt="Raqib"></a>
      <p align="center"><sub>تحليلات فورية بلا تنفيذ أوامر</sub></p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <a href="https://github.com/tibatechapp-ship-it/pharma-sdl"><img src="assets/pharma.svg" alt="Pharma SDL"></a>
      <p align="center"><sub>اكتشاف الأدوية بالذكاء الاصطناعي</sub></p>
    </td>
    <td width="50%">
      <a href="https://github.com/tibatechapp-ship-it/nexhub"><img src="assets/nexhub.svg" alt="NexHub"></a>
      <p align="center"><sub>منصة Git محلية عربية</sub></p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <a href="https://github.com/tibatechapp-ship-it/chess-cli"><img src="assets/chess-cli.svg" alt="Chess CLI"></a>
      <p align="center"><sub>شطرنج الطرفية — وُلد من Nexus Studio</sub></p>
    </td>
    <td width="50%">
      <p align="center"><b>… والمزيد قادم</b></p>
      <p align="center"><sub><a href="https://github.com/orgs/tibatechapp-ship-it/repositories">تابع المنظمة</a> ليصلك الجديد</sub></p>
    </td>
  </tr>
</table>

---

## 📸 لقطات حقيقية | Real Screenshots

من LifeLink كما هو — بلا تجميل، من جلسات تشغيل فعلية:

<table>
  <tr>
    <td width="50%"><img src="assets/screenshot-lifelink-home.png" alt="LifeLink — الرئيسية"><p align="center"><sub><b>الرئيسية</b> — قوائم PII-minimal</sub></p></td>
    <td width="50%"><img src="assets/screenshot-lifelink-emergencies.png" alt="LifeLink — النداءات الاستعجالية"><p align="center"><sub><b>النداءات الاستعجالية</b> — رحلة تعمل للزائر</sub></p></td>
  </tr>
</table>

---

## 🕒 آخر تحديث | Last Updated

<!-- LAST-UPDATED:START -->
| المشروع | آخر دفعة (UTC) | فرع نشط |
|---|---|---|
| Rasan | 2026-10-31 | main |
| lifelink-app | 2026-10-31 | main |
| pharma-sdl | 2026-10-30 | main |
| nexhub | 2026-10-31 | main |
| nexus-core | 2026-10-31 | main |
| chess-cli | 2026-10-30 | main |
| raqib | 2026-10-30 | main |
<!-- LAST-UPDATED:END -->

> 🤖 هذا الجدول يتحدّث **تلقائياً** كل 6 ساعات عبر GitHub Actions (`.github/workflows/update-readme.yml`) — لا تعدّله يدوياً.

---

## 🧭 مبادئنا | Principles

- **الخصوصية ليست ميزة تُضاف** — بل تُصمَّم من السطر الأول (Rasan بلا أرقام، NexHub بلا سحابة، LifeLink بقوائم PII-minimal)
- **عربي أولاً ثم العالم** — RTL أصلي، لا ترجمة لاحقة
- **بوابات لا وعود** — CI يعمل على main، والاختبارات شرط للدمج
- **صدق التقدم** — لا عدّادات وهمية ولا بيانات مختلقة، والمحدوديات تُعلَن في التوثيق

## 📬 التواصل

- 🏢 المنظمة: [tibatechapp-ship-it](https://github.com/orgs/tibatechapp-ship-it/repositories)
- 🔐 ثغرة أمنية في أحد المشاريع؟ استخدم **Security Advisories** في المستودع المعني — لا Issues عامة.
