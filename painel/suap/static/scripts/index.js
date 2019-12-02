const check = () => {
    if (!('serviceWorker' in navigator)) {
      throw new Error('Service Worker não suportado!')
    }
    if (!('PushManager' in window)) {
      throw new Error('Push API não suportado!')
    }
  }

// Registering the service worker 
const registerSw = async () => {
    const swRegistration = await navigator.serviceWorker.register('/static/scripts/service.js');
    return swRegistration;
}

// Permission for notification on browser
const reqNotificationPerm = async () => {
    const permission = await window.Notification.requestPermission();

    if (permission !== 'granted'){
        throw new Error('Permissão para notificação negada.');
    }
} 

const showLocalNotification = (title, body, swRegistration) => {
    const options = {
        body,
    };
    swRegistration.showNotification(title, options);
}

const main = async () => {
    check();
    const swRegistration = await registerSw();
    const permission = await reqNotificationPerm();
    showLocalNotification('This is title', 'This is message', swRegistration);
}

main();