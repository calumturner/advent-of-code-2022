
with open("input.txt") as f:
    lines = f.read().splitlines()

COMMAND_PREFIX = '$ '
CD_COMMAND = 'cd'
LS_COMMAND = 'ls'
PREVIOUS_DIR = '..'

DIR_PREFIX = 'dir '
current_dir = '/'

dirs = {
    '/': {
        'dirs': [],
        'files': [],
        'parent': '/',
        'size': None
    }
}

for line in lines[1:]:
    if line.startswith(COMMAND_PREFIX):
        command = line.replace(COMMAND_PREFIX, '')
        if command[:2] == CD_COMMAND:
            # Move directory
            if command[3:] == PREVIOUS_DIR:
                current_dir = dirs.get(current_dir).get('parent')
            else:
                if current_dir == '/':
                    current_dir = current_dir + command[3:]
                else:
                    current_dir = current_dir + '/' + command[3:]
    else:

        if current_dir == '/':
            file_prefix = current_dir
        else:
            file_prefix = current_dir + '/'
        if line.startswith(DIR_PREFIX):
            dirs.get(current_dir).get('dirs').append(file_prefix + line[4:])
            dirs[file_prefix + line[4:]] = {
                'dirs': [],
                'files': [],
                'parent': current_dir
            }
        else:
            size, name = line.split(' ')
            dirs.get(current_dir).get('files').append((int(size), name))


def calculate_size(name, dirs):
    dir = dirs.get(name)
    files_total = sum([file[0] for file in dir.get('files')])
    sub_dirs_total = []
    for sub_dir in dir.get('dirs'):
        if dirs.get(sub_dir).get('size') is None:
            calculate_size(sub_dir, dirs)

        sub_dirs_total.append(dirs.get(sub_dir).get('size'))

    dirs.get(name)['size'] = files_total + sum(sub_dirs_total)
    return dirs.get(name).get('size')


for (key, value) in dirs.items():
    if value.get('size') is not None:
        print(f'{key}: {value.get("size")}')
    else:
        print(f'{key}: {calculate_size(key, dirs)}')

l = dict((key, value.get('size')) for (key, value) in dirs.items() if value.get('size') < 100000)
deletable_total = sum(l.values())


print()
print(f'Deletable: {l}')
print()
print(f'Deletable_total: {deletable_total}')

free_space = 70000000 - dirs.get('/').get('size')
space_needed = 30000000 - free_space
print(free_space, space_needed)

print(min([value.get('size') for (key, value) in dirs.items() if value.get('size') >= space_needed]))


