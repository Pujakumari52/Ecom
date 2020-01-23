from django.conf.urls import include, url
from .import views

urlpatterns = [
    url("", views.index,name="ShopHome"),
    url("about/", views.about,name="AboutUs"),
    url("contact/", views.contact,name="ContactUs"),
    url("tracker/", views.tracker,name="TrackingStatus"),
    url("search/", views.search,name="Search"),
    url("productview/", views.productView,name="ProductView"),
    url("checkout/", views.checkout,name="Checkout"),
]