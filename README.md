# Django python proj

### Virtual Env setup 
/Users/cb-vaibhav/.local/share/virtualenvs/lyricsapp-vm-IDxARr6g
Vm  -> /Users/cb-vaibhav/.local/share/virtualenvs

## Important Commands
* Start VM - pipenv shell
* Stop VM - deactivate
* pipenv install Django
* django-admin startproject cfehome .
* new app creation - python manage.py startapp dao
* python manage.py createsuperuser
```
username: pvai
Email: pvaibhav.1510@gmail.com
Password: 12345
http://127.0.0.1:8000/admin
```

* python manage.py dbshell
* python manage.py makemigrations
* python manage.py migrate
* python manage.py runserver

## Heroku Commands
* heroku config:set DISABLE_COLLECTSTATIC=1 --app django-lyrics-app
* heroku logs --tail --app django-lyrics-app



***
Reference Links

1. https://www.codingforentrepreneurs.com/blog/install-django-on-mac-or-linux
2. https://docs.python-guide.org/dev/virtualenvs/#:~:text=virtualenv%20is%20a%20tool%20to,%24%20pip%20install%20virtualenv
3. https://virtualenv.pypa.io/en/latest/


# GCP Keys
## Local Google Sign-in Keys
```json
{
  "web": {
    "client_id": "172128405680-q1eoam6svviffit6vo99i9r34knm0kbc.apps.googleusercontent.com",
    "project_id": "lyrics-app-282817",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_secret": "vXUArCk4LCs0iGnO8NgELAo4"
  }
}
```

## Heroku Google Sign-in Keys
```json
{
  "web": {
    "client_id": "172128405680-ke31rqqdi9dgoet6r6r20hc7mjvlsgr1.apps.googleusercontent.com",
    "project_id": "lyrics-app-282817",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_secret": "A8hDbssSqIjtr_hJQCZxXGmy",
    "redirect_uris": ["https://django-lyrics-app.herokuapp.com"],
    "javascript_origins": ["https://django-lyrics-app.herokuapp.com"]
  }
}
```
