import os

def read_file(file_path: str) -> str:
    """
    Read the contents of a file.

    :param file_path: The path to the file to read.
    :return: The contents of the file.
    """

    if not os.path.isfile(file_path):
        raise ValueError(f"{file_path} is not a file.")

    with open(file_path, 'r') as file:
        return file.read()

def compute_jaccard_similarity(a: str, b: str) -> float:
    """
    Compute the Jaccard similarity between two programs.

    :param a: The first program to compare.
    :param b: The second program to compare.
    :return: The Jaccard similarity between the two programs.
    """

    a_content = read_file(a).splitlines()
    b_content = read_file(b).splitlines()

    set_a = set(a_content)
    set_b = set(b_content)
    intersection = set_a & set_b
    union = set_a | set_b
    if not union:
        return 1.0
    return len(intersection) / len(union)

def visualise_dot_plot(a: str, b: str) -> str:
    a_content = read_file(a).splitlines()
    b_content = read_file(b).splitlines()

    sep = '-' * 80
    plot = sep + '\n'
    for i in range(len(a_content)):
        plot += f'x{i}: {a_content[i]}\n'
    plot += sep + '\n'
    for j in range(len(b_content)):
        plot += f'y{j}: {b_content[j]}\n'
    plot += sep + '\n'

    n_x = len(a_content)
    header_cells = [f'x{i}' for i in range(n_x)]
    plot += '\t' + '\t'.join(header_cells) + '\t\n'
    for j in range(len(b_content)):
        row_cells = ['*' if a_content[i] == b_content[j] else ' ' for i in range(n_x)]
        plot += f'y{j}\t' + '\t'.join(row_cells) + '\t\n'
    plot += sep

    return plot
