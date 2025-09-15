import datetime
from myproject.users.utils import create_users
from myproject.company.utils import create_company


def main():
    acme = create_company('ACME Inc.')
    acme_users = json.load('/tmp/acme_users.json')
    joined_at = datetime.now()
    create_users(acme, acme_users, joined_at)
