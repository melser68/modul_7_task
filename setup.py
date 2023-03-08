from setuptools import setup, find_namespace_packages

setup(name='sorting_files', 
      version='0.0.2',
      description='File sorter',
      url='https://github.com/melser68/modul_7_task',
      author='melser68',
      author_email='msprivate68@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts':['clean_folder = clean_folder.clean_folder:main']}      
       )