var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#313131',
        fontFamily: '"Open Sans", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#313131',
        }
    },
    invalid: {
        color: '#D91F44',
        iconColor: '#D91F44'
    }
};
var card = elements.create('card', { style: style });
card.mount('#card-details');

// -------------------------------- DOESN'T WORK
// Handle validation errors of card details
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times></i>
            </span>
            <span>error</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContext = 'none';
    } 
});