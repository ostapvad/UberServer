import httpx
from datetime import datetime
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette import status
from .database import get_db, query_credentials
from .config import MAIN_DB_URL


app = FastAPI()
security = HTTPBasic()
database = next(get_db())


def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    """
    Performs the user authentication based on data in DB
    :param db:
    :param credentials:
    :return:
    """
    data = query_credentials(db=database, username=credentials.username, password=credentials.password)
    if not data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )

    return credentials.username


@app.get("/v1/now")
async def get_time() -> dict:
    """
    Current time endpoint
    :return:
    """
    return {"now": datetime.now().isoformat()}


@app.get("/v1/VIP/{point_in_time}", response_model=dict, dependencies=[Depends(authenticate_user)])
async def get_vip_coords(point_in_time: int):
    """
    Coordinates endpoint for the VIP user
    :param point_in_time:
    :return:
    """

    db_url = MAIN_DB_URL
    try:
        # Make a GET request with timeout

        async with httpx.AsyncClient() as client:
            response = await client.get(f"{db_url}/{point_in_time}", timeout=5.0)

        response.raise_for_status()

        data = response.json()
        print(data)
        lat = float(data["latitude"])
        long = float(data["longitude"])

        return {
            "source": "vip-db",
            "gpsCoords": {
                "lat": lat,
                "long": long
            }
        }

    except httpx.HTTPStatusError as error:
        raise HTTPException(
            status_code=error.response.status_code,
            detail=error.response.text
        )

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )
