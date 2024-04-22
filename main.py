import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from router import base_router, websocket_router
from settings import Settings

logger = logging.getLogger(__name__)
# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG,
#                     format='%(asctime)s.%(msecs)05d %(levelname)s - %(filename)s - line %(lineno)d - %(message)s', )
logging.basicConfig(
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s - %(filename)s - line %(lineno)d - %(message)s",
)

logger.debug("-------Server-Starting------------")


@asynccontextmanager
async def lifespan(
    app: FastAPI,
):
    # 程序启动时执行
    logger.debug("----------lifespan started----------")
    yield

    # 程序结束前执行
    logger.debug("----------lifespan end----------")


app = FastAPI(lifespan=lifespan)
app.include_router(base_router, prefix="/base")
app.include_router(websocket_router, prefix="/ws")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=Settings.PORT)
