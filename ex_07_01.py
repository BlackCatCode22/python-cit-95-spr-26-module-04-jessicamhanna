# Ensure mbox-short.txt is in your PycharmProjects folder
try :
    fh = open( 'mbox-short.txt' )
    for line in fh :
        # rstrip() removes the invisible newline character [cite: 595, 1107]
        ly = line.rstrip()
        print( ly.upper() )
except :
    # This prevents the program from crashing if the file is missing [cite: 752, 793]
    print( 'File cannot be opened: mbox-short.txt' )
    quit()

    # the absolute drag that tokens and commits are to me
