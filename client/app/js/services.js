'use strict';

/* Services */


// Demonstrate how to register services
// In this case it is a simple value service.
angular.module('myApp.factories', [])
 .config(function ( $httpProvider) {        
        delete $httpProvider.defaults.headers.common['X-Requested-With'];
    })
  .factory('projectsFactory', function ($http, $q) {
  
  this._models = [];
  var that = this;
  this.root_url = "http://cfi.zirconiumks.com:8000/api/v1/project/?format=json";

  this.getRecentProjects = function(callback){
  	var deferred = $q.defer();
  	$http({url:that.root_url})
  	.success(function(data){that._models = data.objects; deferred.resolve(data.objects)});
  	return deferred.promise;
  }
  return {getRecentProjects: this.getRecentProjects};
});
