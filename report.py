'''
 USed github markdown format
'''
def reportCoverage(depth, args, loc, EngCount, NonEngCount):
    indent = ""
    for i in range(depth):
        indent += args.indent

    relLoc = loc[len(args.dir):]

    if relLoc == '':
        relLoc = "/"

    return indent + args.prefix +  "[" + relLoc + "](" + relLoc  + ")" + args.suffix +  " " + \
           str(EngCount) + "/" + str(NonEngCount) + \
           " (" + str(NonEngCount*100/(EngCount+NonEngCount)) + "%)"
