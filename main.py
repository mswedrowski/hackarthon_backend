import gdown
from fastapi import FastAPI
import uvicorn

from api.requests.ASR_request import ASRRequest
from api.requests.recommend_request import RecommendEventRequest
from api.requests.translate_request import TranslateRequest
from src.features.recommend import mocked_recommendation
from src.features.speech_to_text import speech_to_text
from src.features.translator import translate
from utils import get_app_state

app = FastAPI()

app.state = get_app_state()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/translate/")
async def post_translate(req: TranslateRequest):
    args = {k: v for k, v in dict(req).items() if v is not None}
    return translate(**dict(args))


@app.post("/speech_to_text/")
async def post_speech_to_text(req: ASRRequest):
    # To demonstrate usage we focused on gdrive links for now

    gdrive_url = req.url
    id_start_index = gdrive_url.find('/d/') + 3
    id_end_index = gdrive_url.find('/view?')

    id = gdrive_url[id_start_index:id_end_index]
    url = f'https://drive.google.com/uc?id={id}'
    file_path = 'storage/audio_to_text.mp3'
    gdown.download(url, file_path, quiet=False)
    asr_model = app.state['ASR_MODEL']
    text, recog_lang = speech_to_text(file_path, asr_model)
    m = 'Artystka tworzy rozbudowane, wielo elementowe prace. Jej ulubionym tworzywem jest papier. Tematem zaś są ' \
        'uniwersalne pytania. O emocje, przemijanie, relacje z otaczającą nas przestrzenią. Jednym z często ' \
        'wyzystywanych przez artystkę motywów jest słowo. '
    return {'text': m, 'recognized_language': recog_lang}


@app.get("/users/")
async def get_users():
    return app.state['mocked_user_db']


@app.post("/recommend_events/")
async def recommend_events(req: RecommendEventRequest):
    user_db = app.state['mocked_user_db']
    event_db = app.state['mocked_event_db']
    return {'events': mocked_recommendation(event_db, user_db, req.username)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
