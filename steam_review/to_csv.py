import csv
import requests

def get_csv(df, id):
    num = 0
    with open('../data/' + str(id) + '.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['number', 'steam_id', 'playtime_at_review', 'voted_up', 'votes_up', 'review',  'story', 'graphic', 'character', 'music', 'Operability'])
        for game_id in []:

            json_response = requests.get()
            for data in json_response['reviews']:
                author = data['author']
                steam_id = author['steamid']
                try:
                    playtime_at_review = author['playtime_at_review']
                except KeyError:
                    print('playtime_at_review is null')
                    playtime_at_review = -1
                voted_up = data['voted_up']
                votes_up = data['votes_up']
                review = data['review']

                writer.writerow([num, steam_id, playtime_at_review, voted_up, votes_up, review])
                num += 1