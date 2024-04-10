# Write a file name.txt with your name

def writeFile(fileName: str, name: str) -> bool:
    with open(fileName, "w") as f:
        f.write(name)

if __name__ == "__main__":
    fileName = "test_files/name.txt"
    name = "Austin\n"
    
    writeFile(fileName, name)
    