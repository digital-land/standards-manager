"""reorganise spefication dataset

Revision ID: 028da4deb836
Revises: d562be7d5919
Create Date: 2023-06-08 17:29:57.540417

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "028da4deb836"
down_revision = "d562be7d5919"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("specification_dataset", schema=None) as batch_op:
        batch_op.add_column(sa.Column("dataset_id", sa.Text(), nullable=False))
        batch_op.add_column(sa.Column("specification_id", sa.Text(), nullable=False))
        batch_op.add_column(sa.Column("guidance", sa.Text(), nullable=True))
        batch_op.drop_constraint(
            "specification_dataset_dataset_fkey", type_="foreignkey"
        )
        batch_op.drop_constraint(
            "specification_dataset_specification_fkey", type_="foreignkey"
        )
        batch_op.create_foreign_key(
            None, "specification", ["specification_id"], ["specification"]
        )
        batch_op.create_foreign_key(None, "dataset", ["dataset_id"], ["dataset"])
        batch_op.drop_column("dataset")
        batch_op.drop_column("specification")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("specification_dataset", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("specification", sa.TEXT(), autoincrement=False, nullable=False)
        )
        batch_op.add_column(
            sa.Column("dataset", sa.TEXT(), autoincrement=False, nullable=False)
        )
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.create_foreign_key(
            "specification_dataset_specification_fkey",
            "specification",
            ["specification"],
            ["specification"],
        )
        batch_op.create_foreign_key(
            "specification_dataset_dataset_fkey", "dataset", ["dataset"], ["dataset"]
        )
        batch_op.drop_column("guidance")
        batch_op.drop_column("specification_id")
        batch_op.drop_column("dataset_id")

    # ### end Alembic commands ###
