

def reset_count():
    with open('data/count.txt', 'w') as f:
        f.write(str(0))


def check_count():
    with open('data/count.txt', 'r') as f:
        count = int(f.read())
        if count == 1:
            return True
        return False


def add_count():
    with open('data/count.txt', 'r') as f:
        count = int(f.read())

    count += 1

    with open('data/count.txt', 'w') as f:
        f.write(str(count))