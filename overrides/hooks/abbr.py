from markdown.extensions.abbr import AbbrPreprocessor


def _generate_pattern(self, text: str) -> str:
    """
    Given a string, returns an regex pattern to match that string.
    """
    chars = list(text)
    for i in range(len(chars)):
        chars[i] = r'[%s]' % chars[i]
    return r'(?P<abbr>%s)' % (r''.join(chars))


AbbrPreprocessor._generate_pattern = _generate_pattern
