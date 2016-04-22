# Logentries Big Panda integration

A Python twisted proxy server that receives, modifies and then forwards Webhook alerts from Logentries to BigPandas REST api endpoint.


Usage

• Download script

• Edit script to replace Header key and App key and with your own, as well as desired port (default 10000)

• Keys can be found when creating a new REST alert api integration in Bigpanda UI.

• Run the twisted proxy server `sudo twistd -y bigpanda_proxy.py`

• In Logentries, modify alert webhook url e.g. `http://127.0.0.1:10000/form` replacing with your ip and port

• Trigger a test Logentries alert and view your Bigpando.io UI.


