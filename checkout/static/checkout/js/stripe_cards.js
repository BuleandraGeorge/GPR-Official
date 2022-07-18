var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', { style: style });
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = $('card-errors');
    let fieldset_card = document.querySelector("#fieldset-card");
    if (event.error) {
        fieldset_card.classList.add("border-danger");
        fieldset_card.classList.remove("border-dark");
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        fieldset_card.classList.add("border-dark");
        fieldset_card.classList.remove("border-danger");
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({ 'disabled': true });
    $('#submit-button').attr('disabled', true);

    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.nume.value),
                    phone: $.trim(form.telefon.value),
                    email: $.trim(form.email.value),
                    address: {
                        line1: $.trim(form.adresa.value),
                        line2: $.trim(form.adresa_linia_2.value),
                        city: $.trim(form.judet.value),
                        country: $.trim(form.tara.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.nume.value),
                phone: $.trim(form.telefon.value),
                address: {
                    line1: $.trim(form.adresa.value),
                    line2: $.trim(form.adresa_linia_2.value),
                    city: $.trim(form.judet.value),
                    country: $.trim(form.tara.value),
                }
            },
        }).then(function (result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                card.update({ 'disabled': false });
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        // just reload the page, the error will be in django messages
        location.reload();
    })
});