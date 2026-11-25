#!/usr/bin/env python3
"""Calculate WCAG contrast for two already-resolved opaque sRGB colors."""
import argparse
import re


def color(value):
    if not re.fullmatch(r'#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?', value):
        raise argparse.ArgumentTypeError('expected an opaque sRGB color in #RGB or #RRGGBB form')
    digits = value[1:]
    if len(digits) == 3:
        digits = ''.join(c * 2 for c in digits)
    return tuple(int(digits[i:i + 2], 16) / 255 for i in (0, 2, 4))


def luminance(rgb):
    def linear(channel):
        return channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4
    return sum(weight * linear(channel) for weight, channel in zip((0.2126, 0.7152, 0.0722), rgb))


def contrast(first, second):
    light, dark = sorted((luminance(first), luminance(second)), reverse=True)
    return (light + 0.05) / (dark + 0.05)


def main():
    parser = argparse.ArgumentParser(description=__doc__, epilog=(
        'Inputs must be final rendered opaque colors, not unresolved CSS, transparency, gradients or images. '
        'A numeric result does not establish WCAG conformance or verify applicability and exceptions.'))
    parser.add_argument('foreground', type=color, help='foreground as #RGB or #RRGGBB')
    parser.add_argument('background', type=color, help='background as #RGB or #RRGGBB')
    args = parser.parse_args()
    ratio = contrast(args.foreground, args.background)
    print(f'Contrast ratio: {ratio:.6f}:1 (display rounded; comparisons use the unrounded ratio)')
    for label, threshold in [('normal text (4.5:1)', 4.5), ('large text (3:1)', 3.0),
                             ('applicable non-text information (3:1)', 3.0)]:
        print(f'{label}: {"meets" if ratio >= threshold else "below"} numeric threshold')
    print('Numeric comparison only: verify rendered colors, applicability, exceptions and user experience.')


if __name__ == '__main__':
    main()
