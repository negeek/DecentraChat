const id = JSON.parse(document.getElementById('json-username').textContent);
const message_username = JSON.parse(document.getElementById('json-message-username').textContent);
const socket = new WebSocket(
    'wss://' + window.location.host + '/ws/' + id + '/'
);

socket.onopen = function (e) {
    console.log("CONNECTION ESTABLISHED");
}

socket.onclose = function (e) {
    console.log(e);

    console.log("CLOSED");
}

socket.onerror = function (e) {
    console.log(e);

    console.log("ERROR");
}
socket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    const d = new Date();
    if (data.username == message_username) {
        document.querySelector('#chat-body').innerHTML += `<tr>
                                                                <td>
                                                                <p class="bg-success p-2 mt-2 mr-5 shadow-sm text-white float-right rounded">${data.message}<small style="font-size:0.5em; ">&nbsp; ${d.toTimeString().slice(0, 5)}</small><a href="/delete/${data.thread_name}/${data.id}"><small
                                                                style="font-size:0.5em;color: #000;">delete</small></a></p>
                                                                </td>
                                                            </tr>`
    } else {
        document.querySelector('#chat-body').innerHTML += `<tr>
                                                                <td>
                                                                <p class="bg-primary p-2 mt-2 mr-5 shadow-sm text-white float-left rounded">${data.message}<small style="font-size:0.5em; ">&nbsp; ${d.toTimeString().slice(0, 5)}</small><a href="/delete/${data.thread_name}/${data.id}"><small
                                                                style="font-size:0.5em;color: #000;">delete</small></a></p>
                                                                </td>
                                                            </tr>`
    }
    document.querySelector(".message-table-scroll").scrollTo(0, document.querySelector(".message-table-scroll").scrollHeight);
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

