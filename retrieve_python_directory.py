import os

def find_python_dirs(root_dir):
    python_dirs = []
    for dirpath, dirnames, files in os.walk(root_dir):
        for dirname in dirnames:
            if dirname == 'python':
                python_dirs.append(os.path.join(dirpath, dirname))
    return python_dirs

root_dir = '/' # or any other directory you want to start searching from
python_dirs = find_python_dirs(root_dir)
print(python_dirs)
