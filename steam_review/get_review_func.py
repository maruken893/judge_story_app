import requests
import time
import urllib.parse
import csv


def get_reviews(id):
    BASE_URL = 'https://store.steampowered.com/appreviews/{game_id}?json=1&filter=recent&language=japanese&day_range=all&review_type={review_type}&purchase_type={purchase_type}&num_per_page=100'
    BASE_URL = BASE_URL.replace('{game_id}', str(id))
    review_types = ['positive', 'negative']
    purchase_types = ['non_steam_purchase', 'steam']
    reviews_list = []
    for review_type in review_types:
        BASE_URL = BASE_URL.replace('{review_type}', review_type)
        for purchase_type in purchase_types:
            BASE_URL = BASE_URL.replace('{purchase_type}', purchase_type)

            reviews = requests.get(BASE_URL).json()
            for review in reviews['reviews']:
                reviews_list.append(review['review'])
            time.sleep(.1)
            BASE_URL = BASE_URL.replace('non_steam_purchase', '{purchase_type}')


        BASE_URL = 'https://store.steampowered.com/appreviews/{game_id}?json=1&filter=recent&language=japanese&day_range=all&review_type={review_type}&purchase_type={purchase_type}&num_per_page=100'
        BASE_URL = BASE_URL.replace('{game_id}', str(id))

    return reviews_list






def get_reviews_imp(id):
    BASE_URL = 'https://store.steampowered.com/appreviews/{game_id}?json=1&filter=updated&language=japanese&day_range=all&cursor=*&review_type=all&purchase_type=all&num_per_page=100'
    reviews_list = []
    cursor = '*'

    num = 0


    res = requests.get(BASE_URL.replace('{game_id', str(id)))
    res = res.json()
    total_review_num = res['query_summary']['total_reviews']
    range_num = round(total_review_num / 100) + 1

    # if range_num > 3:
    #     range_num = 3

    if range_num > 5:
        range_num = 5





    with open('steam_review/reviews/' + str(id) + '.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['number', 'steam_id', 'playtime_at_review', 'voted_up', 'votes_up', 'review',  'story', 'graphic', 'character', 'music', 'Operability'])

        for i in range(range_num):
            res = requests.get(BASE_URL.replace('{cursor}', urllib.parse.quote(cursor)).replace('{game_id}', str(id)))
            res = res.json()
            reviews = res['reviews']
            for review in reviews:
                reviews_list.append(review['review'])

                #csv
                author = review['author']
                steam_id = author['steamid']
                try:
                    playtime_at_review = author['playtime_at_review']
                except KeyError:
                    print('playtime_at_review is null')
                    playtime_at_review = -1
                voted_up = review['voted_up']
                votes_up = review['votes_up']

                writer.writerow([num, steam_id, playtime_at_review, voted_up, votes_up, review['review']])
                num += 1
            cursor = res['cursor']
            time.sleep(.1)
            BASE_URL = 'https://store.steampowered.com/appreviews/{game_id}?json=1&filter=updated&language=japanese&day_range=all&cursor={cursor}&review_type=all&purchase_type=all&num_per_page=100'
    return reviews_list

#
# reviews_list = get_reviews_imp(377160)
#
# print(len(reviews_list))
#
# for review in reviews_list:
#     print(review)
