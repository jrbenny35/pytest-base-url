from setuptools import setup

setup(name='pytest-base-url',
      use_scm_version=True,
      description='pytest plugin for URL based testing',
      long_description=open('README.rst').read(),
      author='Dave Hunt',
      author_email='dhunt@mozilla.com',
      url='https://github.com/pytest-dev/pytest-base-url',
      packages=['pytest_base_url'],
      install_requires=[
          'pytest>=2.7.3',
          'requests'],
      setup_requires=['setuptools_scm'],
      entry_points={'pytest11': ['base_url = pytest_base_url.plugin']},
      license='Mozilla Public License 2.0 (MPL 2.0)',
      keywords='py.test pytest base url mozilla automation',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Framework :: Pytest',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
          'Operating System :: POSIX',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: MacOS :: MacOS X',
          'Topic :: Software Development :: Quality Assurance',
          'Topic :: Software Development :: Testing',
          'Topic :: Utilities',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy'])
