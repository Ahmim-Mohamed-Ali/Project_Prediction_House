function getRoomValue() {
    var uiBathrooms = document.getElementsByName("rooms");
    for (var i = 0; i < uiBathrooms.length; i++) {
        if (uiBathrooms[i].checked) {
            return parseInt(uiBathrooms[i].value); // Utilisez la valeur du bouton radio
        }
    }
    return -1; // Invalid Value
}

function getFloorsValue() {
    var uiFloor = document.getElementsByName("floors");
    for (var i = 0; i < uiFloor.length; i++) {
        if (uiFloor[i].checked) {
            return parseInt(uiFloor[i].value); // Utilisez la valeur du bouton radio
        }
    }
    return -1; // Invalid Value
}

function getYard() {
    var yard = document.getElementById("has_yard");
    return yard.checked ? 1 : 0; // Utilisation de checked directement sur l'élément
}

function getPool() {
    var pool = document.getElementById("has_pool");
    return pool.checked ? 1 : 0; // Utilisation de checked directement sur l'élément
}

function getBuild() {
    var build = document.getElementById("is_new_build");
    return build.checked ? 1 : 0; // Utilisation de checked directement sur l'élément
}

function onClickedEstimatePrice(event) {
    event.preventDefault(); // Empêche le comportement par défaut
    console.log("Estimate price button clicked");
    
    var sqft = document.getElementById("uiSqft");
    console.log(sqft.value);
    
    var floor = getFloorsValue();
    console.log(floor);
    
    var rooms = getRoomValue();
    console.log(rooms);
    
    var date = document.getElementById("uimade");
    console.log(date.value);
    
    var haspool = getPool();
    console.log(haspool);
    
    var hasyard = getYard();
    console.log(hasyard);
    
    var build = getBuild();
    console.log(build);
    
    var estPrice = document.getElementById("uiEstimatedPrice");
    console.log("jen SUIS LA");

    var url = "http://127.0.0.1:5000/predict_home_price";

    $.post(url, {
        total_sqft: parseFloat(sqft.value),
        made: parseInt(date.value),
        rooms: rooms,
        build: build,
        floors: floor,
        haspool: haspool,
        hasyard: hasyard,
        is_new_built: build
    }, function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " Euros</h2>";
        console.log(status);
    });
}
