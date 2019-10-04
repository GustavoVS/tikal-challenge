(function () {
    'use strict';

    angular
        .module('app')
        .factory('RecortesService', RecortesService);

    RecortesService.$inject = ['$http', '$filter'];
    function RecortesService($http, $filter) {
        var service = {};

        service.Search = Search;
        service.SearchByUrl = SearchByUrl;

        return service;

        function Search(filters) {
        
            var q_filters = angular.copy(filters);
            
            if (filters.q)
                q_filters.q = q_filters.q.split(' ').join('-');
            
            if (filters.t)
                q_filters.t = $filter('date')(filters.t, 'ddMMyyyy');

            return $http.get('/api/recortes/', {params: q_filters})
                .then(handleSuccess, handleError('Erro ao buscar recortes'));
        }
        
        function SearchByUrl (url, error_message) {
            return $http.get(url, {}).then(handleSuccess, handleError(error_message));
        }

        function handleSuccess(res) {
            return res.data;
        }

        function handleError(error) {
            return function (r) {
                return { success: false, message: error };
            };
        }
    }

})();
