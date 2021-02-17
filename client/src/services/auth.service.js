/* eslint-disable */
import axios from 'axios';
import paths from "@/paths";

const host = window.location.protocol + '//' + window.location.host;

class AuthService {
  // POST {username, password} & save JWT to local storage
  login(user) {
    return axios
      .post(`${host}${paths.login}`, {
        email: user.email,
        password: user.password,
      })
      .then((response) => {
        if (response.data.token) {
          localStorage.setItem('user', JSON.stringify(response.data));
          // eslint-disable-next-line
          console.log(response.data)
        }

        return response.data;
      });
  }

  // remove JWT from Local Storage
  logout() {
    localStorage.removeItem('user');
  }

  // POST {email, password}
  register(user) {
    return axios.post(`${host}${paths.register}`, {
      email: user.email,
      password: user.password,
    });
  }
}

export default new AuthService();
