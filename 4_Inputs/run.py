import webview

class Api:
    def pyprint(self, data):
        print(data)

api=Api()
window = webview.create_window("My First App", url="web\\index.html", js_api=api)
webview.start(http_server=True, debug=True)
