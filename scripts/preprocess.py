import re
import os
import sys


def convert_admonitions(content, depth=0):
    colon_count = 3 + depth
    close = ":" * colon_count

    while True:
        pattern = r"^([ ]*)!!!\s+(.+?)$\n((?:(?:^\1    .*|^\1[ ]*)$(?:\n|$))*)"
        match = re.search(pattern, content, re.MULTILINE)
        if not match:
            break

        def replacer(m, cc=close, d=depth):
            indent = m.group(1)
            raw = m.group(2).strip()
            body = m.group(3)

            body = re.sub(
                r"^" + re.escape(indent) + r"    ", indent, body, flags=re.MULTILINE
            )
            body = re.sub(
                r"^" + re.escape(indent) + r"[ ]*$", indent, body, flags=re.MULTILINE
            )
            body = convert_admonitions(body, d + 1)

            parts = raw.split(None, 1)
            type_ = parts[0]
            title = parts[1] if len(parts) > 1 else None

            result = f"\n{indent}{cc} {{.admonition .{type_}}}\n"
            if title:
                result += f"{indent}**{title}**\n\n"
            result += body
            if not result.endswith("\n"):
                result += "\n"
            result += f"{indent}{cc}\n"
            return result

        content = re.sub(pattern, replacer, content, flags=re.MULTILINE)
    return content


def strip_mpe_extras(content):
    content = re.sub(r"\{[^}]*ignore[^}]*\}", "", content)
    content = re.sub(
        r"<!--\s*code_chunk_output\s*-->.*?<!--\s*/code_chunk_output\s*-->",
        "",
        content,
        flags=re.DOTALL,
    )
    content = re.sub(r'<!--\s*@import\s+"\[TOC\].*?-->', "", content)
    return content


def preprocess(content, source_dir, output_root):
    content = convert_admonitions(content)

    def resolve_path(path):
        full = os.path.normpath(os.path.join(source_dir, path))
        if not os.path.exists(full):
            return None
        return full

    def resolve_image(path):
        full = resolve_path(path)
        if full:
            return "![](" + os.path.relpath(full, output_root) + ")"
        return ""

    def inline_markdown(path):
        full = resolve_path(path)
        if full and os.path.isfile(full):
            with open(full, "r", encoding="utf-8") as f:
                return preprocess(f.read(), os.path.dirname(full), output_root)
        return ""

    def handle_import(m):
        prefix = m.group(1) or ""
        path = m.group(2)
        if path.lower().endswith(".md"):
            result = inline_markdown(path)
            if prefix:
                lines = result.rstrip("\n").split("\n")
                result = "\n".join(prefix + line for line in lines) + "\n"
            return result
        elif path.lower().endswith(".png"):
            return prefix + resolve_image(path)
        return m.group(0)

    content = re.sub(
        r'^((?:> )*)@import "([^"]+)"[ ]*$', handle_import, content, flags=re.MULTILINE
    )

    def handle_html_import(m):
        path = m.group(1).strip()
        if path.lower().endswith(".md"):
            return inline_markdown(path)
        elif path.lower().endswith(".png"):
            return resolve_image(path)
        return ""

    content = re.sub(r'<!--\s*@import\s+"([^"]+)"\s*-->', handle_html_import, content)

    content = strip_mpe_extras(content)
    return content


def main():
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    root = os.path.dirname(os.path.abspath(input_path))

    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    result = preprocess(content, root, root)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result)


if __name__ == "__main__":
    main()
