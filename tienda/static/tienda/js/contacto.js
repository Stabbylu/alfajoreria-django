
window.onload = function(){
    const myToastEl = document.getElementById('Toast');
    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(myToastEl);
    toastBootstrap.show();
}