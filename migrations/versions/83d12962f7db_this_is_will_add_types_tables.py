"""This is will add types tables

Revision ID: 83d12962f7db
Revises: 
Create Date: 2018-02-21 06:41:50.531000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83d12962f7db'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('social_id', sa.String(length=64), nullable=True),
    sa.Column('pwd_hash', sa.String(length=512), nullable=True),
    sa.Column('nickname', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('cdate', sa.DateTime(), nullable=True),
    sa.Column('ladate', sa.DateTime(), nullable=True),
    sa.Column('mob', sa.BigInteger(), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mob'),
    sa.UniqueConstraint('social_id')
    )
    op.create_table('EarType',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('u_id', sa.Integer(), nullable=False),
    sa.Column('EarType_name', sa.String(length=64), nullable=True),
    sa.Column('EarType_cdate', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['u_id'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_EarType_EarType_name'), 'EarType', ['EarType_name'], unique=False)
    op.create_table('Earnings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('u_id', sa.Integer(), nullable=False),
    sa.Column('Ear_per_name', sa.String(length=64), nullable=True),
    sa.Column('Ear_type_name', sa.String(length=100), nullable=True),
    sa.Column('Ear_amt', sa.Float(), nullable=True),
    sa.Column('Ear_date', sa.DateTime(), nullable=True),
    sa.Column('Ear_img', sa.Binary(), nullable=True),
    sa.Column('Ear_comm', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['u_id'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Earnings_Ear_date'), 'Earnings', ['Ear_date'], unique=False)
    op.create_index(op.f('ix_Earnings_Ear_per_name'), 'Earnings', ['Ear_per_name'], unique=False)
    op.create_index(op.f('ix_Earnings_Ear_type_name'), 'Earnings', ['Ear_type_name'], unique=False)
    op.create_table('ExpType',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('u_id', sa.Integer(), nullable=False),
    sa.Column('ExpType_name', sa.String(length=64), nullable=True),
    sa.Column('ExpType_cdate', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['u_id'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ExpType_ExpType_name'), 'ExpType', ['ExpType_name'], unique=False)
    op.create_table('Expesnes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('u_id', sa.Integer(), nullable=False),
    sa.Column('Exp_per_name', sa.String(length=64), nullable=True),
    sa.Column('Exp_type_name', sa.String(length=100), nullable=True),
    sa.Column('Exp_amt', sa.Float(), nullable=True),
    sa.Column('Exp_date', sa.DateTime(), nullable=True),
    sa.Column('Exp_comm', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['u_id'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Expesnes_Exp_date'), 'Expesnes', ['Exp_date'], unique=False)
    op.create_index(op.f('ix_Expesnes_Exp_per_name'), 'Expesnes', ['Exp_per_name'], unique=False)
    op.create_index(op.f('ix_Expesnes_Exp_type_name'), 'Expesnes', ['Exp_type_name'], unique=False)
    op.create_table('InvType',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('u_id', sa.Integer(), nullable=False),
    sa.Column('InvType_name', sa.String(length=64), nullable=True),
    sa.Column('InvType_cdate', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['u_id'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_InvType_InvType_name'), 'InvType', ['InvType_name'], unique=False)
    op.create_table('Investments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('u_id', sa.Integer(), nullable=False),
    sa.Column('Inv_per_name', sa.String(length=64), nullable=True),
    sa.Column('Inv_type_name', sa.String(length=100), nullable=True),
    sa.Column('Inv_init_amt', sa.Float(), nullable=True),
    sa.Column('Inv_mat_amt', sa.Float(), nullable=True),
    sa.Column('Inv_date', sa.DateTime(), nullable=True),
    sa.Column('Inv_mat_date', sa.DateTime(), nullable=True),
    sa.Column('Inv_due_date', sa.DateTime(), nullable=True),
    sa.Column('Inv_img', sa.Binary(), nullable=True),
    sa.Column('Inv_comm', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['u_id'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Investments_Inv_date'), 'Investments', ['Inv_date'], unique=False)
    op.create_index(op.f('ix_Investments_Inv_due_date'), 'Investments', ['Inv_due_date'], unique=False)
    op.create_index(op.f('ix_Investments_Inv_mat_date'), 'Investments', ['Inv_mat_date'], unique=False)
    op.create_index(op.f('ix_Investments_Inv_per_name'), 'Investments', ['Inv_per_name'], unique=False)
    op.create_index(op.f('ix_Investments_Inv_type_name'), 'Investments', ['Inv_type_name'], unique=False)
    op.create_table('Persons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('u_id', sa.Integer(), nullable=False),
    sa.Column('per_name', sa.String(length=64), nullable=True),
    sa.Column('per_cdate', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['u_id'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Persons_per_name'), 'Persons', ['per_name'], unique=False)
    op.create_table('Shares',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('u_id', sa.Integer(), nullable=False),
    sa.Column('Share_per_name', sa.String(length=64), nullable=True),
    sa.Column('Share_tick_name', sa.String(length=100), nullable=True),
    sa.Column('Share_Count', sa.Float(), nullable=True),
    sa.Column('Share_tran_type', sa.String(length=50), nullable=True),
    sa.Column('Share_pershare_amt', sa.Float(), nullable=True),
    sa.Column('Share_inv_sell_date', sa.DateTime(), nullable=True),
    sa.Column('Share_img', sa.Binary(), nullable=True),
    sa.Column('Share_comm', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['u_id'], ['Users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Shares_Share_inv_sell_date'), 'Shares', ['Share_inv_sell_date'], unique=False)
    op.create_index(op.f('ix_Shares_Share_per_name'), 'Shares', ['Share_per_name'], unique=False)
    op.create_index(op.f('ix_Shares_Share_tick_name'), 'Shares', ['Share_tick_name'], unique=False)
    op.create_index(op.f('ix_Shares_Share_tran_type'), 'Shares', ['Share_tran_type'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Shares_Share_tran_type'), table_name='Shares')
    op.drop_index(op.f('ix_Shares_Share_tick_name'), table_name='Shares')
    op.drop_index(op.f('ix_Shares_Share_per_name'), table_name='Shares')
    op.drop_index(op.f('ix_Shares_Share_inv_sell_date'), table_name='Shares')
    op.drop_table('Shares')
    op.drop_index(op.f('ix_Persons_per_name'), table_name='Persons')
    op.drop_table('Persons')
    op.drop_index(op.f('ix_Investments_Inv_type_name'), table_name='Investments')
    op.drop_index(op.f('ix_Investments_Inv_per_name'), table_name='Investments')
    op.drop_index(op.f('ix_Investments_Inv_mat_date'), table_name='Investments')
    op.drop_index(op.f('ix_Investments_Inv_due_date'), table_name='Investments')
    op.drop_index(op.f('ix_Investments_Inv_date'), table_name='Investments')
    op.drop_table('Investments')
    op.drop_index(op.f('ix_InvType_InvType_name'), table_name='InvType')
    op.drop_table('InvType')
    op.drop_index(op.f('ix_Expesnes_Exp_type_name'), table_name='Expesnes')
    op.drop_index(op.f('ix_Expesnes_Exp_per_name'), table_name='Expesnes')
    op.drop_index(op.f('ix_Expesnes_Exp_date'), table_name='Expesnes')
    op.drop_table('Expesnes')
    op.drop_index(op.f('ix_ExpType_ExpType_name'), table_name='ExpType')
    op.drop_table('ExpType')
    op.drop_index(op.f('ix_Earnings_Ear_type_name'), table_name='Earnings')
    op.drop_index(op.f('ix_Earnings_Ear_per_name'), table_name='Earnings')
    op.drop_index(op.f('ix_Earnings_Ear_date'), table_name='Earnings')
    op.drop_table('Earnings')
    op.drop_index(op.f('ix_EarType_EarType_name'), table_name='EarType')
    op.drop_table('EarType')
    op.drop_table('Users')
    # ### end Alembic commands ###
