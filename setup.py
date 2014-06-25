from setuptools import setup

setup(name='putils',
      version='0.1',
      zip_safe=False,
      author='Deep',
      author_email='deep@mayalogy.com',
      description='Basic python utilities package',
      package_dir={'':'src/main/py'},
      py_modules=['putils_stats', 'putils_misc', 'putils_io'])
