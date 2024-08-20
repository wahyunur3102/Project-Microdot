from microdot_asyncio import Microdot, Response, send_file
from microdot_utemplate import render_template
from microdot_asyncio_websocket import with_websocket
from powerLab import POWERlab
from machine import Pin, I2C, ADC
import ujson
from boot import do_connect


I2C_ID = 1
SCL_PIN = 7
SDA_PIN = 6
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)

ip= do_connect()
print('Get IP :', ip)

app = Microdot()
Response.default_content_type = 'text/html'

l1 = POWERlab(15)
l2 = POWERlab(16)
l1.offPower()
l2.offPower()

@app.route('/')
async def index(request): 
    return render_template('index.html')

@app.route('/updateData')
async def get_sensor_data(request):
    print("Receive get data request!")
    ip= do_connect()

    return ujson.dumps({
        "ip":ip
    })

@app.route("/ws")
@with_websocket
async def kontrolButton(request, ws):
    while True:
        data = await ws.receive()
        print(data)
        if data == 'on1':
            l1.onPower()
        if data == 'off1':          
          l1.offPower()
          
        if data == 'on2':
            l2.onPower()
        if data == 'off2':
            l2.offPower()
            
        await ws.send("OK")

@app.route('/static/<path:path>')
def static(request, path):
    if '..' in path:
        # directory traversal is not allowed
        return 'Not found', 404
    return send_file('static/' + path)

@app.route('/shutdown')
async def shutdown(request):
    request.app.shutdown()
    return 'The server is shutting down...'

if __name__ == "__main__":
    app.run(debug = True, host='192.168.57.69')