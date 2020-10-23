from api.project import spec, requests
from internal.helpers import add_request_bodies


def save(data):
    with open('api.yaml', 'w') as f:
        f.write(data)


if __name__ == '__main__':
    yaml = add_request_bodies(spec, requests)

    print(yaml)

    save(yaml)

    print()
    print()
    print()

    print('The content was saved into the api.yaml file!')
