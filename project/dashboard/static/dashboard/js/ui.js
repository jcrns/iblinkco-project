// UI functioning
  // Hidding buttons
  $("#hidden-button-instagram").hide();
  $("#hidden-button-facebook").hide();
  $("#hidden-button-twitter").hide();
  $("#hidden-button-youtube").hide();

  // showing dashboard row by default
  $("#admin").show();

  // hiding analytics by default
  $("#analytics").hide();
  $("#stream").hide();

  //test
  // $("#connect-header-instagram").hide();
  // $("#content-instagram").show();
  // $("#connect-header-instagram").hide();


  // hiding the dashboard row toggle by default
  $("#show-admin").hide();

  $("#show-analytics").click(function() {
    $("#admin").hide();
    $("#analytics").show();
    $("#show-admin").show();
    $("#show-analytics").hide();
    $("#show-stream").show();
    $("#stream").hide();

  });

  $("#show-admin").click(function() {
    $("#admin").show();
    $("#analytics").hide();
    $("#show-admin").hide();
    $("#show-analytics").show();
    $("#show-stream").show();
    $("#stream").hide();
  })

  $("#show-stream").click(function() {
    $("#admin").hide();
    $("#analytics").hide();
    $("#show-admin").show();
    $("#show-analytics").show();
    $("#show-stream").hide();
    $("#stream").show();
  })

  //Full Screen functions and Animations

  //Full Screen Instagram
  $('#button-instagram').click(function() {
    $('#dash-instagram')
    $('#dash-facebook').hide()
    $('#dash-twitter').hide()
    $('#dash-youtube').hide()
    $('#dash-instagram').animate({
      height: '75vh',
      width: '70vh'
    }, 500);
    $('#button-instagram').hide()
    $('#hidden-button-instagram').show()
  });

  //Shrink Full Screen Instagram
  $('#hidden-button-instagram').click(function() {
    $('#dash-instagram')
    $('#dash-facebook').show()
    $('#dash-twitter').show()
    $('#dash-youtube').show()
    $('#dash-instagram').animate({
      height: '47.25vh',
      width: '60vh'
    }, 500);
    $('#button-instagram').show()
    $('#hidden-button-instagram').hide()
  });


  //Full Screen Facebook
  $('#button-facebook').click(function() {
    $('#dash-instagram').hide()
    $('#dash-facebook')
    $('#dash-twitter').hide()
    $('#dash-youtube').hide()
    $('#dash-facebook').animate({
      height: '75vh',
      width: '60vh'
    }, 500);
    $('#button-facebook').hide()
    $('#hidden-button-facebook').show()
  });

  //Shrink Full Screen Facebook
  $('#hidden-button-facebook').click(function() {
    $('#dash-instagram').show()
    $('#dash-facebook')
    $('#dash-twitter').show()
    $('#dash-youtube').show()
    $('#dash-facebook').animate({
      height: '47.25vh',
      width: '60vh'
    }, 500);
    $('#button-facebook').show()
    $('#hidden-button-facebook').hide()
  });


  //Full Screen Twitter
  $('#button-twitter').click(function() {
    $('#dash-instagram').hide();
    $('#dash-facebook').hide();
    $('#dash-youtube').hide();
    $('#dash-twitter').animate({
      height: '75vh',
      width: '60vh'
    }, 500);
    $('#button-twitter').hide();
    $('#hidden-button-twitter').show();
  });

  //Shrink Full Screen Twitter
  $('#hidden-button-twitter').click(function() {
    $('#dash-instagram').show();
    $('#dash-facebook').show();
    $('#dash-youtube').show()
    $('#dash-twitter').animate({
      height: '47.25vh',
      width: '60vh'
    }, 500);
    $('#button-twitter').show();
    $('#hidden-button-twitter').hide();
  });


  //Full Screen Youtube
  $('#button-youtube').click(function() {
    $('#sm-container').hide();
    $('#dash-facebook').hide();
    $('#dash-twitter').hide();
    $('#dash-youtube').animate({
      height: '75vh',
      width: '60vh'
    }, 500);
    $('#button-youtube').hide();
    $('#hidden-button-youtube').show();
  });

  //Shrink Full Screen Youtube
  $('#hidden-button-youtube').click(function() {
    $('#sm-container').show();
    $('#dash-facebook').show();
    $('#dash-twitter').show();
    $('#dash-youtube').animate({
      height: '47.25vh',
      width: '100vh'
    }, 500);
    $('#button-youtube').show();
    $('#hidden-button-youtube').hide()
  });
  // Functions to show content through dialog popup
  $('#connect-instagram').submit(function() {
    $("#content-instagram").show();
    $("#disconnect-instagram").show();
    $("#connect-header-instagram").hide();
  });

  $("#fb-btn").click(function() {
    $("#content-facebook").show();
    $("#disconnect-facebook").show();
    $("#connect-header-facebook").hide();
  });

  $("#show-content-youtube").click(function() {
    $("#content-youtube").show();
    $("#disconnect-youtube").show();
    $("#connect-header-youtube").hide();
  });

  $("#show-content-settings").click(function() {
    $("#content-settings").show();
  });

  // Hiding Disconnect buttons
  $("#disconnect-instagram").hide();
  $("#disconnect-facebook").hide();
  $("#disconnect-twitter").hide();
  $("#disconnect-youtube").hide();


  $("#disconnect-facebook").click(function() {
    $("#content-facebook").hide();
    $("#disconnect-facebook").hide();
    $("#connect-header-facebook").show();
  })
  $("#disconnect-youtube").click(function() {
    $("#content-youtube").hide();
    $("#disconnect-youtube").hide();
    $("#connect-header-youtube").show();
  })

  //Putting logged in user in a Variable
  var usernameVerify = "{{ user.username }}";

  //Getting Info to verify twitter account is connected in database
  var getTwitterUser = "{% for twitter_user_verify in content_twitter %}{{ twitter_user_verify.user }}{% endfor %}";
  var twitterUsers = "{% for twitter_user_verify in content_twitter %}{{ twitter_user_verify.twitter_username }}{% endfor %}"
  console.log("Twitter User Model: " + getTwitterUser)
  console.log("Twitter Database usernames: " + twitterUsers)
  if ((getTwitterUser == usernameVerify)) {
    $("#content-twitter").show();
    $("#disconnect-twitter").show();
    $("#connect-header-twitter").hide();
    console.log("Twitter connected");
  } else {
    console.log("Twitter Not connected")
  }

  if (getTwitterUser.includes(usernameVerify)) {
    console.log("Hella True");
    $("#content-twitter").show();
    $("#connect-header-twitter").hide();
  } else {
    console.log("not true")
  }


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
