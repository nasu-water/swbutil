## swbutil

This is a simple SwitchBot, SwitchBot Curtain, SwitchBot Meter operation commands.   
You don't have to know anything about Bluetooth specifications to use this.   
The only thing you need to know is the MAC address of the SwitchBot device.   

### Install

```bash
$ sudo apt install libbluetooth3-dev libglib2.0 libboost-python-dev libboost-thread-dev  
$ pip3 install git+https://github.com/nasu-water/swbutil#egg=swbutil
```

### Usage

#### SwitchBot Bot (SwitchBot)
```python
from swbutil import SwitchBotBot
bot = SwitchBotBot(BOT_MAC_ADDR)

# Execute command
bot.off()
bot.on()
bot.pull()
bot.push()

```

#### SwitchBot Curtain
```python
rom swbutil import SwitchBotCurtain
curtain = SwitchBotCurtain(CURTAIN_MAC_ADDR)

# Execute command
curtain.close()
curtain.open()

```

#### SwitchBot Meter
```python
from swbutil import SwitchBotMeter
meter = SwitchBotMeter(METER_MAC_ADDR)

# Scan
meter.scan()

# Get result
meter_result = meter.get_scan_data()

```

swbutil uses `bluepy`, and it won't work unless you run in superuser.

### Environment & Softwares
- Python 3.8.0
- Raspberry Pi 4 / Raspbian 10

 For more details, please refer `Pipfile` and `Pipfile.lock`.
