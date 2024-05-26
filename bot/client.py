# (c) @AbirHasan2005
from typing import Union
from pyromod import listen
from pyrogram import Client as RawClient
from pyrogram.storage import Storage
from configs import Config
from bot.core.new import New
import ntplib

LOGGER = Config.LOGGER
log = LOGGER.getLogger(__name__)

class Client(RawClient, New):
    """ Custom Bot Class """

    def __init__(self, session_name: Union[str, Storage] = "RenameBot"):
        super().__init__(
            session_name,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(
                root="bot/plugins"
            )
        )

    async def start(self):
        await self.sync_time()
        await super().start()
        log.info("Bot Started!")

    async def stop(self, *args):
        await super().stop()
        log.info("Bot Stopped!")

    async def sync_time(self):
        ntp_client = ntplib.NTPClient()
        response = ntp_client.request('pool.ntp.org')
        ntp_time = response.tx_time
        await self.set_time(int(ntp_time))

    async def set_time(self, ntp_time):
        await self.set_time_offset(ntp_time - time.time())

    async def set_time_offset(self, offset):
        self._time_offset = offset

# Assuming you import `time` somewhere in your code
import time
