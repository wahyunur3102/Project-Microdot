from microdot_asyncio import Microdot, Response, send_file
from microdot_utemplate import render_template
from bme_module import BME280Module
import sh1106
from machine import Pin, I2C, ADC
import ujson
from boot import do_connect


I2C_ID = 1
SCL_PIN = 7
SDA_PIN = 6
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)

ip= do_connect()
print('Get IP :', ip)


bme_module = BME280Module(I2C_ID,SCL_PIN,SDA_PIN)
display = sh1106.SH1106_I2C(128, 64, i2c, Pin(2), 0x3c)

app = Microdot()
Response.default_content_type = 'text/html'

def update_display(temp):
    try:
        display.fill(0)  # Clear the display
        display.hline(0, 0, 127, 1) #atas monitoring
        display.hline(0, 12, 127, 1) #bawah monitoring
        display.hline(0, 25, 127, 1) #atas status
        display.hline(0, 37, 127, 1) #bawah status
        display.hline(0, 63, 127, 1) #bawah ip
        display.hline(0, 53, 127, 1) #line atas ip
        display.vline(0, 0, 65, 1) #status kiri
        display.vline(127, 0, 65, 1) #status kanan
        display.fill_rect(0, 37, 5, 30, 1) # border kiri
        display.fill_rect(123, 37, 5, 30, 1) #border kanan
        display.text('Monitoring', 23, 3)
        display.text(f'T:{temp:.0f}C',0, 15)
        #display.text(f'Co:{co:.1f} PM', 45, 15)
        display.text(f'Status',43, 28)
        #display.text(f'{status}',14, 42)
        display.text(f'{ip}', 10, 55)
        display.show()
    except Exception as e:
        print("Error updating display:", e)
   
@app.route('/')
async def index(request): 
    return render_template('index.html')

@app.route('/updateData')
async def get_sensor_data(request):
    print("Receive get data request!")
    ip= do_connect()
    sensor_reads_temp, sensor_reads_press, sensor_reads_hum, sensor_reads_alt = bme_module.get_sensor_readings()
    update_display(sensor_reads_temp)
    
    return ujson.dumps({
        "readingTemp": sensor_reads_temp, 
        "readingHum": sensor_reads_hum,
        "ip":ip
    })

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
    app.run(debug = True, host='192.168.59.15')