import pycurl


class CurlUtility():

    @classmethod
    def get_response(cls, url):
        crl = pycurl.Curl()
        # Set URL value
        crl.setopt(crl.URL, url)

        # Perform a file transfer
        return crl.perform()

