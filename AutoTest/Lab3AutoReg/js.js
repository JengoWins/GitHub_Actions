console.log("Тест-скрипт")

document.getElementById('registrationForm').addEventListener('submit', (event) => {
    event.preventDefault(); // предотвращаем стандартное поведение формы
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    checkComp = 0

    if (username.length < 3) 
        alert('Username must be at least 3 characters long.');
    else
        checkComp++

    if (password.length < 6) 
        alert('Password must be at least 6 characters long.');
    else
        checkComp++

    
    if(checkComp==2)
        window.location.href = 'Main.html'

})