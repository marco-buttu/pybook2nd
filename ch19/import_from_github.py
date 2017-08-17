import importlib
import requests
import sys
import types

from importlib.machinery import ModuleSpec


class GitImporter:

    def __init__(self):
        self.module_content = ''

    def find_spec(self, name, path, target=None):
        print('In find_spec()')
        response = requests.get(
            'https://raw.githubusercontent.com/'
            'marco-buttu/pybook2nd/master/ghmodule.py',
             verify=False)

        if response.text:
            self.module_content = response.text
            return ModuleSpec(name, self)

    def create_module(self, spec):
        print('In create_module()')
        module = types.ModuleType(spec.name)
        sys.modules[spec.name] = module
        return module

    def exec_module(self, module):
        print('In exec_module()')
        exec(self.module_content, module.__dict__)


requests.packages.urllib3.disable_warnings()
sys.meta_path.append(GitImporter())
