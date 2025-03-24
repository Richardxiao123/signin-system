

# signin-system

這是一個使用 Django 建立的網頁專案範例，包含基本的檔案架構與網頁架構說明。

---

## 📁 專案架構
```
signin/                # 專案目錄
│
├── firstproject/            
│   ├── __init__.py        
│   ├── settings.py     
│   ├── urls.py           
│   ├── asgi.py            
│   └── wsgi.py            
│
├── myapp/                
│   ├── migrations/        
│   ├── admin.py           
│   ├── apps.py            
│   ├── models.py         
│   ├── tests.py           
│   └── views.py           
│
├── static/
│   ├──css
│   └──images
│
├── templates/             
│   ├──1.html
│   ├──boss.html
│   ├──home.html
│   ├──info.html
│   ├──login.html
│   └──page.html
│
├── db.sqlite3
├──manage.py
└──user_data.json
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

---




