from os import environ
from pathlib import Path

try:
    storage_dir = Path(environ["STORAGE_DIR"]).resolve()
except KeyError:
    raise Exception("No storage directory set")


def get_file_to_store(collection, filename):
    target = (storage_dir / collection / filename)
    if target.exists():
        raise Exception("File already exists")
    target.parent.mkdir(exist_ok=True, parents=True)
    return target


def store_bytes(collection, filename, blob):
    target = get_file_to_store(collection, filename)
    target.write_bytes(blob)


def store_string(collection, filename, text):
    target = get_file_to_store(collection, filename)
    target.write_text(text)

def query_storage(path=""):
    target = (storage_dir / path)
    if not target.exists():
        raise Exception("Does not exists")
    elif target.is_dir():
        return dict(
            path=str(target.relative_to(storage_dir)),
            type="directory",
            content=[str(p.relative_to(storage_dir)) for p in target.iterdir()]
        )
    elif target.is_file():
        return dict(
            path=str(target.relative_to(storage_dir)),
            type="file",
            metadata=dict(
                size=target.stat().st_size,
            )
        )
    return {}
