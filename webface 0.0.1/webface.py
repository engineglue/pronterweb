import threading
import webbrowser
import BaseHTTPServer
import SimpleHTTPServer
import printcore

FILE = './www/'
PORT = 8080


class webface(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.getheader('content-length'))        
        data_string = self.rfile.read(length)
        self.wfile.write(data_string)


def open_browser():
    def _open_browser():
        webbrowser.open('http://localhost:%s/%s' % (PORT, FILE))
    thread = threading.Timer(0.5, _open_browser)
    thread.start()

def start_server():
    server_address = ("", PORT)
    server = BaseHTTPServer.HTTPServer(server_address, webface)
    server.serve_forever()

if __name__ == "__main__":
    open_browser()
    start_server()