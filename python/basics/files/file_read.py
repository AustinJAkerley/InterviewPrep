import datetime
import logging

logging.basicConfig(level=logging.DEBUG)

# Prompt: 
#
# Read in a file and iterate through each line to verify that
# it follows the following LINE structure
# "string | number | date(xx-xx-xxxx format)"
# if NOT return the line number and throw a ValueError in the parent call with the line number in the error
# if it is, return 0

def file_format_verifier(filename: str) -> int:
    """ 
    This function verifies that a file has the following structure on every line
    "string | number | date(xx-xx-xxxx format)"

    :param filename: This is the file's name
    :return boolean: If true the file has the intended format, if it does not returns false
    """

    with open(filename, "r") as myFile:
        lines = myFile.readlines()
        fileLen = len(lines)
        for i, line in enumerate(lines):
            parsedLine = line.split(" ") # Will be a list such as ["string", "|", "number", "|", "date"]

            # If last line is empty it is still a successful format.
            if fileLen == i and parsedLine == []:
                return 0 
            
            # Check length before accessing the array, may be 6 depending on the newline character counting
            if len(parsedLine) != 5:
                logging.error("Length is not 5")
                return i + 1
            
            # First element of line
            if not isinstance(parsedLine[0], str)  or parsedLine[0] == "|": #  TODO: add additional verification to make sure it is not a number
                logging.error("Is not a string or is |")
                return i + 1
            
            # Second element check and Fourth element check
            if parsedLine[1] != "|" or parsedLine[3] != "|":
                logging.error("Element is not a | as expected")
                return i + 1
            
            # Third element check
            try: 
                num = int(parsedLine[2]) # int() will throw an error if a non numerical number is passed to it
            except Exception:
                logging.error("Element is not a | as expected")
                return i + 1
            
            # Last element check, this is a guess on syntax, essentially we're using the built in datetime.date constructor to verify the string format.
            lineDate = parsedLine[4]
            try:
                if len(lineDate) != 11 or (len(lineDate) != 10 and lineDate[-1] != "\n"):
                    logging.error("Length of year element is incorrect, should be 11 or 10")
                    return i + 1
                year = int(parsedLine[4][6:10])
                month = int(parsedLine[4][0:2])
                day = int(parsedLine[4][3:5])

                myDate = datetime.date(year, month, day) # The successful creation of this object is proof that it is correct. If it is not, the except will catch it.
            except Exception:
                logging.error("Could not create a datetime.date with the day, month, year provided.")
                return i + 1
            
        return 0 # Never found an issue, therefore it is a valid format


if __name__ == "__main__":
    lineNumber = file_format_verifier("test_files/test_file1.txt")
    if lineNumber:
        logging.error(f"File format error on line {lineNumber}")
        raise ValueError(f"File format error on line {lineNumber}")
    else:
        logging.debug("Valid File")
    
