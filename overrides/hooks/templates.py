
from __future__ import annotations

import posixpath
import re

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import File, Files
from mkdocs.structure.pages import Page
from re import Match

# -----------------------------------------------------------------------------
# Hooks
# -----------------------------------------------------------------------------

# @todo
def on_page_markdown(
    markdown: str, *, page: Page, config: MkDocsConfig, files: Files
):

    # Replace callback
    def replace(match: Match):
        type, args = match.groups()
        args = args.strip('|')
        if type == "nbt":        return nbt(args, page, files)
        elif type == "json":     return json(args, page, files)
        elif type == "samp":     return samp(args)

        # Otherwise, raise an error
        raise RuntimeError(f"Unknown template name: {type}")

    # Find and replace all external asset URLs in current page
    return re.sub(
        r"\{\{([^|}]+)(.*?)}}",
        replace, markdown, flags = re.I | re.M
    ).replace(r"{/{", r"{{")

# -----------------------------------------------------------------------------
# Helper functions
# -----------------------------------------------------------------------------

def samp(type: str):
    return f'<samp>{type}</samp>'

# -----------------------------------------------------------------------------

# Resolve path of file relative to given page - the posixpath always includes
# one additional level of `..` which we need to remove
def _resolve_path(path: str, page: Page, files: Files):
    path, anchor, *_ = f"{path}#".split("#")
    path = _resolve(files.get_file_from_path(path), page)
    return "#".join([path, anchor]) if anchor else path

# Resolve path of file relative to given page - the posixpath always includes
# one additional level of `..` which we need to remove
def _resolve(file: File, page: Page):
    path = posixpath.relpath(file.src_uri, page.file.src_uri)
    return posixpath.sep.join(path.split(posixpath.sep)[1:])

# -----------------------------------------------------------------------------
# Template functions
# -----------------------------------------------------------------------------

def parse_arg(arg: str, key: str):
    if arg.startswith(key):
        if len(arg) == len(key):
            return True
        if arg[len(key)] == "=":
            return arg[len(key) + 1:]
    return None

def nbt(args: str, page: Page, files: Files):
    splitted = args.split("|")
    if len(splitted) == 1:
        return build_nbt_key(args, "", page, files)
    type, *nextArgs = splitted
    key = nextArgs[0] if nextArgs else ""
    required = False
    existonsave = False
    if len(nextArgs) > 1:
        for arg in nextArgs[1:]:
            if parse_arg(arg, "required") and parse_arg(arg, "required") != "0":
                required = True
            if parse_arg(arg, "existonsave") and parse_arg(arg, "existonsave") != "0":
                existonsave = True
    return build_nbt_key(type, key, required, existonsave, page, files)

def build_nbt_key(icon: str, key: str, required: bool, existonsave: bool, page: Page, files: Files):
    href = _resolve_path(f"help/docs/contributing.md#{icon}", page, files)

    tagNames = {
        "end": "终末",
        "byte": "字节",
        "short": "短整型",
        "int": "整型",
        "long": "长整型",
        "float": "单精度浮点数",
        "double": "双精度浮点数",
        "byte-array": "字节型数组",
        "string": "字符串",
        "list": "列表",
        "compound": "复合",
        "int-array": "整型数组",
        "long-array": "长整型数组",
        "boolean": "布尔值",
    }

    text = samp(key) if key else ""

    indicator = f"<span class=\"nbt-indicators\" style=\"width:0.312em;\">"
    if required or existonsave:
        if required:
            indicator += "<span class=\"nbt-required minetip\" title=\"此项为必选项\">&#42</span>"
            if existonsave:
                indicator += "<br>"
        if existonsave:
            indicator += "<span class=\"nbt-existed minetip\" title=\"存储时必存在\">&#42</span>"
    indicator += "</span>"

    return f"[:nbt-tag-{icon}:]({href} '{tagNames.get(icon, "")}标签'){indicator}**{text}**"

def json(args: str, page: Page, files: Files):
    splitted = args.split("|")
    if len(splitted) == 1:
        return build_json_key(args, "", page, files)
    type, *nextArgs = splitted
    key = nextArgs[0] if nextArgs else ""
    required = False
    if len(nextArgs) > 1:
        for arg in nextArgs[1:]:
            if parse_arg(arg, "required") and parse_arg(arg, "required") != "0":
                required = True
    return build_json_key(type, key, required, page, files)

def build_json_key(icon: str, key: str, required: bool, page: Page, files: Files):
    href = _resolve_path(f"help/docs/contributing.md#{icon}", page, files)

    tagNames = {
        "null": "空",
        "int": "整型",
        "float": "浮点数",
        "string": "字符串",
        "array": "数组",
        "object": "对象",
        "boolean": "布尔值",
    }

    text = samp(key) if key else ""

    indicator = f"<span class=\"nbt-indicators\" style=\"width:0.312em;\">"
    if required:
        indicator += "<span class=\"nbt-required minetip\" title=\"此项为必选项\">&#42</span>"
    indicator += "</span>"

    return f"[:json-field-{icon}:]({href} '{tagNames.get(icon, "")}'){indicator}**{text}**"
