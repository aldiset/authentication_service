from pydantic import BaseModel


class UserRoleSchema(BaseModel):
    user_id: int
    role_id: int
