<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <meta charset="UTF-8">
        <title>Fraud dtc</title>
        
            <style>

        .body{
            background-color: white;
        }
        .titre{
            color: darkslategray;
            text-align: center;
            font-style: normal;
            font-family: "Gill Sans Nova", sans-serif;
            font-size: 30.5px;
            letter-spacing: 1.4px;
            word-spacing: 2px;

        }

        .message{
            position: relative;
            top: 200px;
            text-align: center;
            color: white;
            font-family: "Gill Sans Nova", sans-serif;
            letter-spacing: 1.4px;
            word-spacing: 2px;
            font-size: 25.2px;


        }

        .division1{
            background-color: darkslategray;
            height: 650px;
        }
        
        
        .texte {
            display: block;
            position: relative;
            top: 250px;
            text-align: center;
            color: white;
            font-family: "Gill Sans Nova", sans-serif;
            letter-spacing: 1.4px;
            word-spacing: 2px;
            font-size: 25.2px;

        }

        .fichier {
            margin: .4rem 0;
            font-family: "Gill Sans Nova", sans-serif;
            color: white;

            text-align: center;
            position: absolute;
            top : 45%;
            left : 45%;

        }
        
        
        .bouton1{

            background-color: transparent;
            font-family: "Gill Sans Nova", sans-serif;
            -webkit-appearance: none;
            display: inline-block;
            color: white;
            border-radius: 4px !important;
            border: 1px solid;
                border-top-color: rgb(white);
                border-right-color: rgb(white);
                border-bottom-color: rgb(white);
                border-left-color: rgb(white);
            height: auto;
            width:900px;
            padding: 18px 30px;
            box-sizing: border-box;
            vertical-align: top;
            position: relative;
            top: 350px;
            display: block;
            margin: 0 20% auto;
            text-decoration: none;
            box-sizing: border-box;
            text-align: center;
            

        }
        


            </style>

    </head>
    <body class="body">

    <h1 class="titre">
        Est-ce une fraude ?
    </h1>
    <div class="division1" data-cc-animate="">
    <h2 class = "message">
        Testez votre dataset avec le model Decision Tree Classifier
    </h2>
        
        

   
    <label class = "texte" for="dataset">Charger votre dataset :</label>    
    <input class="fichier" type="file"
   id="dataset" name="dataset"
   accept=".csv">
    <form action="Resultat_dtc.php" method="POST">
    <a href="Resultat_dtc.php" target="_blank" class="bouton1">GO!</a>
    </form>
    


</div>
        
        
<?php

    

    if(isset($_GET['on'])){
        exec('python /Applications/MAMP/htdocs/FRAUDE/Test_fraude_print.py');
                    }

?>
</html>