Hash all phone numbers
========

How long would it take your computer to precompute SHA256 of all North
American phone numbers?

Be smart about "NPA" or area codes (there are only about 300 in use). Be smart
about the NXX as well. Not all strings 000 to 999 are allowed.

Answer if we are printing to Terminal.app on my MacBook Pro, 2.7 GHz
Intel Core i7, Early 2011:

    3947385          items complete
    108.02           sec
    36541.68         per sec

    316 npa * 792 nxx * 10000 =
    2502720000       items to complete
    19.02            hours

Answer if not printing:

    7034763       items complete
    23.36         sec
    301184.66     per sec

    316 npa * 792 nxx * 10000 =
    2502720000    items to complete
    2.31          hours
