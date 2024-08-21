from dataclasses import dataclass

from ..record_base import BaseRecord


@dataclass
class Nekoalice(BaseRecord):
    isButton: bool
    isComplete: bool
    isBadge: bool
