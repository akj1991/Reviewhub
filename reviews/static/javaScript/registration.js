
const phoneInputField = document.querySelector("#phone");
        const phoneInput = window.intlTelInput(phoneInputField, {
            preferredCountries: ["us", "co", "in", "de"],
          utilsScript:
            "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
        });