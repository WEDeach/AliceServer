from dataclasses import dataclass
from typing import Any, Dict

from .record_base import BaseRecord


@dataclass
class BaseReq:
    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        # 自定义反序列化逻辑
        init_kwargs = {}
        for field_name, field_info in cls.__dataclass_fields__.items():
            field_type = field_info.type
            json_key = field_info.metadata.get("json_key", field_name)
            val = data.get(json_key)
            print(field_name, field_type, str(val)[:20])
            if hasattr(field_type, '__origin__') and issubclass(field_type.__origin__, list):
                item_type = field_type.__args__[0]
                
                if isinstance(item_type, type) and issubclass(item_type, BaseRecord):
                    val = [item_type(**item) for item in data.get(field_name, [])]
            elif isinstance(field_type, type) and issubclass(field_type, BaseRecord):
                if val is None:
                    val = {}
                val = field_type(**val)
            init_kwargs[field_info.name] = val
        return cls(**init_kwargs)

    def __repr__(self):
        L = ["%s=%r" % (key, value) for key, value in self.__dict__.items()]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))
