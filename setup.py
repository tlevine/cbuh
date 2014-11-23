from distutils.core import setup

setup(name='cbuh',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Tom\'s contact list',
      url='https://github.com/tlevine/cbuh',
      packages=['cbuh'],
      install_requires = [
          'xapian',
      ],
      scripts = [
          'bin/cbuh',
      ],
      tests_require = ['nose'],
      version='0.0.1',
      license='AGPL',
      classifiers=[
          'Programming Language :: Python :: 3.4',
      ],
)
