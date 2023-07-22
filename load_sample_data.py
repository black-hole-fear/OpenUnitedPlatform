import os
import datetime
import django
from django.apps import apps
import json
from utility.utils import *

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "openunited.settings")
django.setup()

from talent.models import Person, Skill, Expertise, PersonSkill
from commerce.utils import CurrencyTypes, PaymentTypes
from security.models import User
from commerce.services import (
    OrganisationService,
    OrganisationAccountService,
    OrganisationAccountCreditService,
    CartService,
    PointPriceConfigurationService,
)
from security.services import UserService
from talent.services import PersonService


def load_reference_data(classname):
    klass = eval(classname.capitalize())
    klass.objects.all().delete()
    file = os.path.abspath("utility/reference_data/" + classname + ".json")
    with open(file) as json_file:
        data_set = json.load(json_file)
        for data in data_set:
            obj = klass(**data)
            obj.save()


def clear_rows_by_model_name(model_names_mapping: dict) -> None:
    for model_name, app_name in model_names_mapping.items():
        model = apps.get_model(app_name, model_name)
        model.objects.all().delete()


proceed = input(
    "Running this script will replace all your current data. Ok? (Y/N)"
).lower()

if len(proceed) == 0:
    fancy_out("Execution Abandoned")
    exit()

if proceed[0] != "y":
    fancy_out("Stopped at your request")
    exit()
else:
    d = {
        "Organisation": "commerce",
        "OrganisationAccount": "commerce",
        "OrganisationAccountCredit": "commerce",
        "Cart": "commerce",
        "Person": "talent",
        "User": "security",
    }

    fancy_out(f"Delete all the records of the following models: {d.keys()}")
    # Deletes all the existing records before populating sample data according to the dictionary
    clear_rows_by_model_name(d)

    fancy_out("Create User & Person records")

    user_data = [
        {
            "email": "test+gary@openunited.com",
            "username": "garyg",
            "password": "123456789",
        },
        {
            "email": "test+shirley@openunited.com",
            "username": "shirleyaghost",
            "password": "123456789",
        },
    ]

    users = []
    user_service = UserService()
    for ud in user_data:
        user = user_service.create(
            email=ud.get("email"),
            username=ud.get("username"),
            password=ud.get("password"),
        )

        users.append(user)

    person_data = [
        {
            "full_name": "Gary Test",
            "preferred_name": "Gary",
            "headline": "Lorem ipsum sit amet",
        },
        {
            "full_name": "Shirley Test",
            "preferred_name": "Shirley",
            "headline": "Lorem ipsum sit amet",
        },
    ]

    # len(person_data) and len(user_datas) must be equal
    persons = []
    person_service = PersonService()
    for index, pd in enumerate(person_data):
        person = person_service.create(
            user=users[index],
            full_name=pd.get("full_name"),
            preferred_name=pd.get("preferred_name"),
            headline=pd.get("headline"),
            send_me_bounties=False,
            test_user=True,
        )

        persons.append(person)

    # Temporarily commented-out

    # fancy_out("Setup Skills & Expertise records")

    # load_reference_data("skill")
    # load_reference_data("expertise")

    # fancy_out("Create PersonSkill records")

    # # Skill: Full-stack Development
    # full_stack_development = Skill.objects.get(pk=106)

    # # Expertise: Django
    # django_expertise = Expertise.objects.get(pk=33)

    # gary_skill = PersonSkill(
    #     person=gary,
    #     skill=full_stack_development.ancestry(),
    #     expertise=django_expertise.ancestry(),
    # )
    # gary_skill.save()

    fancy_out("Create Organisation records")

    usernames = [
        "organisation_1",
        "organisation_2",
        "organisation_3",
        "organisation_4",
        "organisation_5",
    ]
    organisations = []
    organisation_service = OrganisationService()
    for username in usernames:
        organisations.append(organisation_service.create(username, username))

    fancy_out("Create OrganisationAccount records")

    organisation_accounts = []
    organisation_account_service = OrganisationAccountService()
    for organisation in organisations:
        # TODO: replace the below 0's with random numbers
        organisation_accounts.append(
            organisation_account_service.create(organisation, 0, 0)
        )

    organisation_account_credits = []
    organisation_account_credit_service = OrganisationAccountCreditService()
    for organisation_account in organisation_accounts:
        # TODO: replace the below 0 with a random number
        organisation_account_credits.append(
            organisation_account_credit_service.create(organisation_account, 0)
        )

    fancy_out("Create a PointPriceConfiguration record")

    point_price_conf_service = PointPriceConfigurationService()
    point_price_conf_service.create(
        applicable_from_date=datetime.date.today(),
        usd_point_inbound_price_in_cents=1,
        eur_point_inbound_price_in_cents=1,
        gbp_point_inbound_price_in_cents=1,
        usd_point_outbound_price_in_cents=2,
        eur_point_outbound_price_in_cents=2,
        gbp_point_outbound_price_in_cents=2,
    )

    fancy_out("Create Cart records")

    carts = []
    cart_service = CartService()
    for index, organisation_account in enumerate(organisation_accounts):
        if index == 0:
            person_index = 0
        else:
            person_index = index % len(persons)

        cart = cart_service.create(
            organisation_account,
            persons[person_index],
            0,  # TODO: replace 0 with something meaningful
            CurrencyTypes.EUR,
            PaymentTypes.ONLINE,
        )

        carts.append(cart)

    fancy_out("Create Product records")

    fancy_out("Create ProductRole records")

    fancy_out("Create Capability records")

    fancy_out("Create Challenge records")

    fancy_out("Create Challenge Dependency records")

    fancy_out("Create Bounty records")

    fancy_out("Create BountyClaim records")

    fancy_out("Create BountyClaim Submission Attempt records")

    fancy_out("Create Portfolio records")

    fancy_out("Complete!")