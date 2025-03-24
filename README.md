# signin-system

這是一個使用 Django 建立的網頁專案，包含基本的檔案架構與網頁架構說明。

---

## 📁 專案架構
```
myproject/                # 專案目錄
│
├── myproject/            # Django 專案設定目錄
│   ├── __init__.py        # 專案初始化檔案
│   ├── settings.py        # 專案設定檔案
│   ├── urls.py            # 全域 URL 配置檔案
│   ├── asgi.py            # ASGI 設定檔
│   └── wsgi.py            # WSGI 設定檔
│
├── myapp/                # Django 應用程式目錄
│   ├── migrations/        # 資料庫遷移檔案目錄
│   ├── templates/         # 模板資料夾 (HTML 檔案)
│   │   └── myapp/         # 應用專屬模板資料夾
│   │       └── index.html # 範例首頁模板
│   ├── static/            # 靜態檔案資料夾 (CSS, JS, 圖片等)
│   │   └── css/           # 範例 CSS 資料夾
│   │       └── style.css  # 範例 CSS 檔案
│   ├── admin.py           # 後台管理設定檔案
│   ├── apps.py            # App 設定檔案
│   ├── forms.py           # 表單檔案 (選用)
│   ├── models.py          # 資料庫模型檔案
│   ├── tests.py           # 測試檔案
│   └── views.py           # 視圖函式檔案
│
├── static/                # 全域靜態檔案資料夾 (可選)
├── db.sqlite3             # SQLite 資料庫檔案
├── manage.py              # Django 管理指令檔案
└── requirements.txt       # 專案相依套件檔案
```

---

## 🌟 網頁架構
- `index.html`: 網站首頁，使用 Django 模板引擎渲染。
- `style.css`: 簡單的 CSS 檔案用於美化網頁。
- `views.py`: 定義渲染網頁的視圖函式。
- `urls.py`: 配置 URL 對應的視圖。

---

## 🚀 環境設定與啟動方式
### 1. 安裝 Django
```bash
pip install django
```

### 2. 遷移資料庫
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. 啟動開發伺服器
```bash
python manage.py runserver
```

瀏覽器開啟 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)





