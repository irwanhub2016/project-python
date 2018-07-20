def ntp_time(servers):
    """
    Retorna a hora oficial do Brasil (NTP.br)

    Returns the official time of Brazil (NTP.br).
    """
    ntp_time = None
    client = NTPClient()

    for host in servers:
        try:
            response = client.request(host)
            ntp_time = ctime(response.orig_time)
            break
        except (NTPException, socket.gaierror):
            pass

    return ntp_time 
