function restaurant(column) {
    if(column == 1){
        name = document.getElementById("dropdown1").value;
    }
    if(column == 2){
        name = document.getElementById("dropdown2").value;
    }
    console.log(name);
    $.ajax({                  
      url: '/homepage/index.calculate/' + name + '/' + column + '/',
      async: false,
      }).done(function(data) {
        if(column == 1){
            document.getElementById("restaurant1").innerHTML = data;
        }
        if(column == 2){
            document.getElementById("restaurant2").innerHTML = data;
        }
  
    }).fail(function(data) {
        console.log("fail testing...");
    });
  }

  function restaurant2() {
    name = document.getElementById("dropdown2").value;
    column = 2;
    console.log(name);
    $.ajax({                  
      url: '/homepage/index.calculate/' + name + '/' + column + '/',
      async: false,
      }).done(function(data) {
        document.getElementById("restaurant2").innerHTML = data;
  
    }).fail(function(data) {
        console.log("fail testing...");
    });
  }
