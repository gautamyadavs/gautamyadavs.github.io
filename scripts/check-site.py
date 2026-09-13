"""Check the updated portfolio's local links, fragments, and image descriptions."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PAGES = [
    ROOT / 'index.html', ROOT / 'resume.html',
    *sorted((ROOT / 'work').glob('*.html')),
    ROOT / 'projects/equation.html', ROOT / 'projects/CTAT.html',
]


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.ids, self.links, self.errors = path, set(), [], []
        self.headings = 0
        self.feed(path.read_text())

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                self.errors.append(f'Duplicate id: {attrs["id"]}')
            self.ids.add(attrs['id'])
        if tag == 'h1':
            self.headings += 1
        if tag == 'img' and 'alt' not in attrs:
            self.errors.append('Image is missing alt text')
        for attribute in ('href', 'src'):
            if attribute in attrs:
                self.links.append(attrs[attribute])


errors = []
cache = {page: Page(page) for page in PAGES}
for path, page in list(cache.items()):
    errors.extend(f'{path.relative_to(ROOT)}: {error}' for error in page.errors)
    if page.headings != 1:
        errors.append(f'{path.name}: expected one h1, found {page.headings}')
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        target = (ROOT / unquote(url.path).lstrip('/') if url.path.startswith('/')
                  else path.parent / unquote(url.path)) if url.path else path
        target = target.resolve()
        if target.is_dir():
            target /= 'index.html'
        if not target.is_file():
            errors.append(f'{path.relative_to(ROOT)}: missing {link}')
        elif url.fragment and target.suffix == '.html':
            if target not in cache:
                cache[target] = Page(target)
            if unquote(url.fragment) not in cache[target].ids:
                errors.append(f'{path.relative_to(ROOT)}: missing fragment {link}')

if errors:
    raise SystemExit('\n'.join(errors))
print(f'Passed: {len(PAGES)} portfolio pages; local links, fragments, h1s, image descriptions.')
