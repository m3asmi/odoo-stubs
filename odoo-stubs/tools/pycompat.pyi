from typing import Any, Optional

def reraise(tp: Any, value: Any, tb: Optional[Any] = ...) -> None: ...

_reader: Any
_writer: Any

def csv_reader(stream: Any, **params: Any): ...
def csv_writer(stream: Any, **params: Any): ...
def to_text(source: Any): ...