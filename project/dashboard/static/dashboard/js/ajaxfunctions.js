//Setting Global Variables

// Instagram variables
var INSTAGRAM_TOTAL_POST = '';
var INSTAGRAM_TOTAL_FOLLOWERS;
var INSTAGRAM_TOTAL_FOLLOWING = '';

// Twitter variables
var TWITTER_TOTAL_TWEETS = '';
var TWITTER_TOTAL_FOLLOWERS;
var TWITTER_TOTAL_FOLLOWING = '';

// INSTAGRAM AJAX FUNCTIONS

  //Checking State of logged in accounts
  function checkInstagramAccount(e){
    var usernameVerify = "{{ user.username }}";
    var url = '{% url 'check-out-instagram/' %}';
    console.log("Instagram Username: " + usernameVerify)
    $.ajax({
      type: 'POST',
      url: url,
      dataType: 'text',
      data: {
        csrfmiddlewaretoken: '{{ csrf_token }}',
        'instagram_user':usernameVerify,

      },
      success: function (content) {
        //Showing and hidding certain information depending on returned information
        var econtent = JSON.parse(content);
        if(content == ''){
          $("#content-instagram").hide();
          $("#disconnect-instagram").hide();
          $("#connect-header-instagram").show();
          $('#content-instagram').html(content);
        } else {
          if(econtent.user == usernameVerify){
            $("#content-instagram").show();
            $("#disconnect-instagram").show();
            $("#connect-header-instagram").hide();
            $('#content-instagram').html("<b>"+ econtent.username + "</b>" + "<br /><p>User Post: "+ econtent.userPost + "</p>" + "<br /><p>Followers: "+ econtent.userFollowers + "</p>" + "<br /><p>Following: "+ econtent.userFollowing + "</p>");

            INSTAGRAM_TOTAL_POST = econtent.userPost;
            INSTAGRAM_TOTAL_FOLLOWERS = econtent.userFollowers;
            INSTAGRAM_TOTAL_FOLLOWING = econtent.userFollowing;

            //Creating a Div
            var dashboardRow = document.getElementById('dashboard-row')

            var instagramDiv = document.createElement('div');
            instagramDiv.className = "col-sm-16";
            instagramDiv.setAttribute('id', "holder-2");
            dashboardRow.appendChild(instagramDiv);
            $('#holder-2').html("<div class='card' style='background: linear-gradient(#7d30e2,#d81dac,#ef1a6e);'> <b>"+ econtent.username + "</b>" + "<br /><p>User Post: "+ econtent.userPost + "</p>" + "<br /><p>Followers: "+ econtent.userFollowers + "</p>" + "<br /><p>Following: "+ econtent.userFollowing + "</p><a href='#' style='color:#000' data-toggle='modal' data-target='#disconnect-instagram-menu'><p style='color:#fff; position: absolute; bottom:1px; right:3%; float:right;'>Disconnect</p></a></div>");
          }
        }
      },
      async:false,
    });
  }
  checkInstagramAccount();

  // Instagram Post
  //Using ajax onsubmit and running function
  $(document).ready(function(){
    $('#instagram-form').submit(function(event){
      event.preventDefault();
      var instagramPostUser = "{{ user.username }}";
      var url = '{% url 'instagram-post/' %}';
      $('#instagram-post-login').html('Logging In.');
      //using ajax to call function
      $.ajax({
        type: 'POST',
        url: url,
        dataType: 'text',
        data: {
          csrfmiddlewaretoken: '{{ csrf_token }}',
          //Returning Information as objects
          'instagramPostUser':$('#instagram-user').val(),
          'instagramUsername':$('#instagram-username').val(),
          'instagramPassword':$('#instagram-password').val()
        },
        success: function (value) {
          var evalue = JSON.parse(value);
          console.log(evalue);
          var message = evalue.message;
          if(message == 'success'){
            //dismissing modal
            checkInstagramAccount();
            $("#hidden-cancel-instagram").click();
          } else {
            $('#instagram-post-error').html('Error logging in. Please try again.');
          }
        }
      });
    });
  });

  // Instagram Disconnect
  $(document).ready(function(){
    $('#disconnect-button-instagram').click(function(event){
      event.preventDefault();
      var url = '{% url 'disconnect-instagram/' %}'
      var usernameVerify = "{{ user.username }}";
      //using ajax to call function
      $.ajax({
        type: 'POST',
        url: url,
        dataType: 'text',
        data: {
          // Token needed to return data in Python
          csrfmiddlewaretoken: '{{ csrf_token }}',
          //Returning Information as objects
          'instagramPostUser':usernameVerify,
        },
        success: function (value) {
          //dismissing modal
          $('#hidden-cancel-instagram-disconnect').click();
          $('#content-instagram').html(content);

          //Displaying information
          $("#content-instagram").hide();
          $("#disconnect-instagram").hide();
          $("#connect-header-instagram").show();
        }
      });
    });
  });

  // TWITTER AJAX FUNCTIONS

  function checkTwitterAccount(e){
    var usernameVerify = "{{ user.username }}";
    var url = '{% url 'check-out-twitter/' %}';
    console.log("Twitter Username: " + usernameVerify)
    $.ajax({
      type: 'POST',
      url: url,
      dataType: 'text',
      data: {
        csrfmiddlewaretoken: '{{ csrf_token }}',
        'twitter_user':usernameVerify,

      },
      success: function (content) {
        //Showing and hidding certain information depending on returned information
        var econtent = JSON.parse(content);
        if(content == ''){
            $("#content-twitter").hide();
            $("#disconnect-twitter").hide();
            $("#connect-header-twitter").show();
            $('#content-twitter').html(content);
        } else {
          if(econtent.user == usernameVerify){
            $("#content-twitter").show();
            $("#disconnect-twitter").show();
            $("#connect-header-twitter").hide();
            $('#content-twitter').html("<b>"+ econtent.username + "</b>" + "<br /><p>User Tweets: "+ econtent.userPost + "</p>" + "<br /><p>Followers: "+ econtent.userFollowers + "</p>" + "<br /><p>Following: "+ econtent.userFollowing + "</p>");

            // Checking Global variables
            TWITTER_TOTAL_TWEETS = econtent.userPost;
            TWITTER_TOTAL_FOLLOWERS = econtent.userFollowers;
            TWITTER_TOTAL_FOLLOWING = econtent.userFollowing;

            //Creating a Div
            var dashboardRow = document.getElementById('dashboard-row')

            var twitterDiv = document.createElement('div');
            twitterDiv.className = "col-sm-16";
            var divID = 'holder-3'
            twitterDiv.setAttribute('id', "holder-3");

            dashboardRow.appendChild(twitterDiv);
            $('#holder-3').html("<div class='card' style='background: #28aae1;;'> <b>"+ econtent.username + "</b>" + "<br /><p>User Post: "+ econtent.userPost + "</p>" + "<br /><p>Followers: "+ econtent.userFollowers + "</p>" + "<br /><p>Following: "+ econtent.userFollowing + "</p><a href='#' style='color:#000' data-toggle='modal' data-target='#disconnect-twitter-menu'><p style='color:#fff; position: absolute; bottom:1px; right:3%; float:right;'>Disconnect</p></a></div>");
          }
        }
      },
      async:false,
    });
  }
  checkTwitterAccount();

  // Twitter Post
  //Using ajax onsubmit and running function
  $(document).ready(function(){
    $('#twitter-form').submit(function(event){
      event.preventDefault();
      var twitterPostUser = "{{ user.username }}"
      var url = '{% url 'twitter-post/' %}'
      $('#twitter-post-login').html('Logging In.');
      //using ajax to call function
      $.ajax({
        type: 'POST',
        url: url,
        dataType: 'text',
        data: {
          csrfmiddlewaretoken: '{{ csrf_token }}',
          //Returning Information as objects
          'twitterPostUser':$('#twitter-user').val(),
          'twitterUsername':$('#twitter-username').val(),
          'twitterPassword':$('#twitter-password').val()
        },
        success: function (value) {
          var evalue = JSON.parse(value);
          var message = evalue.message;
          if (message == 'success') {
            //dismissing modal
            checkTwitterAccount();
            $('#hidden-cancel-twitter').click();
          } else {
          $('#twitter-post-error').html('Error logging in. Please try again.');
          }
        }
      });
    });
  });

  // Twitter Disconnect
  $(document).ready(function(){
    $('#disconnect-button-twitter').click(function(event){
      event.preventDefault();
      var url = '{% url 'disconnect-twitter/' %}'
      var usernameVerify = "{{ user.username }}";

      //using ajax to call function
      $.ajax({
        type: 'POST',
        url: url,
        dataType: 'text',
        data: {
          // Token needed to return data in Python
          csrfmiddlewaretoken: '{{ csrf_token }}',
          //Returning Information as objects
          'twitterPostUser':usernameVerify,
        },
        success: function (content) {
          //dismissing modal
          $('#hidden-cancel-twitter-disconnect').click();
          $('#content-twitter').html(content);

          //Displaying information
          $("#content-twitter").hide();
          $("#disconnect-twitter").hide();
          $("#connect-header-twitter").show();
        }
      });
    });
  });
  var instagram_total_followers = parseInt(INSTAGRAM_TOTAL_FOLLOWERS, 10);
  var twitter_total_followers = parseInt(TWITTER_TOTAL_FOLLOWERS, 10);

  alert(instagram_total_followers + twitter_total_followers);
