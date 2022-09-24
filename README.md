# Backend

Application is POC of ArtMatch backend which allows user via REST API. It contains following features
- Translating from any other language to Polish language
- Obtaining trancription from recordings provided as link from Google Drive
- Recommending users from mocked database


Video explaining use of application in details:
[link](https://drive.google.com/file/d/12NfhZuSq76QbjqJ6Ro5Nk6ormr-TTlr0/view?usp=sharing)

## How to run

1. Install requirements
```pip install -r requirements.txt```
2. Run uvicorn app by typing in terminal
```commandline
uvicorn main:app
```

## Usage
You can access endpoints of our application by typing `localhost:8000/docs`