"""
Test for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models
from decimal import Decimal


def create_user(email='user@example.com', password='userpass123'):
    """create and return the new user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    """test for user model"""

    def test_create_user_with_email(self):
        """test creating with email"""
        email = "test@example.com"
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_for_normalized_email(self):
        """test for normalized email"""
        sample_email = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com'],
        ]

        for email, expected in sample_email:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_error(self):
        """test email raises error without email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """test create superuser"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """Creating test for recipe"""

        user = get_user_model().objects.create_user(
            email='test@example.com',
            password='test123'
        )

        recipe = models.Recipe.objects.create(
            user=user,
            title='Sample Recipe',
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample Recipe Description.'
        )

        self.assertEqual(str(recipe), recipe.title)

    def test_create_tag(self):
        """create test for tag"""
        user = create_user()
        tag = models.Tag.objects.create(user=user, name='tag')
        self.assertEqual(str(tag), tag.name)

    def test_create_ingredient(self):
        """Test create an ingredient"""
        user = create_user()
        ingredient = models.Ingredient.objects.create(
            user=user,
            name='ingredient'
        )
        self.assertEqual(str(ingredient), ingredient.name)
