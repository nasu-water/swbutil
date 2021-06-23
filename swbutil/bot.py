import binascii
from . import SwitchBotBase

class SwitchBotBot(SwitchBotBase):
    ON = binascii.a2b_hex('570101')
    OFF = binascii.a2b_hex('570102')
    PRESS = binascii.a2b_hex('570103')
    PULL = binascii.a2b_hex('570104')

    
    def on(self, retry_count=5):
        return self._execute(self.ON, retry_count)

    
    def off(self, retry_count=5):
        return self._execute(self.OFF, retry_count)

    
    def press(self, retry_count=5):
        return self._execute(self.PRESS, retry_count)

    
    def pull(self, retry_count=5):
        return self._execute(self.PULL, retry_count)
