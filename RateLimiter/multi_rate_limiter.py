import time
from collections import defaultdict, deque

class MultiRateLimiter:
    def __init__(self, domain_max_5s, global_max_30s, domain_max_2s):
        self.domain_max_5s = domain_max_5s
        self.global_max_30s = global_max_30s
        self.domain_max_2s = domain_max_2s

        self.domain_requests = defaultdict(deque)
        self.global_requests = deque()
        self.domain_intervals = defaultdict(deque)

    def allow_request(self, domain):
        current_time = time.time()

        # Clean up domain_requests
        while self.domain_requests[domain] and self.domain_requests[domain][0] < current_time - 5:
            self.domain_requests[domain].popleft()

        # Clean up global_requests
        while self.global_requests and self.global_requests[0] < current_time - 30:
            self.global_requests.popleft()

        # Clean up domain_intervals
        while self.domain_intervals[domain] and self.domain_intervals[domain][0] < current_time - 2:
            self.domain_intervals[domain].popleft()

        if (len(self.domain_requests[domain]) < self.domain_max_5s and
            len(self.global_requests) < self.global_max_30s and
            len(self.domain_intervals[domain]) < self.domain_max_2s):

            self.domain_requests[domain].append(current_time)
            self.global_requests.append(current_time)
            self.domain_intervals[domain].append(current_time)
            return True

        return False

# Usage
limiter = MultiRateLimiter(domain_max_5s=4, global_max_30s=25, domain_max_2s=1)

requests = ["domain1", "domain1","domain1","domain1","domain1","domain1","domain2", "domain3", "domain2", "domain3","domain6","domain2", "domain3", "domain2","domain2", "domain3", "domain2", "domain4", "domain5"] * 3

for i, domain in enumerate(requests):
    if limiter.allow_request(domain):
        print(f"Request {i + 1} from {domain}: ok")
    else:
        print(f"Request {i + 1} from {domain}: too many")
    time.sleep(1)

