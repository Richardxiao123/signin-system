

# signin-system

這是一個使用 Django 建立的網頁專案，目標能夠達成使用隨機生成QRCODE開關門禁並且紀錄下人物登入時間。
---

## 專案架構
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

## 環境設定與啟動方式
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




