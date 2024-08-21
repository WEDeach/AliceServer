from dotenv import load_dotenv
from typing import Optional

from ..database import AliceDatabase

load_dotenv()

alice_shared_gate: Optional["AliceShared"] = None


class AliceShared:
    databese: Optional[AliceDatabase]

    @staticmethod
    def instance():
        global alice_shared_gate
        if alice_shared_gate is None:
            alice_shared_gate = __class__()
        return alice_shared_gate

    @staticmethod
    def get_database():
        ins = __class__.instance()
        if ins.databese is not None:
            return ins.databese
        raise NotImplementedError
