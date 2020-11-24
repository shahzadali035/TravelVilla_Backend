from rest_framework.routers import DefaultRouter
# from ..views import ArticleViewSet, FormViewSet
from ..views import FormViewSet

# Is File Main ap jis ko upar rakho gy wohi File (e.g UserProfiles ya Form)
# apko backend py api likhny sy show hogi

router = DefaultRouter()
router.register(r'', FormViewSet, basename='UserProfiles')
# router.register(r'', ArticleViewSet, basename='UserProfiles')
urlpatterns = router.urls

# from django.urls import path
#
# from .views import (
#     ArticleListView,
#     ArticleDetailView,
#     ArticleCreateView,
#     ArticleDeleteView,
#     ArticleUpdateView
# )
#
#
# urlpatterns = [
#     path('', ArticleListView.as_view()),
#     path('create/', ArticleCreateView.as_view()),
#     path('<pk>', ArticleDetailView.as_view()),
#     path('<pk>/update/', ArticleUpdateView.as_view()),
#     path('<pk>/delete', ArticleDeleteView.as_view())
#
# ]