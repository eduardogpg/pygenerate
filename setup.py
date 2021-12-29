from distutils.core import setup

setup(
    name = 'pylogi',
    packages = ['pylogi'],
    version = '0.4',
    license='MIT',
    description = 'Python generator project',
    author = 'Eduardo Ismael García Pérez',
    author_email = 'eduardo78d@gmail.com',
    url = 'https://github.com/eduardogpg/pybose',
    keywords = ['Python', 'Generator', 'Project'],
    install_requires=[
        'click'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.8',
    ],
)