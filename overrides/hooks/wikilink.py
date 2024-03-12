
import re

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import File, Files
from mkdocs.structure.pages import Page
from re import Match


# -----------------------------------------------------------------------------
# Hooks
# -----------------------------------------------------------------------------

def on_page_markdown(
    markdown: str, *, page: Page, config: MkDocsConfig, files: Files
):

    # Replace callback
    def replace(match: Match):
        page_name, name = match.groups()
        if name != "":
            name = name.replace("|", "")
            if name == "":
                label = page_name.split(":")[-1].split(" (")[0].split("（")[0]
            else:
                label = name
        else:
            label = page_name
        return f'<a href="https://wiki.mcbe-dev.net/p/{page_name}" class="wikilink">{label}</a>'

    # Find and replace all external asset URLs in current page
    return re.sub(
        r"\[\[(.+?)((?:\|.*?)?)\]\]",
        replace, markdown, flags = re.I | re.M
    ).replace(r"[|[", r"[[")