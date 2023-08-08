from fastapi import APIRouter
from app.uds.utils import find_user

router = APIRouter()


@router.get(
    path="/operation"
)
def make_operation(total, number: str, code: str):
    """
    Получаем на ввод код из телефона или номер телефона, ищем клиента,
    """
    user = find_user(number, code)
    return user
