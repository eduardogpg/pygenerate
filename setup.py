from distutils.core import setup

setup(
    name = 'pybose',
    packages = ['pybose'],
    version = '0.3',
    license='MIT',
    description = 'Python generator project',
    author = 'Eduardo Ismael García Pérez',
    author_email = 'eduardo78d@gmail.com',
    url = 'https://github.com/eduardogpg/pybose',
    download_url = 'https://github.com/eduardogpg/pybose/archive/refs/tags/0.3.tar.gz',
    keywords = ['Python', 'Generator', 'Project'],
    install_requires=[
        'click'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.8',
    ],
)