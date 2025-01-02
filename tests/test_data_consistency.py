from src.data_ingestion import read_csv

def test_backend_and_schedule_consistency():
    backend_df = read_csv("./data/raw/allowance_backend_table.csv")
    schedule_df = read_csv("./data/raw/payment_schedule_backend_table.csv")

    assert not backend_df.empty, "The allowance backend table is empty."
    assert not schedule_df.empty, "The payment schedule table is empty."

    enabled_users = backend_df[backend_df["status"] == "enabled"]["uuid"].tolist()

    scheduled_users = schedule_df["user_id"].tolist()

    problematic_users = [user for user in scheduled_users if user not in enabled_users]

    assert problematic_users, (
        f"Schedule contains users with disabled allowances: {problematic_users}"
    )
