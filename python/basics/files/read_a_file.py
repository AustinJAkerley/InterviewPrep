# Prompt: Read in a file line by line and print it to the cmd line
def read_lines(filename: str) -> bool: 
    """
    Reads a file line by line and prints it to the console. Equivalent to cat linux cmd.

    :param filename: String representing the relative or absolute path to a file.
    :return boolean: True if file was able to be read, False if not
    """
    try:
        with open(filename, "r") as f:
            for line in f.readlines():
                print(line)
        return True
    except Exception:
        return False

if __name__ == "__main__":
    print("Success Case:")
    filename = "test_files/basic.txt"
    if not read_lines(filename):
        raise  ValueError(f"Unable to open and read file {filename}")

    print("Failure Case:")
    filename = "test_files/basica.txt"
    if not read_lines(filename):
        raise  ValueError(f"Unable to open and read file {filename}")
    
    