from api.project import spec


def save(data):
    with open('api.yaml', 'w') as f:
        f.write(data)


if __name__ == '__main__':
    yaml = spec.to_yaml()

    print(yaml)

    save(yaml)

    print()
    print()
    print()

    print('The content was saved into the api.yaml file!')
