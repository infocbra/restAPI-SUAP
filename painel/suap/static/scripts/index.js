// const check = () => {
//     if (!('serviceWorker' in navigator)) {
//       throw new Error('Service Worker não é suportado nesse navegador!')
//     }
//     if (!('PushManager' in window)) {
//       throw new Error('Não suporta notificações!')
//     }
// }

// const registerServiceWorker = async () => {
// const swRegistration = await navigator.serviceWorker.register('service.js')
//     return swRegistration
//   }
// const requestNotificationPermission = async () => {
//     const permission = await window.Notification.requestPermission()
//         // value of permission can be 'granted', 'default', 'denied'
//         // granted: user has accepted the request
//         // default: user has dismissed the notification permission popup by clicking on x
//         // denied: user has denied the request.
//     if (permission !== 'granted') {
//         throw new Error('Permission not granted for Notification')
//     }
// }
// const main = async () => {
//     check()
//     const swRegistration = await registerServiceWorker()
//     const permission = await requestNotificationPermission()
// }
//  main(); //we will not call main in the beginning.