import collections
import pandas as pd


def mocked_recommendation(event_list, user_list, target_user):
    users_score = {}
    for u in user_list:
        events_scores = []
        for e in event_list:
            event_score = 0
            event_score += len(set(u['liked_authors']).intersection(e['author']))
            event_score += len(set(u['liked_tags']).intersection(e['tags']))
            events_scores.append(event_score)

        users_score[u['username']] = events_scores

    df = pd.DataFrame.from_dict(users_score, orient='index', columns=[e['event_name'] for e in event_list])

    target_user_scoring = df.loc[target_user]
    return target_user_scoring.sort_values(ascending=False).to_dict()
