from scanner import step

def main():
    scanner = {
        'field_matrix': [[1]],
        'current_cell': (0, 0),
        'orientation': (0, 1),
        'agent': Agent()
    }
    while True:
        if not step(scanner):
            break;


if __name__ == '__main__':
    main()
