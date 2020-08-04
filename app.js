function onClickedEstimation() {
    console.log("Diabities Prediction button clicked");
    var Pregnancies = document.getElementById("uipreg");
    var Glucose = document.getElementById("uiglucose");
    var BloodPressure = document.getElementById("uibp");
    var SkinThickness = document.getElementById("uiskin");
    var Insulin = document.getElementById("uiinsulin");
    var BMI = document.getElementById("uibmi");
    var DiabetesPedigreeFunction = document.getElementById("uidia");
    var Age = document.getElementById("uiage");
    var estdia = document.getElementById("uiEstimation");


  
     var url = "http://127.0.0.1:5000/predict_diabities";
    //var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  
    $.post(url, {
        Pregnancies: Pregnancies,
        Glucose: Glucose,
        BloodPressure: BloodPressure,
        SkinThickness: SkinThickness,
        Insulin: Insulin,
        BMI: BMI,
        DiabetesPedigreeFunction: DiabetesPedigreeFunction,
        Age: Age,
    },function(data, status) {
        console.log(data.estimation);
        estdia.innerHTML = "<h2>" + data.estimation.toString() + " </h2>";
        console.log(status);
    });
  }
  
 