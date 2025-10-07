


def format_mention_html(user):
    """Create a clickable mention for a user."""
    return f'<a href="tg://user?id={user.id}">{user.full_name()}</a>'