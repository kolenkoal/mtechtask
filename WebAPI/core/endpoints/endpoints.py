from fastapi import APIRouter, HTTPException
from starlette import status

from ..models.database import execute_query
from ..schemas.schemas import LogRequest

router = APIRouter()


@router.post("/api/data/", status_code=status.HTTP_201_CREATED)
async def process_log(request_data: LogRequest):
    """
    Функция, которая обрабатывает пришедшую строку и сохраняет ее в базу данных.
    :param request_data: {"log": "{IP-address} {HTTP Method} {URI} {HTTP Response}"}
    :return: Response
    """
    try:
        ip_address, http_method, uri, http_status = request_data.log.split()
    except ValueError:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT,
                            detail="Что-то пошло не так")

    query = """
    INSERT INTO log_entries (ip_address, http_method, uri, http_status)
    VALUES (%s, %s, %s, %s)
    RETURNING id, created_at
    """
    params = (ip_address, http_method, uri, http_status)

    try:
        result = execute_query(query, params)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT,
                            detail="Что-то пошло не так")

    if result:
        return {"message": "Лог сохранен"}
    else:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT,
                            detail="Что-то пошло не так")


@router.get("/api/data/", status_code=status.HTTP_200_OK)
async def get_logs():
    """
    Эндпоинт для извлечения всех записей журнала из базы данных.
    """
    query = """
        SELECT json_build_object(
        'id', id,
        'created', created_at,
        'log', json_build_object(
            'ip', ip_address,
            'method', http_method,
            'uri', uri,
            'status_code', http_status
        )
    ) as log
    FROM log_entries
        """
    try:
        cursor = execute_query(query)
        result = cursor.fetchall()

        cursor.close()
        return [row[0] for row in result]
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Failed to retrieve logs")
