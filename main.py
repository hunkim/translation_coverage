import argparse
import sys
from os import listdir
from os.path import isfile, isdir, join
from string import ascii_letters

from reader import read_file_with_source_code
from report import report_coverage

print_que = []


def is_ascii(char):
    try:
        return ord(char) < 128
    except:
        return False


def trans_coverage_file(filename, ext_set=None):
    text_content, text_non_source_code = read_file_with_source_code(filename, ext_set)

    content_len = len(text_content)
    non_source_code_len = len(text_non_source_code)

    # Source code length will be added to 'others'
    # This is not plain english
    source_code_len = content_len - non_source_code_len

    words, others = 0, 0

    for c in text_non_source_code:
        if is_ascii(c):
            if c in ascii_letters:
                words += 1
        else:
            others += 1

    return words, others + source_code_len


def trans_coverage(depth, args, loc, ext_set=None, exclude_path=None):
    global print_que

    depth += 1

    # Exclude path
    rel_loc = loc[len(args.dir):]
    if exclude_path is not None and rel_loc.startswith(exclude_path):
        return 0, 0

    if isfile(loc):
        eng_count, noneng_count = trans_coverage_file(loc, ext_set)
    elif isdir(loc):
        eng_count, noneng_count = 0, 0

        for f in sorted(listdir(loc), reverse=True):
            full_file = join(loc, f)
            e_count, n_count = trans_coverage(depth, args, full_file, ext_set,
                                              exclude_path)

            eng_count += e_count
            noneng_count += n_count
    else:
        eng_count, noneng_count = 0, 0

    if eng_count is not 0 or noneng_count is not 0:
        out = report_coverage(depth, args, loc, eng_count, noneng_count)
        print_que.append(out)

    return eng_count, noneng_count


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='.',
                        help='directory to check translation progress')
    parser.add_argument('--ext', type=str, default='.txt .ml .md .html',
                        help='Space separated translation file extensions such as ".txt .ml .md .html."')
    parser.add_argument('--indent', type=str, default='  ',
                        help='Indentation for depth.')
    parser.add_argument('--prefix', type=str, default='* ',
                        help='Prefix for the location output.')
    parser.add_argument('--suffix', type=str, default='',
                        help='Suffix for the location output.')
    parser.add_argument('--exclude_path', type=str,
                        default='/g3doc/resources /g3doc/api_docs \
                        /g3doc/contrib',
                        help='Exclude directory.')
    parser.add_argument('--head', type=str,
                        default='# Translation Coverage \
                        \n(Automatically generated. DO NOT edit.)',
                        help='Exclude directory.')
    return parser.parse_args(args)


def print_out(args):
    global print_que

    powered_by = "\n\n---\nPowered by [Translation Coverage]" \
                 "(https://github.com/hunkim/translation_coverage)"
    return args.head + '\n' + '\n'.join(reversed(print_que)) + powered_by


def main():
    args = parse_args(sys.argv[1:])
    ext_set = tuple(args.ext.split())
    exclude_path = tuple(args.exclude_path.split())

    trans_coverage(-1, args, args.dir, ext_set, exclude_path)

    # Print results in the right order
    print(print_out(args))

if __name__ == '__main__':
    main()
