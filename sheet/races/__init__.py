from os.path import dirname, basename, isfile, join
import glob
modules = glob.glob(join(dirname(__file__), "*.py"))
# Add __all__ variable that is the names of all files in this directory.
# Used to import all configs in views
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py') and not f.endswith('races.py')]

for current in __all__:
    name = "sheet.races." + current
    __import__(name)