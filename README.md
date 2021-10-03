# Photo Converter

### Installation

- Clone Repository
```
git clone https://github.com/badrabbit100/PhotoConverter.git
cd PhotoConverter
```
- Create virtual environment, install modules from requirements.txt
```
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

- Generate Random Django Secret Key to the file 

> You can use any random generating service for example [DJecrety.ir](https://djecrety.ir/) 
```
nano .secret_key.txt
```
- Create db.sqlite3 and migrate, create superuser
```
python3 manage.py migrate
python3 manage.py createsuperuser   
```
- Start Application
```
python3 manage.py runserver
```

> You can find admin panel here http://localhost:8000/any_non_standard_path/admin/

### Testing
```
python3 manage.py test
```

### API Path
- Get Photos list, Upload New Photo, Rotate Photo
> http://localhost:8000/api/v1/photos/

- Delete all Photo just call
> http://localhost:8000/api/v1/delete_all/

### Support
Telegram [@TonyFreeSec](https://t.me/tonyfreesec) 