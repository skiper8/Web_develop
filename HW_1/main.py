from http.server import BaseHTTPRequestHandler, HTTPServer
import json

hostName = 'localhost'
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def load_json(self):
        with open('list.json', 'r') as json_file:
            return json.load(json_file)

    def do_POST(self):
        self.send_response(201)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes('[]', "UTF-8"))

    def do_GET(self):
        json_data = self.load_json()
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(json.dumps(json_data), "UTF-8"))


wedServer = HTTPServer((hostName, serverPort), MyServer)
print("Server started http://%s:%s" % (hostName, serverPort))
try:
    wedServer.serve_forever()
except KeyboardInterrupt:
    pass
