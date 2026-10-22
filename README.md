# ChessCup

 Django + SQLite. Возможности: список турниров, регистрация/вход, подача заявок, личный кабинет, управление турнирами и статусами заявок через `/admin/`.

## Запуск в Windows
```powershell
py -m venv .venv
.venv\Scripts\activate
py -m pip install -r requirements.txt
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```
Откройте http://127.0.0.1:8000/ . Админка: http://127.0.0.1:8000/admin/

Добавьте турниры через админку. База `db.sqlite3` создаётся при миграции. 
