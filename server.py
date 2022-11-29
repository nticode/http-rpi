import RPi.GPIO as GPIO
from http.server import BaseHTTPRequestHandler, HTTPServer

server_ip = '' # RPi IP ADDRESS
server_port = 1011

RPi_port = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(RPi_port, GPIO.OUT)

class MyServer(BaseHTTPRequestHandler):
  def do_POST(self):
    global status
    content_length = int(self.headers['Content-Length'])
    state = self.rfile.read(content_length).decode()
    
    if state == 'true':
      GPIO.output(RPi_port, GPIO.HIGH)
      
    elif state == 'false':
      GPIO.output(RPi_port, GPIO.LOW)
   
  self.send_response(200)
  self.end_headers()
  
Server = HTTPServer((server_ip, server_port), MyServer)
print('Server Online')
Server.serve_forever()
