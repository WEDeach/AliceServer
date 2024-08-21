from flask import Blueprint, request

from ....game_lib.character.record_character_data import CharacterDataRecord


from ....game_lib.req_container import ReqContainer
from ....game_lib.res_container import ResContainer
from ....game_lib.character.res_get_character_data_list import GetCharacterDataListRes


bp_api_chara = Blueprint("Character", __name__)


@bp_api_chara.route("/get_character_data_list", methods=["POST"])
def get_character_data_list():
    req = ReqContainer.unwrap(request.data)

    res = GetCharacterDataListRes(
        characterDataList=[
            CharacterDataRecord(
                characterDataId=1,
                characterMstId=1,
                userId=700001,
                level=1,
                maxLevel=10,
                exp=0,
                limitBreakCount=0,
                openedStoryStep=1,
                isDeleted=False,
                createdTime=0,
                isJobAwakening=False
            )
        ]
    )
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()
