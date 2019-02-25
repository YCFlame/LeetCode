class Solution:
    def numUniqueEmails(self, emails: 'List[str]') -> 'int':
        emails_set = set()
        for email in emails:
            [temp_local_name, domain_name] = email.split('@')
            [tmp_local_name, a, b] = temp_local_name.partition('+')
            local_name = tmp_local_name.replace('.', '')
            fixed_email = local_name + '@' + domain_name
            emails_set.add(fixed_email)
        return len(emails_set)
