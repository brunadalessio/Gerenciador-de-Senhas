function showPassword(){
    var input = document.getElementById("password");
    var input_button = document.getElementById("password-button");
    var type = input.getAttribute("type") === "password" ? "text" : "password";
    input.setAttribute("type", type);
    input_button.classList.toggle("bi-eye-slash-fill");
}

function showConfirmPassword(){
    var input = document.getElementById("confirmPassword");
    var input_button = document.getElementById("confirmPassword-button");
    var type = input.getAttribute("type") === "password" ? "text" : "password";
    input.setAttribute("type", type);
    input_button.classList.toggle("bi-eye-slash-fill");
}

function showMultiplePassword(id) {
    var input = document.getElementById("password-" + id);
    var input_button = document.getElementById("password-button-" + id);
    var type = input.getAttribute("type") === "password" ? "text" : "password";
    input.setAttribute("type", type);
    input_button.classList.toggle("bi-eye-slash-fill");
}
