import random as r
import whisper

SAMPLE_POLISH_NAMES = ['Jakub', 'Tomasz', 'Marek', 'Marcin',
                       'Paweł', 'Jan', 'Agnieszka', 'Magłorzata',
                       'Marcelina', 'Kinga', 'Ania', 'Elżbieta',
                       'Grażyna']

SAMPLE_EVENTS = [{'event_name': 'KONSUMPCJA, KONSTRUKCJA I MELANCHOLIA',
                  'author': ['Mariola Przyjemska'],
                  'duration': '16.09.2022 – 08.01.2023',
                  'type': 'Exhibition',
                  'tags': ['fotografia', 'lata 90.']},
                 {'event_name': 'NIEPOKÓJ PRZYCHODZI O ZMIERZCHU',
                  'author': ['Lena Achtelik', 'Agnieszka Antkowiak', 'Karolina Balcer', 'Zuzanna Bartoszek',' Jan Baszak',
                            'Paweł Baśnik', 'Justyna Baśnik', 'Katarzyna Bogucka', 'Martyna Czech', 'Jagoda Dobecka',
                            'Kinga Dobosz', 'Eternal Engine (Jagoda Wójtowicz & Martix Navrot)', 'Monika Falkus,' 
                            'Wiktor Gałka', 'Jakub Gliński', 'Zuza Golińska', 'Marcelina Gorczyńska', 'Justyna Górowska',
                            'Anna Grzymała', 'Veronika Hapchenko', 'Agata Ingarden', 'Karolina Jabłońska', 'Maja Janczar',
                            'Jan Jurczak', 'Maria Kniaginin-Ciszewska', 'Karolina Konopka', 'Adam Kozickiz', 'Tomasz Kręcicki',],
                  'duration': '16.07 – 16.10.2022',
                  'type': 'Exhibition',
                  'tags': ['XXI wiek', 'sculpture', 'video', 'photography', 'ceramics', 'textiles', 'performance']},
                 {'event_name': 'KRYJÓWKI. ARCHITEKTURA PRZETRWANIA',
                  'author': ['Natalia Romik'],
                  'duration': '04.08 – 06.11.2022',
                  'type': 'Exhibition',
                  'tags': ['architektura', 'II wojna światowa']},
                 {'event_name': 'GRY I ZABAWKI',
                  'author': ['Aleksandra Badura', 'Wioletta Bogunia-Bugaj', 'Magdalena Bojko-Michalak, Olga Cytowska, '
                            'Agnieszka Doczyńska', 'Natalia Gajo i Zuzanna Walkiewicz', 'Karolina Glanowska, '
                            'Adam Miklaszewski', 'Ola Mirecka', 'Kacper Mutke', 'Paweł Lewandowski', 'Barbara Olejarczyk, '
                            'Martyna Piątek', 'Julia Szymanowska', 'Patrycja Żurawicz'],
                  'duration': '29.07 – 09.10.2022',
                  'type': 'Exhibition',
                  'tags': ['XXI wiek', 'games']}
                 ]


def get_random_phone_number():
    return ''.join(str(r.randint(0, 9)) for _ in range(1, 10))


def get_mocked_user_db():
    db = []
    authors = [e['author'] for e in SAMPLE_EVENTS]
    authors = [item for sublist in authors for item in sublist]

    tags = [e['tags'] for e in SAMPLE_EVENTS]
    tags = [item for sublist in tags for item in sublist]

    for i in range(100):
        name = r.sample(SAMPLE_POLISH_NAMES, 1)[0]
        db.append({'name':  name,
                   'username': f'{name}_{i}',
                   'phone': get_random_phone_number(),
                   'liked_authors': r.sample(authors, 5),
                   'liked_tags': r.sample(tags, 2)})
    return db


def get_app_state():
    return {'ASR_MODEL': whisper.load_model("base"),
            'mocked_user_db': get_mocked_user_db(),
            'mocked_event_db': SAMPLE_EVENTS}
