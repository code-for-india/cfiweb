'use strict';


// Declare app level module which depends on filters, and services
angular.module('myApp', [
  'ngRoute',
  'myApp.filters',
  'myApp.factories',
  'myApp.directives',
  'myApp.controllers'
]).
config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/', {templateUrl: 'partials/home.html', controller: 'homeController'});
  $routeProvider.when('/projects', {templateUrl: 'partials/projects.html', controller: 'projectsController'});
  $routeProvider.otherwise({redirectTo: '/view1'});
}]);


$(document).ready(function(){
	$('#button-home-latestProjects').click(function(){
		console.log("clicked");
		$('html, body').animate({
    		scrollTop: $("#-home-latestProjects").offset().top
		}, 1000);
	});
	
})