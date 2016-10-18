'''
 Used github markdown format
 Feel free to modify for your purpose
'''


def report_coverage(depth, args, loc, eng_count, non_eng_count):
    indent = ""
    for i in range(depth):
        indent += args.indent

    rel_loc = loc[len(args.dir):]

    if rel_loc == '':
        rel_loc = "/"

    text_count = eng_count + non_eng_count

    ratio = int(non_eng_count * 100 / text_count)
    # No translation
    style = "**" if ratio == 0 else "*" if ratio > 50 else ""

    return indent + args.prefix + \
        "[" + style + rel_loc + style + "]" + \
        "(" + rel_loc + ")" + \
        args.suffix + \
        " (" + str(non_eng_count) + "/" + str(text_count) + ")" + \
        " [" + str(ratio) + "%]"
