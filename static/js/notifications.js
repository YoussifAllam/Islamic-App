const token = localStorage.getItem('access_token');  // Retrieve the JWT token

const socket = new WebSocket(`ws://${window.location.host}/ws/notifications/?token=${token}`);

socket.onopen = function () {
    console.log('WebSocket connected successfully');
};

socket.onmessage = function (event) {
    const data = JSON.parse(event.data);  // Parse the JSON data from WebSocket
    const notificationsDiv = document.getElementById('notifications');

    // Add the subject and message to the notifications div
    notificationsDiv.innerHTML += `<p><strong>${data.subject}</strong>: ${data.message}</p>`;
};

socket.onclose = function () {
    console.error('WebSocket closed unexpectedly');
};

socket.onerror = function (error) {
    console.error('WebSocket error:', error);
};
