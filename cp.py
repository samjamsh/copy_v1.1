def inputs():
    if len(args) == 2 and args[1] == "-h":
        help_msg = """Copy Program (CP) version 1.2 (v1.2), this is help message for this tool.\nUsage: python3 %s source-file target-file [option]\n[options]\n    -w  write, this mode writes new data over old file data, this option deletes old file data and write the new data in file\n    -a  append, this mode appends new data in final or end of file without deleting old file data (it increments the old file data with new file data)\n\n    source-file - filename you want to copy\n    target-file - destination filename or new filename\n\nexamples:\n    python3 %s source-file target-file \n""" %(args[0], args[0])
        exit(help_msg)

    elif len(args) == 3:
        source_file = args[1]
        destination_file = args[2]
        return source_file, destination_file, "wb"

    elif len(args) == 4:
        source_file = args[1]
        destination_file = args[2]
        option = args[3]

        if option == "-a": # append in final of final (do not delete old filedata)
            return source_file, destination_file, "ab" # mode

        elif option == "-w": # write in file (modify old filedata with new file data)
            return source_file, destination_file, "wb"

        else:
            exit("parameter error: invalid option")

    else:
        exit(f"use: python3 {args[0]} source-file destination-file")
      

def copy(data, destination_name, target_type):
    try:
        if target_type == "file":
            with open(destination_name, "ab") as target_file:
                target_file.write(data)

        elif target_type == "dir":
            with open(destination_name + '/'+ source_file, "ab") as file:
                file.write(data)

        else:
            exit("source code syntax error")

    except Exception as error:
        exit(error)


def __work__(filename, destination_filename, target_type):
    try:
        with open(filename, "rb", buffering=1024*1024) as filedata:
            for filebytes in filedata:
                copy(filebytes, destination_filename, target_type)

    except Exception as error:
        exit(error)


def main():
    source_filename, destination, mode = inputs()

    if mode == "wb": f = open(destination, "w"); f.write(""); f.close()
    if path.isdir(destination) == True:
        __work__(source_filename, destination, "dir")
    else:
        __work__(source_filename, destination, "file")

from os import path
from sys import argv as args
main()
