<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Fraud Home Page</title>
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
            height: 850px;
        }

        .paragraphe{
            position: relative;
            top: 250px;
            text-align: center;
            color: white;
            font-family: "Gill Sans Nova", sans-serif;
            letter-spacing: 1.4px;
            word-spacing: 2px;
            moz-osx-font-smoothing: grayscale;
            line-height: 1.5em
        }

        .bouton{

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
            width: 500px;
            padding: 18px 30px;
            box-sizing: border-box;
            vertical-align: top;
            position: relative;
            top: 300px;
            left: 15%;
            display: block;
            margin: 0 20% auto;
            text-decoration: none;
            box-sizing: border-box;
            text-align: center;

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
            width: 500px;
            padding: 18px 30px;
            box-sizing: border-box;
            vertical-align: top;
            position: relative;
            top: 350px;
            left: 15%;
            display: block;
            margin: 0 20% auto;
            text-decoration: none;
            box-sizing: border-box;
            text-align: center;

        }
        
                .bouton2{

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
            width: 500px;
            padding: 18px 30px;
            box-sizing: border-box;
            vertical-align: top;
            position: relative;
            top: 400px;
            left: 15%;
            display: block;
            margin: 0 20% auto;
            text-decoration: none;
            box-sizing: border-box;
            text-align: center;

        }
        
        .bouton3{

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
            width: 500px;
            padding: 18px 30px;
            box-sizing: border-box;
            vertical-align: top;
            position: relative;
            top: 450px;
            left: 15%;
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
    Bienvenue sur la page d'accueil
</h2>
<p class = "paragraphe">
    Vous voulez v??rifier si une transaction est une fraude ou non ?

</p>
<p class="paragraphe">
        Vous ??tes au bon endroit ! N'attendez pas plus et cliquez sur le bouton !
</p>
    <a href="dtc.php" target="_blank" class="bouton">Testez votre dataset avec Decision Tree Classifier!</a>
    <a href="knn.php" target="_blank" class="bouton1">Testez votre dataset avec KNN!</a>
    <a href="logreg.php" target="_blank" class="bouton2">Testez votre dataset avec Logistic Regression!</a>
    <a href="clf.php" target="_blank" class="bouton3">Testez votre dataset avec Random Forest Classifier!</a>


</div>
</body>
</html>