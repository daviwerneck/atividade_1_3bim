"""empty message

Revision ID: 7fe635616f19
Revises: 8bc1166564d5
Create Date: 2024-11-18 16:24:13.496561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7fe635616f19'
down_revision = '8bc1166564d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('paciente', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'medico', ['id_medico'], ['id_medico'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('paciente', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
