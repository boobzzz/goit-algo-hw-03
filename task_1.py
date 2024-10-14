import os
import shutil
from pathlib import Path


def parse_input(user_input: str) -> Path:
    path = ''
    if user_input:
        path = user_input.split()[0]
        path = path.strip().lower()
    else:
        print('Invalid path')

    return Path(path)


def copy_files(source_dir, dest_dir):
    if source_dir.is_dir():
        for child in source_dir.iterdir():
            if child.is_dir():
                copy_files(child, dest_dir)
            else:
                file_ext = child.name.split('.')[1]
                dest_subdir = dest_dir.joinpath(file_ext)

                if not dest_subdir.exists():
                    dest_subdir.mkdir()

                try:
                    shutil.copy2(child, dest_subdir)
                    print(f"Copied {child} to {dest_subdir}")
                except Exception as e:
                    print(f"Failed to copy {child}: {e}")


def main():
    src_path = parse_input(input('Enter source directory path: '))
    out_path = parse_input(input('Enter output directory path: '))
    default_output = 'dist'

    try:
        if not src_path.exists():
            print('Source directory does not exists')
        elif not out_path.exists():
            os.makedirs(default_output)
        else:
            copy_files(src_path, out_path)
    except KeyboardInterrupt:
        print('Interrupted by user')


if __name__ == "__main__":
    main()
