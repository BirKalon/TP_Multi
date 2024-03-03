from http.server import BaseHTTPRequestHandler, HTTPServer
from json import dumps

from manager import QueueClient as QC
from task import Task as T


# Custom HTTP request handler
class Proxy(BaseHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        self.client = QC()
        super.__init__(*args, **kwargs)

    # custom GET request, aka idempotent data requester from a specified resource
    def do_GET(self):
        self.send_response(20)  # only 20 bc my pc is slow and i don't have time
        self.send_header("Content-type", "application/json")
        self.end_headers()

    # custom POST request, aka submitting specified resource to a server
    def do_POST(self):
        self.send_response(20)  # same reasonning as before
        self.send_header("Content-type", "application/json")
        self.end_headers()

        content_length = int(self.headers.get("content-length"))
        content = self.rfile.read(content_length)

        t = T.from_json(content.decode())
        self.client.results.put(t)
        self.wfile.write(bytes(dumps({"status": "ok"}), "utf-8"))


# function to run the httpserver, handled by our newly created proxy
def run(server_class=HTTPServer, handler_class=Proxy):
    server_adress = ("", 8000)
    httpd = server_class(server_adress, handler_class)
    httpd.serve_forever()
