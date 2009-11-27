from django.test import TestCase
from models import *
import time
class CacheTest(TestCase):
    fixtures = ['test']

    def test_cache_get_by_pk(self):
        a = Author(pk=10,name=u'anarcher')
        a.save()
        time.sleep(10)
        b = Author.objects.get(pk=10)
        self.assertFalse(b.from_cache)
#        time.sleep(10)
        c = Author.objects.get(pk=10)
        self.assertTrue(c.from_cache)

    """
    def test_cache_get_by_pk(self):
        self.assertFalse(Article.objects.get(pk=1).from_cache)
        time.sleep(10)
        self.assertTrue(Article.objects.get(pk=1).from_cache)
    """

    """
    def test_cache_get_not_pk(self):
        # Prime cache
        self.assertFalse(Article.objects.get(pk=1).from_cache)
        self.assertTrue(Article.objects.get(pk=1).from_cache)

        # Not from cache b/c it's not a simple get by pk
        self.assertFalse(Article.objects.get(pk=1, name='Mike Malone').from_cache)
    """

