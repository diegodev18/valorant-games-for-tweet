from datetime import datetime


def upload_items(my_items_to_add: list, name: str):
    try:
        with open(name, 'r') as f:
            my_items = f.read().split('\n')
        f.close()
    except FileNotFoundError:
        my_items = []
    with open(name, 'w') as f:
        if len(my_items) != 0:
            for item in my_items:
                f.write(f'{item}\n')
        f.write(f'{datetime.now()}\n')
        for item in my_items_to_add:
            f.write(f'{item}\n')
    f.close()
