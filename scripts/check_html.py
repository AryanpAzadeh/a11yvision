#!/usr/bin/env python3
"""Identify a small set of source-level accessibility review candidates in HTML."""
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
import sys


class Inspector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.findings = []
        self.document = None
        self.title_count = 0
        self.in_title = False
        self.title_text = []

    def add(self, rule, message, line=None):
        self.findings.append({'rule': rule, 'outcome': 'NEEDS_REVIEW', 'evidence': 'SOURCE',
                              'line': line if line is not None else self.getpos()[0], 'message': message})

    def handle_starttag(self, tag, attrs):
        pairs = dict(attrs)
        if tag == 'html':
            self.document = pairs
            if not (pairs.get('lang') or '').strip():
                self.add('AV-LNG-001', 'Document language is missing or empty in source; verify the rendered document and its actual language.')
        elif tag == 'title':
            self.title_count += 1
            self.in_title = True
        elif tag == 'img' and 'alt' not in pairs:
            self.add('AV-IMG-001', 'Image has no alt attribute. Review purpose and other possible naming mechanisms in context.')
        if (pairs.get('aria-hidden') or '').lower() == 'true':
            if tag in ('button', 'input', 'select', 'textarea') and 'disabled' not in pairs:
                self.add('AV-HID-001', 'A potentially focusable native control has aria-hidden; inspect its actual visibility and focusability.')
            elif tag == 'a' and 'href' in pairs:
                self.add('AV-HID-001', 'A potentially focusable link has aria-hidden; inspect its actual visibility and focusability.')
            elif pairs.get('tabindex') in ('0',):
                self.add('AV-HID-001', 'An element with tabindex=0 has aria-hidden; inspect its actual visibility and focusability.')

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title_text.append(data)

    def finish(self):
        if self.document is not None and (self.title_count == 0 or not ''.join(self.title_text).strip()):
            self.add('AV-TIT-001', 'Document title is missing or empty in source; inspect generated output and page purpose.', 1)


def main():
    parser = argparse.ArgumentParser(description=__doc__, epilog=(
        'A fragment or template may omit document metadata intentionally. Results are review candidates, '
        'not proof of violations or conformance. The parser does not render pages or execute scripts.'))
    parser.add_argument('paths', nargs='+', type=Path, help='HTML files to inspect (not directories)')
    args = parser.parse_args()
    reports, errors = [], []
    for path in args.paths:
        try:
            text = path.read_text(encoding='utf-8')
            inspector = Inspector()
            inspector.feed(text)
            inspector.close()
            inspector.finish()
            reports.append({'path': str(path), 'findings': inspector.findings})
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append(f'{path}: {exc}')
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 2
    print(json.dumps({'scope': 'source-only', 'files': reports,
                      'limitations': 'Review candidates only; no accessibility or WCAG conformance conclusion.'},
                     ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
