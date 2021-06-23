from bluepy.btle import Peripheral
from time import sleep

class SwitchBotBase:
    
    SWITCH_BOT_UUID_1 = 'cba20d00-224d-11e6-9fb8-0002a5d5c51b'
    SWITCH_BOT_UUID_2 = 'cba20002-224d-11e6-9fb8-0002a5d5c51b'
    
    def __init__(self, mac_addr):
        self.mac_addr = mac_addr

    def _execute(self, command, retry_count):
        status = False

        for connection_count in range(retry_count):
            try:
                peripheral = Peripheral(self.mac_addr, 'random')
                hand_service = peripheral.getServiceByUUID(self.SWITCH_BOT_UUID_1)
                hand = hand_service.getCharacteristics(self.SWITCH_BOT_UUID_2)[0]
                hand.write(command)
                peripheral.disconnect()
                status = True
                break
            except Exception as e:
                sleep(0.5)
                continue

        return status
