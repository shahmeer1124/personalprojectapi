"""second migration

Revision ID: 1688d6e48642
Revises: 4d88294ed1a7
Create Date: 2023-02-22 02:09:08.977678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1688d6e48642'
down_revision = '4d88294ed1a7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('hotel_pictures',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('picture', sa.String(), nullable=False),
        sa.Column('hotel_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['hotel_id'], ['posts.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('posts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('location', sa.String(), nullable=False),
        sa.Column('mobile_number', sa.String(), nullable=False),
        sa.Column('view_count', sa.Integer(), nullable=True),
        sa.Column('google_maps_location', sa.String(), nullable=True),
        sa.Column('hotel_pic', sa.String(), nullable=False),
        sa.Column('hotel_type', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('owner_id', sa.Integer(), nullable=False),
        sa.UniqueConstraint('owner_id'),
        sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('phone_number', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('phone_number')
    )
    op.create_table('hotel_features',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('parking', sa.Boolean(), nullable=False),
        sa.Column('child_playarea', sa.Boolean(), nullable=False),
        sa.Column('ground_lighting', sa.Boolean(), nullable=False),
        sa.Column('chiller', sa.Boolean(), nullable=False),
        sa.Column('sound_system', sa.Boolean(), nullable=False),
        sa.Column('bridal_system', sa.Boolean(), nullable=False),
        sa.Column('hotel_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['hotel_id'], ['posts.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('packages',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('package_name', sa.String(), nullable=False),
        sa.Column('charges_per_head_without_food', sa.String(), nullable=False),
        sa.Column('charges_per_head_with_food', sa.String(), nullable=False),
        sa.Column('food_served', sa.String(), nullable=False),
        sa.Column('free_wifi', sa.Boolean(), nullable=False),
        sa.Column('stage_decoration', sa.Boolean(), nullable=False),
        sa.Column('sound_system', sa.Boolean(), nullable=False),
        sa.Column('ground_lighting', sa.Boolean(), nullable=False),
        sa.Column('bridal_room', sa.Boolean(), nullable=False),
        sa.Column('free_parking', sa.Boolean(), nullable=False),
        sa.Column('chiller', sa.Boolean(), nullable=False),
        sa.Column('heater', sa.Boolean(), nullable=False),
        sa.Column('hotel_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['hotel_id'], ['posts.id'], ),
        sa.PrimaryKeyConstraint('id')
    )




def downgrade():
    op.drop_table('packages')
