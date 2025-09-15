from myproject.company.utils import add_user_to_company, add_user_to_group, create_user


def create_users(company, users_data, is_active=False, joined_at=None):
    for ud in users_data:
        user = create_user(
            name=ud['name'],
            email=ud['email'],
            is_active=is_active,
            joined_at=joined_at,
        )

        add_user_to_company(company.id, user_id=user.id)

        for grp in ud['groups']:
            add_user_to_group(company.id, user.id, group_id=grp.get('id'))
