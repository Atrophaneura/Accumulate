configure_file(
  input: 'accumulate.in',
  output: 'accumulate',
  configuration: conf,
  install_dir: get_option('bindir')
)

configure_file(
  input: 'accumulate.in',
  output: 'local-accumulate',
  configuration: local_conf
)

configure_file(
  input: 'constants.py.in',
  output: 'constants.py',
  configuration: configuration_data({
    'APP_ID': APPLICATION_ID,
    'RELEASE_VER': meson.project_version(),
    'VERSION': meson.project_version() + VERSION_SUFFIX,
    'BUILD_TYPE': get_option('buildtype'),
    'PROJECT_URL': PROJECT_URL,
    'BUGTRACKER_URL': BUGTRACKER_URL,
    'HELP_URL': HELP_URL,
    'TRANSLATE_URL': TRANSLATE_URL
  }),
  install: true,
  install_dir: PY_INSTALLDIR.get_install_dir() / 'accumulate',
)

launcher = join_paths(meson.project_build_root(), 'accumulate', 'local-' + meson.project_name())

run_target('run',
  command: [launcher]
)

# Install sources
accumulate_sources = [
  '__init__.py',
  'main.py',
  'window.py',
  'client.py',
]

PY_INSTALLDIR.install_sources(accumulate_sources, subdir: 'accumulate')