.. title: Get Localhost IPv6 with Python
.. slug: get-localhost-ipv6-with-python
.. date: 2024-01-25 12:14:56 UTC+08:00
.. tags: IPv6
.. category: Python
.. link: 
.. description: 
.. type: text

.. code-block:: python

    def get_ipv6():
        import socket
        host_ipv6 = []
        ips = socket.getaddrinfo(socket.gethostname(),80)
        for ip in ips:
            if ip[4][0].startswith('24'):
                # 2408 中国联通
                # 2409 中国移动
                # 240e 中国电信
                host_ipv6.append(ip[4][0])
        return host_ipv6

        
