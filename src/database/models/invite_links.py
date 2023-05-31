import sqlalchemy as sa
from sqlalchemy.dialects.mysql import ENUM

from src.database.models.base import TimedBaseModel
from src.database.services.enums import UserStatusEnum


class Invite(TimedBaseModel):
    invite_id = sa.Column(sa.BIGINT, primary_key=True, autoincrement=True, nullable=False, default=1)
    user_id = sa.Column(sa.BIGINT, sa.ForeignKey('users.user_id', ondelete='SET NULL'), nullable=False)
    create_link = sa.Column(sa.VARCHAR(100), nullable=True)
    is_used = sa.Column(sa.Boolean)
    counter_invites = sa.Column(sa.BIGINT, autoincrement=True, default=0)

