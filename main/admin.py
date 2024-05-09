from django.contrib import admin
from main.models import Organization, Product, Contact
from django.urls import reverse
from django.utils.html import format_html


@admin.action(description="Очистка задолженности")
def clear_arrears(model_admin, request, queryset):
    """
    Кастомное действие для админ панели
    """
    queryset.update(arrears=0.0)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    """
    Настройки для админ панели для организаций
    """
    list_display = ('name', 'type_of_organization', 'rang', 'get_parent_link', 'get_contact_link', 'city', 'get_user_link', 'arrears', 'created')
    list_filter = ('contact__city',)  # Добавляем фильтр по городу контакта
    actions = [clear_arrears]       # Добавление кастомного действия

    def city(self, obj):
        """
        Для вывода столбца city контакта
        """
        return obj.contact.city if obj.contact else None

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('contact')
        return queryset

    def get_contact_link(self, obj):
        """
        Делает ссылку для контакта
        """
        contact = obj.contact
        if contact:
            contact_url = reverse('admin:%s_%s_change' % (contact._meta.app_label, contact._meta.model_name),
                                 args=[contact.id])
            return format_html('<a href="{}">{}</a>', contact_url, contact)
        else:
            return '-'

    get_contact_link.short_description = 'Контакт'

    def get_user_link(self, obj):
        """
        Делает ссылку для пользователя
        """
        user = obj.user
        if user:
            user_url = reverse('admin:%s_%s_change' % (user._meta.app_label, user._meta.model_name),
                                 args=[user.id])
            return format_html('<a href="{}">{}</a>', user_url, user.email)
        else:
            return '-'

    get_user_link.short_description = 'Пользователь'

    def get_parent_link(self, obj):
        """
        Делает ссылку для поставщика
        """
        parent = obj.parent
        if parent:
            parent_url = reverse('admin:%s_%s_change' % (parent._meta.app_label, parent._meta.model_name), args=[parent.id])
            return format_html('<a href="{}">{}</a>', parent_url, parent.name)
        else:
            return '-'

    get_parent_link.short_description = 'Поставщик'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Настройки для админ панели для продуктов
    """
    list_display = ('name', 'model', 'date',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Настройки для админ панели для контактов
    """
    list_display = ('email', 'country', 'city', 'street', 'house')
    list_filter = ('city',)
