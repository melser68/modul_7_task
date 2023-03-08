from setuptools import setup, find_namespace_packages

setup(name='sorting_files', 
      version='0.0.1',
      description='File sorter',
      url='https://github.com/melser68/modul_7_task',
      author='melser68',
      author_email='msprivate68@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts':['sortingfiles = sorting_files. sorting_files_2:first_procedure']}      
       )