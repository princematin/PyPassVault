from app.models.password_entry import PasswordEntry

def test_password_entry_success():
    entry = PasswordEntry(
        id= 1,
        user_id=1,
        site_name="frokade.com",
        username="frobas",
        password="frokbozorg",
        url="http//:frokade.com",
        tags=["work", "pooool"],
        created_at="2025",
        updated_at="2026"
    )

    assert entry.user_id == 1
    assert entry.password == "frokbozorg"
    assert entry.tags is not None