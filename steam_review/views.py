from django.views.generic import TemplateView
from django.views import View
from django.shortcuts import render
import pandas as pd

from .get_review_func import get_reviews, get_reviews_imp
from .tool.main_func import scoreing
from .get_game_name import get_game_name
from .get_id_f_url import get_id

class HelloView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'hello.html')



class ResultView(View):
    def post(self, request, *args, **kwargs):
        url = request.POST['url']
        id = get_id(url)
        print(id)

        reviews = get_reviews_imp(id)
        story_state = scoreing(reviews).values()
        df = pd.read_csv('steam_review/reviews/' + str(id) + '.csv')
        df['story_state'] = story_state
        df.to_csv('steam_review/reviews/' + str(id) + '.csv')

        title = get_game_name(id)


        positive_score = 0
        neutral_score = 0
        negative_score = 0

        for score in story_state:
            if score == 1:
                positive_score += 1
            elif score == 0:
                neutral_score += 1
            else:
                negative_score += 1

        if (positive_score + negative_score) == 0:
            star = '評価がありません'
        else:
            star = round(5 * (positive_score / (positive_score + negative_score)), 1)

        context = {
            'id': id,
            'title': title,
            'positive_score': positive_score,
            'neutral_score': neutral_score,
            'negative_score': negative_score,
            'star': star,
        }

        return render(request, 'result.html', context)


# class HomePageView(TemplateView):
#     template_name = 'home.html'


