from django.urls import path
from apps.users.api.api import user_api_view, user_detail_api_view
# from apps.users.api.api import UserApiView


urlpatterns = [
    path('', user_api_view, name = 'usuario_api'),
    path('<int:pk>', user_detail_api_view, name = 'user_detail_api')
    # path('', UserApiView.as_view(), name = 'usuario_api')
]