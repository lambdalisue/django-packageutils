#!/usr/bin/env python
# vim: set fileencoding=utf8:
"""
Unittest module of ...


AUTHOR:
    lambdalisue[Ali su ae] (lambdalisue@hashnote.net)
    
Copyright:
    Copyright 2011 Alisue allright reserved.

License:
    Licensed under the Apache License, Version 2.0 (the "License"); 
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unliss required by applicable law or agreed to in writing, software
    distributed under the License is distrubuted on an "AS IS" BASICS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
__AUTHOR__ = "lambdalisue (lambdalisue@hashnote.net)"
from packageutils.testcase import AppTestCase

from testapp.models import Article

class TestAppTestCase(AppTestCase):
    fixtures = ['test.yaml']
    installed_apps = [
            'author',
            'tests.blogs.tests.testapp',
        ]
    middleware_classes = [
            'author.middleware.AuthorDefaultBackendMiddleware',
        ]
    
    def test_creation(self):
        """blogs.tests.testapp.Article: creation works correctly"""
        article = Article(title='foo', body='bar')
        article.full_clean()
        self.assertEqual(article.title, 'foo')
        self.assertEqual(article.body, 'bar')

        article.save()
        article = Article.objects.get(pk=article.pk)
        self.assertEqual(article.title, 'foo')
        self.assertEqual(article.body, 'bar')

    def test_modification(self):
        """blogs.tests.testapp.Article: modification works correctly"""
        article = Article(title='foo', body='bar')
        article.full_clean()
        article.save()

        article.title = 'foofoo'
        article.body = 'barbar'
        article.full_clean()
        article.save()
        article = Article.objects.get(pk=article.pk)
        self.assertEqual(article.title, 'foofoo')
        self.assertEqual(article.body, 'barbar')

    def test_validation(self):
        """blogs.tests.testapp.Article: validation works correctly"""
        from django.core.exceptions import ValidationError
        article = Article(title='foo', body='bar')
        article.full_clean()
        article.save()

        article.title = ''
        self.assertRaises(ValidationError, article.full_clean)

        article.body = ''
        self.assertRaises(ValidationError, article.full_clean)

        article.title = '*' * 100
        self.assertRaises(ValidationError, article.full_clean)

    def test_deletion(self):
        """blogs.tests.testapp.Article: deletion works correctly"""
        article = Article(title='foo', body='bar')
        article.full_clean()
        article.save()

        num = Article.objects.all().count()
        article.delete()
        self.assertEqual(Article.objects.all().count(), num - 1)
