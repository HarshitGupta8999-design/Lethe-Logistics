
import os
import sys
import io

from dotenv import load_dotenv
from supabase import create_client

# Support UTF-8 output in Windows terminal
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(
        sys.stdout.buffer,
        encoding="utf-8",
        errors="replace"
    )

# Load environment variables from project-root .env
load_dotenv()

URL = os.getenv("SUPABASE_URL")
KEY = os.getenv("SUPABASE_KEY")
TEST_EMAIL = os.getenv("TEST_USER_EMAIL")
TEST_PASSWORD = os.getenv("TEST_USER_PASSWORD")

# Validate required configuration
required_vars = {
    "SUPABASE_URL": URL,
    "SUPABASE_KEY": KEY,
    "TEST_USER_EMAIL": TEST_EMAIL,
    "TEST_USER_PASSWORD": TEST_PASSWORD,
}

missing_vars = [
    name for name, value in required_vars.items() if not value
]

if missing_vars:
    raise ValueError(
        "Missing environment variables: " + ", ".join(missing_vars)
    )

client = create_client(URL, KEY)

try:
    # Check test user's organisation
    print("Test user organisation:")

    response = client.auth.sign_in_with_password({
        "email": TEST_EMAIL,
        "password": TEST_PASSWORD,
    })

    if not response.user:
        raise RuntimeError("Test user login failed.")

    uid = response.user.id

    profile = (
        client.schema("identity_mod")
        .table("users")
        .select("org_id, organisations(org_name, org_type)")
        .eq("user_id", uid)
        .single()
        .execute()
    )

    print(f"  org_id: {profile.data['org_id']}")
    print(f"  org:    {profile.data['organisations']}")

    client.auth.sign_out()

    # Check batch counts per manufacturer
    print("\nBatch counts per manufacturer_id:")

    batches = (
        client.schema("product_and_batch_intelligence")
        .table("batch_master")
        .select("batch_id, manufacturer_id")
        .execute()
        .data
    )

    counts = {}

    for batch in batches:
        manufacturer_id = batch["manufacturer_id"]
        counts[manufacturer_id] = (
            counts.get(manufacturer_id, 0) + 1
        )

    for manufacturer_id, count in counts.items():
        print(
            f"  manufacturer_id={manufacturer_id} -> {count} batches"
        )

    # List manufacturer organisations
    print("\nAll Manufacturer organisations:")

    organisations = (
        client.schema("identity_mod")
        .table("organisations")
        .select("org_id, org_name, org_type")
        .eq("org_type", "Manufacturer")
        .execute()
        .data
    )

    for organisation in organisations:
        print(
            f"  {organisation['org_name']} "
            f"({organisation['org_id']})"
        )

finally:
    client.auth.sign_out()
