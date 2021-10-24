from flask_office.admin.admin_blueprint import AdminBlueprint
from flask_admin.contrib.sqla import ModelView
from flask_office.models import RoomBooking, db


app = AdminBlueprint('admin2', __name__,url_prefix='/admin2',static_folder='static', static_url_path='/static/admin')
app.add_view(ModelView(RoomBooking, db.session))