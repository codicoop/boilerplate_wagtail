(function() {
  var contactForm = document.getElementById("contact__form");

  if (contactForm) {
    contactForm.addEventListener('submit', function(event){
      contactFormSubmit(event);
    });
  }

  function contactFormSubmit(event) {
    // This stops the normal functionality of the <form>
    event.preventDefault()
    // This is the general error, in case is needed
    //var errorEl = event.target.getElementsByClassName('error')[0];

    var postURL = event.target.getAttribute('data-url');
    const csrftoken = getCookie('csrftoken');

    const request = new Request(
        postURL,
        {
          headers: {
            'X-CSRFToken': csrftoken,
            'X-Requested-With': 'XMLHttpRequest',
            "Accept": "application/json",
            'Content-type': 'application/json',
          },
          credentials: "same-origin",
        }
    );
    fetch(request, {
      method: 'POST',
      body: JSON.stringify(Object.fromEntries(new FormData(event.target))),
    })
    .then(response => {
      if (!response.ok) {
        throw new Error("Could not finish the request.");
      }
      return response.json();
    })
    .then(data => {
      successEl = contactForm.querySelector('p');
      btn = document.getElementById('btn_send');
      inputItems = event.target.getElementsByClassName('input__item');
      errorSpans = event.target.getElementsByClassName('input__error');

      // Reset to default state
      // Eliminates any error classes
      Array.from(inputItems).forEach(function(el) {
        el.classList.remove('error');
      })
      // Deletes any possibly generated error span
      Array.from(errorSpans).forEach(function(el) {
          el.remove();
      })
      // Hides any success messages
      successEl.style.display = 'none';

      // reset button styles
      btn.classList.remove("btn--orange");
      btn.classList.add("btn--blue");
      btn.innerHTML = "Enviar";
      btn.setAttribute("style", "pointer-events: auto");

      if ('errors' in data) {
        // Changes in the button when there's an error
        btn.classList.remove("btn--blue");
        btn.classList.add("btn--orange");
        btn.innerHTML = "Error";
        btn.setAttribute("style", "pointer-events: none");

        Object.entries(data['errors']).forEach(function(error_blocks) {
        /* When converting the object into an array, each property of the
        object is converted into an array in which [0] is the property name
        and [1] is the value. */
        block_name = error_blocks[0]
        error_messages = error_blocks[1]
          // For the general error
          if (error_blocks[0] == '__all__') {
            // Not handling this type of errors for the contact form.
            //error_messages.forEach(function(error_message) {
            //  throw new Error(error_message);
            //});
          } else {
            // For the field-specific errors
            // Gets the field name
            el = event.target.elements[block_name];
            if (el) {
              // Creates a new error <span>
              errorDiv = el.parentNode;
              inputItem = errorDiv.parentNode;
              inputItem.classList.add('error');

              newnode = document.createElement('span');
              newnode.classList.add('input__error');
              newnode.innerText = error_messages[0];
              el.parentNode.appendChild(newnode);

            };
          };
        });

        // If the user writes in the textfield, the error styling is removed
        Array.from(inputItems).forEach(function(el) {
          el.addEventListener("input", function() {
            el.classList.remove('error');
            btn.classList.remove("btn--orange");
            btn.classList.add("btn--blue");
            btn.innerHTML = "Enviar";
            btn.setAttribute("style", "pointer-events: auto");
          })
        })

      } else {
        // Show success message
        successEl.style.display = 'block';
        // Cleans up the form fields
        event.target.reset();
        // Optionally, redirect to success page
        // window.location.href = postURL + 'sent/';
      };
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  };

  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
})();
