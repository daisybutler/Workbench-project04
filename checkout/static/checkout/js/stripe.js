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

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({ 'disabled': true });
    $('#submit-button').attr('disabled', true);
    $('#payment-form').toggle(100);
    $('#loading-icon').toggle(100);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
                    name: $.trim(form.first_name.value) + ' ' + $.trim(form.last_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address:{
                        line1: $.trim(form.billing_address.value) + ', ' + $.trim(form.county.value),
                        postal_code: $.trim(form.postcode.value),
                        country: 'GB',
                    }
            }
        }
    }).then(function (result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            $('#payment-form').toggle(100);
            $('#loading-icon').toggle(100);
            card.update({ 'disabled': false });
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});