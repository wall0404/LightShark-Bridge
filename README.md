# LightShark-Bridge
 
This python-project enables to control the Work LightShark DMX-Console via HTTP and MIDI.



## Usage

```
pip install python-rtmidi, pythonosc
```



## Currently working HTTP Requests

- GET `/state`


- GET `/fader/#id`
- POST `/fader/#id/#value`


- GET `/executor/#x/#y/#z`
- POST `/executor/#x/#y/#z/#value`


- GET `/master`
- POST `/master/#value`



