import json
import os
from typing import Dict, List

from flask import Blueprint, request

from ....database import MstTable, MstTableVersions
from ....game_lib.mst.record_mst_version_summary import MstVersionSummaryRecord
from ....game_lib.mst.req_mst_version import MstVersionReq
from ....game_lib.mst.res_mst_version import MstVersionRes
from ....game_lib.req_container import ReqContainer
from ....game_lib.res_container import ResContainer

bp_api_mst = Blueprint("Mst", __name__)


@bp_api_mst.route("/check_mst_version", methods=["POST", "GET"])
def check_mst_version():
    cl_msts: Dict[int, int] = {}
    if request.method == "POST":
        req = ReqContainer.unwrap(request.data, MstVersionReq)

        if req.payload:
            for i in req.payload.mstVersionSummaryList:
                cl_msts[i.mstTableId] = i.version

    server_msts: List[MstVersionSummaryRecord] = []
    for i in MstTableVersions:
        if i["mstTableId"] in cl_msts:
            if cl_msts[i["mstTableId"]] >= i["version"]:
                continue
        server_msts.append(MstVersionSummaryRecord(**i))

    res = MstVersionRes(
        lastMstVersionCreatedTime=1733088606,
        lastCreatedTime="2024-06-30 13:00:00",
        mstVersionSummaryList=server_msts,
    )
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()


@bp_api_mst.route("/get_<mst_table_name>_mst_list", methods=["POST", "GET"])
def get_mst_list(mst_table_name: str):
    if request.method == "POST":
        req = ReqContainer.unwrap(request.data)

    dummy_table_file_key = f"{mst_table_name}.json"
    dummy_table_file_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "dummy_tables",
        dummy_table_file_key,
    )
    table_key = mst_table_name + "_mst"
    if table_key in MstTable:
        mstTableId = MstTable[mst_table_name + "_mst"]
        mstVersionSummary = None
        for i in MstTableVersions:
            if i["mstTableId"] == mstTableId:
                mstVersionSummary = i
        if mstVersionSummary is None:
            raise ValueError(f"Mst Version not found: {mstTableId}")
    else:
        raise ValueError(f"Mst Table not found: {table_key}")
    if os.path.exists(dummy_table_file_path):
        with open(dummy_table_file_path, encoding="utf-8") as f:
            d = json.loads(f.read())

            float_patch_key = {
                "movie_resource": ["vibStartTime"],
                "navigator_talk": [
                    "leftPositionX",
                    "leftPositionY",
                    "rightPositionX",
                    "rightPositionY",
                ],
                "quest_card_bonus_reward_drop_rate": [
                    "addRateWhenNoLimitBreak",
                    "addRateWhenOneLimitBreak",
                    "addRateWhenTwoLimitBreak",
                    "addRateWhenThreeLimitBreak",
                    "addRateWhenMaxLimitBreak",
                ],
                "quest_campaign": ["campaignValue"],
            }
            if mst_table_name in float_patch_key:
                # patch float
                for i in d:
                    for pk in float_patch_key[mst_table_name]:
                        if pk in i:
                            i[pk] = float(i[pk])
            if mst_table_name == "resource_file":
                total_size = 0
                for i in d:
                    total_size += i["androidFileSize"]

            rc = ResContainer.new(
                200,
                {
                    "mstList": d,
                    "mstVersionSummary": mstVersionSummary,
                    "isForceUpdate": True,
                },
            )
            return rc.dump_msgpack()
    raise ValueError
