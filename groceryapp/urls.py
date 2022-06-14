from django.urls import include, path
from .views import HomeView, OtpView, ProductsView, ProductView, SimilarView, FreqView
urlpatterns = [
        path('', HomeView.as_view(), name='home_view'),
        path('otp', OtpView.as_view(), name='otp_view'),
        path('products', ProductsView.as_view(), name='products_view'),
        path('product', ProductView.as_view(), name='product_view'),
        path('similar', SimilarView.as_view(), name='similar_view'),
        path('freq', FreqView.as_view(), name='freq_view'),
]