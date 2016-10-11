'''
 Used github markdown format
 Feel free to modify for your purpose
'''


def report_coverage(depth, args, loc, eng_count, noneng_count):
    indent = ""
    for i in range(depth):
        indent += args.indent

    rel_loc = loc[len(args.dir):]

    if rel_loc == '':
        rel_loc = "/"

    return indent + args.prefix + "[" + rel_loc + "](" + rel_loc + ")" +\
        args.suffix + " " + str(eng_count) + "/" + str(noneng_count) +\
        " (" + str(int(noneng_count * 100 / (eng_count + noneng_count))) + "%)"
