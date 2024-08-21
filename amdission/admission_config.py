import base64
import gzip
import io
import json
from enum import IntEnum
from dataclasses import asdict, dataclass
import os
from ..utils.crypto import AliceCrypto


class AdmissionStatusType(IntEnum):
    AllThrough = 0
    LimitThrough = 1
    CantThrough = 2


@dataclass
class AdmissionConfig:
    status: AdmissionStatusType

    def dump_gzip(self) -> bytes:
        """Dump admission config to gzip."""
        d = asdict(self)
        j = json.dumps(d)
        buf = io.BytesIO()
        k = bytes.fromhex(os.getenv("H_ADM_KEY") or "")
        i = bytes.fromhex(os.getenv("H_ADM_IV") or "")
        enc = AliceCrypto.encrypt(j.encode(), k, i)
        b64 = base64.b64encode(enc)

        with gzip.GzipFile(fileobj=buf, mode='wb') as gzip_file:
            gzip_file.write(b64)

        return buf.getvalue()