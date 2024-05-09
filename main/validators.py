from rest_framework.serializers import ValidationError


class IfFactoryToZeroValidator:
    """
    Если организация - завод, то ранг всегда 0.
    И не может быть поставщика.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get('type_of_organization') == "factory" and value.get('parent'):
            raise ValidationError('У завода не может быть поставщика.')
