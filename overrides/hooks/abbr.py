from markdown.extensions.abbr import AbbrPreprocessor, AbbrExtension
from markdown.treeprocessors import Treeprocessor
from markdown.util import AtomicString
import re
import xml.etree.ElementTree as etree
from markdown import Markdown

def _generate_pattern(self, text: str) -> str:
    """
    Given a string, returns an regex pattern to match that string.
    """
    chars = list(text)
    for i in range(len(chars)):
        chars[i] = r'[%s]' % chars[i]
    return r'(?P<abbr>%s)' % (r''.join(chars))


AbbrPreprocessor._generate_pattern = _generate_pattern



class AbbrTreeprocessor(Treeprocessor):
    """ Replace abbreviation text with `<abbr>` elements. """

    def __init__(self, md: Markdown | None = None, abbrs: dict | None = None):
        self.abbrs: dict = abbrs if abbrs is not None else {}
        self.RE: re.RegexObject | None = None
        super().__init__(md)

    def iter_element(self, el: etree.Element, parent: etree.Element | None = None) -> None:
        ''' Recursively iterate over elements, run regex on text and wrap matches in `abbr` tags. '''
        for child in reversed(el):
            self.iter_element(child, el)
        if text := el.text:
            for m in reversed(list(self.RE.finditer(text))):
                if self.abbrs[m.group(0)]:
                    abbr = etree.Element('abbr', {'title': self.abbrs[m.group(0)]})
                    abbr.text = AtomicString(m.group(0))
                    abbr.tail = text[m.end():]
                    el.insert(0, abbr)
                    text = text[:m.start()]
            el.text = text
        if parent is not None and el.tail:
            tail = el.tail
            index = list(parent).index(el) + 1
            for m in reversed(list(self.RE.finditer(tail))):
                abbr = etree.Element('abbr', {'title': self.abbrs[m.group(0)]})
                abbr.text = AtomicString(m.group(0))
                abbr.tail = tail[m.end():]
                parent.insert(index, abbr)
                tail = tail[:m.start()]
            el.tail = tail

    def run(self, root: etree.Element) -> etree.Element | None:
        ''' Step through tree to find known abbreviations. '''
        if not self.abbrs:
            # No abbreviations defined. Skip running processor.
            return
        # Build and compile regex
        abbr_list = list(self.abbrs.keys())
        abbr_list.sort(key=len, reverse=True)
        # 构建新的正则表达式，支持单词边界和汉字边界
        pattern = (
            r'(?:\b|(?<=[\u4e00-\u9fff]))'  # 前边界：单词边界 或 汉字
            + r'(?:' + '|'.join(re.escape(key) for key in abbr_list) + r')'  # 缩写
            + r'(?:\b|(?=[\u4e00-\u9fff]))'  # 后边界：单词边界 或 汉字
        )
        self.RE = re.compile(pattern)
        # Step through tree and modify on matches
        self.iter_element(root)

primalExtendMarkdown = AbbrExtension.extendMarkdown

def extendMarkdown(self, md):
    """ Insert `AbbrTreeprocessor` and `AbbrBlockprocessor`. """
    primalExtendMarkdown(self, md)
    md.treeprocessors.deregister('abbr')
    md.treeprocessors.register(AbbrTreeprocessor(md, self.abbrs), 'abbr', 7)

AbbrExtension.extendMarkdown = extendMarkdown