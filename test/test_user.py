from flask_login import AnonymousUserMixin
from app.role import Role

class TestUser(AnonymousUserMixin):
    id = None
    role = Role.WRITER.value