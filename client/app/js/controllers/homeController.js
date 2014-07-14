'use strict';

/* Controllers */

  controllerModule.controller('homeController', function($scope, $route, $routeParams, $location, projectsFactory) {
  	$scope.__controllerName = "home";
  	$scope.projects = [];
  	jQuery('.top_menu_item').removeClass('active');
  	jQuery('#menu_'+$scope.__controllerName).addClass('active');
	projectsFactory.getRecentProjects()
 		.then(function(data){$scope.projects = data});
  });
