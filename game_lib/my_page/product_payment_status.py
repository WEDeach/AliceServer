from typing import Optional
from dataclasses import dataclass, field

from ..record_base import BaseRecord


@dataclass
class ProductPaymentStatus(BaseRecord):
    purchaseOptionType: Optional[int] = field(default=None)
    purchaseOptionStatus: Optional[bool] = field(default=None)
