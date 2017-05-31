from django.test import TestCase
from django.urls import reverse
from .models import Category


class HtmlTest(TestCase):
    fixtures = ['initial_data.json']

    def test_category_list_page(self):
        """
        Fixture contains categories
        Expect result: all category names are in rendered html.
        :return:
        """
        response = self.client.get(reverse('category-list-view'))

        for category in Category.objects.all():
            self.assertContains(response, category.name)
