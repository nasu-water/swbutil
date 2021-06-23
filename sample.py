from swbutil import SwitchBotMeter
from swbutil import SwitchBotBot
from swbutil import SwitchBotCurtain
from time import sleep

#################################
### SwitchBotMeter Sample
#################################
METER_MAC_ADDR = 'YOUR_METER_MAC_ADDR'
meter = SwitchBotMeter(METER_MAC_ADDR)

# Execute scan
meter.scan()

# Get result
meter_result = meter.get_scan_data()
print(meter_result)

sleep(3)

#################################
### SwitchBotCurtain Sample
#################################
CURTAIN_MAC_ADDR = 'YOUR_CURTAIN_MAC_ADDR'
curtain = SwitchBotCurtain(CURTAIN_MAC_ADDR)

# Execute command
curtain.close()
sleep(10)
curtain.open()

sleep(5)

#################################
### SwitchBotBot Sample
#################################
BOT_MAC_ADDR = 'YOUR_BOT_MAC_ADDR'
bot = SwitchBotBot(BOT_MAC_ADDR)

# Execute command
bot.off()
sleep(3)
bot.on()
