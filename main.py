import argparse
from os import listdir
from os.path import isfile, isdir, join
from string import ascii_letters

from report import report_coverage

# 'itertools.imap' was moved to 'map' in Python3
try:
    from itertools import imap
except ImportError:
    imap = map

print_que = []


def is_only_eng_alpha(char):
    if char in ascii_letters:
        return True
    return False


def trans_coverage_file(file, ext=None):
    if ext is not None and not file.lower().endswith(ext):
        return 0, 0

    try:
        with open(file, "r") as myfile:
            s = myfile.read()

            # http://stackoverflow.com/questions/24878174/
            # TODO: It does not work in Python3. Need a better solution
            words = sum(imap(is_only_eng_alpha, s))
            numbers = sum(imap(str.isdigit, s))
            spaces = sum(imap(str.isspace, s))
            others = len(s) - numbers - words - spaces

            return words, others
    except:
        return 0, 0


def trans_coverage(depth, args, loc, ext=None, exclude_path=None):
    global print_que

    depth += 1

    # Exclude path
    rel_loc = loc[len(args.dir):]
    if exclude_path is not None and rel_loc.startswith(exclude_path):
        return 0, 0

    if isfile(loc):
        eng_count, noneng_count = trans_coverage_file(loc, ext)
    elif isdir(loc):
        eng_count, noneng_count = 0, 0

        for f in listdir(loc):
            full_file = join(loc, f)
            e_count, n_count = trans_coverage(depth, args, full_file, ext, exclude_path)

            eng_count += e_count
            noneng_count += n_count
    else:
        eng_count, noneng_count = 0, 0

    if eng_count is not 0 or noneng_count is not 0:
        out = report_coverage(depth, args, loc, eng_count, noneng_count)
        print_que.insert(0, out)

    return eng_count, noneng_count


def main():
    global print_que

    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='.',
                        help='directory to check translation progress')
    parser.add_argument('--ext', type=str, default='.txt .md .html',
                        help='Translation file extentions. Space separated.')
    parser.add_argument('--indent', type=str, default='  ',
                        help='Indentation for depth.')
    parser.add_argument('--prefix', type=str, default='* ',
                        help='Prefix for the locaton output.')
    parser.add_argument('--suffix', type=str, default='',
                        help='Suffix for the locaton output.')
    parser.add_argument('--exclude_path', type=str, default='/g3doc/resources /g3doc/api_docs /g3doc/contrib',
                        help='Exclude directory.')
    parser.add_argument('--head', type=str, default='# Translation Coverage \n(Automatically generated. DO NOT edit.)',
                        help='Exclude directory.')

    args = parser.parse_args()

    ext = tuple(args.ext.split())
    exclude_path = tuple(args.exclude_path.split())
    trans_coverage(-1, args, args.dir, ext, exclude_path)

    print (args.head)

    # Print results in the right order
    for s in print_que:
        print(s)

    print ("\n\n---\nPowered by [Translation Coverage](https://github.com/hunkim/translation_coverage)")

if __name__ == '__main__':
    main()
