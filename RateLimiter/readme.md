Assumtions:
    * 1 request per secon

    Rate Limiting Rules: (configurable)
        - 1 request per domain per 2 sec
        - 4 request per domain per 5 sec
        - 25 request per 30 sec
    
    Request allowed if above rules met
    Request not allowed if above rules are not met - too many request from domain

Run: 
./multi_rate_limiter.py

Output:
Request 1 from domain1: ok
Request 2 from domain1: too many
Request 3 from domain1: ok
Request 4 from domain1: too many
Request 5 from domain1: ok
Request 6 from domain1: too many
Request 7 from domain2: ok
Request 8 from domain3: ok
Request 9 from domain2: ok
Request 10 from domain3: ok
Request 11 from domain6: ok
Request 12 from domain2: ok
Request 13 from domain3: ok
Request 14 from domain2: ok
Request 15 from domain2: too many
Request 16 from domain3: ok
Request 17 from domain2: ok
Request 18 from domain4: ok
Request 19 from domain5: ok
Request 20 from domain1: ok
Request 21 from domain1: too many
Request 22 from domain1: ok
Request 23 from domain1: too many
Request 24 from domain1: ok
Request 25 from domain1: too many
Request 26 from domain2: ok
Request 27 from domain3: ok
Request 28 from domain2: ok
Request 29 from domain3: ok
Request 30 from domain6: ok
Request 31 from domain2: ok
Request 32 from domain3: ok
Request 33 from domain2: ok
Request 34 from domain2: too many
Request 35 from domain3: ok
Request 36 from domain2: ok
Request 37 from domain4: ok
Request 38 from domain5: ok
Request 39 from domain1: ok
Request 40 from domain1: too many
Request 41 from domain1: ok
Request 42 from domain1: too many
Request 43 from domain1: ok
Request 44 from domain1: too many
Request 45 from domain2: ok
Request 46 from domain3: ok
Request 47 from domain2: ok
Request 48 from domain3: ok
Request 49 from domain6: ok
Request 50 from domain2: ok
Request 51 from domain3: ok
Request 52 from domain2: ok
Request 53 from domain2: too many
Request 54 from domain3: ok
Request 55 from domain2: ok
Request 56 from domain4: ok
Request 57 from domain5: ok
