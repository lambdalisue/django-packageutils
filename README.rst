Django packageutils
======================================
This is a utility collection for packaging Django App. The following features
are available.

1.  Unittest utility for running with setup.py

2.  Unittest utility for dynamically adding models only used in the test

3.  Automatically create user within syncdb command

How to install
----------------------------
Use pip comand or easy_install::

    pip install django-packageutils

Directory tree assumed
--------------------------------------------
::

    django-packagename
        +- setup.py
        +- RELEASE-VERSION          # used for git versioning
        +- packagename              # your package
            +- __init__.py
            +- models.py            # or whatever
            +- tests
                +- __init__.py
                +- test_models.py   # or whatever
                +- testapp          # App only required in tests of this package 
                    +- __init__.py
                    +- models.py
        +- test                     # django project for testing
            +- __init__.py
            +- settings.py
            +- manage.py
            +- urls.py
            +- runtests.py          # for running test with setup.py

Unittest utility for running with setup.py
------------------------------------------------------------------------------------
Write your ``runtests.py`` in your package directory as::

    import os
    from packageutils.test import get_package_runner
    from packageutils.test import run_tests

    def runtests(verbosity=1, interactive=True):
        package_dir = os.path.dirname(__file__)
        test_runner = get_package_runner(package_dir, verbosity, interactive)
        run_tests(test_runner, ['some_application_name'])

    if __name__ == '__main__':
        runtests()

Add test suite to your ``setup.py`` as::

    setup(
        # ... some configures
        install_requires = [
            'distribute',           # recommended
            'setuptools-git',       # recommended
            'django-packageutils',  # required
            # and some other requires
        ],
        test_suite = 'tests.runtests.runtests',
        test_require = [
            'django',
        ],
    )
    
Then execute the following command::

    python setup.py test

Unittest utility for dynamically adding models only used in the test
----------------------------------------------------------------------------------------------------------------------------------------
With Django default TestCase, you cannot add required models within test. Sometime you need extra models for testing your django package
then you can use ``AppTestCase`` as::

    from packageutils.testcase import AppTestCase
    from testapp.models import Article

    class TestAppTestCase(AppTestCase):
        # Apps only required in this test
        installed_apps = [
            'packagename.tests.testapp',
        ]
        # Middlewares only required in this test
        middleware_classes = [
            'testapp.middleware.SomeMiddlewareRequired',
        ]

        def test_creation(self):
            article = Article.objects.create(title='foo')
            assert Article.objects.filter(title='foo').exists()

Automatically create user within syncdb command
----------------------------------------------------------------------------------------------
Add ``packageutils.syncdb.autouser`` in ``INSTALLED_APPS`` then admin user is created automatically
within syncdb command (password will be set as 'admin')

