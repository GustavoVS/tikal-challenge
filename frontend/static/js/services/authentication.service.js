(function () {
    'use strict';

    angular
        .module('app')
        .factory('AuthenticationService', AuthenticationService);

    AuthenticationService.$inject = ['$http', '$cookies', '$rootScope', '$timeout'];
    function AuthenticationService($http, $cookies, $rootScope, $timeout) {
        var service = {};

        service.Login = Login;
        service.Logout = Logout;
        service.SetCredentials = SetCredentials;
        service.ClearCredentials = ClearCredentials;
        service.GetUser = GetUser;

        return service;

        function Login(username, password, callback) {
            var param = { username: username, password: password };
            $http.post('/api/login/', param)
               .success(function (response) {
                   console.log('success', response);
                   callback(response);
                })
                .error(function (response) {
                    console.log('error', response);
                    callback(response);
            });

        }

        function Logout(callback) {
            $http.post('/api/logout/')
                .success(function (response){
                    callback(response);
            });
        }

        function GetUser() {
            return $http.get('/api/user/').then(handleSuccess, handleError('Erro ao carregar dados do usuário'));
        }

        function SetCredentials(username, token) {

            $rootScope.globals = {
                currentUser: {
                    username: username,
                    token: token
                }
            };

            // set default auth header for http requests
            $http.defaults.headers.common['Authorization'] = 'Token ' + token;

            // store user details in globals cookie that keeps user logged in for 1 week (or until they logout)
            var cookieExp = new Date();
            cookieExp.setDate(cookieExp.getDate() + 7);
            $cookies.putObject('globals', $rootScope.globals, { expires: cookieExp });
        }

        function ClearCredentials() {
            $rootScope.globals = {};
            $cookies.remove('globals');
            $http.defaults.headers.common.Authorization = '';
        }
    

        function handleSuccess(response) {
            return response.data;
        }

        function handleError(error) {
            return function () {
                return { success: false, message: error };
            };
        }
    };

})();
