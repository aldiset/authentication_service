from pydantic import BaseModel


class RolePermissionSchema(BaseModel):
    role_id: int
    permission: int
