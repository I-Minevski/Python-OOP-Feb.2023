import re


class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name: str) -> bool:
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail: str) -> bool:
        return mail in self.mails

    def __is_domain_valid(self, domain: str) -> bool:
        return domain in self.domains

    def validate(self, email: str) -> bool:
        pattern = r'([\w\.]*)@([\w]*)\.([\w]+)'
        result = re.search(pattern, email)

        validations = []

        name = result.group(1)
        validations.append(self.__is_name_valid(name))

        mail = result.group(2)
        validations.append(self.__is_mail_valid(mail))

        domain = email.split('.')[-1]
        validations.append(self.__is_domain_valid(domain))

        return all(validations)


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
