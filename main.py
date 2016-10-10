from os import listdir
from os.path import isfile, isdir, join
from report import reportCoverage
import argparse

printQue = []

def trans_coverage_file(file, ext=None):
    if ext is not None and not file.lower().endswith(ext):
        return 0, 0

    try:
        with open(file, "r") as myfile:
            s = myfile.read()

            numbers = sum(c.isdigit() for c in s)
            words = sum(c.isalpha() for c in s)
            spaces = sum(c.isspace() for c in s)
            others = len(s) - numbers - words - spaces

            return words, others
    except:
        return 0, 0


def trans_coverage(depth, args, loc, ext = None, exclude_path = None):
    global printQue

    depth += 1

    # Exclude path
    relLoc = loc[len(args.dir):]
    if exclude_path is not None and relLoc.startswith(exclude_path):
        return 0, 0

    if isfile(loc):
        EngCount, NonEngCount = trans_coverage_file(loc, ext)
    elif isdir(loc):
        EngCount, NonEngCount = 0, 0

        for f in listdir(loc):
            fullFile = join(loc, f)
            eCount, nCount = trans_coverage(depth, args, fullFile, ext, exclude_path)

            EngCount += eCount
            NonEngCount += nCount
    else:
        EngCount, NonEngCount = 0, 0

    if EngCount is not 0 or NonEngCount is not 0:
        out = reportCoverage(depth, args, loc, EngCount, NonEngCount)
        printQue.insert(0, out)


    return EngCount, NonEngCount

def main():
    global printQue

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

    ext =  tuple(args.ext.split())
    exclude_path =  tuple(args.exclude_path.split())
    trans_coverage(-1, args, args.dir, ext, exclude_path)

    print (args.head)

    # Print results in the right order
    for s in printQue:
        print(s)

    print ("Powered by ")

if __name__ == '__main__':
    main()
