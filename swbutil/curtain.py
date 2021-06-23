import binascii
from . import SwitchBotBase

class SwitchBotCurtain(SwitchBotBase):
    OPEN = binascii.a2b_hex('570F450105FF00')
    CLOSE = binascii.a2b_hex('570f450105FF64')
    
    def open(self, retry_count=5):
        return self._execute(self.OPEN, retry_count)

    
    def close(self, retry_count=5):
        return self._execute(self.CLOSE, retry_count)
