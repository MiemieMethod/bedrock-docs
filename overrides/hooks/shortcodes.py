# Copyright (c) 2016-2024 Martin Donath <martin.donath@squidfunk.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

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
        args = args.strip()
        if type == "version":        return version(args, page, files)
        # elif type == "sponsors":     return _badge_for_sponsors(page, files)
        elif type == "flag":         return flag(args, page, files)
        elif type == "option":       return option(args)
        elif type == "setting":      return setting(args)
        elif type == "sortable":     return sortable(args)
        elif type == "samp":     return samp(args)
        elif type == "optional":     return _badge_for_optional(args, page, files)
        # elif type == "plugin":       return _badge_for_plugin(args, page, files)
        # elif type == "extension":    return _badge_for_extension(args, page, files)
        # elif type == "utility":      return _badge_for_utility(args, page, files)
        elif type == "example":      return _badge_for_example(args, page, files)
        elif type == "default":
            if   args == "none":     return _badge_for_default_none(page, files)
            elif args == "computed": return _badge_for_default_computed(page, files)
            else:                    return _badge_for_default(args, page, files)

        # Otherwise, raise an error
        raise RuntimeError(f"Unknown shortcode: {type}")

    # Find and replace all external asset URLs in current page
    return re.sub(
        r"<!-- md:(\w+)(.*?) -->",
        replace, markdown, flags = re.I | re.M
    ).replace(r"<!-/- md:", r"<!-- md:")

# -----------------------------------------------------------------------------
# Helper functions
# -----------------------------------------------------------------------------

# Create a flag of a specific type
def flag(args: str, page: Page, files: Files):
    type, *_ = args.split(" ", 1)
    if   type == "experimental":  return _badge_for_experimental(page, files)
    elif type == "required":      return _badge_for_required(page, files)
    elif type == "customization": return _badge_for_customization(page, files)
    elif type == "metadata":      return _badge_for_metadata(page, files)
    elif type == "multiple":      return _badge_for_multiple(page, files)
    elif type == "deprecated":    return _badge_for_deprecated(page, files)
    elif type == "china":         return _badge_for_china(page, files)
    raise RuntimeError(f"Unknown type: {type}")

# Create a linkable option
def option(type: str):
    _, *_, name = re.split(r"[.:]", type)
    return f"[`{name}`](#+{type}){{ #+{type} }}\n\n"

# Create a linkable setting - @todo append them to the bottom of the page
def setting(type: str):
    _, *_, name = re.split(r"[.*]", type)
    return f"`{name}` {{ #{type} }}\n\n[{type}]: #{type}\n\n"

def sortable(type: str):
    return f'<script src="https://unpkg.com/tablesort@5.3.0/dist/tablesort.min.js"></script><script>var tables = document.querySelectorAll("article table");new Tablesort(tables.item(tables.length - 1));</script>'

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

# Create badge
def _badge(icon: str, text: str = "", type: str = ""):
    classes = f"mdx-badge mdx-badge--{type}" if type else "mdx-badge"
    return "".join([
        f"<span class=\"{classes}\">",
        *([f"<span class=\"mdx-badge__icon\">{icon}</span>"] if icon else []),
        *([f"<span class=\"mdx-badge__text\">{text}</span>"] if text else []),
        f"</span>",
    ])

def _double_badge(icon: str, text1: str = "", text2: str = "", type: str = ""):
    classes = f"mdx-badge mdx-badge--{type}" if type else "mdx-badge"
    return "".join([
        f"<span class=\"{classes}\">",
        *([f"<span class=\"mdx-badge__text\">{text1}</span>"] if text1 else []),
        *([f"<span class=\"mdx-badge__icon\">{icon}</span>"] if icon else []),
        *([f"<span class=\"mdx-badge__text\">{text2}</span>"] if text2 else []),
        f"</span>",
    ])

# Create sponsors badge
def _badge_for_sponsors(page: Page, files: Files):
    icon = "material-heart"
    href = _resolve_path("sponsor.md", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} '仅赞助者')",
        type = "heart"
    )

# Create badge for version
def version(args: str, page: Page, files: Files):
    if len(args.split(" ")) == 1:
        return _badge_for_version(args, page, files)
    type, *nextArgs = args.split(" ")
    nextArgs = " ".join(nextArgs)
    if   type == "range":   return _badge_for_version_range(nextArgs, page, files)
    elif type == "command": return _badge_for_version_range(nextArgs, page, files, '命令版本')
    elif type == "engine":  return _badge_for_version_range(nextArgs, page, files, '最低引擎版本')
    elif type == "format":  return _badge_for_version_range(nextArgs, page, files, '格式版本')
    elif type == "game":    return _badge_for_version_range(nextArgs, page, files, '基游戏版本')
    raise RuntimeError(f"Unknown type: {type}")

def _badge_for_version(text: str, page: Page, files: Files):
    spec = text
    path = f"index.md#{spec}"

    # Return badge
    icon = "material-tag-outline"
    href = _resolve_path("help/docs/contributing.md#version", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} '最小版本')",
        text = f"[{text}]({_resolve_path(path, page, files)})" if spec else ""
    )

