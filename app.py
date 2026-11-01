from http.server import BaseHTTPRequestHandler, HTTPServer


def get_message():
    return "Hello from DVP Week 12 CI/CD Pipeline!"


def add_numbers(a, b):
    return a + b


class AppHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        message = get_message()

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

    def log_message(self, format, *args):
        print(format % args)


if __name__ == "__main__":
    print("Starting DVP Week 12 application on port 8000...")
    server = HTTPServer(("0.0.0.0", 8000), AppHandler)
    server.serve_forever()
