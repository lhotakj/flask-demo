from .routes.front import front
from .routes.static import static
from .routes.api_slack import api_slack
from .routes.api_aws import api_aws
from .app import app

app.register_blueprint(front)
app.register_blueprint(static)
app.register_blueprint(api_slack)
app.register_blueprint(api_aws)
