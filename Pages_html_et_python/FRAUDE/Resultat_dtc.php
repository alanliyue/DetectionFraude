
<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <meta charset="UTF-8">
        <title>Resultat Decision Tree Classifier</title>
    </head>
    <body>
        
            <h1 class="titre">
        Est-ce une fraude ?
    </h1>
        
<?php

    
    #$resultat=shell_exec('python /Applications/MAMP/htdocs/FRAUDE/Test_fraude_print.py ');
    #echo "<p style ='color:red'>".$resultat. "</p>";
    
    $command = escapeshellcmd('python3 /Applications/MAMP/htdocs/FRAUDE/Test_fraude_print.py');
    $output = shell_exec($command);
    echo $output;
    


?>
        
    </body>
</html>