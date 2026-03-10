def square(x):
    return x**2


def hello_world():
    return "Hello, World!"


def matmul(a, b):
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    if cols_a != rows_b:
        raise ValueError(f"Incompatible shapes: ({rows_a}x{cols_a}) and ({rows_b}x{cols_b})")
    result = [[0] * cols_b for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]
    return result

def read_and_sort_words(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    words = text.split()
    words_sorted = sorted(words, key=str.lower)

    return words_sorted


if __name__ == "__main__":
    #print(square(2))

    words = read_and_sort_words("example.txt")
    for w in words:
        print(w)