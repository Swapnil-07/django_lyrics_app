function onSignIn(googleUser) {
    alert("111");
    // Useful data for your client-side scripts:

    var profile = googleUser.getBasicProfile();
    console.log("ID: " + profile.getId()); // Don't send this directly to your server!
    console.log('Full Name: ' + profile.getName());
    console.log('Given Name: ' + profile.getGivenName());
    console.log('Family Name: ' + profile.getFamilyName());
    console.log("Image URL: " + profile.getImageUrl());
    console.log("Email: " + profile.getEmail());

    // The ID token you need to pass to your backend:
    var id_token = googleUser.getAuthResponse().id_token;
    console.log("ID Token: " + id_token);
//    signInTest(id_token);
}



function signOut() {
alert("222");
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
      console.log('User signed out.');
    });
  }

function signInTest() {
    // The ID token you need to pass to your backend:
    var id_token = "token_jwt";
    console.log("ID Token: " + id_token);
    $('input[name=token_id]').val(id_token);

    var serializedData = $("#gsignin-form").serialize();
        // make POST ajax call
        $.ajax({
            type: 'POST',
            url: '/login',
            data: serializedData,
            success: function (response) {
                // on successfull creating object
                // 1. clear the form.
                $("#friend-form").trigger('reset');
                // 2. focus to nickname input
                $("#id_nick_name").focus();

                // display the newly friend to table.
                var instance = JSON.parse(response["instance"]);
                var fields = instance[0]["fields"];
                $("#my_friends tbody").prepend(
                    `<tr>
                    <td>${fields["nick_name"]||""}</td>
                    <td>${fields["first_name"]||""}</td>
                    <td>${fields["last_name"]||""}</td>
                    <td>${fields["likes"]||""}</td>
                    <td>${fields["dob"]||""}</td>
                    <td>${fields["lives_in"]||""}</td>
                    </tr>`
                )
            },
            error: function (response) {
                // alert the error if any error occured
                alert(response["responseJSON"]["error"]);
            }
        })

}
