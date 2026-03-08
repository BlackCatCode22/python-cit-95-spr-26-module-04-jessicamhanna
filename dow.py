# # Open the mailbox data file
# fhand = open('mbox-short.txt')
#
# for line in fhand:
#     # Split the line into a list of words
#     words = line.split()
#
#     # Guardian Pattern: Check length BEFORE checking index
#     # This prevents 'index out of range' errors
#     if len(words) < 3 or words[0] != 'From':
#         continue
#
#     # Python uses zero-based indexing; index 2 is the 3rd word
#     print(words[2])
# fhand = open('mbox-short.txt')
#
# for line in fhand:
#     words = line.split()
#
#     # Guardian Pattern: Check length before index
#     if len(words) < 3 or words[0] != 'From':
#         continue
#
#     print(words[2])
file_handle = open('mbox-short.txt')

for line in file_handle:
    words = line.split()

    # Guardian Pattern: Check length before index
    if len(words) < 3 or words[0] != 'From':
        continue

    print(words[2])