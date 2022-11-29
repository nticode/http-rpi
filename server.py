import RPi.GPIO as GPIO
from http.server import BaseHTTPRequestHandler, HTTPServer

server_ip = '' # RPi IP ADDRESS
server_port = 1011

RPi_port = 18

status = 'none'

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RPi_port, GPIO.OUT)

class MyServer(BaseHTTPRequestHandler):
  def do_POST(self):
    global status
    content_length = int(self.headers['Content-Length'])
    state = self.rfile.read(content_length).decode()
    
    if state == status:
      self.send_response(304)
     
    elif state == 'true':
      GPIO.output(RPi_port, GPIO.HIGH)
      self.send_response(201)
      status = 'true'
      
    elif state == 'false':
      GPIO.output(RPi_port, GPIO.LOW)
      self.send_response(200)
      status = 'false'
      
   self.end_headers()
  
Server = HTTPServer((server_ip, server_port), MyServer)
print('Server Online')
Server.serve_forever()
