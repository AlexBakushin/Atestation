from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from main.models import Organization, Contact
from users.models import User


class MainTests(APITestCase):

    def test_create_organization_is_admin(self):
        """
        Тест на то, что админ может создать организацию
        """
        self.client = APIClient()
        self.user = User.objects.create(email="admin@sky.pro", is_superuser=True, is_staff=True)
        self.client.force_authenticate(user=self.user)

        data = {
            "contact": {
                "email": "test@test.com",
                "country": "US",
                "city": "LA",
                "street": "11",
                "house": "1"
            },
            "name": "test",
            "type_of_organization": "factory",
            "arrears": 0.0
        }

        response = self.client.post('/organization/create/', data=data, format='json')
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_create_organization_is_user(self):
        """
        Тест на то, что пользователь может создать организацию
        """
        self.client = APIClient()
        self.user = User.objects.create(email="test@sky.pro", is_superuser=False, is_staff=False)
        self.client.force_authenticate(user=self.user)

        data = {
            "contact": {
                "email": "test_2@test.com",
                "country": "US",
                "city": "LA",
                "street": "11",
                "house": "1"
            },
            "name": "test",
            "type_of_organization": "factory",
            "arrears": 0.0
        }

        response = self.client.post('/organization/create/', data=data, format='json')
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_create_organization_is_user_no_active(self):
        """
        Тест на то, что не активный пользователь не может создать организацию
        """
        self.client = APIClient()
        self.user = User.objects.create(email="test@sky.pro", is_superuser=False, is_staff=False, is_active=False)
        self.client.force_authenticate(user=self.user)

        data = {
            "contact": {
                "email": "test_2@test.com",
                "country": "US",
                "city": "LA",
                "street": "11",
                "house": "1"
            },
            "name": "test",
            "type_of_organization": "factory",
            "arrears": 0.0
        }

        response = self.client.post('/organization/create/', data=data, format='json')
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_list_organization_is_active(self):
        """
        Тест на то, что можно получить все организации
        """
        self.client = APIClient()
        self.user = User.objects.create(email="test@sky.pro", is_superuser=False, is_staff=False, is_active=True)
        self.client.force_authenticate(user=self.user)

        response = self.client.get('/organization/')
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_list_organization_no_active(self):
        """
        Тест на то, что нельзя получить организации, если пользователь не активен
        """
        self.client = APIClient()
        self.user = User.objects.create(email="test@sky.pro", is_superuser=False, is_staff=False, is_active=False)
        self.client.force_authenticate(user=self.user)

        response = self.client.get('/organization/')
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_retrieve_organization_is_active(self):
        """
        Тест на то, что можно получить организацию
        """
        self.client = APIClient()
        self.user = User.objects.create(email="test@sky.pro", is_superuser=False, is_staff=False, is_active=True)
        self.client.force_authenticate(user=self.user)

        data = {
            "contact": {
                "email": "test_4@test.com",
                "country": "US",
                "city": "LA",
                "street": "11",
                "house": "1"
            },
            "name": "test_4",
            "type_of_organization": "factory",
            "arrears": 0.0
        }

        contact_data = data.pop('contact')
        contact = Contact.objects.create(**contact_data)
        Organization.objects.create(contact=contact, user=self.user, **data)

        response = self.client.get('/organization/6/')
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_retrieve_organization_no_active(self):
        """
        Тест на то, что нельзя получить организацию, если пользователь не активен
        """
        self.client = APIClient()
        self.user = User.objects.create(email="test_5@sky.pro", is_superuser=False, is_staff=False, is_active=False)
        self.client.force_authenticate(user=self.user)

        data = {
            "contact": {
                "email": "test_5@test.com",
                "country": "US",
                "city": "LA",
                "street": "11",
                "house": "1"
            },
            "name": "test_5",
            "type_of_organization": "factory",
            "arrears": 0.0
        }

        contact_data = data.pop('contact')
        contact = Contact.objects.create(**contact_data)
        Organization.objects.create(contact=contact, user=self.user, **data)

        response = self.client.get('/organization/1/')
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_update_organization_is_active(self):
        """
        Тест на то, что можно обновить организацию
        """
        self.client = APIClient()
        self.user = User.objects.create(email="test_6@sky.pro", is_superuser=False, is_staff=False, is_active=True)
        self.client.force_authenticate(user=self.user)

        data = {
            "contact": {
                "email": "test_6@test.com",
                "country": "US",
                "city": "LA",
                "street": "11",
                "house": "1"
            },
            "name": "test_6",
            "type_of_organization": "factory",
            "arrears": 0.0
        }

        contact_data = data.pop('contact')
        contact = Contact.objects.create(**contact_data)
        Organization.objects.create(contact=contact, user=self.user, **data)

        data_2 = {
            "name": "test_66"
        }

        response = self.client.patch('/organization/update/8/', data=data_2)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_organization_no_active(self):
        """
        Тест на то, что нельзя обновить организацию, если пользователь не активен
        """
        self.client = APIClient()
        self.user = User.objects.create(email="test_7@sky.pro", is_superuser=False, is_staff=False, is_active=False)
        self.client.force_authenticate(user=self.user)

        data = {
            "contact": {
                "email": "test_7@test.com",
                "country": "US",
                "city": "LA",
                "street": "11",
                "house": "1"
            },
            "name": "test_7",
            "type_of_organization": "factory",
            "arrears": 0.0
        }

        contact_data = data.pop('contact')
        contact = Contact.objects.create(**contact_data)
        Organization.objects.create(contact=contact, user=self.user, **data)

        data_2 = {
            "name": "test_77"
        }

        response = self.client.patch('/organization/update/1/', data=data_2)
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_delete_organization_is_active(self):
        """
        Тест на то, что можно удалить организацию хозяину
        """
        self.client = APIClient()
        self.user = User.objects.create(email="test_8@sky.pro", is_superuser=False, is_staff=False, is_active=True)
        self.client.force_authenticate(user=self.user)

        data = {
            "contact": {
                "email": "test_8@test.com",
                "country": "US",
                "city": "LA",
                "street": "11",
                "house": "1"
            },
            "name": "test_8",
            "type_of_organization": "factory",
            "arrears": 0.0
        }

        contact_data = data.pop('contact')
        contact = Contact.objects.create(**contact_data)
        Organization.objects.create(contact=contact, user=self.user, **data)

        response = self.client.delete('/organization/delete/3/')
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_delete_organization_no_active(self):
        """
        Тест на то, что нельзя удалить организацию, если пользователь не активен
        """
        self.client = APIClient()
        self.user = User.objects.create(email="test_9@sky.pro", is_superuser=False, is_staff=False, is_active=False)
        self.client.force_authenticate(user=self.user)

        data = {
            "contact": {
                "email": "test_9@test.com",
                "country": "US",
                "city": "LA",
                "street": "11",
                "house": "1"
            },
            "name": "test_9",
            "type_of_organization": "factory",
            "arrears": 0.0
        }

        contact_data = data.pop('contact')
        contact = Contact.objects.create(**contact_data)
        Organization.objects.create(contact=contact, user=self.user, **data)

        response = self.client.delete('/organization/delete/1/')
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_delete_organization_no_owner(self):
        """
        Тест на то, что нельзя удалить организацию не хозяину
        """
        self.client = APIClient()
        self.user = User.objects.create(email="test_10@sky.pro", is_superuser=False, is_staff=False, is_active=True)
        self.client.force_authenticate(user=self.user)

        data = {
            "contact": {
                "email": "test_10@test.com",
                "country": "US",
                "city": "LA",
                "street": "11",
                "house": "1"
            },
            "name": "test_10",
            "type_of_organization": "factory",
            "arrears": 0.0
        }

        user = User.objects.create(email="test_10", is_superuser=False, is_active=True)

        contact_data = data.pop('contact')
        contact = Contact.objects.create(**contact_data)
        Organization.objects.create(contact=contact, user=user, **data)

        response = self.client.delete('/organization/delete/1/')
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )
