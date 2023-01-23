import os

# find python directories


def find_python_dirs(root_dir):
    python_dirs = []
    for dirpath, dirnames, files in os.walk(root_dir):
        for dirname in dirnames:
            if dirname == 'python':
                python_dirs.append(os.path.join(dirpath, dirname))
    return python_dirs


root_dir = '/'
python_dirs = find_python_dirs(root_dir)
print(python_dirs)
