# from django.urls import path
# from . import views


# urlpatterns = [

# ]
from django.urls import path
from . import views

app_name = 'catalog'
urlpatterns = [
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # path('', views.index, name='index'),
    # # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/specifics/5/
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('specifics/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/specifics/5/results/
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('specifics/<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/specifics/5/vote/
    # path('<int:pk>/vote/', views.vote, name='vote'),
    # path('specifics/<int:question_id>/vote/', views.vote, name='vote'),
]