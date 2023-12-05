from django.urls import path
from .views import home, transaction, transaction_history

urlpatterns = [
    path('', home, name='index'),
    path('transfer/',transaction, name='transaction' ),
    path('history/', transaction_history, name='transaction_history'),

]