
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
        elif type == "file":     return file(args, page, files)
        elif type == "samp":     return samp(args)
        elif type == "video":    return video(args)

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
        return build_nbt_key(args, "", False, False, page, files)
    type, *nextArgs = splitted
    key = nextArgs[0]
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
            indicator += "<span class=\"nbt-required\" title=\"此项为必选项\">&#42</span>"
            if existonsave:
                indicator += "<br>"
        if existonsave:
            indicator += "<span class=\"nbt-existed\" title=\"存储时必存在\">&#42</span>"
    indicator += "</span>"

    return f"[:nbt-tag-{icon}:]({href} '{tagNames.get(icon, "")}标签'){indicator}**{text}**"

def json(args: str, page: Page, files: Files):
    splitted = args.split("|")
    if len(splitted) == 1:
        return build_json_key(args, "", False, page, files)
    type, *nextArgs = splitted
    key = nextArgs[0]
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
        indicator += "<span class=\"nbt-required\" title=\"此项为必选项\">&#42</span>"
    indicator += "</span>"

    return f"[:json-field-{icon}:]({href} '{tagNames.get(icon, "")}'){indicator}**{text}**"

def file(args: str, page: Page, files: Files):
    splitted = args.split("|")
    if len(splitted) == 1:
        splitted = args.split(".")
        if len(splitted) == 1:
            return build_file_key("file", args, False, page, files)
        else:
            if splitted[0] == "":
                return build_file_key(splitted[-1], args, True, page, files)
            else:
                return build_file_key(splitted[-1], args, False, page, files)
    key, *nextArgs = splitted
    type = nextArgs[0]
    hide = False
    if key.split(".")[0] == "":
        hide = True
    if len(nextArgs) > 1:
        for arg in nextArgs[1:]:
            if parse_arg(arg, "hide") and parse_arg(arg, "hide") != "0":
                hide = True
            else:
                hide = False
    return build_file_key(type, key, hide, page, files)

def build_file_key(icon: str, key: str, hide: bool, page: Page, files: Files):
    href = _resolve_path(f"help/docs/contributing.md#{icon}", page, files)

    typeNames = {
        "file": "文件",
        "text": "文本",
        "txt": "纯文本",
        "doc": "DOC文档",
        "docx": "DOCX文档",
        "wps": "WPS文档",
        "image": "图片",
        "png": "PNG图片",
        "jpg": "JPG图片",
        "tga": "TGA图片",
        "gif": "GIF图片",
        "script": "脚本",
        "js": "JavaScript脚本",
        "py": "Python脚本",
        "lua": "Lua脚本",
        "php": "PHP脚本",
        "sh": "Shell脚本",
        "archive": "压缩包",
        "zip": "ZIP压缩包",
        "rar": "RAR压缩包",
        "gz": "GZ压缩包",
        "video": "视频",
        "mov": "MOV视频",
        "flv": "FLV视频",
        "avi": "AVI视频",
        "wmv": "WMV视频",
        "mp4": "MP4视频",
        "dat": "DAT视频",
        "audio": "音频",
        "wav": "WAV音频",
        "ogg": "OGG音频",
        "fsb": "FSB音频",
        "mp3": "MP3音频",
        "log": "日志",
        "db": "存档数据库",
        "bin": "二进制编码文件",
        "apk": "Android应用程序包",
        "apks": "Android应用程序包",
        "xapk": "Android应用程序包",
        "ipa": "苹果系统应用程序包",
        "json": "JSON数据文件",
        "xml": "可扩展标记语言文件",
        "html": "超文本标记语言文件",
        "css": "层叠样式表文件",
        "java": "Java源文件",
        "cpp": "C++源文件",
        "glsl": "OpenGL着色器文件",
        "hlsl": "HLSL着色器文件",
        "xls ": "XLS表格",
        "xlsx": "XLSX表格",
        "ppt": "PPT演示文稿",
        "pptx": "PPTX演示文稿",
        "pdf": "可携带文档格式文件",
        "exe": "可执行程序",
        "data": "数据",
        "ttf": "字体",
        "dex": "Dalvik可执行文件",
        "arsc": "Android应用程序资源文件",
        "mcpack": "Minecraft基岩版附加包",
        "mcaddon": "Minecraft基岩版附加包集合",
        "mcworld": "Minecraft基岩版世界存档",
        "mctemplate": "Minecraft基岩版世界模板",
        "mcstructure": "Minecraft基岩版结构文件",
        "mcfunction": "Minecraft基岩版函数文件",
        "lang": "Minecraft基岩版语言文件",
        "material": "Minecraft基岩版材质文件",
        "h": "C++头文件",
        "c": "C源文件",
        "wikitext": "维基文本",
        "jar": "Java归档",
        "smali": "Dalvik指令集",
        "class": "Java字节码文件",
        "lib": "静态链接库",
        "folder": "文件夹",
        "dll": "动态链接库",
        "bak": "备份",
        "kt": "Kotlin文件",
        "cfg": "配置文件",
        "nbt": "Minecraft二进制命名标签",
        "mcdat": "Minecraft基岩版存档数据",
        "mca": "Minecraft基岩版区域文件",
        "mcr": "Minecraft基岩版世界片区文件",
        "mcmeta": "Minecraft基岩版资源包配置文件",
        "mcgame": "Minecraft基岩版游戏备份数据",
        "mcproject": "Minecraft基岩版项目",
        "tmp": "临时文件",
        "bat": "Bat脚本",
        "ts": "TypeScript脚本",
        "svg": "SVG矢量图",
        "md": "MarkDown文档",
        "so": "Linux共享对象库文件",
        "tgz": "TGZ压缩包",
        "webm": "WEBM视频",
    }

    text = samp(key) if key else ""

    inject = ""
    if hide:
        inject = "style=\"opacity:0.5;\""
    indicator = f"<span class=\"nbt-indicators\" style=\"width:0.312em;\">"
    indicator += "</span>"

    return f":file-type-{icon}:{{ title=\"{typeNames.get(icon, "")}\" {inject} }}{indicator}**{text}**"

def video(args: str):
    splitted = args.split("|")
    if len(splitted) != 2:
        raise RuntimeError(f"video template wrong: {type}")
    type, id = splitted
    if type == "youtube":
        return build_youtube(id)
    return ""

def build_youtube(id):
    return f"<div style=\"max-width: 700px; aspect-ratio: 16 / 9;\"><iframe src=\"https://www.youtube-nocookie.com/embed/{id}\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen=\"\" style=\"\width: 100%; height: 100%;\"></iframe></div>"
