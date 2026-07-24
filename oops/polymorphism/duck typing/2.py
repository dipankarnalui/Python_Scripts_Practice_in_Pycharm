class File:
    def read(self):
        return "Reading from file"

class NetworkStream:
    def read(self):
        return "Reading from network"

def process(source):
    print(source.read())

process(File())
process(NetworkStream())