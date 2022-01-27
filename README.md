# LightShark-Bridge
 
This python-project enables to control the Work LightShark DMX-Console via HTTP and MIDI. 
Unlike the built-in MIDI function of the LightShark, this application also supports MIDI feedback for MIDI consoles with motorized faders like the Behringer X-Touch.



## Usage

```
pip install python-rtmidi pythonosc
```

Define the faders and executor configuration with the related MIDI CC Codes in `main.py initial_conf`


## Currently working HTTP Requests

- GET `/state`


- GET `/fader/#id`
- POST `/fader/#id/#value`


- GET `/executor/#x/#y/#z`
- POST `/executor/#x/#y/#z/#value`


- GET `/master`
- POST `/master/#value`



