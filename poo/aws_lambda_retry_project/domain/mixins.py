class AccountValidationMixin:
    VALID_AWS_REGIONS = {
        "us-east-1",
        "us-west-1",
        "us-west-2",
        "eu-west-1",
        "eu-central-1",
        "ap-southeast-1",
        "ap-southeast-2",
        "ap-northeast-1",
        "sa-east-1",
    }

    def validate_account_id(self, account_id: str) -> None:
        if not account_id.isdigit() or len(account_id) != 12:
            raise ValueError(f"Invalid AWS Account ID: {account_id}")

    def validate_region(self, region: str) -> None:
        if not region or not isinstance(region, str):
            raise ValueError("Region must be a non-empty string.")

        if region not in self.VALID_AWS_REGIONS:
            raise ValueError(f"Invalid AWS region: {region}")
