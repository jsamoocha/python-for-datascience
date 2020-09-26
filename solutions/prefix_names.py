def prefix_names(users, **kwargs):
    return [f'{kwargs.get(name[0], "")}{name}' for _, name, _ in users]
