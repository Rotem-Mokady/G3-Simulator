from gevent.pywsgi import WSGIServer
from app.create_app import create_app
from configs.dash import settings


app = create_app()


def main():
    http = WSGIServer(('', settings.PORT), app.server.wsgi_app)
    http.serve_forever()


if __name__ == '__main__':
    # app.run_server(host=settings.HOST, port=settings.PORT, threaded=settings.THREADED)
    main()
