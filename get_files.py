
def get_file(path: str):
    with open(path, 'r') as f:
        return f.read().split('\n')
