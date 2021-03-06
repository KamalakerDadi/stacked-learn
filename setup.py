#! /usr/bin/env python
import os
from setuptools import setup


descr = """A scikit-learn based library for prediction stacking."""
DISTNAME = 'stlearn'
DESCRIPTION = 'A scikit-learn based library for prediction stacking.'
LONG_DESCRIPTION = descr
MAINTAINER = 'Mehdi Rahim'
MAINTAINER_EMAIL = 'rahim.mehdi@gmail.com'
URL = 'https://github.com/mrahim/stacked-learn'
LICENSE = 'new BSD'
DOWNLOAD_URL = 'https://github.com/mrahim/stacked-learn'
VERSION = '0.alpha'


def configuration(parent_package='', top_path=None):
    if os.path.exists('MANIFEST'):
        os.remove('MANIFEST')

    from numpy.distutils.misc_util import Configuration
    config = Configuration(None, parent_package, top_path)

    config.add_subpackage('stlearn')

    return config


if __name__ == "__main__":
    setup(configuration=configuration,
          name=DISTNAME,
          maintainer=MAINTAINER,
          include_package_data=True,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          long_description=LONG_DESCRIPTION,
          test_suite="nose.collector",  # for python setup.py test
          zip_safe=False,  # the package can run out of an .egg file
          classifiers=[
              'Intended Audience :: Science/Research',
              'Intended Audience :: Developers',
              'License :: OSI Approved',
              'Programming Language :: C',
              'Programming Language :: Python',
              'Topic :: Software Development',
              'Topic :: Scientific/Engineering',
              'Operating System :: Microsoft :: Windows',
              'Operating System :: POSIX',
              'Operating System :: Unix',
              'Operating System :: MacOS'],)
