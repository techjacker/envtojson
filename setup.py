from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='envtojson',
    version='0.0.1',
    description='Write environment variables to a file in JSON format.',
    long_description=long_description,
    url='https://github.com/techjacker/envtojson',
    license='MIT',
    author='Andrew Griffiths',
    author_email='mail@andrewgriffithsonline.com',
    packages=['envtojson'],
    entry_points={
        'console_scripts': [
            'envtojson = envtojson.envtojson:main'
        ]
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Text Processing :: Markup'
    ],
)
