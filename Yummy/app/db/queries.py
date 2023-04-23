QUERIES = {
    'add_user': '''INSERT INTO user(telegram_id, full_name) VALUES(?, ?)''',
    'deactivate_user': 'DELETE FROM user WHERE user_id=(?)',

}
