// create a function to delete a note from the database

function deleteNote(noteId) {
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({noteId: noteId}),
    }).then((_res) => {
        window.location.href = "/";
    });
}

// basic way to send a request in javascript to the backend..
// this funciton takes the noteId that we pass it and sends a POST request to the /delete-note end point (which we must create), then when it gets a response.. it will reload the window (which is done with the .then() )
