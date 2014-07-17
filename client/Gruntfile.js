module.exports = function(grunt) {
  // Project configuration.
  grunt.initConfig({
  	pkg: grunt.file.readJSON('package.json')
  	,exec: {
  		install: {
  			command: 'npm install && bower install',
  			stdout: true,
  			stderr: true
  		}
  	}
  	,bower_concat: {
  		all: {
  			dest: 'app/build/_bower.js',
  			exclude: [
  			
  			],
  			dependencies: {
  				
  			},
  			bowerOptions: {
  				relative: false
  			}
  		}
  	}
    ,  uglify: {
      options: {
        compress: {
          drop_console: true
        }
        ,mangle: false
      },
      my_target: {
        files: {
          'app/build/_bower.min.js': ['app/build/_bower.js']
          ,'app/build/app.min.js': ['app/js/*.js','app/js/controllers/*.js']

        }
      }
    }
    ,cssmin: {
    combine: {
      files: {
        'app/build/_bootstrap.css': ['bower_components/bootstrap/dist/css/bootstrap.min.css', 'bower_components/bootstrap/dist/css/bootstrap-theme.min.css']
      }
    }
  }



  });

  // Load the plugin that provides the "uglify" task.
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-exec');
  grunt.loadNpmTasks('grunt-bower-concat');
  grunt.loadNpmTasks('grunt-contrib-cssmin');

  grunt.registerTask('install', ['exec:install','bower_concat','uglify','cssmin']);

};
