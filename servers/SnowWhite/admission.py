from flask import Blueprint

from ...amdission.admission_config import AdmissionConfig, AdmissionStatusType

bp_sw_admission = Blueprint("Admission", __name__)


@bp_sw_admission.route("/admission_status.json.gzip")
def admission_status():
    ins = AdmissionConfig(
        status=AdmissionStatusType.AllThrough,
    )
    return ins.dump_gzip()
