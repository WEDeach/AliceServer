import os
import time
from threading import Thread

from flask import Flask

from .database import AliceDummyDatabase
from .servers.Akazukin.base import bp_aka_base
from .servers.Alice.base import bp_alice_base
from .servers.SnowWhite.base import bp_sw_base
from .utils.logger import AliceLogger
from .utils.shared import AliceShared


class AliceServer:
    """Main server instance."""

    def __init__(self, port: int = 8311) -> None:
        self.logger = AliceLogger(["Game"])

        self.port = port
        self.app = Flask(__name__)

        self.app.register_blueprint(bp_alice_base)

        self.snow_white = SnowWhiteServer()
        self.akazukin = AkazukinServer()

        # shared init
        self.shared = AliceShared.instance()
        self.shared.databese = AliceDummyDatabase.instance()

    def run(self):
        self.logger.info("Start servers 🦨🦨🦨🦨")
        self.logger.info(f"Start GameLib on {self.port} 🦨🦨🦨")
        ss = [
            Thread(target=self.app.run, args=(None, self.port)),
            Thread(target=self.snow_white.run, args=()),
            Thread(target=self.akazukin.run, args=()),
        ]

        for s in ss:
            s.daemon = True
            s.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.logger.info("server down 🦨🦨🦨🦨")


class SnowWhiteServer:
    """CDN instance."""

    def __init__(self, port: int = 8312) -> None:
        self.logger = AliceLogger(["CDN"])
        self.port = port
        self.app = Flask(__name__)

        @self.app.route("/version/ios/version_999.json")
        def json_version():
            return b'{"version":"99.9.1","reviewValidDateFrom":"2017/10/12 00:00:00","reviewValidDateTo":"2025/10/15 23:59:59"}'

        self.app.register_blueprint(bp_sw_base)

    def run(self):
        self.logger.info(f"Start CDN on {self.port}")
        try:
            self.app.run(port=self.port)
        except RuntimeError:
            self.logger.error("server down 🦨🦨🦨🦨")


class AkazukinServer:
    """Gree-Apps instance."""

    def __init__(self, port: int = 8313) -> None:
        self.logger = AliceLogger(["GreeApps"])
        self.port = port
        self.app = Flask(__name__)

        self.app.register_blueprint(bp_aka_base)

    def run(self):
        ssl_crt = os.path.join(os.path.dirname(os.path.realpath(__file__)), "cert.pem")
        ssl_key = os.path.join(os.path.dirname(os.path.realpath(__file__)), "key.pem")
        self.logger.info(f"Start Gree-Apps on {self.port} 🦨🦨🦨")
        try:
            self.app.run(port=self.port)
        except RuntimeError:
            self.logger.error("server down 🦨🦨🦨🦨")
