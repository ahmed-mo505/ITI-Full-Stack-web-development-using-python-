// function registerUser(event) {
//     event.preventDefault();
//     const username = document.getElementById("registerUsername").value;
//     const password = document.getElementById("registerPassword").value;

//     if (username && password) {
//         localStorage.setItem("username", username);
//         localStorage.setItem("password", password);
//         alert("User registered successfully!");
//         document.getElementById("registerForm").reset();
//     } else {
//         alert("Please fill in both fields.");
//     }
// }

// function loginUser(event) {
//     event.preventDefault();
//     const username = document.getElementById("loginUsername").value;
//     const password = document.getElementById("loginPassword").value;

//     const storedUsername = localStorage.getItem("username");
//     const storedPassword = localStorage.getItem("password");

//     if (username === storedUsername && password === storedPassword) {
//         alert("Login successful!");
//     } else {
//         alert("Invalid username or password.");
//     }
// }

// document.addEventListener("DOMContentLoaded", () => {
//     const storedUsername = localStorage.getItem("username");
//     if (storedUsername) {
//         document.getElementById(
//             "userGreeting"
//         ).innerText = `Hello, ${storedUsername}`;
//     }
// });

// function registerUser(event) {
//     event.preventDefault();
//     const username = document.getElementById("registerUsername").value;
//     const password = document.getElementById("registerPassword").value;

//     if (username && password) {
//         localStorage.setItem("username", username);
//         localStorage.setItem("password", password);
//         alert("User registered successfully!");
//         document.getElementById("registerForm").reset();
//     } else {
//         alert("Please fill in both fields.");
//     }
// }

// function loginUser(event) {
//     event.preventDefault();
//     const username = document.getElementById("loginUsername").value;
//     const password = document.getElementById("loginPassword").value;

//     const storedUsername = localStorage.getItem("username");
//     const storedPassword = localStorage.getItem("password");

//     if (username === storedUsername && password === storedPassword) {
//         alert("Login successful!");
//         document.getElementById(
//             "userGreeting"
//         ).innerText = `Hello, ${username}`;
//     } else {
//         alert("Invalid username or password.");
//     }
// }
// document.addEventListener("DOMContentLoaded", () => {
//     const storedUsername = localStorage.getItem("username");
//     if (storedUsername) {
//         document.getElementById(
//             "userGreeting"
//         ).innerText = `Hello, ${storedUsername}`;
//     }
// });

// function showLoginForm() {
//     document.getElementById("registerForm").style.display = "none";
//     document.getElementById("loginForm").style.display = "block";
// }

// function showRegisterForm() {
//     document.getElementById("registerForm").style.display = "block";
//     document.getElementById("loginForm").style.display = "none";
// }

// function registerUser(event) {
//     event.preventDefault();
//     const username = document.getElementById("registerUsername").value;
//     const password = document.getElementById("registerPassword").value;

//     if (username && password) {
//         localStorage.setItem("username", username);
//         localStorage.setItem("password", password);
//         alert("User registered successfully!");
//         document.getElementById("registerForm").reset();
//     } else {
//         alert("Please fill in both fields.");
//     }
// }

// function loginUser(event) {
//     event.preventDefault();
//     const username = document.getElementById("loginUsername").value;
//     const password = document.getElementById("loginPassword").value;

//     const storedUsername = localStorage.getItem("username");
//     const storedPassword = localStorage.getItem("password");

//     if (username === storedUsername && password === storedPassword) {
//         alert("Login successful!");
//         localStorage.setItem("currentUser", username);
//         window.location.href = "index.html";
//     } else {
//         alert("Invalid username or password.");
//     }
// }
document.addEventListener("DOMContentLoaded", () => {
    const storedUsername = localStorage.getItem("username");
    if (storedUsername) {
        document.getElementById(
            "userGreeting"
        ).innerText = `Hello, ${storedUsername}`;
        document.getElementById("logoutButton").style.display = "block";
    }
});

function showLoginForm() {
    document.getElementById("registerForm").style.display = "none";
    document.getElementById("loginForm").style.display = "block";
}

function showRegisterForm() {
    document.getElementById("registerForm").style.display = "block";
    document.getElementById("loginForm").style.display = "none";
}

function registerUser(event) {
    event.preventDefault();
    const username = document.getElementById("registerUsername").value;
    const password = document.getElementById("registerPassword").value;

    if (username && password) {
        localStorage.setItem("username", username);
        localStorage.setItem("password", password);
        alert("User registered successfully!");
        document.getElementById("registerForm").reset();
        window.location.href = "index.html";
        // showLoginForm();
    } else {
        alert("Please fill in both fields.");
    }
}

function loginUser(event) {
    event.preventDefault();
    const username = document.getElementById("loginUsername").value;
    const password = document.getElementById("loginPassword").value;

    const storedUsername = localStorage.getItem("username");
    const storedPassword = localStorage.getItem("password");

    if (username === storedUsername && password === storedPassword) {
        alert("Login successful!");
        localStorage.setItem("currentUser", username);
        window.location.href = "index.html";
    } else {
        alert("Invalid username or password.");
    }
}

function logoutUser() {
    // localStorage.removeItem("currentUser");
    localStorage.clear();
    alert("Logged out successfully!");
    window.location.href = "index.html";
    // showRegisterForm();
}
