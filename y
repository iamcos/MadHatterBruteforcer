from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

base = 'Console'

executables = [
    Executable('rotator.py', base=base)
]

setup(name='RR',
      version = '1.2',
      description = '000',
      options = dict(build_exe = buildOptions),
      executables = executables)
