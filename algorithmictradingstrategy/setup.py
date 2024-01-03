from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 11',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='amirtraddingstrategy',
  version='0.0.1',
  description='A very basic tradding advisor',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',
  author='Amirhossein Beigi',
  author_email='amirhossein.beigi@bahcesehir.edu.tr',
  license='MIT',
  classifiers=classifiers,
  keywords='indicator',
  packages=find_packages(),
  install_requires=['']
)