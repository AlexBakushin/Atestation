from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from main.models import Organization, Contact, Product
from main.serliazers import OrganizationSerializer, ContactSerializer, ProductSerializer
from main.permissions import IsOwnerOrganization, IsOwnerProduct
from users.permissions import IsActive


class OrganizationCreateAPIView(generics.CreateAPIView):
    """
    Создание модели организации
    """
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated, IsActive]

    def perform_create(self, serializer):
        """
        При создании, user - пользователь
        """
        new_organization = serializer.save()
        new_organization.user = self.request.user
        new_organization.save()


class OrganizationFilter(filters.FilterSet):
    country = filters.CharFilter(field_name='contact__country')  # Указываем поле country в связанной модели contact

    class Meta:
        model = Organization
        fields = ['country']


class OrganizationListAPIView(generics.ListAPIView):
    """
    Список привычек
    """
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    permission_classes = [IsAuthenticated, IsActive]
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrganizationFilter

    def get_queryset(self):
        """
        Передает queryset организаций, где user - пользователь, кроме админа
        """
        if self.request.user.is_staff:
            return Organization.objects.all()
        return Organization.objects.filter(user=self.request.user)


class OrganizationRetrieveAPIView(generics.RetrieveAPIView):
    """
    Выводит модель выбранной организации, где user - пользователь, кроме админа
    """
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    permission_classes = [IsAuthenticated, IsActive]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Organization.objects.all()

        user_organizations = Organization.objects.filter(user=self.request.user)
        return user_organizations


class OrganizationUpdateAPIView(generics.UpdateAPIView):
    """
    Обновление выбранной организации, только те, где user - пользователь, кроме админа
    """
    serializer_class = OrganizationSerializer
    queryset = Organization.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class OrganizationDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление выбранной организации, только те, где user - пользователь
    """
    queryset = Organization.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrganization, IsActive]


class ContactCreateAPIView(generics.CreateAPIView):
    """
    Создание модели контакта
    """
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated, IsActive]


class ContactListAPIView(generics.ListAPIView):
    """
    Список контактов
    """
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ContactRetrieveAPIView(generics.RetrieveAPIView):
    """
    Выводит модель выбранного контакта
    """
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ContactUpdateAPIView(generics.UpdateAPIView):
    """
    Обновление выбранного контакта
    """
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ProductCreateAPIView(generics.CreateAPIView):
    """
    Создание модели продукта
    """
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActive]


class ProductUpdateAPIView(generics.UpdateAPIView):
    """
    Обновление выбранного продукта
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ProductListAPIView(generics.ListAPIView):
    """
    Список продуктов
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """
    Выводит модель выбранного контакта
    """
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = [IsAuthenticated, IsActive]


class ProductDeleteAPIView(generics.DestroyAPIView):
    """
    Удаление выбранного продукта
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerProduct, IsActive]