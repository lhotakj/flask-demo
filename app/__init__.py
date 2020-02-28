from .routes.front import front
from .routes.secure import secure
from .routes.static import static
from .routes.api import api
from .app import app

app.register_blueprint(front)
app.register_blueprint(secure)
app.register_blueprint(static)
app.register_blueprint(api)
