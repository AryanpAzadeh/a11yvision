#!/usr/bin/env python3
"""Validate rule documents and produce a deterministic metadata manifest."""
import argparse
import json
import re
import sys
from pathlib import Path

try:
    import yaml
    from jsonschema import Draft202012Validator
except ImportError:
    sys.exit('Install the optional maintenance dependencies: pip install -r requirements-maintenance.txt')

ROOT = Path(__file__).resolve().parent.parent
SECTIONS = ['User impact', 'Requirement', 'Applies to', 'Does not apply / exceptions',
            'Failure patterns', 'Passing patterns', 'Evaluation procedure', 'Outcome rules',
            'Remediation guidance', 'Unsafe or misleading fixes', 'Verification',
            'Framework notes', 'Test fixtures', 'References']


class UniqueLoader(yaml.SafeLoader):
    pass


def mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str):
            raise ValueError('metadata keys must be strings')
        if key in result:
            raise ValueError(f'duplicate YAML key: {key}')
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)


def collect(root):
    errors, records, seen = [], [], {}
    schema_path = root / 'schemas/rule.schema.json'
    try:
        schema = json.loads(schema_path.read_text(encoding='utf-8'))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)
        expected = set(schema['properties']['id']['enum'])
    except (OSError, ValueError, KeyError) as exc:
        return [], [f'{schema_path}: invalid schema: {exc}']
    except Exception as exc:
        return [], [f'{schema_path}: invalid schema: {exc}']

    rule_dir = root / 'references/rules'
    for path in sorted(rule_dir.rglob('*.md')):
        relative = path.relative_to(root).as_posix()
        try:
            content = path.read_text(encoding='utf-8')
            parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
            if len(parts) != 3 or parts[0].strip():
                raise ValueError('missing or malformed YAML front matter')
            metadata = yaml.load(parts[1], Loader=UniqueLoader)
            if not isinstance(metadata, dict):
                raise ValueError('front matter must be a mapping')
        except (OSError, UnicodeError, ValueError, yaml.YAMLError) as exc:
            errors.append(f'{relative}: {exc}')
            continue
        issues = sorted(validator.iter_errors(metadata), key=lambda e: list(map(str, e.absolute_path)))
        for issue in issues:
            where = '.'.join(map(str, issue.absolute_path)) or 'metadata'
            errors.append(f'{relative}: {where}: {issue.message}')
        ident = metadata.get('id')
        if isinstance(ident, str):
            if ident in seen:
                errors.append(f'{relative}: duplicate ID {ident}, also in {seen[ident]}')
            else:
                seen[ident] = relative
            if path.stem != ident:
                errors.append(f'{relative}: filename must match ID {ident}')
        if metadata.get('status') == 'active':
            heading = f"# {ident} — {metadata.get('title')}"
            top = re.findall(r'^# (.+)$', parts[2], re.MULTILINE)
            if top != [heading[2:]]:
                errors.append(f'{relative}: expected one title heading matching ID and title')
            headings = re.findall(r'^## (.+)$', parts[2], re.MULTILINE)
            if headings != SECTIONS:
                errors.append(f'{relative}: required sections missing, extra or out of order')
            if metadata.get('scope') == 'conformance' and 'https://www.w3.org/' not in parts[2]:
                errors.append(f'{relative}: conformance rule needs a W3C reference')
        if not issues:
            records.append({'path': relative, **metadata})
    for ident in sorted(expected - set(seen)):
        errors.append(f'missing rule: {ident}')
    for ident in sorted(set(seen) - expected):
        errors.append(f'unexpected rule: {ident}')
    return sorted(records, key=lambda item: item['id']), errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT, help='repository root (default: script parent)')
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('validate', help='validate schema, rule metadata and required sections')
    manifest = sub.add_parser('manifest', help='write deterministic JSON manifest to stdout')
    manifest.add_argument('--check', type=Path, help='compare output with an existing manifest')
    args = parser.parse_args(argv)
    records, errors = collect(args.root.resolve())
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    if args.command == 'validate':
        print(f'Validated {len(records)} rules; no structural errors found.')
    else:
        result = json.dumps({'rules': records}, ensure_ascii=False, indent=2) + '\n'
        if args.check:
            try:
                existing = args.check.read_text(encoding='utf-8')
            except OSError as exc:
                print(f'{args.check}: {exc}', file=sys.stderr)
                return 1
            if existing != result:
                print(f'{args.check}: manifest is out of date', file=sys.stderr)
                return 1
            print(f'{args.check}: manifest is up to date')
        else:
            sys.stdout.write(result)
    return 0


if __name__ == '__main__':
    sys.exit(main())
