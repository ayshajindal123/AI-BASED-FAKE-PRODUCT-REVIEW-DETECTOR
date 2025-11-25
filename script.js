
function togglePassword() {
    const pass = document.getElementById("password");
    pass.type = pass.type === "password" ? "text" : "password";
}

// LOGIN

 function login() {

    let user = document.getElementById("username").value.trim();
    let pass = document.getElementById("password").value.trim();

    if (user === "" || pass === "") {
        alert("Enter username and password!");
        return;
    }

    // SAVE LOGIN STATUS
    localStorage.setItem("loggedIn", "true");

    // REDIRECT TO MAIN PAGE
    window.location.href = "index.html";
}
function signup() {
    let user = document.getElementById("newUser").value.trim();
    let pass = document.getElementById("newPass").value.trim();

    if (user === "" || pass === "") {
        alert("Fill all fields!");
        return;
    }

    alert("Account created successfully!");

    window.location.href = "login.html";
}
