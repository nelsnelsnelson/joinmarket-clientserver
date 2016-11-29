from setuptools import setup


setup(name='joinmarketclient',
      version='0.1',
      description='Joinmarket client library for Bitcoin coinjoins',
      url='http://github.com/AdamISZ/joinmarket-clientserver/jmclient',
      author='Adam Gibson',
      author_email='ekaggata@gmail.com',
      license='GPL',
      packages=['jmclient'],
      install_requires=['joinmarketbase'],
      zip_safe=False)
