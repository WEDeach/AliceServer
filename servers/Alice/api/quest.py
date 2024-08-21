from flask import Blueprint, request

from ....game_lib.quest_out_battle.req_get_alice_stage_list import GetAliceStageListReq
from ....game_lib.quest_out_battle.req_get_area_map_list import GetAreaMapListReq
from ....game_lib.quest_out_battle.req_get_stage_data import GetStageDataReq
from ....game_lib.quest_out_battle.req_get_stage_reward import GetStageRewardReq
from ....game_lib.quest_out_battle.res_get_alice_stage_list import GetAliceStageListRes
from ....game_lib.quest_out_battle.res_get_area_map_list import GetAreaMapListRes
from ....game_lib.quest_out_battle.res_get_attention import GetAttentionRes
from ....game_lib.quest_out_battle.res_get_stage_data import GetStageDataRes
from ....game_lib.quest_out_battle.res_get_stage_reward import GetStageRewardRes
from ....game_lib.req_container import ReqContainer
from ....game_lib.res_container import ResContainer

bp_api_quest = Blueprint("Quest", __name__)


@bp_api_quest.route("/get_attention", methods=["POST"])
def get_attention():
    req = ReqContainer.unwrap(request.data)

    res = GetAttentionRes()
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()


@bp_api_quest.route("/get_alice_area_map", methods=["POST"])
def get_alice_area_map():
    req = ReqContainer.unwrap(request.data, GetAreaMapListReq)

    res = None
    if req.payload is not None:
        quest_map_mst_id = req.payload.questMapMstId
        res = GetAreaMapListRes.get(quest_map_mst_id)
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()


@bp_api_quest.route("/get_alice_stage_list", methods=["POST"])
def get_alice_stage_list():
    req = ReqContainer.unwrap(request.data, GetAliceStageListReq)

    res = None
    if req.payload is not None:
        res = GetAliceStageListRes.get(
            questAreaMstId=req.payload.questAreaMstId,
            battleNum=req.payload.battleNum,
            prisonRangeId=req.payload.rangeId,
        )
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()


@bp_api_quest.route("/get_stage_data", methods=["POST"])
def get_stage_data():
    req = ReqContainer.unwrap(request.data, GetStageDataReq)

    res = None
    if req.payload is not None:
        res = GetStageDataRes.get(questStageMstId=req.payload.questStageMstId)
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()


@bp_api_quest.route("/get_stage_reward", methods=["POST"])
def get_stage_reward():
    req = ReqContainer.unwrap(request.data, GetStageRewardReq)

    res = None
    if req.payload is not None:
        res = GetStageRewardRes.get(questStageMstId=req.payload.questStageMstId)
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()


@bp_api_quest.route("/get_tutorial_result", methods=["POST"])
def get_tutorial_result():
    req = ReqContainer.unwrap(request.data, GetStageRewardReq)

    res = None
    if req.payload is not None:
        res = GetTutorialResult.get(questStageMstId=req.payload.questStageMstId)
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()
