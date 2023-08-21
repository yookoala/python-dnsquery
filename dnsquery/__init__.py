import httpx

import dns.message
import dns.query
import dns.rdatatype

def dnsquery(qnames, callback=lambda item: item.address, where="https://cloudflare-dns.com/dns-query"):
    """
    Map qnames query answer items with the given function fn.
    Returns an array of string (supposedly IP addresses).
    """
    l = []
    with httpx.Client() as client:
        for qname in qnames:
            q = dns.message.make_query(qname, dns.rdatatype.A)
            r = dns.query.https(q, where, session=client)
            for answer in r.answer:
                for item in answer.items:
                    l.append(callback(item))
    return l