from fastapi import FastAPI, APIRouter

from views import converter_router


app = FastAPI()
router = APIRouter()

app.include_router(prefix='', router=router)
app.include_router(converter_router)
