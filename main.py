from starlette.applications import Starlette
from starlette.routing import Route
from handlers.user_handler import *
from handlers.role_handler import *
from db.db_setup import engine
from handlers.utils.models import user,courses
# Base.metadata.drop_all(bind=engine)
# user.Base.metadata.create_all(bind=engine)
# courses.Base.metadata.create_all(bind=engine)

routes=[


Route("/users", endpoint=read_users, methods=["GET"]),
Route( "/users", endpoint= create_new_user, methods = ["POST"]), 
Route("/users/{user_id}", endpoint=read_user, methods= ["GET"]),
Route("/users/{user_id}/courses" , endpoint= read_user_courses, methods= ["GET"]),
Route("/roles", endpoint=read_roles, methods=["GET"]),
Route( "/roles", endpoint= create_new_role, methods = ["POST"]),
Route( "/roles/{role_id}", endpoint= read_role, methods = ["GET"]),
Route("/users/{user_id}/roles/{role_id}" , endpoint=add_user_roles, methods= ["POST"]),
]

app = Starlette(debug=True, routes=routes)



