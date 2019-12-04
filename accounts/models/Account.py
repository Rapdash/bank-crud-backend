from django.db.models import Model, CharField, IntegerField, ForeignKey, CASCADE

# Create your models here.

account_type_choices = (
    ('CHK', 'Checking'),
    ('SVG', 'Savings'),
    ('MMK', 'Money Market')
)


class Account(Model):
    """
    Represents a bank account.
    """
    owner = ForeignKey(to='auth.User', on_delete=CASCADE,
                       related_name='accounts')

    # See https://docs.djangoproject.com/en/2.2/ref/models/fields/#choices for why I did it this way.
    CHECKING = 'CHK'
    SAVINGS = 'SVG'
    MONEY_MARKET = 'MMK'
    account_type_choices = (
        (CHECKING, 'Checking'),
        (SAVINGS, 'Savings'),
        (MONEY_MARKET, 'Money Market'),
    )
    account_type = CharField(max_length=3)
    # Make sure to document that this is in cents, not (dollars/euros/etc)
    account_balance = IntegerField(default=0)