def _badge_for_version_range(args: str, page: Page, files: Files, iconText: str = "版本区间"):
    text1, text2, left, right, *_ = args.split(" ")
    spec1 = True
    spec2 = True
    if text1 == '*':
        spec1 = False
    if text2 == '*':
        spec2 = False

    if left == "true":
        text1 = f"`{text1}`≤"
    else:
        text1 = f"`{text1}`＜"
    if right == "true":
        text2 = f"≤`{text2}`"
    else:
        text2 = f"＜`{text2}`"

    # Return badge
    icon = "material-tag-check-outline"
    href = _resolve_path("help/docs/contributing.md#version", page, files)
    return _double_badge(
        icon = f"[:{icon}:]({href} '{iconText}')",
        text1 = f"{text1}" if spec1 else "",
        text2 = f"{text2}" if spec2 else ""
    )

# Create badge for version of Insiders
def _badge_for_version_insiders(text: str, page: Page, files: Files):
    spec = text.replace("insiders-", "")
    path = f"insiders/changelog/index.md#{spec}"

    # Return badge
    icon = "material-tag-heart-outline"
    href = _resolve_path("help/docs/contributing.md#version-insiders", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} '最小版本')",
        text = f"[{text}]({_resolve_path(path, page, files)})" if spec else ""
    )

# Create badge for feature
def _badge_for_optional(text: str, page: Page, files: Files):
    icon = "material-toggle-switch"
    href = _resolve_path("help/docs/contributing.md#optional", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} '可选')",
        text = text
    )

# Create badge for plugin
def _badge_for_plugin(text: str, page: Page, files: Files):
    icon = "material-floppy"
    href = _resolve_path("help/docs/contributing.md#plugin", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} '插件')",
        text = text
    )

# Create badge for extension
def _badge_for_extension(text: str, page: Page, files: Files):
    icon = "material-language-markdown"
    href = _resolve_path("help/docs/contributing.md#extension", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} 'Markdown扩展')",
        text = text
    )

# Create badge for utility
def _badge_for_utility(text: str, page: Page, files: Files):
    icon = "material-package-variant"
    href = _resolve_path("help/docs/contributing.md#utility", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} '第三方工具')",
        text = text
    )

# Create badge for example
def _badge_for_example(text: str, page: Page, files: Files):
    return "\n".join([
        _badge_for_example_download(text, page, files),
        _badge_for_example_view(text, page, files)
    ])

# Create badge for example view
def _badge_for_example_view(text: str, page: Page, files: Files):
    icon = "material-folder-eye"
    href = f"https://miemiemethod.github.io/bedrock-docs/examples/{text}/"
    return _badge(
        icon = f"[:{icon}:]({href} '查看示例')",
        type = "right"
    )

# Create badge for example download
def _badge_for_example_download(text: str, page: Page, files: Files):
    icon = "material-folder-download"
    href = f"https://miemiemethod.github.io/bedrock-docs/examples/{text}.zip"
    return _badge(
        icon = f"[:{icon}:]({href} '下载示例')",
        text = f"[`.zip`]({href})",
        type = "right"
    )

# Create badge for default value
def _badge_for_default(text: str, page: Page, files: Files):
    icon = "material-water"
    href = _resolve_path("help/docs/contributing.md#default", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} '默认值')",
        text = text
    )

# Create badge for empty default value
def _badge_for_default_none(page: Page, files: Files):
    icon = "material-water-outline"
    href = _resolve_path("help/docs/contributing.md#default", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} '默认值为空')"
    )

# Create badge for computed default value
def _badge_for_default_computed(page: Page, files: Files):
    icon = "material-water-check"
    href = _resolve_path("help/docs/contributing.md#default", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} '默认值由实时计算得到')"
    )

# Create badge for metadata property flag
def _badge_for_metadata(page: Page, files: Files):
    icon = "material-list-box-outline"
    href = _resolve_path("help/docs/contributing.md#metadata", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} '元数据属性')"
    )

# Create badge for required value flag
def _badge_for_required(page: Page, files: Files):
    icon = "material-alert"
    href = _resolve_path("help/docs/contributing.md#required", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} '必选')"
    )

# Create badge for customization flag
def _badge_for_customization(page: Page, files: Files):
    icon = "material-brush-variant"
    href = _resolve_path("help/docs/contributing.md#customization", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} '自定义')"
    )

# Create badge for multiple instance flag
def _badge_for_multiple(page: Page, files: Files):
    icon = "material-inbox-multiple"
    href = _resolve_path("help/docs/contributing.md#multiple-instances", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} '多态')"
    )

# Create badge for experimental flag
def _badge_for_experimental(page: Page, files: Files):
    icon = "material-flask-outline"
    href = _resolve_path("help/docs/contributing.md#experimental", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} '实验性')"
    )

# Create badge for deprecated flag
def _badge_for_deprecated(page: Page, files: Files):
    icon = "octicons-trash-24"
    href = _resolve_path("help/docs/contributing.md#deprecated", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} '已弃用')",
        type = "deprecated"
    )

# Create badge for china flag
def _badge_for_china(page: Page, files: Files):
    icon = "material-inbox-full"
    href = _resolve_path("help/docs/contributing.md#deprecated", page, files)
    return _badge(
        icon = f"[:{icon}:]({href} '中国版独有')",
        type = "china"
    )