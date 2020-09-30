def path_to_bytes(path: str) -> bytes:
    data = open(path, "rb")
    return data.read()
