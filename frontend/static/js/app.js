(function () {
    'use strict';

    angular
        .module('app', ['ngRoute', 'ngCookies'])
        .config(config)
        .run(run);

    config.$inject = ['$routeProvider', '$locationProvider'];
    function config($routeProvider, $locationProvider) {
        $routeProvider
            .when('/', {
                controller: 'RecortesController',
                templateUrl: 'static/js/views/recortes.view.html',
                controllerAs: 'vm'
            })

            .when('/login', {
                controller: 'LoginController',
                templateUrl: 'static/js/views/login.view.html',
                controllerAs: 'vm'
            })

            .when('/register', {
                controller: 'RegisterController',
                templateUrl: 'static/js/views/register.view.html',
                controllerAs: 'vm'
            })

            .otherwise({ redirectTo: '/login' });
    }

    run.$inject = ['$rootScope', '$location', '$cookies', '$http'];
    function run($rootScope, $location, $cookies, $http) {
        
        $rootScope.globals = $cookies.getObject('globals') || {};
        if ($rootScope.globals.currentUser) {
            $http.defaults.headers.common['Authorization'] = 'Token ' + $rootScope.globals.currentUser.token;
        }

        $rootScope.$on('$locationChangeStart', function (event, next, current) {
            var restrictedPage = $.inArray($location.path(), ['/login', '/register']) === -1;
            var loggedIn = $rootScope.globals.currentUser;
            if (restrictedPage && !loggedIn) {
                $location.path('/login');
            }
        });
        
        $rootScope.$on('$locationChangeSuccess', function (event, next, current) {
            var loginPage = $.inArray($location.path(), ['/login', '/register']) > -1;
            var loggedIn = $rootScope.globals.currentUser;
            
            if (loginPage && loggedIn) {
                $location.path('/');
            }
        });

    }

})();
