# vim: set fileencoding=utf8:
from setuptools import setup, find_packages

version = '0.1.0'

def read(filename):
    import os.path
    return open(os.path.join(os.path.dirname(__file__), filename)).read()
setup(
    name="django-packageutils",
    version=version,
    description = "Utility collection of Django package",
    long_description=read('README.rst'),
    classifiers = [
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords = "django package utilty",
    author = "Alisue",
    author_email = "lambdalisue@hashnote.net",
    url=r"https://github.com/lambdalisue/django-packageutils",
    download_url = r"https://github.com/lambdalisue/django-packageutils/tarball/master",
    license = 'MIT',
    packages = find_packages(),
    include_package_data = True,
    install_requires=[
        'distribute',
        'setuptools-git',
    ],
    test_suite='tests.runtests.runtests',
    tests_require=[
        'django>=1.3',
        'PyYAML',
        'django-author',
    ],
)
