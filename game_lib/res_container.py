from dataclasses import dataclass

from .res_error import ResError
from .res_base import BaseRes
from typing import Generic, List, TypeVar, Union

T = TypeVar('T')

@dataclass
class ResContainer(BaseRes, Generic[T]):
    ctag: str
    status: int
    errors: Union[List[ResError], None] = None
    payload: Union[T, None] = None

    @staticmethod
    def new_with_error(status: int, error: ResError):
        """Create new res container instance with error."""
        return ResContainer(
            ctag="",
            status=status,
            errors=[error]
        )

    @staticmethod
    def new(status: int, payload: T):
        """Create new res container instance with error."""
        return ResContainer[T](
            ctag="",
            status=status,
            payload=payload
        )