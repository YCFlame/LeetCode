class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        from collections import Counter
        result = Counter()
        for item in cpdomains:
            count, domain = item.split()
            count = int(count)
            domains = domain.split('.')
            for i in range(len(domains)):
                result['.'.join(domains[i:])] += count
        
        return [f"{count} {domain}" for domain, count in result.items()]
