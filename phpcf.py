import re

from base_linter import BaseLinter

CONFIG = {
    'language': 'phpcf',
    'executable': 'phpcf',
    'lint_args': ['check', '{filename}']
}


class Linter(BaseLinter):
    def parse_errors(self, view, errors, lines, errorUnderlines, violationUnderlines, warningUnderlines, errorMessages, violationMessages, warningMessages):
        for line in errors.splitlines():
            match = re.match(r'^(?P<error>.+?)\s+on\s+line\s+(?P<line>\d+)', line)

            if match:
                error, line = match.group('error'), match.group('line')
                self.add_message(int(line), lines, error, errorMessages)
