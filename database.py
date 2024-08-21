import json
import os
from typing import Optional

from typing_extensions import Self


class AliceDatabase:
    __instance: Optional[Self] = None

    def __init__(self):
        pass

    @classmethod
    def instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    @property
    def mst_tables(self):
        return {}

    def get_mst_table(self, mst_table_name: str):
        if mst_table_name in self.mst_tables:
            return self.mst_tables[mst_table_name]
        raise FileNotFoundError(f"MstTable name `{mst_table_name}` not found.")


class AliceDummyDatabase(AliceDatabase):
    def __init__(self):
        self.dummy_tables = {}

        self.load_msts()

    @property
    def mst_tables(self):
        return self.dummy_tables

    def load_msts(self):
        dummy_table_file_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "servers",
            "Alice",
            "api",
            "dummy_tables",
        )
        for table_name in os.listdir(dummy_table_file_path):
            file_path = os.path.join(dummy_table_file_path, table_name)
            if os.path.isfile(file_path):
                table_key = os.path.splitext(table_name)[0]
                with open(file_path, "r", encoding="utf-8") as file:
                    self.dummy_tables[table_key] = json.loads(file.read())
        print(f"成攻讀取 {len(self.dummy_tables)} 個 MstTable...")
