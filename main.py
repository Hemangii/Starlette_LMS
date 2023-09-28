from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import PlainTextResponse, JSONResponse

async def index(request):
    return JSONResponse({"message": "Hello World"})
    # return PlainTextResponse("Hi Starlette!")

routes=[ Route("/", endpoint=index, methods=["GET"])]
app= Starlette(debug=True, routes=routes)