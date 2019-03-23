// showing dashboard row by default
$("#admin").show();

// hiding analytics by default
$("#analytics").hide();
$("#accounts").hide();
$("#settings").hide();

// Hidding and Showing Dashboard content onclick

$("#show-analytics").click(function(){
 $("#admin").hide();
 $("#analytics").show();
 $("#settings").hide();
 $("#accounts").hide();
});

$("#show-accounts").click(function(){
  $("#admin").hide();
  $("#analytics").hide();
  $("#settings").hide();
  $("#accounts").show();
});
$("#show-home").click(function(){
  $("#admin").show();
  $("#analytics").hide();
  $("#settings").hide();
  $("#accounts").hide();
});

$("#account-title").click(function(){
  $("#admin").hide();
  $("#analytics").hide();
  $("#accounts").show();
  $("#settings").hide();
});

$("#show-settings").click(function(){
  $("#admin").hide();
  $("#analytics").hide();
  $("#accounts").hide();
  $("#settings").show();
});
// Creating Divs

    // // Random Id Generator
    // var ID = function () {
    //   // Math.random should be unique because of its seeding algorithm.
    //   // Convert it to base 36 (numbers + letters), and grab the first 9 characters
    //   // after the decimal.
    //   return '_' + Math.random().toString(36).substr(2, 9);
    // };
    //
    // // Print function
    // function print(e){
    //   console.log(e);
    // }
    //
    // // Removing the Footer
    // $("#footer").remove();
    //
    // // Function to get element by Xpath
    // function getElementByXpath(path) {
    //   return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    // }
    // // INSTAGRAM AJAX FUNCTIONS
    //   function getInstagramData(content){
    //     var econtent = JSON.parse(content);
    //     var user = [];
    //     var length = [];
    //     var username = [];
    //     var totalPostArray = [];
    //     var totalFollowersArray = [];
    //     var totalFollowingArray = [];
    //     var bio = [];
    //     var location = [];
    //
    //     for (let i = 0; i < econtent.length; i++) {
    //       user.push(econtent[i].user);
    //       length.push(econtent.length);
    //       username.push(econtent[i].username);
    //       totalPostArray.push(econtent[i].userPost);
    //       totalFollowersArray.push(econtent[i].userFollowers);
    //       totalFollowingArray.push(econtent[i].userFollowing);
    //       bio.push(econtent[i].userBio);
    //     }
    //     var obj={
    //         "user":user,
    //         "length":length,
    //         "username":username,
    //         "userPost":totalPostArray,
    //         "userFollowers": totalFollowersArray,
    //         "userFollowing": totalFollowingArray,
    //         "bio": bio,
    //
    //     };
    //
    //     return obj;
    //
    //   }
    //
    //   function showInstagramDiv(content, i){
    //
    //     var econtent = content;
    //     var instagramId = 'instagram-div';
    //     $('#' + instagramId).html("<div class='card'><a href='#'><img src='../../../static/dashboard/img/instagram.jpg' style='position: absolute; right:3%; float:right;'/></a><b> <select id='select-account-instagram' onchange='instagramSelectChange(this)'><option selected>"+ econtent.username[i] + "</option></select></b><br /><p>User Post: <span id='instagram-user-post'>" + econtent.userPost[i] +"</span> Bio: <a href='#' data-toggle='modal' data-target='#edit-bio-instagram-menu'><span id='instagram-user-bio'>" + econtent.bio[i] + "</span></a></p>" + "<br /><p>Followers: <span id='instagram-user-followers'>" + econtent.userFollowers[i] + "</span></p><br /><p>Following: <span id='instagram-user-following'>" + econtent.userFollowing[i] + "</span></p><p></p><a href='#' style='color:#000' data-toggle='modal' data-target='#disconnect-instagram-menu'><p style='position: absolute; bottom:1px; right:3%; float:right;'>Disconnect</p></a></div>");
    //   }
    //   function showInstagramSelect(content, i){
    //     var econtent = content;
    //     var addInstagramAccount = document.createElement('option');
    //     var parentElement = document.getElementById('select-account-instagram');
    //     var instagramIdUnique = ID();
    //     var uniqueId = 'handler-' + instagramIdUnique;
    //     addInstagramAccount.setAttribute('id', uniqueId);
    //
    //     var text = document.createTextNode(econtent.username[i]);
    //     parentElement.appendChild(addInstagramAccount);
    //     addInstagramAccount.appendChild(text);
    //
    //   }
    //
    //   function InstagramDisplay(content){
    //     //Showing and hidding certain information depending on returned information
    //     var econtent = content;
    //     if(econtent != ''){
    //       var usernameVerify = "{{ user.username }}";
    //       if(econtent.user[0] == usernameVerify){
    //         for (var i = 0; i < econtent.length[0]; i++) {
    //
    //           // Defining account div
    //           var dashboardRow = document.getElementById('account-divs');
    //
    //           // Instagram Account Div
    //           var instagramDiv = document.createElement('div');
    //           instagramDiv.className = "col-sm-16";
    //           instagramDiv.setAttribute('id', 'instagram-div');
    //           dashboardRow.appendChild(instagramDiv);
    //
    //           // Defining Graph Div
    //           var instagramGraph = document.createElement('canvas');
    //           instagramGraph.className = "container";
    //           instagramGraph.setAttribute('id', 'instagram-graph');
    //           dashboardRow.appendChild(instagramGraph);
    //
    //           // Adding Checkboxes to Popups
    //
    //           // Defining Choose Social Media Div
    //           var chooseSocialPostDiv = document.getElementById('choose-social-media-post-opperation');
    //
    //           // Defining New Div for Checkboxes
    //           var chooseSocialPostName = document.createElement('p');
    //           var chooseSocialPostCheckbox = document.createElement('input');
    //           chooseSocialPostCheckbox.className = 'post-opperation-item';
    //           chooseSocialPostCheckbox.setAttribute('type', 'checkbox');
    //           chooseSocialPostCheckbox.setAttribute('value', econtent.username[i]);
    //
    //           var chooseSocialPostUsername = document.createTextNode(econtent.username[i] + "(instagram) ");
    //           chooseSocialPostName.appendChild(chooseSocialPostUsername);
    //           chooseSocialPostName.appendChild(chooseSocialPostCheckbox);
    //           chooseSocialPostDiv.appendChild(chooseSocialPostName);
    //
    //
    //
    //           var elementExists = document.getElementById("select-account-instagram");
    //           if (elementExists != null) {
    //             showInstagramSelect(econtent, i);
    //           } else {
    //             showInstagramDiv(econtent, i);
    //             // graphsInstagramControl(econtent, i);
    //           }
    //         }
    //       }
    //     }
    //   }
    //   function viewOpperationHistory(content){
    //     econtent = content;
    //     var dashboardRow = document.getElementById('opperation-history');
    //
    //     var opperationHistoryItem = document.createElement('div');
    //     opperationHistoryItem.setAttribute('id', 'opperation-div-card');
    //     opperationHistoryItem.className = "card";
    //     $(opperationHistoryItem).html('');
    //   }
    //
    //   function graphsInstagramControl(content, i){
    //     econtent = content;
    //     alert(econtent.userFollowers[i]);
    //     var elementExists = document.getElementById("instagram-graph");
    //     let instagramGraphDiv = elementExists.getContext("2d");
    //
    //     let instagramGraph = new Chart(instagramGraphDiv, {
    //       type:'bar', // Making a pie chart
    //       data:{
    //         labels:['Followers', 'Following', 'Post'],
    //         datasets:[{
    //           label:'Works',
    //           data:[
    //             econtent.userFollowers[i],
    //             econtent.userFollowing[i],
    //             econtent.userPost[i]
    //           ],
    //           backgroundColor: [
    //             '#000',
    //             '#000',
    //             '#000'
    //           ]
    //         }]
    //       },
    //       options:{
    //         title:{
    //           display:true,
    //           text: 'Followers Vs. Following',
    //           responsive: false
    //         }
    //       }
    //     });
    //   }
    //   function instagramOptionChange(selectObject, content, i){
    //     var hope = content;
    //   }
    //   //Checking State of logged in accounts
    //   function checkInstagramAccount(e){
    //     var url = 'instagram-account-check';
    //     var usernameVerify = "{{ user.username }}";
    //     $.ajax({
    //       type: 'POST',
    //       url: url,
    //       dataType: 'text',
    //       data: {
    //         csrfmiddlewaretoken: $('meta[name="_token"]').attr('content'),
    //         'instagram_user':usernameVerify,
    //
    //       },
    //       success: function (content) {
    //         var getData = getInstagramData(content);
    //         var getInfo = InstagramDisplay(getData);
    //         var ttlAmount = totalAmountInstagram(content);
    //         changeBioPlaceHolder();
    //       },
    //     });
    //   }
    //   checkInstagramAccount();
    //   // Instagram Disconnect
    //   $(document).ready(function(){
    //     $('#disconnect-button-instagram').click(function(event){
    //       var getSelected = document.getElementById("select-account-instagram");
    //       var selectedOption = getSelected.options[getSelected.selectedIndex].value;
    //       event.preventDefault();
    //       var url = 'instagram-account-disconnect'
    //       var usernameVerify = "{{ user.username }}";
    //       //using ajax to call function
    //       $.ajax({
    //         type: 'POST',
    //         url: url,
    //         dataType: 'text',
    //         data: {
    //           // Token needed to return data in Python
    //           csrfmiddlewaretoken: $('meta[name="_token"]').attr('content'),
    //           //Returning Information as objects
    //           'instagramPostUser':usernameVerify,
    //           'selectedOption':selectedOption,
    //         },
    //         success: function (value) {
    //           location.reload();
    //         }
    //       });
    //     });
    //   });
    //
    //   function changeBioPlaceHolder(){
    //     // Getting Current Text and Putting it in text boxes
    //     var textUserInstagram = $('#instagram-user-bio').text();
    //     var textUserTwitter = $('#twitter-user-bio').text();
    //
    //     $('#new-bio-instagram').val(textUserInstagram);
    //     $('#new-bio-twitter').val(textUserTwitter);
    //
    //   }
    //
    //
    //   // Change Bio Twitter
    //   $(document).ready(function(){
    //     $('#bio-change-submit-instagram').click(function(event){
    //       var getSelected = document.getElementById("select-account-instagram");
    //       var newBio = document.getElementById("new-bio-instagram").value;
    //       var selectedOption = getSelected.options[getSelected.selectedIndex].value;
    //       event.preventDefault();
    //       var url = 'instagram-bio-change'
    //       var usernameVerify = "{{ user.username }}";
    //       //using ajax to call function
    //       $.ajax({
    //         type: 'POST',
    //         url: url,
    //         dataType: 'text',
    //         data: {
    //           // Token needed to return data in Python
    //           csrfmiddlewaretoken: $('meta[name="_token"]').attr('content'),
    //           //Returning Information as objects
    //           'instagramPostUser':usernameVerify,
    //           'selectedOption':selectedOption,
    //           'newBio': newBio
    //         },
    //         success: function (value) {
    //           checkInstagramAccount();
    //           if(value == 'succes'){
    //
    //           }
    //         }
    //       });
    //     });
    //   });
    //
    //   // Change Bio Twitter
    //   $(document).ready(function(){
    //     $('#bio-change-submit-twitter').click(function(event){
    //       var getSelected = document.getElementById("select-account-twitter");
    //       var newBio = document.getElementById("new-bio-twitter").value;
    //       var selectedOption = getSelected.options[getSelected.selectedIndex].value;
    //       event.preventDefault();
    //       var url = 'twitter-bio-change'
    //       var usernameVerify = "{{ user.username }}";
    //       //using ajax to call function
    //       $.ajax({
    //         type: 'POST',
    //         url: url,
    //         dataType: 'text',
    //         data: {
    //           // Token needed to return data in Python
    //           csrfmiddlewaretoken: $('meta[name="_token"]').attr('content'),
    //           //Returning Information as objects
    //           'twitterPostUser':usernameVerify,
    //           'selectedOption':selectedOption,
    //           'newBio': newBio
    //         },
    //         success: function (value) {
    //           checkTwitterAccount();
    //           if(value == 'success'){
    //
    //           }
    //         }
    //       });
    //     });
    //   });
    //
    //
    //   function twitterOptionChange(selectObject, content, i){
    //     var hope = content;
    //   }
    //
    //   function showTwitterDiv(content, i){
    //     var econtent = content;
    //     var twitterId = 'twitter-div';
    //     var chick = 'dfv';
    //     $('#' + twitterId).html("<div class='card'><a href=''><img src='../../../static/dashboard/img/twitter.png' style='position: absolute; right:3%; float:right;'/></a><b> <select id='select-account-twitter' onchange='twitterSelectChange(this)'><option selected>"+ econtent.username[i] + "</option></select></b><br /><p>User Tweets: <span id='twitter-user-post'>" + econtent.userPost[i] +"</span> Bio: <a href='#' data-toggle='modal' data-target='#edit-bio-twitter-menu'><span id='twitter-user-bio'>" + econtent.bio[i] + "</span></a></p>" + "<p>Followers: <span id='twitter-user-followers'>" + econtent.userFollowers[i] + "</span></p>" + "<br /><p>Following: <span id='twitter-user-following'>" + econtent.userFollowing[i] + "</p><p id='twitter-user-location'>Location: <span>" + econtent.location[i] + "</span></p><a href='#' style='color:#000' data-toggle='modal' data-target='#disconnect-twitter-menu'><p style='position: absolute; bottom:1px; right:3%; float:right;'>Disconnect</p></a></div>");
    //   }
    //
    //   function showTwitterSelect(content, i){
    //     var econtent = content;
    //     var addTwitterAccount = document.createElement('option');
    //     var parentElement = document.getElementById('select-account-twitter');
    //     var twitterIdUnique = ID();
    //     var uniqueId = 'handler-' + twitterIdUnique;
    //     addTwitterAccount.setAttribute('id', uniqueId);
    //
    //     var text = document.createTextNode(econtent.username[i]);
    //     parentElement.appendChild(addTwitterAccount);
    //     addTwitterAccount.appendChild(text);
    //   }
    //
    //   function TwitterDisplay(content){
    //     //Showing and hidding certain information depending on returned information
    //     var econtent = content;
    //
    //     if(econtent != ''){
    //       var usernameVerify = "{{ user.username }}";
    //
    //       if(econtent.user[0] == usernameVerify){
    //
    //         for (let i = 0; i < econtent.length[0]; i++) {
    //           //Creating a Div
    //           var dashboardRow = document.getElementById('account-divs');
    //
    //           var twitterDiv = document.createElement('div');
    //           twitterDiv.className = "col-sm-16";
    //           var twitterId = 'twitter-div';
    //           twitterDiv.setAttribute('id', twitterId);
    //           dashboardRow.appendChild(twitterDiv);
    //
    //           // Adding Checkboxes to Popups
    //
    //           // Defining Choose Social Media Div
    //           var chooseSocialPostDiv = document.getElementById('choose-social-media-post-opperation');
    //
    //           // Defining New Div for Checkboxes
    //           var chooseSocialPostName = document.createElement('p');
    //           var chooseSocialPostCheckbox = document.createElement('input');
    //           chooseSocialPostCheckbox.className = 'post-opperation-item';
    //           chooseSocialPostCheckbox.setAttribute('type', 'checkbox');
    //           chooseSocialPostCheckbox.setAttribute('value', econtent.username[i]);
    //
    //           var chooseSocialPostUsername = document.createTextNode(econtent.username[i] + "(twitter) ");
    //           chooseSocialPostName.appendChild(chooseSocialPostUsername);
    //           chooseSocialPostName.appendChild(chooseSocialPostCheckbox);
    //           chooseSocialPostDiv.appendChild(chooseSocialPostName);
    //
    //           var elementExists = document.getElementById("select-account-twitter");
    //
    //           if (elementExists == null) {
    //             showTwitterDiv(econtent, i);
    //           } else {
    //             showTwitterSelect(econtent, i);
    //           }
    //           // changeOpp(content, i);
    //         }
    //       }
    //     }
    //   }
    //
    //   function getTwitterData(content){
    //     var econtent = JSON.parse(content);
    //     var user = [];
    //     var length = [];
    //     var username = [];
    //     var totalPostArray = [];
    //     var totalFollowersArray = [];
    //     var totalFollowingArray = [];
    //     var bio = [];
    //     var location = [];
    //
    //
    //     for (let i = 0; i < econtent.length; i++) {
    //       user.push(econtent[i].user);
    //       length.push(econtent.length);
    //       username.push(econtent[i].username);
    //       totalPostArray.push(econtent[i].userPost);
    //       totalFollowersArray.push(econtent[i].userFollowers);
    //       totalFollowingArray.push(econtent[i].userFollowing);
    //       bio.push(econtent[i].userBio);
    //       location.push(econtent[i].userLocation);
    //     }
    //     var obj={
    //         "user":user,
    //         "length":length,
    //         "username":username,
    //         "userPost":totalPostArray,
    //         "userFollowers": totalFollowersArray,
    //         "userFollowing": totalFollowingArray,
    //         "bio": bio,
    //         "location": location
    //
    //     };
    //
    //     return obj;
    //
    //   }
    //
    //   // TWITTER AJAX FUNCTIONS
    //
    //   function checkTwitterAccount(e){
    //     var usernameVerify = "{{ user.username }}";
    //     var url = 'twitter-account-check';
    //     $.ajax({
    //       type: 'POST',
    //       url: url,
    //       dataType: 'text',
    //       data: {
    //         csrfmiddlewaretoken: $('meta[name="_token"]').attr('content'),
    //         'twitter_user':usernameVerify,
    //
    //       },
    //       success: function (content) {
    //         var getData = getTwitterData(content)
    //         var getInfo = TwitterDisplay(getData);
    //         changeBioPlaceHolder();
    //         // var ttlAmount = totalAmountTwitter(content);
    //         // summary(ttlAmount);
    //
    //       },
    //     });
    //   }
    //   checkTwitterAccount();
    //
    //   // Twitter Disconnect
    //   $(document).ready(function(){
    //     $('#disconnect-button-twitter').click(function(event){
    //       var getSelected = document.getElementById("select-account-twitter");
    //       var selectedOption = getSelected.options[getSelected.selectedIndex].value;
    //       event.preventDefault();
    //       var url = 'twitter-account-disconnect'
    //       var usernameVerify = "{{ user.username }}";
    //
    //       //using ajax to call function
    //       $.ajax({
    //         type: 'POST',
    //         url: url,
    //         dataType: 'text',
    //         data: {
    //           // Token needed to return data in Python
    //           csrfmiddlewaretoken: $('meta[name="_token"]').attr('content'),
    //           //Returning Information as objects
    //           'twitterPostUser':usernameVerify,
    //           'selectedOption':selectedOption
    //         },
    //         success: function (content) {
    //           location.reload();
    //         }
    //       });
    //     });
    //   });
    //
    //   // Posting
    //
    //   // Getting Selected option
    //   function optionChange(selectObject) {
    //       selectedValue = selectObject.value;
    //       if(selectedValue == 'instagram'){
    //       $('#username').attr('placeholder','Instagram Username');
    //       $('#password').attr('placeholder','Instagram Password');
    //       postSocial(selectedValue);
    //       } else if (selectedValue == 'twitter') {
    //       $('#username').attr('placeholder','Twitter Username');
    //       $('#password').attr('placeholder','Twitter Password');
    //       postSocial(selectedValue);
    //     } else {
    //       $('#username').attr('placeholder','Account Username');
    //       $('#password').attr('placeholder','Account Password');
    //     }
    //   }
    //   function opperationOptionChange(){
    //     var e = document.getElementById("select-opperation-type");
    //     var opperationSelectedValuePlatform = e.options[e.selectedIndex].value;
    //       if(opperationSelectedValuePlatform == 'post-on-social'){
    //         // Option to Post on social Media at Once
    //         $('#opperation-post-javascript').html('<p>Post On Social Media <br /><input type="file" name="post-image" accept="image/*"><br /</p>Add a caption:<p><textarea maxlength="2200" id="post-caption-opperation" placeholder="Caption/Tweet" cols="30" rows="5"></textarea></p>Choose Platform(s): <br />');
    //         postOpperation(null, null, opperationSelectedValuePlatform);
    //         $('#choose-social-media-post-opperation').show();
    //       } else if (opperationSelectedValuePlatform == 'auto-like') {
    //
    //         // Auto Likes
    //         $('#opperation-post-javascript').html('<p>Auto Like Post on Social Media: </p><p>Automatic Likes/Favorites <select id="number-likes-favorites"><option value="25">25 Likes</option><option value="50">50 Likes</option><option value="100">100 Likes</option></select></p>Hashtags<p><textarea maxlength="140" id="likes-favorites-hashtags" cols="30" rows="5" placeholder="Ex: money,entrepreneur,lifestyle"></textarea></p>Choose Platform(s): <br />');
    //         postOpperation(null, null, opperationSelectedValuePlatform);
    //         $('#choose-social-media-post-opperation').show();
    //       } else if (opperationSelectedValuePlatform == 'auto-follow') {
    //
    //         // Auto Follow
    //         $('#opperation-post-javascript').html('<p>Auto Follow Users on Social Media </p><p><select id="number-followers"><option value="25">25 Follows</option><option value="50">50 Follows</option><option value="100">100 Follows</option></select></p><p><textarea maxlength="140" id="follow-hashtags" cols="20" rows="5" placeholder="Ex: money, entrepreneur, lifestyle"></textarea></p>Choose Platform(s): <br />');
    //         postOpperation(null, null, opperationSelectedValuePlatform);
    //         $('#choose-social-media-post-opperation').show();
    //     }
    //   }
    //   opperationOptionChange();
    //
    //
    //
    //
    //
    //
    //
    //
    //   function postOpperation(content, contentTwo, selectedObject){
    //     selectedValue = selectedObject;
    //     $('#opperation-post-form').submit(function(event){
    //       event.preventDefault();
    //       var usernames = [];
    //       postOpperationItem = document.getElementsByClassName("post-opperation-item");
    //       for(var i = 0; i < postOpperationItem.length; i++) {
    //           // Looking for value which is the username
    //           var pushedPostOpperationItem = postOpperationItem[i].value;
    //           if(postOpperationItem[i].checked){
    //
    //             // Checking if box is checked
    //             usernames.push(pushedPostOpperationItem);
    //         }
    //       }
    //       var postUser = "{{ user.username }}";
    //       if (selectedValue == 'post-on-social') {
    //         var opperationCaption = document.getElementById('post-caption-opperation');
    //         var url = 'post-on-social';
    //         $('#opperation-success').html('Attempting Opperation.');
    //         //using ajax to call function
    //         $.ajax({
    //           type: 'POST',
    //           url: url,
    //           dataType: 'text',
    //           data: {
    //             csrfmiddlewaretoken: $('meta[name="_token"]').attr('content'),
    //             // Posting information
    //             'opperationPostUser':postUser,
    //
    //             // Returning Inputed Values
    //             'opperationCaption':opperationCaption.value,
    //
    //             // Returning Values of Checked off Boxes
    //             'usernames[]':usernames,
    //
    //           },
    //           success: function (value) {
    //             var evalue = JSON.parse(value);
    //             alert(evalue.message);
    //             if (evalue.message == 'success'){
    //               $('#opperation-success').html('Opperation Successful!');
    //               getOpperationHistory();
    //             } else if (evalue.message == 'failed') {
    //               $('#opperation-failed').html('Something went wrong. Try again');
    //             } else{
    //               $('#opperation-failed').html('Something went wrong. Try again');
    //             }
    //           }
    //         });
    //       } else if (selectedValue == 'auto-like'){
    //         var e = document.getElementById('number-likes-favorites');
    //         var selectedAmount = e.options[e.selectedIndex].value;
    //         var hashtags = document.getElementById('likes-favorites-hashtags').value;
    //         // alert(hashtags);
    //         // var hashtagArray = JSON.parse("[" + hashtags + "]");
    //         var hashtagArray = hashtags.split(",")
    //         var url = 'auto-like-favorite';
    //         $('#opperation-success').html('Attempting Opperation.');
    //         //using ajax to call function
    //         $.ajax({
    //           type: 'POST',
    //           url: url,
    //           dataType: 'text',
    //           data: {
    //             csrfmiddlewaretoken: $('meta[name="_token"]').attr('content'),
    //             // Posting information
    //             'opperationPostUser':postUser,
    //
    //             // Returning Inputed Values
    //             'hashtagsArray[]':hashtagArray,
    //
    //             // Returning Values of Checked off Boxes
    //             'usernames[]':usernames,
    //
    //             // Getting Selected Request of likes
    //             'amountOfLikes':selectedAmount,
    //
    //
    //           },
    //           success: function (value) {
    //             if (value == 'success'){
    //               $('#opperation-success').html('Opperation Successful!');
    //               getOpperationHistory();
    //             } else if (value == 'failed') {
    //               $('#opperation-failed').html('Something went wrong. Try again');
    //             } else{
    //               $('#opperation-failed').html('Something went wrong. Try again');
    //             }
    //           }
    //         });
    //       } else if(selectedValue == 'auto-follow'){
    //         var e = document.getElementById('number-followers');
    //         var selectedAmount = e.options[e.selectedIndex].value;
    //         var hashtags = document.getElementById('follow-hashtags').value;
    //         // alert(hashtags);
    //         // var hashtagArray = JSON.parse("[" + hashtags + "]");
    //         var hashtagArray = hashtags.split(",")
    //         var url = 'auto-follow';
    //         $('#opperation-success').html('Attempting Opperation.');
    //         //using ajax to call function
    //         $.ajax({
    //           type: 'POST',
    //           url: url,
    //           dataType: 'text',
    //           data: {
    //             csrfmiddlewaretoken: $('meta[name="_token"]').attr('content'),
    //             // Posting information
    //             'opperationPostUser':postUser,
    //
    //             // Returning Inputed Values
    //             'hashtagsArray[]':hashtagArray,
    //
    //             // Returning Values of Checked off Boxes
    //             'usernames[]':usernames,
    //
    //             // Getting Selected Request of likes
    //             'amountOfLikes':selectedAmount,
    //
    //
    //           },
    //           success: function (value) {
    //             alert(value);
    //             if (value == 'success'){
    //               $('#opperation-success').html('Opperation Successful!');
    //               getOpperationHistory();
    //             } else if (value == 'failed') {
    //               $('#opperation-failed').html('Something went wrong. Try again');
    //             } else{
    //               alert(value)
    //               $('#opperation-failed').html('Something went wrong. Try again');
    //             }
    //           }
    //         });
    //       }
    //     });
    //   }
    //
    //
    //
    //
    //
    //
    //
    //   function instagramSelectChange(element){
    //     var selectedValue = element.options[element.selectedIndex].text;
    //     var url = 'instagram-onchange';
    //     var usernameVerify = "{{ user.username }}";
    //     $.ajax({
    //       type: 'POST',
    //       url: url,
    //       dataType: 'text',
    //       data: {
    //         csrfmiddlewaretoken: $('meta[name="_token"]').attr('content'),
    //         //Returning Information as objects
    //         'usernameVerify': usernameVerify,
    //         'selectedValue': selectedValue
    //       },
    //       success: function (content) {
    //         var econtent = JSON.parse(content);
    //         $('#instagram-user-post').html(econtent.userPost);
    //         $('#instagram-user-followers').html(econtent.userFollowers);
    //         $('#instagram-user-following').html(econtent.userFollowing);
    //         $('#instagram-user-following').html(econtent.bio);
    //       }
    //     });
    //   }
    //
    //
    //
    //
    //
    //
    //
    //   function twitterSelectChange(element){
    //     var selectedValue = element.options[element.selectedIndex].text;
    //     var url = 'twitter-onchange';
    //     var usernameVerify = "{{ user.username }}";
    //     $.ajax({
    //       type: 'POST',
    //       url: url,
    //       dataType: 'text',
    //       data: {
    //         csrfmiddlewaretoken: $('meta[name="_token"]').attr('content'),
    //         //Returning Information as objects
    //         'usernameVerify': usernameVerify,
    //         'selectedValue': selectedValue
    //       },
    //       success: function (content) {
    //         var econtent = JSON.parse(content);
    //         $('#twitter-user-post').html(econtent.userPost);
    //         $('#twitter-user-followers').html(econtent.userFollowers);
    //         $('#twitter-user-following').html(econtent.userFollowing);
    //       }
    //     });
    //   }
    //   //Checking State of logged in accounts
    //   function getTotalSummary(e){
    //     var url = 'get-total-summary';
    //     var usernameVerify = "{{ user.username }}";
    //     $.ajax({
    //       type: 'POST',
    //       url: url,
    //       dataType: 'text',
    //       data: {
    //         csrfmiddlewaretoken: $('meta[name="_token"]').attr('content'),
    //         'usernameVerify':usernameVerify,
    //
    //       },
    //       success: function (content) {
    //         summary(content);
    //       },
    //     });
    //   }
    //   getTotalSummary();
    //
    //
    //
    //
    //
    //
    //
    //   function postSocial(selectedObject){
    //     var selectedValue = selectedObject;
    //     // Getting Selected Value
    //     var e = document.getElementById("select-account-type");
    //
    //     $('#posting-form').submit(function(event){
    //
    //       if (selectedValue == 'instagram') {
    //         event.preventDefault();
    //         var instagramPostUser = "{{ user.username }}";
    //         var url = 'instagram-posting';
    //         $('#post-login').html('Logging In.');
    //         //using ajax to call function
    //         $.ajax({
    //           type: 'POST',
    //           url: url,
    //           dataType: 'text',
    //           data: {
    //             csrfmiddlewaretoken: $('meta[name="_token"]').attr('content'),
    //             //Returning Information as objects
    //             'instagramPostUser':$('#user').val(),
    //             'instagramUsername':$('#username').val(),
    //             'instagramPassword':$('#password').val()
    //           },
    //           success: function (value) {
    //             var evalue = JSON.parse(value);
    //             var message = evalue.message;
    //             if(message == 'success'){
    //               //dismissing modal
    //               checkInstagramAccount();
    //               $("#hidden-cancel").click();
    //               $('#post-login').html('');
    //             } else {
    //               $('#instagram-post-error').html('Error logging in. Please try again.');
    //             }
    //           }
    //         });
    //       } else if (selectedValue == 'twitter') {
    //         event.preventDefault();
    //         var twitterPostUser = "{{ user.username }}"
    //         var url = 'twitter-posting'
    //         $('#post-login').html('Logging In.');
    //         //using ajax to call function
    //         $.ajax({
    //           type: 'POST',
    //           url: url,
    //           dataType: 'text',
    //           data: {
    //             csrfmiddlewaretoken: $('meta[name="_token"]').attr('content'),
    //             //Returning Information as objects
    //             'twitterPostUser':$('#user').val(),
    //             'twitterUsername':$('#username').val(),
    //             'twitterPassword':$('#password').val()
    //           },
    //           success: function (value) {
    //             var evalue = JSON.parse(value);
    //             var message = evalue.message;
    //             if (message == 'success') {
    //
    //               //dismissing modal
    //               checkTwitterAccount();
    //               $('#hidden-cancel').click();
    //               $('#post-login').html('');
    //             } else {
    //             $('#post-error').html('Error logging in. Please try again.');
    //             }
    //           }
    //         });
    //       } else {
    //         $('#post-error').html('Account type is not selected!');
    //       }
    //     });
    //   }
    //
    //   function totalAmountInstagram(content){
    //     var econtent = JSON.parse(content);
    //     var total_post_instagram = 0;
    //     var total_followers_instagram = 0;
    //     var total_following_instagram = 0;
    //
    //     for (let i = 0; i < econtent.length; i++) {
    //       total_post_instagram += parseInt(econtent[i].userPost);
    //       total_followers_instagram += parseInt(econtent[i].userFollowers);
    //       total_following_instagram += parseInt(econtent[i].userFollowing);
    //
    //     }
    //     var obj={
    //         "totalPost":total_post_instagram,
    //         "totalFollowers": total_followers_instagram,
    //         "totalFollowing": total_following_instagram
    //
    //     };
    //
    //     return obj;
    //   }
    //
    //   function summary(content){
    //     var econtent = JSON.parse(content);
    //
    //     // Instagram Variables
    //     var totalInstagramPost = econtent.instagramUserPost;
    //     var totalInstagramFollowers = econtent.instagramUserFollowers;
    //     var totalInstagramFollowing = econtent.instagramUserFollowing;
    //
    //     // Twitter Variables
    //     var totalTwitterPost = econtent.twitterUserPost;
    //     var totalTwitterFollowers = econtent.twitterUserFollowers;
    //     var totalTwitterFollowing = econtent.twitterUserFollowing;
    //
    //     // Total Variables
    //     var totalPost = totalInstagramPost + totalTwitterPost;
    //     var totalFollowers = totalInstagramFollowers + totalTwitterFollowers;
    //     var totalFollowing = totalInstagramFollowing + totalTwitterFollowing;
    //
    //     if (totalPost < 5 && totalFollowers < 5 && totalFollowing < 5) {
    //       $('#total-followers').html("Total Audience:");
    //       $('#total-post').html("Total Post:");
    //       $('#total-following').html("You're following _ people<br /> Not enough data for a graph! Try connecting some accounts! ");
    //     } else {
    //       $('#total-followers').html("Total Audience: " + totalFollowers);
    //       $('#total-post').html("Total Post: " + totalPost);
    //       $('#total-following').html("You're following " + totalFollowing + " people");
    //
    //       // Graphs
    //       if(totalFollowers > 0){
    //         let fullFollowers = document.getElementById("full-followers").getContext("2d");
    //
    //         let fullFollowersChart = new Chart(fullFollowers, {
    //           type:'pie', // Making a pie chart
    //           data:{
    //             labels:['Twitter', 'Instagram'],
    //             datasets:[{
    //               label:'Followers By Platform',
    //               data:[
    //                 totalTwitterFollowers,
    //                 totalInstagramFollowers
    //               ],
    //               backgroundColor: [
    //                 '#28aae1',
    //                 '#d81dac'
    //               ]
    //             }]
    //           },
    //           options:{
    //             title:{
    //               display:true,
    //               text: 'Social Media Followers By Platform'
    //             }
    //           }
    //         });
    //       }
    //     }
    //   }
    //
    //
    //
    //
    //
    //   //Checking State of logged in accounts
    //   function getOpperationHistory(e){
    //     var url = 'get-opperation-history';
    //     var usernameVerify = "{{ user.username }}";
    //     $.ajax({
    //       type: 'POST',
    //       url: url,
    //       dataType: 'text',
    //       data: {
    //         csrfmiddlewaretoken: $('meta[name="_token"]').attr('content'),
    //         'usernameVerify':usernameVerify,
    //
    //       },
    //       success: function (content) {
    //         var econtent = JSON.parse(content);
    //         for (let i = 0; i < econtent.objectLength; i++) {
    //           opperationAddHistory(econtent, i);
    //         }
    //       },
    //     });
    //   }
    //   getOpperationHistory();
    //
    //   // Opperation Div
    //   function opperationDiv(){
    //     var dashboardRow = document.getElementById('opperations');
    //
    //     var createrDiv = document.createElement('div');
    //     createrDiv.className = "col-sm-16";
    //     createrDiv.setAttribute('id', "holder-3");
    //
    //     dashboardRow.appendChild(createrDiv);
    //     $('#holder-3').html('<div class="card" id="holder-4"><h4>Opperations</h4><div class="card" style=" height:17vh; display:inline-block;"id="opperationHistory">History: <table id="opperation-history-table" class="table"><tr><th style="width:33%;" scope="col">Type</th><th style="width:33%" scope="col">Likes/Follows</th><th style="width:33%" scope="col">Text/Hashtags</th><th style="width:33%;" scope="col">Location</th></tr></table></div><a href="#" style="color:#000" data-toggle="modal" data-target="#view-opperation-history"><p style="position: absolute; bottom:-20px; right:3%; float:right;">View All</p></a></div>');
    //
    //     var getTableDiv = document.getElementById('view-all-opperations');
    //     var createrTable = document.createElement('table');
    //     createrTable.setAttribute('id', "view-all-opperations-table");
    //     getTableDiv.appendChild(createrTable);
    //     $('#view-all-opperations-table').html('<tr><th style="width:50%;" scope="col">Type</th><th style="width:50%" scope="col">Likes/Follows</th><th style="width:50%" scope="col">Text/Hashtags</th><th style="width:50%;" scope="col">Location</th><th style="width:50%;" scope="col">Date</th></tr>');
    //
    //   }
    //   opperationDiv();
    //
    //   //Time picker
    //   $('#schedule-time').timepicker({
    //     'scrollDefault': 'now'
    //   });
    //
    //   // Add History for Opperations
    //   function opperationAddHistory(content, i){
    //     econtent = content
    //
    //     // Checking If Element Exist
    //     if ( $( "#fixed-row-opperation-table" ).length ) {
    //       $( "#fixed-row-opperation-table" ).show();
    //     } else {
    //
    //       $( "#fixed-row-opperation-table" ).show();
    //
    //       // Getting and Creating Elements
    //       var opperationTable = document.getElementById('opperation-history-table');
    //
    //       var creatorRow = document.createElement('tr');
    //
    //       // Creating Type Element
    //       var creatorRowType = document.createElement('td');
    //       creatorRowType.innerHTML = econtent.type[i];
    //       creatorRowType.setAttribute('id', "fixed-row-opperation-table");
    //
    //       // Creating Likes Element
    //       var creatorRowLikes = document.createElement('td');
    //       creatorRowLikes.innerHTML = econtent.likes[i];
    //
    //       // Creating Hashtags Element
    //       var creatorRowText = document.createElement('td');
    //       creatorRowText.innerHTML = econtent.hashtags[i];
    //
    //       // Creating Location Element
    //       var creatorRowLocation = document.createElement('td');
    //       creatorRowLocation.innerHTML = econtent.location[i];
    //
    //       // Appending Elements
    //       creatorRow.appendChild(creatorRowType);
    //       creatorRow.appendChild(creatorRowLikes);
    //       creatorRow.appendChild(creatorRowText);
    //       creatorRow.appendChild(creatorRowLocation);
    //
    //       // Appending Elements to Parent Elements
    //       opperationTable.appendChild(creatorRow);
    //     }
    //
    //     // View All Opperations
    //     var opperationTableViewAll = document.getElementById('view-all-opperations-table');
    //
    //     var creatorRowFull = document.createElement('tr');
    //
    //     // Creating Type Element
    //     var creatorRowTypeFull = document.createElement('td');
    //     creatorRowTypeFull.innerHTML = econtent.type[i];
    //
    //     // Creating Likes Element
    //     var creatorRowLikesFull = document.createElement('td');
    //     creatorRowLikesFull.innerHTML = econtent.likes[i];
    //
    //     // Creating Hashtags Element
    //     var creatorRowTextFull = document.createElement('td');
    //     creatorRowTextFull.innerHTML = econtent.hashtags[i];
    //
    //     // Creating Location Element
    //     var creatorRowLocationFull = document.createElement('td');
    //     creatorRowLocationFull.innerHTML = econtent.location[i];
    //
    //     // Creating Date Element
    //     var creatorRowDateFull = document.createElement('td');
    //
    //     creatorRowDateFull.innerHTML = econtent.date[i];
    //
    //     // Appending Elements
    //     creatorRowFull.appendChild(creatorRowTypeFull);
    //     creatorRowFull.appendChild(creatorRowLikesFull);
    //     creatorRowFull.appendChild(creatorRowTextFull);
    //     creatorRowFull.appendChild(creatorRowLocationFull);
    //     creatorRowFull.appendChild(creatorRowDateFull);
    //
    //     opperationTableViewAll.appendChild(creatorRowFull);
    //
    //   }
    //
    //   function formatDate(date) {
    //       var d = new Date(date),
    //           month = '' + (d.getMonth() + 1),
    //           day = '' + d.getDate(),
    //           year = d.getFullYear();
    //
    //       if (month.length < 2) month = '0' + month;
    //       if (day.length < 2) day = '0' + day;
    //
    //       return [year, month, day].join('-');
    //   }
