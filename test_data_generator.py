# test_data_generator.py
from faker import Faker
import pandas as pd

def generate_test_data(num_records=100, output_file="test_data.csv"):
    """Generate fake user data for QA testing and save to CSV."""
    fake = Faker()
    data = {
        "user_id": [], "full_name": [], "email": [],
        "phone_number": [], "address": [], "birth_date": []
    }
    for i in range(num_records):
        data["user_id"].append(i + 1)
        data["full_name"].append(fake.name())
        data["email"].append(fake.email())
        data["phone_number"].append(fake.phone_number())
        data["address"].append(fake.address().replace("\n", ", "))
        data["birth_date"].append(fake.date_of_birth(minimum_age=18, maximum_age=80).strftime("%Y-%m-%d"))
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    print(f"Generated {num_records} records and saved to {output_file}")

if __name__ == "__main__":
    generate_test_data(num_records=100, output_file="test_data_output.csv")