from dataclasses import dataclass

from .record_user_mini_tutorial_data import UserMiniTutorialDataRecord
from .record_user_mini_tutorial_disable_message import (
    UserMiniTutorialDisableMessageRecord,
)
from ..res_base import BaseRes


@dataclass
class GetUserMiniTutorialDataRes(BaseRes):
    userMiniTutorialData: UserMiniTutorialDataRecord
    userMiniTutorialDisableMessage: UserMiniTutorialDisableMessageRecord
