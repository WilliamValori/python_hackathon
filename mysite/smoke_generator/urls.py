from django.urls import path

from . import views

urlpatterns = [
    # ex: /smoke_generator/
    path('', views.index, name='index'),
    # ex: /smoke_generator/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /smoke_generator/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /smoke_generator/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # ex: /smoke_generator/spare_ribs
    path('spare_ribs/', views.recipe, name='recipe'),
]
