from flask import Blueprint, request


from ....game_lib.character.res_get_character_data_list import GetCharacterDataListRes
from ....game_lib.clean.req_clean_end_wave import CleanEndWaveReq
from ....game_lib.clean.req_clean_end import CleanEndReq
from ....game_lib.clean.req_clean_start import CleanStartReq
from ....game_lib.clean.req_get_cleaning_story_mst_model_list import (
    GetCleaningStoryMstModelListReq,
)
from ....game_lib.clean.res_clean_check import CleanCheckRes
from ....game_lib.clean.res_clean_end_wave import CleanEndWaveRes
from ....game_lib.clean.res_clean_end import CleanEndRes
from ....game_lib.clean.res_clean_start import CleanStartRes
from ....game_lib.clean.res_get_cleaning_story_mst_model_list import (
    GetCleaningStoryMstModelListRes,
)
from ....game_lib.req_container import ReqContainer
from ....game_lib.res_container import ResContainer


bp_api_cleaning = Blueprint("Cleaning", __name__)


@bp_api_cleaning.route("/check", methods=["POST", "GET"])
def check():
    if request.method == "POST":
        req = ReqContainer.unwrap(request.data)

    res = CleanCheckRes.get(700001)
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()


@bp_api_cleaning.route("/start", methods=["POST"])
def start():
    req = ReqContainer.unwrap(request.data, CleanStartReq)

    res = CleanStartRes()
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()


@bp_api_cleaning.route("/end", methods=["POST"])
def end():
    req = ReqContainer.unwrap(request.data, CleanEndReq)

    res = CleanEndRes()
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()


@bp_api_cleaning.route("/end_wave", methods=["POST"])
def end_wave():
    req = ReqContainer.unwrap(request.data, CleanEndWaveReq)

    # TODO: end clean wave
    res = None
    if req.payload is not None:
        res = CleanEndWaveRes.get(req.payload)
    rc = ResContainer.new(200 if res is not None else 400, res)
    return rc.dump_msgpack()


@bp_api_cleaning.route("/retire", methods=["POST"])
def retire():
    req = ReqContainer.unwrap(request.data)

    res = GetCharacterDataListRes()
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()


@bp_api_cleaning.route("/get_cleaning_story_mst_model_list", methods=["POST"])
def get_cleaning_story_mst_model_list():
    req = ReqContainer.unwrap(request.data, GetCleaningStoryMstModelListReq)

    characterUniqueId = 0
    if req.payload is not None:
        characterUniqueId = req.payload.characterUniqueId

    res = GetCleaningStoryMstModelListRes.get(characterUniqueId)
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()
