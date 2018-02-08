import re
import subprocess
from datetime import timedelta
from urllib.parse import urlparse

import requests


class Status(object):
    code = ""
    description = ""
    url = ""

    def __init__(self, url, code, description=None):
        self.url = url
        self.code = code
        self.description = description

    def __repr__(self):
        return "<Status %s>" % self.code


class Checker:
    def __init__(self, url):
        self.url = url
        self.parsed_url = self._parse_url()

    def _parse_url(self):
        if self.is_ip():
            return self.url
        elif self.is_host():
            parsed = urlparse(self.url)
            if parsed.scheme == "":
                netloc = parsed.path
                scheme = "https"
            else:
                netloc = parsed.netloc
                scheme = parsed.scheme

            return "%s://%s/" % (scheme, netloc)
        else:
            raise Exception  # FIXME

    def is_ip(self):
        regex = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
        if re.match(regex, self.url):
            return True
        else:
            return False

    def is_host(self):
        regex = re.compile(
            r'(?i)\b((|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))')
        if re.match(regex, self.url):
            return True
        else:
            return False

    def _ping(self):
        p = subprocess.Popen(['/sbin/ping', '-c4', self.parsed_url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        errors = 0
        success = 0
        times = []

        for line in p.stderr:
            l = line.rstrip().decode('utf-8')

            # błędny IP
            if "cannot resolve" in l or 'Unknown host' in l:
                return Status(self.parsed_url, 'UNKNOWN', "Specified IP address is not valid")

        for line in p.stdout:
            l = line.rstrip().decode('utf-8')

            # timeouty
            if "Request timeout" in l:
                errors += 1

            time = l.split('time=')
            # sukcesy
            if len(time) == 2:
                success += 1
                times.append(time[1].split(' ')[0])

        # za długi czas oczekiwania
        for time in times:
            time = float(time)
            if time > 200:
                return Status(self.parsed_url, 'SLOW', 'Server answered, but responds slowly')

        if errors and success == 0:
            return Status(self.parsed_url, 'DOWN', 'Server is down')
        if errors > 0 and success > 0:
            return Status(self.parsed_url, 'FLAPPY', 'Server is in flappy state')
        else:
            return Status(self.parsed_url, 'UP', 'Server is up')

    def _ping_http(self):
        try:
            url = self.parsed_url
            r = requests.head(url, timeout=30)
        except requests.exceptions.ConnectionError:
            return Status(url, 'CONN_ERR', "Website is down, or the URL you provided does not exists")

        # by time
        if r.elapsed > timedelta(seconds=30):
            return Status('DOWN', "Website is down")
        elif r.elapsed > timedelta(seconds=10):
            return Status(url, 'SLOW', "Website is running, but it's slow")

        # by code
        if r.status_code < 399:
            return Status(url, 'UP', "Website is running")
        elif 399 > r.status_code < 499:
            return Status(url, 'HTTP_4xx', "Website is online, but it's returning HTTP %s error code" % r.status_code)
        else:
            return Status(url, 'HTTP_5xx', "Website is online, but it has problems with servers")

        # should be unreachable
        return Status(url, 'DOWN', "Website is down")

    def check(self):
        if self.is_ip():
            return self._ping()
        elif self.is_host():
            return self._ping_http()
        else:
            raise Exception  # FIxmE
