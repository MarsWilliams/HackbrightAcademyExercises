$(document).ready(function () {
    // Normally, JavaScript runs code at the time that the <script>
    // tags loads the JS. By putting this inside a jQuery $(document).ready()
    // function, this code only gets run when the document finishing loading.

    $("#message-form").submit(handleFormSubmit);
    getMessages();
});

function getMessages() {
    //json output like this {"messages": [{"message": "Hi"}, {"message": "There"}], "result": "OK"}
    $.get("/api/wall/list", function (output) {
        console.log("success");
        
        //selects relevent information from json data
        output = output["messages"];
        
        // clears placeholder messages
        $("#message-container").empty();
        // console.log($("#message-container"));

        for (var index = 0; index < output.length; index++) {
            $("#message-container").prepend("<li class='list-group-item'>" + output[index]['message'] + "</li>");
        }
    }
    );
}
/**
 * Handle submission of the form.
 */
function handleFormSubmit(evt) {
    
    evt.preventDefault();

    var textArea = $("#message");
    var msg = textArea.val();

    console.log("handleFormSubmit: ", msg);
    addMessage(msg);

    // Reset the message container to be empty
    textArea.val("");
    $("#message-container").empty();
    
}


/**
 * Makes AJAX call to the server and the message to it.
 */
function addMessage(msg) {
    $.post(
        "/api/wall/add",
        {'m': msg},
        function (data) {
            console.log("addMessage: ", data);
            displayResultStatus(data.result);
            getMessages();
        }
    );
}

function clearMessages() {
    event.preventDefault();
    $('#clearBotton').click(
        $.get("/api/wall/list", function (output) {
        console.log("success");
        
        //selects relevent information from json data
        output = output["messages"];
        
        // clears placeholder messages
        $("#message-container").empty();
})
);
}


/**
 * This is a helper function that does nothing but show a section of the
 * site (the message result) and then hide it a moment later.
 */
function displayResultStatus(resultMsg) {
    var notificationArea = $("#sent-result");
    notificationArea.text(resultMsg);
    notificationArea.slideDown(function () {
        // In JavaScript, "this" is a keyword that means "the object this
        // method or function is called on"; it is analogous to Python's
        // "self". In our case, "this" is the #sent-results element, which
        // is what slideDown was called on.
        //
        // However, when setTimeout is called, it won't be called on that
        // same #sent-results element--"this", for it, wouldn't be that
        // element. We could put inside of our setTimeout call the code
        // to re-find the #sent-results element, but that would be a bit
        // inelegant. Instead, we'll use a common JS idiom, to set a variable
        // to the *current* definition of self, here in this outer function,
        // so that the inner function can find it and where it will have the
        // same value. When stashing "this" into a new variable like that,
        // many JS programmers use the name "self"; some others use "that".
        var self = this;

        setTimeout(function () {
            $(self).slideUp();
        }, 2000);
    });
}