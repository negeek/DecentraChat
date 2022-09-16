const group_id = JSON.parse(document.getElementById('json-groupname').textContent);
const message_username = JSON.parse(document.getElementById('json-message-username').textContent);
const socket = new WebSocket(
    'ws://' + window.location.host + '/ws/' + group_id + '/'
);
console.log(socket)
socket.onopen = function (e) {
    console.log("CONNECTION ESTABLISHED");
}

socket.onclose = function (e) {
    console.log("CLOSED");
}

socket.onerror = function (e) {
    console.log("ERROR");
}
socket.onmessage = function (e) {
    console.log(e);
    const data = JSON.parse(e.data);
    if (data.username == message_username) {
        document.querySelector('#chat-body').innerHTML += `<tr>
                                                                <td>
                                                                <p class="bg-success p-2 mt-2 mr-5 shadow-sm text-white float-right rounded">${data.message}</p><small>${data.username}</small>
                                                                </td>
                                                            </tr>`
    } else {
        document.querySelector('#chat-body').innerHTML += `<tr>
                                                                <td>
                                                                <p class="bg-primary p-2 mt-2 mr-5 shadow-sm text-white float-left rounded">${data.message}</p><small>${data.username}</small>
                                                                </td>
                                                            </tr>`
    }
}

document.querySelector('#chat-message-submit').onclick = function (e) {
    const message_input = document.querySelector('#message_input');
    const message = message_input.value;

    socket.send(JSON.stringify({
        'message': message,
        'username': message_username
    }));

    message_input.value = '';
}