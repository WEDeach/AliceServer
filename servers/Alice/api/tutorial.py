from typing import List
from flask import Blueprint, request

from ....game_lib.tutorial.req_set_character import SetCharacterReq

from ....game_lib.tutorial.res_set_character import SetCharacterRes

from ....game_lib.enums import TutorialMstId

from ....game_lib.user.record_user_data import UserDataRecord

from ....game_lib.tutorial.res_set_user_name import SetUserNameRes

from ....game_lib.tutorial.req_set_user_name import SetUserNameReq

from ....game_lib.gacha.record_multi_gacha_animation_param import (
    MultiGachaAnimationParamRecord,
)


from ....game_lib.req_container import ReqContainer
from ....game_lib.res_container import ResContainer
from ....game_lib.gacha.record_gacha_data import GachaDataRecord
from ....game_lib.gacha.record_gacha_detail_log import GachaDetailLogRecord
from ....game_lib.gacha.record_gacha_pickup_data import GachaPickupDataRecord
from ....game_lib.gacha.record_gacha_series_data import GachaSeriesDataRecord
from ....game_lib.gacha.res_gacha_exec import GachaExecRes
from ....game_lib.gacha.res_get_tutorial_gacha_top import GetTutorialGachaTopRes
from ....game_lib.tutorial.record_user_mini_tutorial_data import (
    UserMiniTutorialDataRecord,
)
from ....game_lib.tutorial.record_user_mini_tutorial_disable_message import (
    UserMiniTutorialDisableMessageRecord,
)
from ....game_lib.tutorial.req_get_next_tutorial_mst_id import GetNextTutorialMstIdReq
from ....game_lib.tutorial.res_agree_legal_document import AgreeLegalDocumentRes
from ....game_lib.tutorial.res_get_next_tutorial_mst_id import GetNextTutorialMstIdRes
from ....game_lib.tutorial.res_get_user_mini_tutorial_data import (
    GetUserMiniTutorialDataRes,
)
from ....game_lib.tutorial.res_tutorial_gacha_exec import TutorialGachaExecRes


bp_api_tutorial = Blueprint("Tutorial", __name__)


@bp_api_tutorial.route("/get_next_tutorial_mst_id", methods=["POST"])
def get_next_tutorial_mst_id():
    req = ReqContainer[GetNextTutorialMstIdReq].unwrap(
        request.data, GetNextTutorialMstIdReq
    )
    res = GetNextTutorialMstIdRes(nextTutorialMstId=TutorialMstId.Quest)
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()


@bp_api_tutorial.route("/agree_legal_document", methods=["POST"])
def agree_legal_document():
    req = ReqContainer.unwrap(request.data)

    res = AgreeLegalDocumentRes(success=True, message="")
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()


@bp_api_tutorial.route("/get_user_mini_tutorial_data", methods=["POST"])
def get_user_mini_tutorial_data():
    req = ReqContainer.unwrap(request.data)

    res = GetUserMiniTutorialDataRes(
        userMiniTutorialData=UserMiniTutorialDataRecord(
            userId=70001,
        ),
        userMiniTutorialDisableMessage=UserMiniTutorialDisableMessageRecord(),
    )
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()


@bp_api_tutorial.route("/get_tutorial_gacha", methods=["POST"])
def get_tutorial_gacha():
    req = ReqContainer.unwrap(request.data)

    gachaSeriesList = GachaSeriesDataRecord.fetch_datas(2)
    gachaList = GachaDataRecord.fetch_datas(gachaMstId=3)
    gachaPickupList = GachaPickupDataRecord.fetch_datas(gachaSeriesMstId=2)
    if gachaSeriesList:
        gachaGroupId = gachaSeriesList[0].gachaGroupId
        for i in gachaList:
            i.gachaGroupId = gachaGroupId
        for i in gachaPickupList:
            i.gachaGroupId = gachaGroupId
    res = GetTutorialGachaTopRes(
        gachaSeriesList=gachaSeriesList,
        gachaList=gachaList,
        gachaPickupList=gachaPickupList,
    )
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()


@bp_api_tutorial.route("/tutorial_gacha_exec", methods=["POST"])
def exec_tutorial_gacha():
    req = ReqContainer.unwrap(request.data)

    # TODO: gacha
    gacha_detail_logs: List[GachaDetailLogRecord] = []
    repeatCount = 11
    for i in range(repeatCount):
        gacha_detail_logs.append(GachaDetailLogRecord(objectId=49, objectRarity=3))
    chance_up_idx = 4
    gacha_detail_logs[chance_up_idx].objectId = 2
    gacha_detail_logs[chance_up_idx].objectRarity = 4
    gacha_detail_logs[chance_up_idx].isChanceUp = 1
    res = TutorialGachaExecRes(
        gachaExecRes=GachaExecRes(
            gachaMstId=3,
            gachaDetailLog=gacha_detail_logs,
            multiGachaAnimationParam=MultiGachaAnimationParamRecord(
                serifType=4,
                isExtraAnimation=True,
                isFallingHeadAnimation=False,
                isReverseAnimation=True,
            ),
            repeatCount=repeatCount,
        ),
        nextTutorialMstId=3,
    )
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()


@bp_api_tutorial.route("/set_user_name", methods=["POST"])
def set_user_name():
    req = ReqContainer.unwrap(request.data, SetUserNameReq)

    # TODO: set user name.
    user_data = UserDataRecord.get(700001)
    res: SetUserNameRes
    if req.payload:
        if req.payload.userName == "6":
            res = SetUserNameRes(
                success=False,
                message="我不知道你發這個<color=red><size=50>6</size></color>是什麼意思, 是覺得我的訊息不滿意還是覺得我煩還是想絕交了, 我有時候確實挺煩, 也不會聊天給不了你滿意的回覆我向你道歉, 以後可以別敷衍我了嗎。\n\n我終覺得朋友的定義不僅僅是朋友那扇門。\n\n我不敢敲開, 看你朋友圈發現你開始新的生活了, 我希望自己和你一樣灑自由, 開弓沒有回頭箭, 我們絕交了, 就再也成不了朋友了, 如果能重來, 我要選李白",
                userData=user_data,
            )
        else:
            user_data.name = req.payload.userName
            res = SetUserNameRes(success=True, message="", userData=user_data)
    else:
        res = SetUserNameRes(success=False, message="請輸入名稱!", userData=user_data)
    print("set_user_name: ", res)
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()


@bp_api_tutorial.route("/set_character", methods=["POST"])
def set_character():
    req: ReqContainer[SetCharacterReq] = ReqContainer.unwrap(
        request.data, SetCharacterReq
    )

    # TODO: set user character.
    user_data = UserDataRecord.get(700001)
    res: SetCharacterRes = SetCharacterRes(message="內部錯誤")
    if req.payload:
        if req.payload.characterMstId in [1, 2, 3, 5]:
            res = SetCharacterRes(
                success=True,
                message="",
                userData=user_data,
            )
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()
