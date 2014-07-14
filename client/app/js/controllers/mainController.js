'use strict';

/* Controllers */


  controllerModule.controller('mainController', function($scope, $route, $routeParams, $location, projectsFactory) {
     $scope.$route = $route;
     $scope.$location = $location;
     $scope.$routeParams = $routeParams;
    
 });
