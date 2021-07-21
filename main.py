
file = open('test.txt')
outputFile = open('output.txt','a')


# read from file and create new line if we have space after characters in line (Remove the characters after everyline)

## get each line of the file

for line in file:
    LastSlicePosition = 0
    ## line_was_sliced is to check weather line is sliced into two line or not
    line_was_sliced = False
    ## counter counts spaces after characters
    counter=0
    ## position_in_line saves the position of the line
    position_in_line=0
    ## check characters if they are space
    for character in line:
        ## increment the position
        position_in_line+=1
        ## check if it is black then increment the counter
        if(character == ' '):
            counter+=1
        elif( character != '\n' and character !=' ' and counter > 25):
            ## slice from zero to the point before blank spaces
            ## Added 5 more characters for flexibility
            point = position_in_line - counter + 5
            ## characters before space in the line
            subline = line[LastSlicePosition: point]

            print(subline)
            LastSlicePosition = position_in_line - 1
            ## next characters after blank spaces
            # nextLine= line[position_in_line - 1:]
            ## write characters before space in the line into a new line 
            outputFile.write(subline + '\n')
            ## write the next characters after blank spaces into a new line
            # outputFile.write(nextLine)
            ## reset the counter 
            counter = 0
            ## set line_was_sliced flag into true
            line_was_sliced = True
        elif (character == '\n'):
            subline = line[LastSlicePosition: position_in_line]
            outputFile.write(subline)

    ## if line wasn't sliced, it wasn't written in output
    ## So here we would print it in the output
    if line_was_sliced == False:
        outputFile.write(line)

outputFile.close()
file.close()

