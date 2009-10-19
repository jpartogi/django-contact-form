from distutils.core import setup

app_name = 'contact_form'

setup(
    name='django-contact-form',
    version='0.9.0',
    packages=[app_name, '%s.templatetags' % app_name],
    package_data = {app_name: ['templates/%s/*.html' % app_name]},
    author = 'Joshua Partogi',
    author_email = 'joshua.partogi@gmail.com',
    url = 'http://github.com/scrum8/django-contact-form',
    download_url = 'http://github.com/scrum8/django-contact-form/downloads',

    license = "BSD License",
    keywords = "django contact form",
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms = ['any'],
)