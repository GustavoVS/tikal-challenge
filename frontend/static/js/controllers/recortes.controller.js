(function () {
    'use strict';

    angular
        .module('app')
        .controller('RecortesController', RecortesController);

    RecortesController.$inject = ['RecortesService', 'AuthenticationService', '$rootScope'];
    function RecortesController(RecortesService, AuthenticationService, $rootScope) {
        var vm = this;

        vm.user = null;
        vm.recortes = [];
        vm.filters = {
            'q': '',
            't': '',
            'nup': ''
        };
        vm.searchRecortes = searchRecortes;
        vm.clearFilters = clearFilters;
        vm.logout = logout;

        initController();

        function initController() {
            loadCurrentUser();
            searchRecortes();
        }

        function loadCurrentUser() {
            AuthenticationService.GetUser()
                .then(function (user) {
                    vm.user = user;
                });
        }

        function searchRecortes() {
            RecortesService.Search(vm.filters)
                .then(function (recortes) {
                    vm.recortes = recortes;
            });

        }

        function clearFilters() {
            vm.filters = [];
        }

        function logout() {
            AuthenticationService.Logout(function(){
                AuthenticationService.ClearCredentials();
            });
        }
    }

})();