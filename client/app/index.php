<!DOCTYPE html>
<!--[if lt IE 7]>      <html lang="en" ng-app="myApp" class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html lang="en" ng-app="myApp" class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html lang="en" ng-app="myApp" class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html lang="en" ng-app="myApp" class="no-js"> <!--<![endif]-->
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>CFI App</title>
  <meta name="description" content="">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="css/app.css"/>
  <link rel="stylesheet" href="css/app.css"/>
  <link rel="stylesheet" href="bower_components/bootstrap/dist/css/bootstrap.min.css"/>
  <link rel="stylesheet" href="bower_components/bootstrap/dist/css/bootstrap-theme.min.css"/>

</head>
<body ng-controller = "mainController">
  


<!-- Fixed navbar -->
    <div class="navbar navbar-default navbar-fixed-top" role="navigation">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">CFI App</a>
        </div>
        <div class="navbar-collapse collapse">
          
          <ul class="nav navbar-nav navbar-right">
            <li id="menu_home" class="top_menu_item"><a href="#/">Home</a></li>
            <li id="menu_projects" class="top_menu_item"><a href="#/projects">Projects</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </div>

    <div class="container">
      <div ng-view></div>

      <!-- Main component for a primary marketing message or call to action -->


    </div> <!-- /container -->





  <!--[if lt IE 7]>
      <p class="browsehappy">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
  <![endif]-->



  <!-- In production use:
  <script src="//ajax.googleapis.com/ajax/libs/angularjs/x.x.x/angular.min.js"></script>
  -->
  <script src="build/_bower.min.js"></script>
  <?php
    // core files    
    $jsfiles = glob("js/" . "*.js");
    foreach($jsfiles as $jsfile)
    {
      echo('<script src="'.$jsfile.'"></script>'."\n");
    }

    // controllers 
     $jsfiles = glob("js/controllers/" . "*.js");
    foreach($jsfiles as $jsfile)
    {
      echo('<script src="'.$jsfile.'"></script>'."\n");
    }



  ?>

</body>
</html>
