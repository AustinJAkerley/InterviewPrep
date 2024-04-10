import os
from pathlib import Path
mode = 0o775

for subdirs, dirs, files in os.walk("/home/aakerley/Projects/InterviewPrep"):
    if ".git" not in subdirs and "python" in subdirs:
        print(Path(subdirs + '/__init__.py'))
        Path(subdirs + '/__init__.py').touch()
        # Path(subdirs + '__init__.py')