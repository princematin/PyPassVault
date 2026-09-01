from  app.models.user import User


def test_set_password():
    user = User(
        user_id=1,
        first_name="Test",
        last_name="User",
        username="testuser",
        email="email@gmail.com",
        created_at="2026-09-01",
        updated_at="2026-09-01"
    )

    password = "MyPassword123!"

    user.set_password(password)

    assert user.password_hash is not None
    assert user.password_hash != password

