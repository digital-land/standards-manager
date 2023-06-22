"""reorganise specification dataset fields

Revision ID: a6293e8260c3
Revises: 028da4deb836
Create Date: 2023-06-22 10:37:56.735373

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "a6293e8260c3"
down_revision = "028da4deb836"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("specification_dataset_field", schema=None) as batch_op:
        batch_op.add_column(sa.Column("dataset_id", sa.Text(), nullable=False))
        batch_op.add_column(sa.Column("specification_id", sa.Text(), nullable=False))
        batch_op.add_column(sa.Column("field_id", sa.Text(), nullable=False))
        batch_op.add_column(sa.Column("entry_date", sa.Date(), nullable=True))
        batch_op.add_column(sa.Column("start_date", sa.Date(), nullable=True))
        batch_op.add_column(sa.Column("end_date", sa.Date(), nullable=True))
        batch_op.drop_constraint(
            "specification_dataset_field_dataset_fkey", type_="foreignkey"
        )
        batch_op.drop_constraint(
            "specification_dataset_field_field_fkey", type_="foreignkey"
        )
        batch_op.drop_constraint(
            "specification_dataset_field_specification_fkey", type_="foreignkey"
        )
        batch_op.create_foreign_key(
            None, "specification", ["specification_id"], ["specification"]
        )
        batch_op.create_foreign_key(None, "field", ["field_id"], ["field"])
        batch_op.create_foreign_key(None, "dataset", ["dataset_id"], ["dataset"])
        batch_op.drop_column("specification")
        batch_op.drop_column("field")
        batch_op.drop_column("dataset")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("specification_dataset_field", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("dataset", sa.TEXT(), autoincrement=False, nullable=False)
        )
        batch_op.add_column(
            sa.Column("field", sa.TEXT(), autoincrement=False, nullable=False)
        )
        batch_op.add_column(
            sa.Column("specification", sa.TEXT(), autoincrement=False, nullable=False)
        )
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.create_foreign_key(
            "specification_dataset_field_specification_fkey",
            "specification",
            ["specification"],
            ["specification"],
        )
        batch_op.create_foreign_key(
            "specification_dataset_field_field_fkey", "field", ["field"], ["field"]
        )
        batch_op.create_foreign_key(
            "specification_dataset_field_dataset_fkey",
            "dataset",
            ["dataset"],
            ["dataset"],
        )
        batch_op.drop_column("end_date")
        batch_op.drop_column("start_date")
        batch_op.drop_column("entry_date")
        batch_op.drop_column("field_id")
        batch_op.drop_column("specification_id")
        batch_op.drop_column("dataset_id")

    # ### end Alembic commands ###
