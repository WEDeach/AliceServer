from dataclasses import dataclass

from .value_client_resource_management_config import ClientResourceManagementConfigValue
from ..res_base import BaseRes


@dataclass
class GetClientResourceManagementConfigRes(BaseRes):
    clientResourceManagementConfig: ClientResourceManagementConfigValue
