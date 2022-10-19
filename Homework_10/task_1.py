import os
from random import choice


def print_os_name():
    print(os.name)


def print_abs_path():
    print(__file__)


def sort_files():
    current_dir_path = os.path.dirname(__file__)
    sorted_dir_path = os.path.join(current_dir_path, "sorted_files")

    if not os.path.exists(sorted_dir_path):
        os.mkdir(sorted_dir_path)

    sorted_files = []

    for file_name in os.listdir(current_dir_path):
        if file_name == os.path.basename(__file__):
            continue

        file_path = os.path.join(current_dir_path, file_name)
        if not os.path.isfile(file_path):
            continue

        file_ext = os.path.splitext(file_path)[1].replace(".", "")
        new_dir_path = os.path.join(sorted_dir_path, file_ext + "_files")
        if not os.path.exists(new_dir_path):
            os.mkdir(new_dir_path)

        new_file_path = os.path.join(new_dir_path, file_name)
        os.rename(file_path, new_file_path)
        sorted_files.append(new_file_path)

    return sorted_files


def print_sorted_files_info(sorted_files):
    counter = {}
    for file_path in sorted_files:
        size = os.path.getsize(file_path)
        file_ext = os.path.splitext(file_path)[1].replace(".", "")
        if file_ext not in counter:
            counter[file_ext] = {"quantity": 0, "size": 0}
        counter[file_ext]["quantity"] += 1
        counter[file_ext]["size"] += size

    for file_ext in counter:
        qnt = counter[file_ext]["quantity"]
        size = counter[file_ext]["size"]  # bytes
        print(
            f"{qnt} file(s) was moved to {file_ext} dir, "
            f"their size is {size} b"
        )


def execute_random_file(sorted_files):
    python_files = list(
        filter(lambda f: os.path.splitext(f)[1] == ".py", sorted_files)
    )

    if not python_files:
        print("No files to execute")
        return

    random_file = choice(python_files)
    print(f"Result of {os.path.basename(random_file)} execution:")
    os.system(f"python3 {random_file}")


def rename_random_file(sorted_files):
    if not sort_files:
        print("No files to rename")
        return

    random_file = choice(sorted_files)
    file_name = os.path.basename(random_file)
    file_dir_path = os.path.dirname(random_file)

    new_file = os.path.join(file_dir_path, "renamed_" + file_name)
    os.rename(random_file, new_file)

    print(
        f"{file_name} was successfully renamed to {os.path.basename(new_file)}"
    )


if __name__ == "__main__":
    print_os_name()
    print_abs_path()
    sorted_files = sort_files()
    print_sorted_files_info(sorted_files)
    execute_random_file(sorted_files)
    rename_random_file(sorted_files)
