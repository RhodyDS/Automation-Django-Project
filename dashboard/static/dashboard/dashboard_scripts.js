

// Notification Bar

// Variáveis globais
const notificationContainer = document.getElementById("notification-container");
const notificationBody = document.getElementById("notification-body");
const notificationHeader = document.getElementById("notification-header");
let notifications = [];

function toggleNotifications() {
  notificationContainer.classList.toggle("opened");
}


notificationHeader.addEventListener("click", toggleNotifications);

// Evento para conectar ao WebSocket quando a página carregar
document.addEventListener("DOMContentLoaded", () => {
  const url = `ws://${window.location.host}/ws/notification/`;
  const chatSocket = new WebSocket(url);
  
  chatSocket.onmessage = function (e) {
    let data = JSON.parse(e.data);
    console.log(data);
    if (data.type === "notification") {
      displayNotification(data.message);
    }
  };
});

function displayNotification(message) {
  const notificationContainer = document.getElementById("notification-body");
  const notificationElement = document.createElement("div");
  notificationElement.textContent = message;
  notificationContainer.insertBefore(notificationElement, notificationContainer.firstChild);
}






