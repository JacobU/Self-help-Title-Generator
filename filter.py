# read_file = open("titles_data.txt","r")
# write_file = open("titles_no_space_data.txt","w+")

# if read_file.mode == 'r':
#     lines = read_file.readlines()
#     for x in lines:
#         if x != "\t\n":
#             write_file.write(x)

# read_file.close()
# write_file.close()


read_file = open("titles.txt","r")
write_file = open("titles_nodup.txt","w+")

if read_file.mode == 'r':
    lines = read_file.readlines()

    titles = [x for x in lines if not x in titles]

    for x in titles:
        write_file.write(x)

read_file.close()
write_file.close()