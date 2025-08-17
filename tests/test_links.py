import re
from pathlib import Path

# Regex to find links like ](./path#fragment)
LINK_RE = re.compile(r"\]\((\.\/[^)#\s]+)(?:#([^\)\s]+))?\)")


def slugify(text: str) -> str:
    """Create a GitHub-style anchor slug from a heading."""
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"\s+", "-", text)
    return text

def heading_slugs(content: str) -> set[str]:
    slugs = set()
    for line in content.splitlines():
        m = re.match(r"^\s*#+\s+(.*)", line)
        if m:
            slugs.add(slugify(m.group(1)))
    return slugs


def test_local_links():
    root = Path(__file__).resolve().parents[1]
    markdown_files = root.rglob("*.md")
    errors = []

    for md_file in markdown_files:
        text = md_file.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            rel_path, fragment = match.groups()
            target = (md_file.parent / rel_path).resolve()
            if not target.exists():
                errors.append(f"{md_file}: missing file {rel_path}")
                continue
            if fragment:
                target_text = target.read_text(encoding="utf-8")
                if fragment.lower() not in heading_slugs(target_text):
                    errors.append(f"{md_file}: missing fragment {rel_path}#{fragment}")

    assert not errors, "Broken links:\n" + "\n".join(errors)
