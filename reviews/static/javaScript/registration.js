const form = document.getElementById('form');
const name = document.getElementById('name');
const username = document.getElementById('username');
const email = document.getElementById('email');
const phonenumber = document.getElementById('phonenumber');
const nationality = document.getElementById('nationality');
const age = document.getElementById('age');
const password = document.getElementById('password');
const repassword = document.getElementById('repassword');

form.addEventListener('submit', e=> {
    e.preventDefault();

    checkInputs();
});

function checkInputs() {
    const nameValue = name.value.trim();
	const usernameValue = username.value.trim();
	const emailValue = email.value.trim();
	const passwordValue = password.value.trim();
	const repasswordValue = repassword.value.trim();

    if(usernameValue === '') {
		setErrorFor(username, 'Username cannot be blank');
	} else {
		setSuccessFor(username);
	}

    if(emailValue === '') {
		setErrorFor(email, 'Email cannot be blank');
	} else if (!isEmail(emailValue)) {
		setErrorFor(email, 'Not a valid email');
	} else {
		setSuccessFor(email);
	}
    
    if(passwordValue === '') {
		setErrorFor(password, 'Password cannot be blank');
	} else {
		setSuccessFor(password);
	}
	
	if(repasswordValue === '') {
		setErrorFor(repassword, 'repassword2 cannot be blank');
	} else if(passwordValue !== repasswordValue) {
		setErrorFor(repassword, 'Passwords does not match');
	} else{
		setSuccessFor(repassword);
	}
}

function setErrorFor(input, message) {
	const formControl = input.parentElement;
	const small = formControl.querySelector('small');
	formControl.className = 'form-control error';
	small.innerText = message;
}

function setSuccessFor(input) {
	const formControl = input.parentElement;
	formControl.className = 'form-control success';
}
	
function isEmail(email) {
	return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}