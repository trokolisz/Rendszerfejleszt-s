// Assuming you have a button or some event to trigger this action
function PostForm(){
    fetch("http://127.0.0.1:8000/comment/", {
        method: "POST",
        body: JSON.stringify({
            body: "Great insights on AI!",
            timestamp: "2024-04-10T06:42:00Z",
            topic_id: 2,
            user_id: 2
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })
    .then((response) => response.json())
    .then((data) => console.log(data));
    
}


