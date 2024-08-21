

from dataclasses import dataclass, fields, is_dataclass
import json
from typing import TypeVar, get_args, get_origin
import msgpack
import copy

from .record_base import BaseRecord

def _asdict_inner(obj, dict_factory=dict):
    if is_dataclass(obj):
        result = []
        for f in fields(obj):
            value = _asdict_inner(getattr(obj, f.name), dict_factory)
            if value is None:
                tt= get_args(f.type)
                for t1 in tt:
                    if isinstance(t1, TypeVar):
                        continue
                    if get_origin(t1) is not None:
                        continue
                    if issubclass(t1, BaseRes) or issubclass(t1, BaseRecord):
                        value = {}
                        break
            result.append((f.name, value))
        return dict_factory(result)
    elif isinstance(obj, tuple) and hasattr(obj, '_fields'):
        return type(obj)(*[_asdict_inner(v, dict_factory) for v in obj])
    elif isinstance(obj, (list, tuple)):
        return type(obj)(_asdict_inner(v, dict_factory) for v in obj)
    elif isinstance(obj, dict):
        return type(obj)((_asdict_inner(k, dict_factory),
                          _asdict_inner(v, dict_factory))
                         for k, v in obj.items())
    else:
        return copy.deepcopy(obj)

@dataclass
class BaseRes:

    def dump_msgpack(self):
        """Dump data."""
        d = _asdict_inner(self)
        print(json.dumps(d))
        return msgpack.packb(d) or b""

    def __repr__(self):
        L = ["%s=%r" % (key, value) for key, value in self.__dict__.items()]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))