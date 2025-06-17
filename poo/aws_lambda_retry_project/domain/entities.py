from domain.mixins import AccountValidationMixin


class AWSAccount(AccountValidationMixin):
    def __init__(self, account_id: str, region: str):
        self._account_id = None
        self._region = None
        self.account_id = account_id  # ⬅️ Chama o setter
        self.region = region  # ⬅️ Chama o setter

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value: str):
        self.validate_account_id(value)
        self._account_id = value

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value: str):
        self.validate_region(value)
        self._region = value
