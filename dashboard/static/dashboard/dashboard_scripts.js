let url = `ws://${window.location.host}/ws/notification/`;

const chatSocket = new WebSocket(url);

chatSocket.onmessage = function (e) {
  let data = JSON.parse(e.data);
  console.log(data);
  if (data.type === "notification") {
    displayNotification(data.message);
  }
};

function displayNotification(message) {
  const notificationContainer = document.getElementById(
    "notification-body"
  );
  const notificationElement = document.createElement("div");
  notificationElement.textContent = message;
  notificationContainer.appendChild(notificationElement);
}

const sendTestMessage = () => {
  const message = {
    type: "notification",
    notification: "Teste de Notificação",
  };
  chatSocket.send(JSON.stringify(message));
};

// Vincular o evento de clique do botão à função de enviar a mensagem
document.getElementById("btnTest").addEventListener("click", sendTestMessage);

// Notification Bar

// Variáveis globais
const notificationContainer = document.getElementById("notification-container");
const notificationBody = document.getElementById("notification-body");
const notificationHeader = document.getElementById("notification-header");
let notifications = [];

function toggleNotifications() {
  notificationContainer.classList.toggle("opened");
}

// Função para adicionar uma nova notificação à janela de notificações
function addNotification(message) {
  const notificationElement = document.createElement("div");
  notificationElement.classList.add("notification");
  notificationElement.innerText = message;
  notificationBody.appendChild(notificationElement);
}





notificationHeader.addEventListener("click", toggleNotifications);

// Evento para conectar ao WebSocket quando a página carregar
document.addEventListener("DOMContentLoaded", () => {
  const url = `ws://${window.location.host}/ws/notification/`;
  const chatSocket = new WebSocket(url);
  chatSocket.onmessage = receiveMessage;
});


// Função para receber mensagens do WebSocket e exibir as notificações
function receiveMessage(e) {
  const data = JSON.parse(e.data);
  if (data.type === "notification") {
    notifications.push(data.notification);
    addNotification(data.notification);
  }
}
