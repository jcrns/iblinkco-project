  // showing dashboard row by default
  $("#admin").show();

  // hiding analytics by default
  $("#analytics").hide();
  $("#accounts").hide();

  // Creating Divs

  // Connect Account Div
  function accountDiv(){
    var dashboardRow = document.getElementById('connect-account-div');

    var createrDiv = document.createElement('div');
    createrDiv.className = "col-sm-16";
    createrDiv.setAttribute('id', "holder-1");

    dashboardRow.appendChild(createrDiv);
    $('#holder-1').html('<div class="card" id="holder-2"><p><a href="#" style="color:#000" data-toggle="modal" data-target="#connect">Add An Account</a></p></div>');
  }
  accountDiv();

  // Create Opperation Div
  function opperationDiv(){
    var dashboardRow = document.getElementById('create-opperation-div');

    var createrDiv = document.createElement('div');
    createrDiv.className = "col-sm-16";
    createrDiv.setAttribute('id', "holder-5");

    dashboardRow.appendChild(createrDiv);
    $('#holder-5').html('<div class="card" id="holder-6"><p><a href="#" id="connect-opperation" data-toggle="modal" data-target="#opperation-post" style="color:#000">Create New Opperation</a></p></div>');
  }
  opperationDiv();
