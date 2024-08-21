import json
from dataclasses import asdict, dataclass
import os
from ..utils.crypto import AliceCrypto

@dataclass
class RemoteConfig:
    standaloneType: int
    legalDocumentVersion: int
    legalDocumentUpdateTitle: str
    legalDocumentUpdateDescription: str
    legalDocumentUpdateContent: str
    endingUserDataListFileSize: int
    endingUserDataListFileHash: str
    resourceFileMstVersion: int
    refundButtonStatus: bool
    questionnaireButtonStatus: bool
    typeAQuestionareUrl: str
    refundRequestUrl: str
    isMaintenance: bool
    maintenanceDescription: str
    appVersion: str

    @staticmethod
    def new():
        """Create new remote config instance."""
        return RemoteConfig(
            standaloneType=0,
            legalDocumentVersion=1,
            legalDocumentUpdateTitle="TEST TITLE",
            legalDocumentUpdateDescription="FK YOU BAO...",
            legalDocumentUpdateContent="TEST CONTENT",
            endingUserDataListFileSize=0,
            endingUserDataListFileHash="66d0f548e5598252bffe7696af982539",
            resourceFileMstVersion=400031,
            refundButtonStatus=True,
            questionnaireButtonStatus=True,
            typeAQuestionareUrl= "https://docs.google.com/forms/d/e/1FAIpQLSc2Z5CxSvQAO_O4wCFTuctvJQha7eZ-l-R_bVJZhc9HIOkUEw/viewform?usp=pp_url&entry.476892191={0}",
            refundRequestUrl="https://help.pokelabo.games/?action=inquiry_form&app_id=831556760402145&x_uid={0}&refund_code={1}",
            isMaintenance=False,
            maintenanceDescription="測試維修...",
            appVersion="99.9.1"
        )

    def dump_bin(self) -> bytes:
        """Dump remote config to bin."""
        d = asdict(self)
        j = json.dumps(d)
        k = bytes.fromhex(os.getenv("H_AES_KEY") or "")
        i = bytes.fromhex(os.getenv("H_AES_IV") or "")
        return AliceCrypto.encrypt(j.encode(), k, i)