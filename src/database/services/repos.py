from src.database.services.db_ctx import BaseRepo
from src.database.models import *


class UserRepo(BaseRepo[User]):
    model = User

    async def get_user(self, user_id: int) -> User:
        return await self.get_one(self.model.user_id == user_id)

    async def update_user(self, user_id: int, **kwargs) -> None:
        return await self.update(self.model.user_id == user_id, **kwargs)

    async def delete_user(self, user_id: int):
        return await self.delete(self.model.user_id == user_id)


class InviteRepo(BaseRepo[Invite]):
    model = Invite

    async def get_invite_user_id(self, user_id: int):
        return await self.get_one(self.model.user_id == user_id)

    async def get_invite_id(self, create_link: int):
        return await self.get_one(self.model.create_link == create_link)

    async def update_link(self, user_id: int, **kwargs) -> None:
        return await self.update(self.model.user_id == user_id, **kwargs)

