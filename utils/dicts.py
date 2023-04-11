def get_val(collection, key, default='git'):
    """Функция возвращает значение из словаря по переданному ключу, если ключ существует. В ином случае возвращается
    значение default."""
    len_collection = len(collection)
    if len_collection != 0:
        return collection["vcs"]
    else:
        return default


def get_val_v2(collection: dict, key, default='git'):
    """Функция возвращает значение из словаря по переданному ключу, если ключ существует. В ином случае возвращается
    значение default."""

    return collection.get(key, default)
