Picon is  Raspberry Zero 1 wh , that I had no use for. So I added it to my 3D printer as second web camera. Is powered only when 3D printer is.


What is on it:

- Connected LED strip via gpio

- Connected raspberry camera

- Apache website with python-cgi enabled

  - password protected

   - cgi base on get trigger LED ON or OFF  (octoprint server run wget toward picon)

   - entry webpage with all the urls for simplicity

- Ustreamer to stream the content from the rpi camera



Is planeed in the future:

- Connected servo to try to kick object from hotbed

- Connected filament detection thing to get a notification before printer detect it

   - via ntfy get push notification

    - filament detection thing is bought, just not implemented due to short cable

- Now I use wget as trigger executed from home assistant.

    - Would like to go more native control via home assistant

- As power on/off is utilized without correct shutdown, making a script to re-copy all in case of failure of storage (bad SD, corrupt data)

    - maybe use ansible