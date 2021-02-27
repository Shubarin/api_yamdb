from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views.reviews import ReviewsViewSet
from .views.comments import CommentsViewSet
from .views.users import MyUserViewSet, registrations_request, get_token, MyUserMeView
from .views.genres import GenreViewSet
from .views.categories import CategoryViewSet
from .views.titles import TitleViewSet

router = DefaultRouter()
router.register(r'titles/(?P<title_id>[^/.]+)/reviews', ReviewsViewSet,
                basename='ReviewsView')
router.register(
    r'titles/(?P<title_id>[^/.]+)/reviews/(?P<review_id>[^/.]+)/comments',
    CommentsViewSet, basename='CommentsView')
# router.register(
#     r'users/me', MyUserMeView, basename='MyUserMeView'
# )
router.register(
    r'users', MyUserViewSet, basename='MyUserViewSet'
)
router.register('genres', GenreViewSet)
router.register('categories', CategoryViewSet)
router.register('titles', TitleViewSet)

urlpatterns = [
    path('v1/users/me/', MyUserMeView.as_view(), name='me'),
    path('v1/', include(router.urls)),
    path('v1/auth/', include([path('email/', registrations_request),
                              path('token/', get_token)]))
]
