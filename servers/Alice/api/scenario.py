from flask import Blueprint, request


from ....game_lib.req_container import ReqContainer
from ....game_lib.res_container import ResContainer
from ....game_lib.scenario.req_get_scenario_story_mst import GetScenarioStoryMstReq
from ....game_lib.scenario.res_get_scenario_story_mst import GetScenarioStoryMstRes


bp_api_scenario = Blueprint("Scenario", __name__)


@bp_api_scenario.route("/get_quest_story_mst_list", methods=["POST"])
def get_quest_story_mst_list():
    req = ReqContainer.unwrap(request.data, GetScenarioStoryMstReq)

    storyIndex = 0
    storyNo = 0
    if req.payload is not None:
        storyIndex = req.payload.storyIndex
        storyNo = req.payload.storyNo

    res = GetScenarioStoryMstRes.get(storyIndex, storyNo)
    rc = ResContainer.new(200, res)
    return rc.dump_msgpack()
