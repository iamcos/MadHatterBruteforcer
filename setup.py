from cx_Freeze import setup, Executable
executables = [
    Executable('selecting.py')
]

options = {
    'build_exe': {
        'includes': ['zlib',ServiceHandler', 'cx_Logging']
    }
}


setup(name='hello',
      version='0.1',
      description='Sample cx_Freeze script',
      executables=executables
      )