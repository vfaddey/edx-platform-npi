from social_core.backends.oauth import BaseOAuth2


class NPIOAuth2(BaseOAuth2):
    HOSTNAME = 'id.tutor-npi.leetpost.ru'
    AUTHORIZATION_URL = "http://%s/oidc/authorize" % HOSTNAME
    ACCESS_TOKEN_URL = "http://%s/oidc/token" % HOSTNAME
    ACCESS_TOKEN_METHOD = "POST"
    DEFAULT_SCOPE = ["openid profile email"]
    REDIRECT_STATE = 'XYZ'

    def get_user_details(self, response):
        return {
            "first_name": response.get('first_name'),
            "last_name": response.get('last_name'),
            "fullname": response.get('first_name') + " " + response.get('last_name'),
            "email": response.get("email", "")
        }

    def user_data(self, access_token, *args, **kwargs):
        url = "http://%s/oidc/userinfo" % self.HOSTNAME
        auth_header = {"Authorization": "Bearer %s" % access_token}
        return self.get_json(url, headers=auth_header)