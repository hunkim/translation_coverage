'''
 Used github markdown format
 Feel free to modify for your purpose
'''
from utils import get_progress_emoji


def report_coverage(depth, args, loc, eng_count, non_eng_count):
    indent = ''
    for i in range(depth):
        indent += args.indent

    rel_loc = loc[len(args.dir):]

    if rel_loc == '':
        rel_loc = '/'

    text_count = eng_count + non_eng_count

    ratio = int(non_eng_count * 100 / text_count)

    progress_emoji = get_progress_emoji(ratio)

    return indent + args.prefix + \
        progress_emoji + ' ' + \
        '[' + rel_loc + ']' + \
        '(' + rel_loc + ')' + \
        args.suffix + \
        ' (' + str(non_eng_count) + '/' + str(text_count) + ')' + \
        ' [' + str(ratio) + '%]'
