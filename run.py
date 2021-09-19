from app.create_app import create_app
from configs.dash import settings


app = create_app()

if __name__ == '__main__':
    app.run_server(host=settings.HOST, port=settings.PORT)

