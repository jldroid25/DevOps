def main():

    print("\n")

    # Open a file for writing and create it if it doesn't exist
    # open() takes 2 args, filename & action/mode "w+" writing
    # Caution : Running exiting file with "W+" mode will override its contents
    
    #f = open("textfile.txt", "w+")

    # Open the file for appending  with "a" mode & add text to the end
    # f = open("textfile.txt", "a")


    # write some lines of data to the file
    # for i in range(10):
    #     f.write("Welcome SRE Devops Jldroid25 " + str(i) + "\r\n")


    # # # close the file when done to prevent memorry leaks
    # f.close()

    # Open the file back up and read the contents 

    # Open the file for read access with "r" mode 
    f = open("textfile.txt", "r")
    
    # check if file mode is equal to read, if yes print its contents
    # else do nothing 
    # if f.mode  == 'r':
    #     contents = f.read()
    #     print(contents)

    # -- Now For reading a file as an array & printing them
    if f.mode  == 'r':
        fl = f.readlines()
        for line in fl:
            print(line)
   

if __name__ == "__main__":
    main()