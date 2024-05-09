from django.urls import path
from main.apps import MainConfig
from main.views import OrganizationCreateAPIView, OrganizationListAPIView, OrganizationRetrieveAPIView, \
    OrganizationUpdateAPIView, OrganizationDestroyAPIView, ContactCreateAPIView, ContactRetrieveAPIView, \
    ContactListAPIView, ContactUpdateAPIView, ProductCreateAPIView, ProductRetrieveAPIView, ProductListAPIView, \
    ProductUpdateAPIView, ProductDeleteAPIView

app_name = MainConfig.name

urlpatterns = [
    path('organization/create/', OrganizationCreateAPIView.as_view(), name='organization_create'),
    path('organization/', OrganizationListAPIView.as_view(), name='organization_list'),
    path('organization/<int:pk>/', OrganizationRetrieveAPIView.as_view(), name='organization_get'),
    path('organization/update/<int:pk>/', OrganizationUpdateAPIView.as_view(), name='organization_update'),
    path('organization/delete/<int:pk>/', OrganizationDestroyAPIView.as_view(), name='organization_delete'),

    path('contact/create/', ContactCreateAPIView.as_view(), name='contact_create'),
    path('contact/', ContactListAPIView.as_view(), name='contact_list'),
    path('contact/<int:pk>/', ContactRetrieveAPIView.as_view(), name='contact_get'),
    path('contact/update/<int:pk>/', ContactUpdateAPIView.as_view(), name='contact_update'),

    path('product/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('product/', ProductListAPIView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_get'),
    path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteAPIView.as_view(), name='product_delete'),
]
