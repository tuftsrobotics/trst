import io
import time
import subprocess
import sys
infile  = 'in.log'
filename = 'test.log'
with io.open(filename, 'wb') as writer, io.open(infile, 'rb', 1) as reader:
    process = subprocess.Popen(['analyzer', '-json'],
                            stdin = reader,
                            stdout = writer)
    while process.poll() is None:
        sys.stdout.write(reader.read())
        time.sleep(0.5)
        # Read the remaining
    sys.stdout.write(reader.read())
