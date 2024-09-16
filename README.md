# HP_6060B
Python module for the HP 6060B 60 V 60 A electronic load.

You must use my GPIB or GPIB_WIFI module to use this module.

## Supported command:
### get_IDN()
Return the *IDN? of the instrument

### reset()
Reset the instrument to the default state

### setLoadState(on)
Set the output
<table>
  <tr><td>on</td><td>Description</td></tr>
  <tr><td>True</td><td>Enable the output</td></tr>
  <tr><td>False</td><td>Disable the output</td></tr>
</table>

### getLoadState()
Get the output state
<table>
  <tr><td>Return</td><td>Description</td></tr>
  <tr><td>True</td><td>The output is enabled</td></tr>
  <tr><td>False</td><td>The output is disabled</td></tr>
</table>

### setVoltage(volt)
Set the voltage to `volt`

### getVoltage()
Return the measured voltage or `False` in case of problem

### setCurrent(amps)
Set the current to `amps`

### getCurrent()
Return the measured current or `False` in case of problem

### setResistance(ohm)
Set the resistance to `ohm`

### getPower()
Return the measured power or `False` in case of problem

### setMode(mode)
Set the load mode
<table>
  <tr><td>mode</td><td>Description</td></tr>
  <tr><td>HP_6060B.Mode.CURRENT</td><td>Set the load to constant current</td></tr>
  <tr><td>HP_6060B.Mode.VOLTAGE</td><td>Set the load to constant voltage</td></tr>
  <tr><td>HP_6060B.Mode.RESISTANCE</td><td>Set the load to constant resistance</td></tr>
</table>

### getMode()
Get the load mode
<table>
  <tr><td>Return </td><td>Description</td></tr>
  <tr><td>HP_6060B.Mode.CURRENT</td><td>Constant current mode</td></tr>
  <tr><td>HP_6060B.Mode.VOLTAGE</td><td>Constant voltage mode</td></tr>
  <tr><td>HP_6060B.Mode.RESISTANCE</td><td>Constant resistance mode</td></tr>
</table>

### setShortMode(on)
Set the short circuit mode
<table>
  <tr><td>on</td><td>Description</td></tr>
  <tr><td>True</td><td>Short circuit mode</td></tr>
  <tr><td>False</td><td>Normal electronic load mode</td></tr>
</table>

### getShortMode()
Get the short circuit mode
<table>
  <tr><td>Return</td><td>Description</td></tr>
  <tr><td>True</td><td>Short circuit mode</td></tr>
  <tr><td>False</td><td>Normal electronic load mode</td></tr>
</table>

### setCurrentRange(currRange)
Set the current range of the load
<table>
  <tr><td>currRange</td><td>Description</td></tr>
  <tr><td>HP_6060B.CurrentRange.I6A</td><td>6A range</td></tr>
  <tr><td>HP_6060B.CurrentRange.I60A</td><td>60A range</td></tr>
</table>

### getCurrentRange()
Get the current range of the load
<table>
  <tr><td>Return</td><td>Description</td></tr>
  <tr><td>HP_6060B.CurrentRange.I6A</td><td>6A range</td></tr>
  <tr><td>HP_6060B.CurrentRange.I60A</td><td>60A range</td></tr>
</table>

### getError()
Get the last error

### local()
Go to local mode (Reenable the front panel control)

## Usage:
```python
from GPIB_WIFI import AR488_WIFI
from HP_6060B import HP_6060B

gpib = AR488_WIFI('192.168.178.36', timeout=5)
load = HP_6060B( gpib, 4)
load.setCurrentRange(HP_6060B.CurrentRange.I6A)
load.setMode(HP_6060B.Mode.CURRENT)
load.setLoadState(True)
print("Voltage:", load.getVoltage(), "V")
print("Current:", load.getCurrent(), "A")
print("Power:", load.getPower(), "W")
load.setLoadState(False)
load.local()
```
## Result of executing the above code:
```
HP 6060B address: 4
Voltage: 4.976 V
Current: 0.309 A
Power: 1.5376 W
```
