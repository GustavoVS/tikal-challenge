(function() {
    'use strict';
    angular.module('app',[
       'ngCookies'
    ], function($interpolateProvider){
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
    })
    .run( function run($http, $cookies ){
        $http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
    });
})();